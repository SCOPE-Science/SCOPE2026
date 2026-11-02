"""Deterministic finite checks for joint shuffle/occupancy formulas.
No asymptotic inference is drawn from these checks.
"""
from itertools import product, combinations, permutations
from collections import Counter
from fractions import Fraction
from math import comb, factorial

checks = 0

def verify(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def stirling2(n, k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    p=[1]+[0]*k
    for row in range(1,n+1):
        q=[0]*(k+1)
        for j in range(1,min(row,k)+1):
            q[j] = j*p[j]+p[j-1]
        p=q
    return p[k]

def stats(deck, moved):
    n=len(deck); k=len(moved)
    F=sum(deck[i]==i+1 for i in range(n))
    F_top=sum(deck[i]==i+1 for i in range(k))
    J=n-max(moved) if k else n
    Dtop=sum(deck[i]>deck[i+1] for i in range(max(k-1,0)))
    D=sum(deck[i]>deck[i+1] for i in range(n-1))
    return (k,F,F_top,J,Dtop,D)

def brute(n,r):
    c=Counter()
    for seq in product(range(1,n+1),repeat=r):
        deck=list(range(1,n+1))
        for v in seq:
            deck.remove(v);deck.insert(0,v)
        c[stats(deck,set(seq))]+=1
    return c

def construct(n,r):
    c=Counter()
    for k in range(min(n,r)+1):
        weight=stirling2(r,k)
        if not weight: continue
        for subset in combinations(range(1,n+1),k):
            for prefix in permutations(subset):
                rest=[a for a in range(1,n+1) if a not in subset]
                deck=prefix+tuple(rest)
                c[stats(deck,set(subset))]+=weight
    return c

for n in range(2,7):
    for r in range(1,5):
        direct=brute(n,r); constructed=construct(n,r)
        verify(direct==constructed,(n,r,'complete distribution'))
        verify(sum(direct.values())==n**r,(n,r,'total'))
        for (k,F,Ftop,J,Dtop,D),ct in constructed.items():
            verify(F==Ftop+J,(n,r,k,F,Ftop,J,'F decomposition'))
            verify(D in (Dtop,Dtop+1),(n,r,k,'boundary descent'))

for n in range(2,11):
    for k in range(1,n+1):
        sets=list(combinations(range(1,n+1),k))
        # Fixed length k selected prefix, averaging uniformly over moved set.
        mean_eligible=Fraction(sum(sum(x<=k for x in ss) for ss in sets),len(sets))
        verify(mean_eligible==Fraction(k*k,n),(n,k,'hypergeometric mean'))
        mean_J=Fraction(sum(n-max(ss) for ss in sets),len(sets))
        verify(mean_J==Fraction(n-k,k+1),(n,k,'geometric suffix mean'))
        for j in range(n-k+1):
            count=sum(n-max(ss)==j for ss in sets)
            verify(Fraction(count,len(sets))==Fraction(comb(n-j-1,k-1),comb(n,k)),(n,k,j,'suffix law'))
        for t in range(1,5):
            # Conditional factorial-moment identity, then averaged over moved set.
            lhs=Fraction(sum(factorial(m)//factorial(m-t) if m>=t else 0 for m in (sum(x<=k for x in ss) for ss in sets)),len(sets))
            rhs=Fraction(factorial(k)**2,factorial(k-t)**2)/Fraction(factorial(n),factorial(n-t)) if t<=k else 0
            verify(lhs==rhs,(n,k,t,'eligible factorial moment'))

# Exact Eulerian distributions: rank descents are independent of the subset.
for n in range(2,8):
    for k in range(1,n+1):
        standard=Counter(sum(p[i]>p[i+1] for i in range(k-1)) for p in permutations(range(k)))
        for subset in combinations(range(1,n+1),k):
            actual=Counter(sum(p[i]>p[i+1] for i in range(k-1)) for p in permutations(subset))
            verify(actual==standard,(n,k,subset,'Eulerian independence'))

print('OK deterministic_assertions=',checks)

# Conditional finite covariance and boundary-failure identities.
for n in range(3,9):
    for k in range(2,n):
        total=comb(n,k)*factorial(k)
        sumf=sumd=sumfd=sumb0=0
        for ss in combinations(range(1,n+1),k):
            rest=tuple(v for v in range(1,n+1) if v not in ss)
            for pref in permutations(ss):
                f=sum(pref[i]==i+1 for i in range(k))
                d=sum(pref[i]>pref[i+1] for i in range(k-1))
                sumf+=f;sumd+=d;sumfd+=f*d
                sumb0 += int(pref[-1]<rest[0])
        cov=Fraction(sumfd,total)-Fraction(sumf*sumd,total*total)
        verify(cov==Fraction(1-k,n*(n-1)),(n,k,'exact conditional fixed-descent covariance',cov))
        verify(Fraction(sumb0,total)==Fraction(1,n-k+1),(n,k,'boundary failure probability'))
print('OK with covariance tests total_assertions=',checks)
