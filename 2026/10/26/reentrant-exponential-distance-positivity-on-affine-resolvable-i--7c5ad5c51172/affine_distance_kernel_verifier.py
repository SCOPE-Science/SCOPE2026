"""Finite-instance diagnostics for distance-radial kernels on affine designs.

Requires Python 3, SymPy, NumPy. The mathematical proof is separate; these checks
confirm the incidence model, spectral reductions, polynomial identities, and samples.
"""
from itertools import product
from collections import deque
import numpy as np
import sympy as sp


def affine_point_hyperplane_distances(prime, dimension):
    p = prime
    pts = list(product(range(p), repeat=dimension))
    covectors = []
    for vector in product(range(p), repeat=dimension):
        if not any(vector):
            continue
        first = next(x for x in vector if x)
        inverse = pow(first, -1, p)
        normalized = tuple(x * inverse % p for x in vector)
        if normalized not in covectors:
            covectors.append(normalized)
    covectors.sort()
    blocks = []
    for direction in covectors:
        for offset in range(p):
            blocks.append(frozenset(i for i,x in enumerate(pts)
                 if sum(u * v for u,v in zip(direction,x)) % p == offset))
    N = len(pts)+len(blocks)
    adj = [[] for _ in range(N)]
    for j,block in enumerate(blocks):
        for i in block:
            adj[i].append(len(pts)+j)
            adj[len(pts)+j].append(i)
    distances = np.zeros((N,N), dtype=np.int64)
    for src in range(N):
        seen = [-1]*N
        seen[src] = 0
        queue = deque([src])
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if seen[u] == -1:
                    seen[u] = seen[v]+1
                    queue.append(u)
        assert -1 not in seen
        distances[src,:] = seen
    return distances, pts, blocks


def symbolic_checks():
    n,k,w = sp.symbols('n k w', positive=True)
    r = (n*k-1)/(n-1)
    v = n*k
    a0 = 1+(v-1)*w
    b0 = 1+n*(r-1)*w+(n-1)*w**2
    c0sq = k*r*w*(1+(n-1)*w)**2
    det0 = sp.factor(a0*b0-c0sq)
    B = -k**2*n + 2*k*n**2 - k*n + k - n**2
    C = (k-1)*(n-1)**2*(k*n-1)
    assert sp.simplify(det0-(1-w)*((n-1)+B*w+C*w**2)/(n-1)) == 0
    assert sp.simplify((1-w)*(1-w**2)-k*w*(1-w)**2 - (1-w)**2*(1-(k-1)*w)) == 0
    assert sp.simplify(1-n*w+(n-1)*w**2 - (1-w)*(1-(n-1)*w)) == 0
    assert sp.simplify(det0.subs({n:3,k:9}) - (1-w)*(1-54*w+416*w*w)) == 0
    wm = (sp.Integer(27)-sp.sqrt(313))/416
    wp = (sp.Integer(27)+sp.sqrt(313))/416
    assert 0 < wm < wp < sp.Rational(1,8)
    assert sp.factor((1-54*w+416*w*w).subs(w,wm)) == 0
    assert sp.factor((1-54*w+416*w*w).subs(w,wp)) == 0
    return wm,wp


def numerical_checks():
    for p,m in [(2,2),(2,3),(3,2),(3,3)]:
        d,pts,blocks = affine_point_hyperplane_distances(p,m)
        v=len(pts); b=len(blocks);n=p;mu=p**(m-2);k=n*mu
        r=(n*k-1)//(n-1)
        assert v==n*k and b==n*r
        assert np.max(d)==4
        M=np.array([[int(i in B) for B in blocks] for i in range(v)],dtype=np.int64)
        assert np.array_equal(M@M.T, k*np.eye(v,dtype=np.int64)+((k-1)//(n-1)) * np.ones((v,v),dtype=np.int64))
        assert np.array_equal(d[:v,:v], 2*(np.ones((v,v),dtype=np.int64)-np.eye(v,dtype=np.int64)))
        for i in range(b):
            for j in range(b):
                if i==j:target=0
                elif i//n==j//n:target=4
                else:target=2
                assert d[v+i,v+j]==target
        print('geometry',p,m,'n,mu,v,b',n,mu,v,b)
        for z in [0.1,0.2,1/3,0.5,0.9]:
            f=z**d
            eig=np.linalg.eigvalsh(f)
            w=z*z
            A0=1+(v-1)*w
            B0=1+n*(r-1)*w+(n-1)*w*w
            C0=(k*r)**0.5*z*(1+(n-1)*w)
            T0=np.array([[A0,C0],[C0,B0]])
            T1=np.array([[1-w,k**0.5*z*(1-w)],[k**0.5*z*(1-w),1-w*w]])
            L=1-n*w+(n-1)*w*w
            pieces= list(np.linalg.eigvalsh(T0)) + list(np.linalg.eigvalsh(T1))*(v-1)+[L]*(r-1)
            assert np.allclose(np.sort(eig),np.sort(pieces),rtol=1e-10,atol=1e-10)
    d,_,_ = affine_point_hyperplane_distances(3,3)
    wm,wp=symbolic_checks()
    for w,expect in [(sp.Rational(1,100),True),(sp.Rational(1,20),False),(sp.Rational(11,100),True),(sp.Rational(3,20),False)]:
        z=float(sp.sqrt(w));eig=np.linalg.eigvalsh(z**d)
        assert (min(eig)>1e-8)==expect,(w,min(eig),expect)
    for w,expect_nullity in [(float(wm),1),(float(wp),1),(1/8,26)]:
        eig=np.linalg.eigvalsh(np.sqrt(w)**d)
        nullity=int(sum(abs(x)<1e-8 for x in eig))
        assert nullity==expect_nullity,(w,nullity,expect_nullity)
        assert eig[0]>-1e-8
    return wm,wp


if __name__=='__main__':
    a,b=numerical_checks()
    print('EXACT ROOTS',a,b)
    print('PASSED all symbolic, geometry, spectral and rank assertions')
