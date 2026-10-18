#!/usr/bin/env python3
"""Independent finite comparison of pair-weight formula with direct cyclic windows."""
from collections import Counter
from itertools import product

def predicted_zero_pairs(p,m):
    # Dense-form operations remain exact integers.
    def mul(a,b):
        c=Counter()
        for i,ai in a.items():
            for j,bj in b.items(): c[i+j]+=ai*bj
        return c
    result=Counter({p**m:1,0:p-1 + p*(p-1)})
    for r in range(1,m):
        a=Counter({0:p-2})
        a[p**(r-1)]+=1
        a[(p-1)*p**(r-1)]+=1
        for j in range(r+2,m+1):
            a=mul(a,Counter({0:p-1,(p-1)*p**(j-2):1}))
        for k,v in a.items():result[k]+=p*(p-1)*v
    return result

def direct_zero_pairs(p,m):
    n=p**m
    vectors=list(product(range(p),repeat=m))
    ans=Counter()
    for a in vectors:
        for c in range(p):
            values=[(sum(a[i]*x[i] for i in range(m))+c)%p for x in vectors]
            cnt=sum(values[j]==0 and values[(j+1)%n]==0 for j in range(n))
            ans[cnt]+=1
    return ans

def test():
    for p,mmax in ((2,5),(3,6),(5,3),(7,3)):
        for m in range(1,mmax+1):
            pred=predicted_zero_pairs(p,m)
            real=direct_zero_pairs(p,m)
            assert pred==real, (p,m,sorted(pred.items()),sorted(real.items()))
            assert sum(pred.values()) == p**(m+1)
            assert real[p**m] == 1
            assert real[0] == p*(p-1)**m+(p-1)
            if m>=2:
                assert max(k for k in real if k < p**m)==p**(m-1)-1
                assert real[p**(m-1)-1]==(p*(p-1) if p>2 else 2*p)
            print('PAIR_OK', 'prime',p,'dimension',m,'codewords',p**(m+1),'distinct_weights',len(real))
    print('VERIFY_OK')
if __name__=='__main__':test()
