"""Exact rational checks for grounded inverse-square leader placements on K_{2,q}."""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def invert(a):
    n=len(a)
    t=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        r=next((r for r in range(i,n) if t[r][i]),None)
        assert r is not None
        t[i],t[r]=t[r],t[i]
        pivot=t[i][i]
        t[i]=[v/pivot for v in t[i]]
        for j in range(n):
            if j==i: continue
            f=t[j][i]
            if f:t[j]=[u-f*v for u,v in zip(t[j],t[i])]
    return [row[n:] for row in t]


def direct(q,leaders):
    n=q+2
    ff=[i for i in range(n) if i not in leaders]
    m=[]
    for i in ff:
        row=[]
        for j in ff:
            if i==j:row.append(q if i<2 else 2)
            elif (i<2)!=(j<2):row.append(-1)
            else:row.append(0)
        m.append(row)
    inv=invert(m)
    return sum((inv[i][j]**2 for i in range(len(ff)) for j in range(len(ff))),F(0))


def costs(q,k):
    h=q-k
    return (
        F(h-1,4)+F(1,q*q)+F(q*q+4*h+4,4*k*k),
        F(h,4)+F(q*q+2*h+6,(q+k-1)**2),
        F(h+2,4),
    )


def main():
    exhaustive=0
    cases=0
    for q in range(2,9):
        for k in range(2,q+1):
            c=costs(q,k)
            for S in combinations(range(q+2),k):
                got=direct(q,S)
                a=len(set(S)&{0,1})
                assert got==c[a],(q,k,S,got,c[a])
                exhaustive+=1
            cases+=1
    representatives=0
    for q in range(2,23):
        for k in range(2,q+1):
            c=costs(q,k)
            for a in range(3):
                S=tuple(range(a))+tuple(range(2,2+k-a))
                assert direct(q,S)==c[a]
                representatives+=1
    winners=0
    for q in range(2,32):
        for k in range(2,q+1):
            c=costs(q,k)
            # Check exact sign identities used in the proof.
            d12=F(q*q+(6-2*k)*q+11-2*k-k*k,2*(q+k-1)**2)
            d02=F((q+2)**2,4*k*k)-F(1,k)-F(3,4)+F(1,q*q)
            assert c[1]-c[2]==d12
            assert c[0]-c[2]==d02
            winners+=1
    # A genuine mixed optimum exists in both exact instances.
    for q in (11,12):
        c=costs(q,7)
        assert c[1]<c[0] and c[1]<c[2]
    # An exact boundary for the one-hub versus two-hub alternatives.
    c=costs(22,11)
    assert c[1]==c[2] and c[0]>c[1]
    # The small-budget qualitative comparisons.
    for q in range(3,40):
        c=costs(q,2)
        assert c[2]<c[0] and c[2]<c[1]
    print('VERIFY_OK')
    print('exhaustive_subsets',exhaustive)
    print('exhaustive_parameter_pairs',cases)
    print('additional_representative_inverses',representatives)
    print('exact_pairwise_difference_checks',winners)
    print('mixed_optimum_k7_q11',tuple(map(str,costs(11,7))))
    print('mixed_optimum_k7_q12',tuple(map(str,costs(12,7))))
    print('tie_k11_q22',tuple(map(str,costs(22,11))))

if __name__=='__main__':main()
