#!/usr/bin/env python3
from functools import lru_cache
from pathlib import Path
import json

TAU={0:(0,1,2),1:(2,0,1),2:(1,2,0)}

def tau_word(w):
    return tuple(y for a in w for y in TAU[a])

def iterate(seed,k):
    w=tuple(seed)
    for _ in range(k):
        w=tau_word(w)
    return w

def x_digit(n):
    # Alternating ternary digit sum, low digit with positive sign.
    s=0
    sign=1
    while n:
        n,r=divmod(n,3)
        s=(s+sign*r)%3
        sign=-sign
    return s%3

@lru_cache(None)
def D(q):
    if q==0:
        return frozenset((0,))
    if q==1:
        return frozenset((0,1))
    if q==2:
        return frozenset((1,2))
    m,r=divmod(q,3)
    if r==0:
        return frozenset((-d)%3 for d in D(m))
    if r==1:
        return frozenset({(1-d)%3 for d in D(m)} | {(1-d)%3 for d in D(m+1)})
    return frozenset({(2-d)%3 for d in D(m)} | {(2-d)%3 for d in D(m+1)})

def expected_D(q):
    if q==0:
        return frozenset((0,))
    z=q
    k=0
    while z%3==0:
        z//=3
        k+=1
    if z==1:
        return frozenset((0,1 if k%2==0 else 2))
    if z==2:
        return frozenset((1,2))
    return frozenset((0,1,2))

def special3(n):
    if n==1:
        return True
    p=3
    e=1
    while p+1<=n:
        if e%2==1 and n==p+1:
            return True
        p*=3
        e+=1
    p=9
    e=2
    while p-1<=n:
        if e%2==0 and n==p-1:
            return True
        p*=3
        e+=1
    return False

def expected_complexity(n):
    if n%3==0:
        return 7
    if special3(n):
        return 3
    return 6

def direct_complexity(w,n):
    c=[0,0,0]
    for a in w[:n]:
        c[a]+=1
    seen={tuple(c)}
    for j in range(n,len(w)):
        c[w[j-n]]-=1
        c[w[j]]+=1
        seen.add(tuple(c))
    return len(seen),seen

# Basic morphism facts and coordinate formula.
for a in range(3):
    assert sorted(TAU[a])==[0,1,2]
    for r in range(3):
        assert TAU[a][r] == (r-a)%3

W=iterate((0,),11)
assert len(W)==3**11
for n in range(len(W)):
    assert W[n]==x_digit(n)
for n in range((len(W)-2)//3):
    for r in range(3):
        assert W[3*n+r] == (r-W[n])%3

# Exact recurrence and classification of the difference sets.
for q in range(0,20001):
    assert D(q)==expected_D(q),(q,D(q),expected_D(q))

# Directly sample the true difference sets from a large prefix and compare
# with the exact recursive sets for moderate shifts.
for q in range(1,1001):
    sampled={(W[i+q]-W[i])%3 for i in range(len(W)-q)}
    assert sampled==D(q),(q,sampled,D(q))

# Translation symmetry of the substitution language.
def translate(w,c):
    return tuple((a+c)%3 for a in w)
for k in range(0,8):
    for a in range(3):
        for c in range(3):
            lhs=iterate(((a+c)%3,),k)
            rhs=translate(iterate((a,),k), ((-1)**k*c)%3)
            assert lhs==rhs

# Direct factor-Parikh stress check.  The theorem is symbolic; these are
# independent finite replays against a long fixed-point prefix.
for n in range(1,251):
    got,_=direct_complexity(W,n)
    assert got==expected_complexity(n),(n,got,expected_complexity(n))

for n in [244,245,728,729,730,2188,2189,6560,6561,6562,10000]:
    got,_=direct_complexity(W,n)
    assert got==expected_complexity(n),(n,got,expected_complexity(n))

# Check the exact first exceptional positions.
special=[n for n in range(1,10000) if expected_complexity(n)==3]
assert special==[1,4,8,28,80,244,728,2188,6560]

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["source_primary_msc"]=="68Q45"
assert cert["morphism"]=={"0":"012","1":"201","2":"120"}

print(
    "VERIFY_OK parikh_constant=1 digit_formula_n<3^11 "
    "D_classification_q=0..20000 sampled_D_q=1..1000 "
    "translation_symmetry_k=0..7 direct_complexity_n=1..250+selected "
    "special_lt10000=1,4,8,28,80,244,728,2188,6560"
)
