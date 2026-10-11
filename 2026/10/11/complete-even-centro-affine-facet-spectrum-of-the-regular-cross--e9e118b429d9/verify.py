from fractions import Fraction
from itertools import product, combinations
from math import comb

for n in range(2,9):
    verts=list(product((-1,1), repeat=n))
    m=Fraction(1,1)
    # Common scaling by (n-1)! turns the true mass into 1.
    # Under the same scaling, true conductance becomes (n-1)/2.
    c=Fraction(n-1,2)
    seen_even={}
    for k in range(n+1):
        count=0
        for S in combinations(range(n),k):
            S=set(S)
            vals={v: (-1 if sum(1 for i in S if v[i]==-1)%2 else 1) for v in verts}
            for v in verts:
                lhs=Fraction(0)
                for i in range(n):
                    w=list(v); w[i]*=-1; w=tuple(w)
                    lhs += c*(vals[v]-vals[w])
                rhs=m*Fraction((n-1)*k)*vals[v]
                assert lhs==rhs, (n,k,S,v,lhs,rhs)
                nv=tuple(-x for x in v)
                assert vals[nv] == ((-1)**k)*vals[v]
            count+=1
        assert count==comb(n,k)
        if k%2==0:
            seen_even[(n-1)*k]=count
    assert seen_even[0]==1
    assert seen_even[2*(n-1)]==comb(n,2)
print('VERIFY_OK n=2..8 full_Walsh_spectrum')
