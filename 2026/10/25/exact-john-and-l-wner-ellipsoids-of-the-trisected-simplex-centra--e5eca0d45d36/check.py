"""Exact rational checks for the trisected-simplex ellipsoid formulas.

Uses only Python's standard library; supports any m >= 3.
Finite tests corroborate the stated all-dimension symbolic proof.
"""
from fractions import Fraction as Q
from math import comb


def critical_k(m):
    q, rem = divmod(m, 3)
    return 2*q if rem == 0 else (2*q+1)


def distance2(m,k):
    return Q(k*(m-k), m*(2*m-k)**2)


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)), Q(0))


def verify(m):
    assert m >= 3
    ones = [Q(1)]*m
    bary = [Q(1,m)]*m
    vlist = []
    for mask in range(1,(1<<m)-1):
        k = mask.bit_count()
        v = [Q(1,2*m-k) if (mask >> i)&1 else Q(2,2*m-k)
             for i in range(m)]
        assert sum(v) == 1
        assert all(v[i] <= 2*v[j] for i in range(m) for j in range(m))
        assert dot([z-b for z,b in zip(v,bary)], [z-b for z,b in zip(v,bary)]) == distance2(m,k)
        vlist.append((mask,k,v))
    kstar = critical_k(m)
    radius2 = distance2(m,kstar)
    assert radius2 == max(distance2(m,k) for k in range(1,m))
    assert sum(k == kstar for _,k,_ in vlist) == comb(m,kstar)
    assert all(distance2(m,k) < radius2 for k in range(1,m) if k != kstar)
    norms=[]
    for i in range(m):
        for j in range(m):
            if i==j: continue
            a=[Q(0)]*m
            a[i]+=1
            a[j]-=2
            a=[z+Q(1,m) for z in a]
            norms.append(a)
            assert sum(a) == 0
            assert dot(a,a) == Q(5)-Q(1,m)
            assert dot(a,bary) == 0
    assert len(norms)==m*(m-1)
    # The facet-normal tight frame, before unit normalization.
    normal_cov=[[sum(a[i]*a[j] for a in norms) for j in range(m)] for i in range(m)]
    normal_scale=5*m-1
    assert all(normal_cov[i][j] == normal_scale*(int(i==j)-Q(1,m)) for i in range(m) for j in range(m))
    # A maximizing vertex orbit is centered and isotropic.
    outer = [v for _,k,v in vlist if k==kstar]
    assert all(sum(v[i]-bary[i] for v in outer)==0 for i in range(m))
    cv=[[sum((v[i]-bary[i])*(v[j]-bary[j]) for v in outer) for j in range(m)] for i in range(m)]
    scale=Q(len(outer),m-1)*radius2
    assert all(cv[i][j]==scale*(int(i==j)-Q(1,m)) for i in range(m) for j in range(m))
    # Inradius squared: all facet distances equal at the centroid.
    assert Q(1,m**2)/Q(5-Q(1,m)) == Q(1,m*(5*m-1))
    return (m,kstar,comb(m,kstar),str(radius2),str(Q(1,m*(5*m-1))))


if __name__ == '__main__':
    for m in range(3,11):
        print(*verify(m))
    for m in range(11,26):
        k=critical_k(m)
        assert k==max(range(1,m),key=lambda j:distance2(m,j))
    print('PASS: exact vertex and contact identities through m=10; index law through m=25')
