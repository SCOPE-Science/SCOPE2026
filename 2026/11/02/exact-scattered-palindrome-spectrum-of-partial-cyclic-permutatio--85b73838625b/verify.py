#!/usr/bin/env python3
"""Independent finite verification of cyclic-permutation-prefix scattered-palindrome spectra.
All counts distinguish target words (not their number of embeddings). Stdlib-only.
"""
from itertools import combinations,product
from collections import Counter
from math import comb

def literal(q,k,s):
    w=tuple(range(q))*k+tuple(range(s))
    found=set()
    for length in range(1,len(w)+1):
        for ix in combinations(range(len(w)),length):
            u=tuple(w[i] for i in ix)
            if u==u[::-1]:found.add(u)
    return Counter(map(len,found)),found

def binomial(n,r):
    return comb(n,r) if 0<=r<=n else 0

def predicted(q,k,s):
    result={}
    for m in range(k+1):
        odd=q*sum(comb(m,e)*(q-1)**(m-e) for e in range(max(0,min(m,k-m-1)+1)))
        if 0<=k-m<=m:odd+=s*comb(m,k-m)*(q-1)**(2*m-k)
        if odd:result[2*m+1]=odd
        if m>=1:
            even=q*sum(comb(m-1,e)*(q-1)**(m-1-e) for e in range(max(0,min(m-1,k-m-1)+1)))
            if 0<=k-m<=m-1:even+=s*comb(m-1,k-m)*(q-1)**(2*m-1-k)
            if even:result[2*m]=even
    return result

def criterion(u,q,k,s):
    if not u or u!=u[::-1]:return False
    m=len(u)//2
    half=u[:m+1] if len(u)%2 else u[:m]
    equal=sum(a==b for a,b in zip(half,half[1:]))
    cost=m+equal
    return (cost<k or (cost==k and u[0]<s))

def gf(q,k,s):
    # Extract coefficient z^k from [q*u*z(1+u*z)/(1-z)
    # +s*u^2*z*(1+u*(q-1+z))]/[1-u^2*z*(q-1+z)]
    a=[{0:1}]
    for j in range(1,k+1):
        t={}
        for d,c in a[j-1].items():t[d+2]=t.get(d+2,0)+(q-1)*c
        if j>=2:
            for d,c in a[j-2].items():t[d+2]=t.get(d+2,0)+c
        a.append(t)
    out={}
    for j in range(k):
        for d,c in a[j].items():out[d+1]=out.get(d+1,0)+q*c
    for j in range(k-1):
        for d,c in a[j].items():out[d+2]=out.get(d+2,0)+q*c
    for d,c in a[k-1].items():
        out[d+2]=out.get(d+2,0)+s*c
        out[d+3]=out.get(d+3,0)+s*(q-1)*c
    if k>=2:
        for d,c in a[k-2].items():out[d+3]=out.get(d+3,0)+s*c
    return {d:v for d,v in out.items() if v}

def main():
    cases=0;pal_words=0; coeffs=0; target_tests=0
    for q in range(2,6):
        for k in range(1,6):
            for s in range(q):
                if q*k+s>16:continue
                counts,words=literal(q,k,s)
                assert counts==Counter(predicted(q,k,s)),(q,k,s,counts,predicted(q,k,s))
                assert all(criterion(u,q,k,s) for u in words)
                for length in range(1,min(q*k+s+2,10)):
                    for half in product(range(q),repeat=(length+1)//2):
                        u=half+half[-2::-1] if length%2 else half+half[::-1]
                        assert (u in words)==criterion(u,q,k,s),(q,k,s,u)
                        target_tests+=1
                cases+=1;pal_words+=len(words)
    for q in range(3,10):
        for k in range(1,35):
            for s in range(q):
                assert predicted(q,k,s)==gf(q,k,s),(q,k,s)
                coeffs+=len(gf(q,k,s))
    print(f'VERIFY_OK literal_parameter_cases={cases} literal_palindromes={pal_words} palindrome_membership_tests={target_tests} exact_formal_coefficients={coeffs} q=3..9 k=1..34 all_prefixes=yes')
if __name__=='__main__':main()
