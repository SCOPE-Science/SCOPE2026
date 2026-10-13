#!/usr/bin/env python3
"""Finite checks for palindromic-periodicity enumeration identities.
These checks complement, and do not replace, the asymptotic proof.
"""
from itertools import product

def is_pal(x):
    return x == x[::-1]

def root_models(d):
    for c in range(d):
        a,b=c,d-c
        for p in product('01', repeat=(a+1)//2):
            # Construct direct palindrome with index-reflection to avoid ambiguities.
            P=''.join(p[i] if i<(a+1)//2 else p[a-1-i] for i in range(a))
            for s in product('01', repeat=(b+1)//2):
                S=''.join(s[i] if i<(b+1)//2 else s[b-1-i] for i in range(b))
                yield c,P+S

def s_formula(d):
    return (3*d*(1<<(d//2))//2 if d%2==0 else d*(1<<((d+1)//2)))

def union_enumerate(n):
    seen=set()
    for d in range(1,n+1):
        count=0
        for c,u in root_models(d):
            count+=1
            seen.add((u*((n+d-1)//d))[:n])
        assert count==s_formula(d),(n,d,count,s_formula(d))
    return seen

def direct(n,w):
    for d in range(1,n+1):
        if any(w[i]!=w[i-d] for i in range(d,n)):continue
        root=w[:d]
        if any(is_pal(root[:c]) and is_pal(root[c:]) for c in range(d)):
            return True
    return False

# Known table from OEIS A374495, first terms checked against original data.
known={i+1:x for i,x in enumerate((2,4,8,16,32,58,108,190,336,560,948,1574,2568,4116,6596,10444,16320,25488,39216,60690,92204,141060))}
for n in range(1,13):
    union=union_enumerate(n)
    verified={''.join(x) for x in product('01',repeat=n) if direct(n,''.join(x))}
    assert union==verified,('direct_model_disagreement',n)
    assert len(union)==known[n],('OEIS',n,len(union))
for n in (16,18,20):
    cnt=len(union_enumerate(n))
    assert cnt==known[n],('OEIS',n,cnt)
print('VERIFY_OK independent_predicate_n=1..12 OEIS_n=1..12,16,18,20 parameter_models_match_formulas')
