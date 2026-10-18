"""Independent finite checks of minimum Italian domination on rook graphs.

Run: python3 verify_italian_rook.py
"""
from itertools import combinations
from math import comb, factorial


def onto(n, m):
    # Inclusion-exclusion for surjections from columns to rows.
    return sum((-1)**j * comb(m,j)*(m-j)**n for j in range(m+1))


def conjectured_count(m,n):
    assert 2<=m<=n
    a=(n+comb(n,2))**m
    b=onto(n,m)
    if n<2*m:
        return b
    if n>2*m:
        return a
    return a+b-factorial(n)//(2**m)


def count_below_or_equal(m,n):
    N=m*n
    nbr=[]
    for i in range(m):
        for j in range(n):
            nbr.append(tuple(i*n+k for k in range(n) if k!=j)+
                       tuple(k*n+j for k in range(m) if k!=i))
    target=min(n,2*m)
    counts=[0]*(target+1)
    indices=range(N)
    for w in range(target+1):
        for n2 in range(w//2+1):
            n1=w-2*n2
            if n1+n2>N: continue
            for twos in combinations(indices,n2):
                two_set=set(twos)
                remaining=(v for v in indices if v not in two_set)
                # Materialize to permit multiple combinational choices.
                remaining=tuple(remaining)
                for ones in combinations(remaining,n1):
                    labels=[0]*N
                    for v in twos: labels[v]=2
                    for v in ones: labels[v]=1
                    if all(labels[v]!=0 or sum(labels[u] for u in nbr[v])>=2
                           for v in indices):
                        counts[w]+=1
    return counts


def main():
    tests=[(2,n) for n in range(2,11)]
    tests +=[(3,n) for n in range(3,10)]
    tests +=[(4,n) for n in range(4,7)]
    for m,n in tests:
        a=count_below_or_equal(m,n)
        gamma=min(n,2*m)
        assert all(c==0 for c in a[:gamma]),(m,n,a)
        predicted=conjectured_count(m,n)
        assert a[gamma]==predicted,(m,n,a[gamma],predicted)
        print(f'{m}x{n}: gamma={gamma}, optimal_count={a[gamma]}')
    print('VERIFICATION_OK', len(tests))

if __name__=='__main__':
    main()
