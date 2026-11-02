"""Exact rational certificate for four-dimensional antipodal-boundary visibility."""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import Counter

WEIGHTS = {
    0: (2, 2, 2, 2, 2),
    1: (1, 1, 1, 4, 4),
    2: (1, 1, 2, 3, 4),
    3: (1, 1, 3, 3, 3),
    4: (1, 1, 1, 3, 5),
}

def solve(A, b):
    a = [[Q(v) for v in row] + [Q(z)] for row, z in zip(A,b)]
    n=len(a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        assert k is not None, 'affine-degeneracy'
        a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        a[j]=[x/pivot for x in a[j]]
        for i in range(n):
            if i==j:continue
            c=a[i][j]
            a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

for d,w in WEIGHTS.items():
    W=sum(w)
    assert 2*max(w)<W
    assert all(2*(w[i]+w[j])!=W for i,j in combinations(range(5),2))
    dominant=[(i,j) for i,j in combinations(range(5),2) if 2*(w[i]+w[j])>W]
    assert len(dominant)==d,(d,dominant)
    # Five rank-four columns; their sole dependence has exactly weights w.
    v = [[Q(int(i==j)) for i in range(4)] for j in range(4)]
    v.append([Q(-w[k],w[4]) for k in range(4)])
    assert all(sum(Q(w[i])*v[i][k] for i in range(5))==0 for k in range(4))
    # With a unique relation, representation of v_i by other ±v_j
    # has l1 coefficient sum (W-w_i)/w_i>1: all ±v_i are vertices.
    assert all(Q(W-wi,wi)>1 for wi in w)
    histogram=Counter()
    for eps in product([-1,1],repeat=5):
        z=[[Q(s)*x for x in vi] for s,vi in zip(eps,v)]
        matrix=[[z[i][k] for i in range(5)] for k in range(4)] + [[Q(1)]*5]
        lam=solve(matrix,[Q(0)]*4+[Q(1)])
        theoretical=tuple(Q(eps[i]*w[i],sum(eps[k]*w[k] for k in range(5))) for i in range(5))
        assert lam==theoretical
        assert sum(lam)==1
        assert all(sum(lam[i]*z[i][k] for i in range(5))==0 for k in range(4))
        histogram[sum(x<0 for x in lam)]+=1
    assert histogram==Counter({0:2,1:10,2:20-2*d,3:2*d}),(w,histogram)
    print('D',d,'weights',w,'dominant_pairs',dominant,'32_sign_histogram',dict(sorted(histogram.items())))
print('ALL_EXACT_VISIBILITY_CHECKS_PASSED')
