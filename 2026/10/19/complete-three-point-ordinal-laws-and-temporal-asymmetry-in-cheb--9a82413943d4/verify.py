"""Exact independent piecewise-linear checks of three-point ordinal laws.

Run: python3 verify.py. Only standard-library modules are used.
The finite checks complement (and do not replace) the general proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations

PERMS = tuple(permutations((0, 1, 2)))

def exact_geometry(q):
    """Partition into q*q affine cells; integrate each strict rank region exactly."""
    m = q*q
    result = defaultdict(lambda: Q(0))
    for j in range(m):
        k = j//q
        a1,b1 = (q,-k) if k%2==0 else (-q,k+1)
        a2,b2 = (m,-j) if j%2==0 else (-m,j+1)
        affine = ((1,0),(a1,b1),(a2,b2))
        lo,hi = Q(j,m),Q(j+1,m)
        knots={lo,hi}
        for i in range(3):
            for h in range(i+1,3):
                ai,bi=affine[i]; ah,bh=affine[h]
                if ai != ah:
                    z=Q(bh-bi,ai-ah)
                    if lo<z<hi:knots.add(z)
        knots=sorted(knots)
        for a,b in zip(knots,knots[1:]):
            mid=(a+b)/2
            values=[s*mid+t for s,t in affine]
            perm=tuple(sorted(range(3),key=values.__getitem__))
            result[perm]+=b-a
    return {p:result[p] for p in PERMS}

def predicted(q):
    n2=q*q
    if q%2:
        return {(0,1,2):Q(1,6), (2,1,0):Q(1,6),
                (0,2,1):Q(n2+2,6*(n2+1)),
                (1,2,0):Q(n2+2,6*(n2+1)),
                (1,0,2):Q(n2,6*(n2+1)),
                (2,0,1):Q(n2,6*(n2+1))}
    return {(0,1,2):Q(n2+2,6*(n2-1)),
            (2,1,0):Q(n2-4,6*(n2-1)),
            (0,2,1):Q(n2*n2-2*n2-2,6*(n2*n2-1)),
            (1,2,0):Q(n2+2,6*(n2+1)),
            (1,0,2):Q(n2,6*(n2+1)),
            (2,0,1):Q(n2*(n2+2),6*(n2*n2-1))}

def pair_formula(q):
    return Q(q*q,2*(q*q-1)) if q%2==0 else Q(1,2)

def reversal_distance(p):
    """Time reversal relabels the three sampling times i->2-i."""
    return sum(abs(p[k]-p[tuple(2-i for i in k)]) for k in PERMS)/2

def predicted_reversal(q):
    if q%2:
        return Q(2,3*(q*q+1))
    return Q(2*q*q+1,q**4-1)

def prove_finite_sum_values(q):
    """Two finite-sum reductions from the proof, exact for each tested q."""
    n=q; m=n*n
    a=Q(0)
    for j in range(n):
        if j%2 == 0:
            a += Q((j+1)*(n-1-j),n*n*(n-1))
        else:
            a += Q(j*(n-j),n*n*(n+1))
    A=lambda k:Q(k*(2*m-k),2)
    c=Q(0)
    for j in range(n):
        if j%2 == 0:
            c += (A(j*(n+1))-A(j*n))/(m*m-1)
        else:
            c += (A((j+1)*n)-A((j+1)*(n-1)))/(m*m-1)
    want=predicted(n)
    assert a==want[(0,1,2)],(n,'a',a,want[(0,1,2)])
    assert c==want[(1,0,2)],(n,'c',c,want[(1,0,2)])


def main():
    checked=0
    for q in list(range(2,65))+[72,81,96,125,128]:
        obs=exact_geometry(q)
        exp=predicted(q)
        assert obs==exp,(q,obs,exp)
        assert sum(obs.values())==1
        assert sum(obs[p] for p in PERMS if p.index(0)<p.index(1))==pair_formula(q)
        assert sum(obs[p] for p in PERMS if p.index(0)<p.index(2))==pair_formula(q*q)
        assert reversal_distance(obs)==predicted_reversal(q)
        prove_finite_sum_values(q)
        checked+=1
    print('VERIFY_OK: %d exactly integrated degrees; six ranks, lag-one/two pair laws, temporal reversal and both finite-sum identities'%checked)

if __name__=='__main__':main()
