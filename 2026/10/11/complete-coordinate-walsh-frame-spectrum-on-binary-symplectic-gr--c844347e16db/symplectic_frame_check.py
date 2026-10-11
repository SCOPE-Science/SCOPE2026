"""Exact finite checks for coordinate Walsh frames on binary symplectic groups.

Requires Python 3.10+ and sympy; NumPy is used only for reported numerical eigenvalues.
No external data or network service is needed.
"""
from collections import deque
from fractions import Fraction
import sympy as sp
import numpy as np


def dot(a, b):
    return (a & b).bit_count() % 2


def symp(a, b, d):
    m = d // 2
    mask = (1 << m) - 1
    return dot(a & mask, b >> m) ^ dot(a >> m, b & mask)


def mate(i, d):
    return (i + d // 2) % d


def transvection(matrix, v, d):
    return tuple(col ^ (v if symp(col, v, d) else 0) for col in matrix)


def symplectic_group_four():
    d = 4
    identity = tuple(1 << i for i in range(d))
    seen = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for v in range(1, 1 << d):
            h = transvection(g, v, d)
            if h not in seen:
                seen.add(h)
                queue.append(h)
    assert len(seen) == 720
    assert all(symp(g[j], g[k], d) == (1 if k == mate(j, d) else 0)
               for g in seen for j in range(d) for k in range(d))
    return seen


def constants(d):
    Q = 2 ** d
    beta = Fraction(-1, Q - 1)
    aa = Fraction(Q + 4, (Q - 1) * (Q - 4))
    gg = Fraction(1, Q - 1)
    return beta, aa, gg


def predicted_gram(d):
    beta, aa, gg = constants(d)
    G = [[Fraction(0) for _ in range(d*d+1)] for _ in range(d*d+1)]
    for j in range(1, d*d+1):
        G[0][j] = G[j][0] = beta
    G[0][0] = Fraction(1)
    for a in range(d*d):
        i,j = divmod(a,d)
        for b in range(d*d):
            k,l = divmod(b,d)
            if a == b:
                v = Fraction(1)
            elif i != k and j != l and k != mate(i,d) and l != mate(j,d):
                v = aa
            elif i != k and j != l and k == mate(i,d) and l == mate(j,d):
                v = gg
            else:
                v = beta
            G[a+1][b+1] = v
    return G


def direct_gram(group):
    d = 4
    G = np.zeros((1+d*d, 1+d*d), dtype=np.int64)
    for g in group:
        z = np.ones(1+d*d, dtype=np.int64)
        for i in range(d):
            for j in range(d):
                z[1+i*d+j] = 1 if ((g[j] >> i) & 1) == 0 else -1
        G += np.outer(z,z)
    return G


def check_pair_enumeration(d):
    Q = 2 ** d
    for c in (0,1):
        pairs = [(v,w) for v in range(1,Q) for w in range(1,Q)
                 if v != w and symp(v,w,d) == c]
        expected_count = (Q-1)*(Q//2 if c else Q//2-2)
        assert len(pairs) == expected_count
        # Same-row/same-column, paired and nonpaired row covectors.
        for (i,k) in [(0,0), (0,1), (0,d//2)]:
            observed = Fraction(sum(1 if ((v>>i) ^ (w>>k)) & 1 == 0 else -1
                                    for v,w in pairs), len(pairs))
            beta,aa,gg = constants(d)
            if i == k:
                target = beta
            elif k == mate(i,d):
                target = gg if c else beta
            else:
                target = beta if c else aa
            assert observed == target, (d,c,i,k,observed,target)
    return 6


def block_eigenvalues(d):
    Q = 2**d
    beta = Fraction(-1,Q-1)
    A = Fraction(2*Q,(Q-1)*(Q-4))
    B = Fraction(2,Q-1)
    base = Fraction(Q,Q-1)
    uu = base + beta*d*d + A*(d-2)**2 + B
    uv = base - 2*A*(d-2) + B
    uw = base - B
    vv = base + 4*A + B
    ww = base + B
    h = beta*d
    return uu,uv,uw,vv,ww,h


def verify_symbolic():
    Q,d = sp.symbols('Q d')
    beta=-1/(Q-1)
    A=2*Q/((Q-1)*(Q-4))
    B=2/(Q-1)
    base=Q/(Q-1)
    uu=base+beta*d*d+A*(d-2)**2+B
    uv=base-2*A*(d-2)+B
    vv=base+4*A+B
    h=beta*d
    Dmin=sp.factor((1-uv)*(uu-uv)-h*h)
    Dmax=sp.factor((1-vv)*(uu-vv)-h*h)
    expected_min=4*d*(Q**2*(d*d-7*d+11)+Q*(4*d*d-6*d-12)+8*d)/((Q-4)**2*(Q-1)**2)
    expected_max=-4*d*(Q**2*(3*d-22)+Q*(6*d+24)-8*d)/((Q-4)**2*(Q-1)**2)
    assert sp.cancel(Dmin-expected_min)==0
    assert sp.cancel(Dmax-expected_max)==0
    assert sp.cancel(uv-(Q**2+(6-4*d)*Q-8)/((Q-1)*(Q-4))) == 0


def check_eigenspaces(d):
    G=sp.Matrix(predicted_gram(d))
    uu,uv,uw,vv,ww,h=block_eigenvalues(d)
    m=d//2
    one=sp.ones(d,1)
    U=one
    E=sp.eye(d)
    V=[E[:,j]+E[:,j+m]-E[:,0]-E[:,m] for j in range(1,m)]
    W=[sp.eye(d)[:,j]-sp.eye(d)[:,j+m] for j in range(m)]
    # Tensor row x column, coordinates (i,j) with j varying fast.
    modes={"U":[U],"V":V,"W":W}
    spec={('U','V'):uv,('V','U'):uv,('U','W'):uw,('W','U'):uw,
          ('V','V'):vv,('V','W'):uw,('W','V'):uw,('W','W'):ww}
    seen=0
    for (a,b),value in spec.items():
        for x in modes[a]:
            for y in modes[b]:
                v=sp.Matrix([0]+list(sp.kronecker_product(x,y)))
                assert G*v == value*v, (d,a,b,value)
                seen+=1
    e0=sp.Matrix([1]+[0]*(d*d))
    u=sp.Matrix([0]+[sp.Rational(1,d)]*(d*d))
    assert G*e0 == e0+h*u
    assert G*u == h*e0+uu*u
    assert seen == d*d-1


def main():
    verify_symbolic()
    group=symplectic_group_four()
    direct=direct_gram(group)
    formula=predicted_gram(4)
    expected=np.asarray([[int(x*len(group)) for x in row] for row in formula],dtype=np.int64)
    assert np.array_equal(direct, expected)
    for d in (4,6,8):
        assert check_pair_enumeration(d) == 6
    for d in (4,6):
        check_eigenspaces(d)
    eig_direct=sorted(np.linalg.eigvalsh(direct/len(group)))
    uu,uv,uw,vv,ww,h=block_eigenvalues(4)
    lp=(1+float(uu)+np.sqrt((1-float(uu))**2+4*float(h)**2))/2
    lm=(1+float(uu)-np.sqrt((1-float(uu))**2+4*float(h)**2))/2
    theory=sorted([lm,lp]+[float(uv)]*2+[float(uw)]*8+[float(vv)]*1+[float(ww)]*4)
    assert np.allclose(eig_direct,theory,atol=1e-12,rtol=0)
    for m in range(2,65):
        d=2*m; Q=2**d
        pmin=Q*Q*(d*d-7*d+11)+Q*(4*d*d-6*d-12)+8*d
        pmax=Q*Q*(3*d-22)+Q*(6*d+24)-8*d
        assert pmin>0
        assert (pmax<0) if m<=3 else (pmax>0)
    print("VERIFY_OK Sp4_size=720 Gram_entry_checks=289 eigenspace_dimensions=17,37 pair_tests=18 symbolic_determinants=2 threshold_dimensions=63")

if __name__ == '__main__':
    main()
