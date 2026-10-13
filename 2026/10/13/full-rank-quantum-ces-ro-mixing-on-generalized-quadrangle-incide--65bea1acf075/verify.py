#!/usr/bin/env python3
"""Independent symbolic and finite-instance checks for generalized-quadrangle incidence-graph quantum mixing.

Requires Python 3, sympy and numpy. All symbolic parameter equalities are exact;
finite graph diagonalizations are numerical cross-checks, not a proof for all orders.
"""
import itertools
import math
import numpy as np
import sympy as S

q, z = S.symbols('q z', positive=True)
N = 2 * (q + 1) * (q*q + 1)
k = [1, q+1, q*(q+1), q*q*(q+1), q**3]
val = [q+1, -q-1, S.sqrt(2*q), -S.sqrt(2*q), S.Integer(0)]
mul = [S.Integer(1), S.Integer(1), q*(q+1)**2/2,
       q*(q+1)**2/2, q*(q*q+1)]

def polynomials(t):
    return [S.Integer(1), t, t*t-(q+1), t**3-(2*q+1)*t,
            (t**4-(3*q+1)*t*t+q*(q+1))/(q+1)]

def zero(v):
    return S.factor(S.radsimp(S.expand(v))) == 0

coeff = [S.factor(sum((mul[j] * polynomials(val[j])[i]
          / (N*k[i]))**2 for j in range(5))) for i in range(5)]
expected_coeff = [
 (3*q**6+4*q**5+10*q**4+4*q**3+3*q**2+4)/(8*(q+1)**2*(q*q+1)**2),
 (q**5+2*q**4+q**3+2)/(4*(q+1)**2*(q*q+1)**2),
 (3*q**4+2*q**2+7)/(8*(q+1)**2*(q*q+1)**2),
 (q*q+4*q+1)/(4*q*(q+1)**2*(q*q+1)**2),
 (3*q**4+4*q**3+14*q*q+4*q+3)/(8*q*q*(q+1)**2*(q*q+1)**2)
]
expected_eigs = [
 S.Integer(1), q/(2*(q+1)),
 (q-1)*(3*q*q+4*q+3+2*(q+1)*S.sqrt(2*q))/(8*q*(q*q+1)),
 (q-1)*(3*q*q+4*q+3-2*(q+1)*S.sqrt(2*q))/(8*q*(q*q+1)),
 (3*q*q-2*q+3)/(8*q*(q+1))
]

def symbolic_check():
    assert S.simplify(sum(k)-N) == 0
    assert S.simplify(sum(mul)-N) == 0
    for i in range(5):
        assert zero(coeff[i]-expected_coeff[i]), i
    for i,theta in enumerate(val):
        mu = sum(coeff[j]*polynomials(theta)[j] for j in range(5))
        assert zero(mu-expected_eigs[i]), i
    assert zero(sum(k[i]*coeff[i] for i in range(5))-1)
    # Strict positivity of smallest-looking branch for q>1 follows from
    # square plus 2(q^2+1), not from bounded tests.
    assert zero((3*q*q+4*q+3-2*(q+1)*S.sqrt(2*q)) -
                ((q+1-S.sqrt(2*q))**2+2*(q*q+1)))
    return 5,5

def symplectic_graph(prime):
    assert prime in (2,3)
    F=range(prime)
    def canon(v):
        idx=next(i for i,x in enumerate(v) if x%prime)
        inv=pow(v[idx],-1,prime)
        return tuple((x*inv)%prime for x in v)
    points=sorted({canon(x) for x in itertools.product(F,repeat=4) if any(x)})
    def omega(x,y):
        return (x[0]*y[2]-x[2]*y[0]+x[1]*y[3]-x[3]*y[1])%prime
    lines=set()
    for x,y in itertools.combinations(points,2):
        if omega(x,y):
            continue
        line=tuple(sorted({canon(tuple((a*u+b*v)%prime for u,v in zip(x,y)))
             for a in F for b in F if a or b}))
        if len(line)==prime+1:
            lines.add(line)
    lines=sorted(lines)
    v=len(points)
    assert v == (prime+1)*(prime*prime+1) == len(lines)
    A=np.zeros((2*v,2*v),dtype=float)
    loc={x:i for i,x in enumerate(points)}
    for j,line in enumerate(lines):
        for x in line:
            A[loc[x],v+j]=A[v+j,loc[x]]=1
    assert np.all(A.sum(axis=1)==prime+1)
    return A

def distance(A):
    n=len(A)
    dist=np.full((n,n),-1,dtype=int)
    neighbors=[np.flatnonzero(A[i]) for i in range(n)]
    for root in range(n):
        dist[root,root]=0
        active=[root]
        for level in range(4):
            new=[]
            for x in active:
                for y in neighbors[x]:
                    if dist[root,y]<0:
                        dist[root,y]=level+1
                        new.append(y)
            active=new
    assert np.min(dist)==0 and np.max(dist)==4
    return dist

def check_graph(prime):
    A=symplectic_graph(prime)
    dist=distance(A)
    n=len(A)
    kk=[int(S.expand(a.subs(q,prime))) if hasattr(a,'subs') else int(a) for a in k]
    assert np.all(np.bincount(dist[0],minlength=5)==kk)
    assert all(np.array_equal(np.bincount(dist[i],minlength=5),np.array(kk)) for i in range(n))
    eigen,V=np.linalg.eigh(A)
    E=[]
    for theta in [-(prime+1),-math.sqrt(2*prime),0,math.sqrt(2*prime),prime+1]:
        eigidx=np.flatnonzero(abs(eigen-theta)<1e-7)
        assert len(eigidx)>0
        E.append(V[:,eigidx]@V[:,eigidx].T)
    actual=sum(P*P for P in E)
    expected=np.zeros_like(actual)
    for i,c in enumerate(coeff):
        expected[dist==i]=float(c.subs(q,prime))
    err=float(np.max(np.abs(actual-expected)))
    observed=np.linalg.eigvalsh(actual)
    target=[]
    for theta,mm,lam in zip(val,mul,expected_eigs):
        target.extend([float(lam.subs(q,prime))]*int(mm.subs(q,prime)) if hasattr(mm,'subs') else [float(lam.subs(q,prime))]*int(mm))
    spectrum_err=float(np.max(np.abs(observed-np.array(sorted(target)))))
    assert err<3e-12 and spectrum_err<3e-12, (err,spectrum_err)
    assert observed[0]>0 and np.max(abs(actual.sum(axis=1)-1))<1e-12
    return n,n*n,err,spectrum_err

if __name__=='__main__':
    ci,ei=symbolic_check()
    rows=[check_graph(p) for p in (2,3)]
    print('VERIFY_OK symbolic_distance_coefficients=%d symbolic_eigenvalues=%d finite_graphs=%d matrix_entries=%d max_entry_error=%.3g max_eigen_error=%.3g' %
          (ci,ei,len(rows),sum(t[1] for t in rows),max(t[2] for t in rows),max(t[3] for t in rows)))
