#!/usr/bin/env python3
"""Independent integer checks for the Italian domination polynomial of crown graphs.
Run with Python 3.9+; uses only the standard library.
"""
from collections import Counter
from itertools import product
from math import comb

def add(*arrays):
    length=max(map(len,arrays))
    return [sum(a[i] if i < len(a) else 0 for a in arrays) for i in range(length)]

def scale(a,k):
    return [k*x for x in a]

def shift(a,k):
    return [0]*k+list(a)

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]+=x*y
    return r

def power(a,n):
    r=[1]
    for _ in range(n): r=mul(r,a)
    return r

def truncate4(a):
    return [0 if i<4 else x for i,x in enumerate(a)]

def coefficients(n):
    if n<4: raise ValueError('requires n>=4')
    P=[1,1,1]; R=[0,1,1]
    H=truncate4(power(P,n))
    B0=power(R,n)
    B1=scale(B0,n)
    B2=add(scale(mul(R,power(P,n-1)),n),
           scale(mul(power(R,2),power(P,n-2)),comb(n,2)))
    B3=add(scale(mul(R,power(P,n-1)),n*(n-1)),
           scale(power(P,n),comb(n,3)))
    low=[0]*7
    low[4]=n+comb(n,2)
    low[5]=2*n*n*(n-1)
    low[6]=comb(n,3)**2+n*(n-1)**2*(n-2)+n*n*(n-1)
    res=add(mul(H,H), low)
    for a,b in enumerate([B0,B1,B2,B3]):
        res=add(res,scale(shift(truncate4(b),a),2))
    return tuple(res+[0]*max(0,4*n+1-len(res)))

def direct_adjacency(n):
    # Vertex labels 0..n-1 are A, n..2n-1 are B.
    return [tuple((n+j for j in range(n) if j !=i)) for i in range(n)]+[tuple(i for i in range(n) if i !=j) for j in range(n)]

def direct_enum(n):
    neighbors=direct_adjacency(n)
    out=[0]*(4*n+1)
    seen=0
    for labels in product((0,1,2),repeat=2*n):
        seen+=1
        if all(labels[i] !=0 or sum(labels[j] for j in nb)>=2
               for i,nb in enumerate(neighbors)):
            out[sum(labels)]+=1
    return tuple(out),seen

def conditional_pair_dp(n):
    # Method independent of the partition formula: enumerate exact side totals
    # and use the original per-index defense condition to form pair transitions.
    out=[0]*(4*n+1)
    for U in range(2*n+1):
        for V in range(2*n+1):
            allowed=[(a,b) for a in range(3) for b in range(3)
                     if (a or V-b>=2) and (b or U-a>=2)]
            if not allowed: continue
            dp={(0,0):1}
            for _ in range(n):
                nd=Counter()
                for (u,v),c in dp.items():
                    for a,b in allowed:
                        if u+a<=U and v+b<=V:
                            nd[(u+a,v+b)]+=c
                dp=nd
                if not dp:break
            out[U+V]+=dp.get((U,V),0)
    return tuple(out)

def main():
    examined=0
    for n in range(3,7):
        brute,cases=direct_enum(n)
        examined+=cases
        dp=conditional_pair_dp(n)
        assert brute==dp,(n,'direct versus pair DP')
        if n>=4: assert brute==coefficients(n),(n,'direct versus closed form')
    for n in range(7,11):
        dp=conditional_pair_dp(n)
        assert dp==coefficients(n),(n,'pair DP versus closed form')
    for n in range(4,11):
        p=coefficients(n)
        assert all(x==0 for x in p[:4])
        assert p[4]==n*(n+1)//2+(2 if n==4 else 0)
        assert p[4*n]==1
    print('VERIFY_OK direct_graph_labelings=%s n=3..6 independent_pair_DP_n=3..10 full_coefficient_matches_n=4..10' % examined)

if __name__=='__main__':main()
