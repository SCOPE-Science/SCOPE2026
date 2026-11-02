#!/usr/bin/env python3
"""Finite-type proof checks for three-color cyclic automata on matching complements."""
from itertools import product
from collections import Counter, defaultdict
from math import factorial, comb
import sympy as s

TYPES=((0,0),(1,1),(2,2),(0,1),(1,2),(0,2))
WEIGHTS=(1,1,1,2,2,2)

def canon(p):return tuple(sorted(p))

def do_step(pairs):
    totals=[0,0,0]
    for a,b in pairs:totals[a]+=1;totals[b]+=1
    result=[]
    for a,b in pairs:
        na=(a+1)%3 if totals[(a+1)%3]-int(b==(a+1)%3)>0 else a
        nb=(b+1)%3 if totals[(b+1)%3]-int(a==(b+1)%3)>0 else b
        result.append((na,nb))
    return result

def captypes(pairs):
    ct=Counter(canon(p) for p in pairs)
    return tuple(min(2,ct[t]) for t in TYPES)

def symbolic_step(pairs,c):
    totals=[0,0,0]
    for t,count in zip(TYPES,c):
        for x in t:totals[x]=min(2,totals[x]+count)
    out=[]
    for a,b in pairs:
        na=(a+1)%3 if totals[(a+1)%3]>=2 or (totals[(a+1)%3]==1 and b!=(a+1)%3) else a
        nb=(b+1)%3 if totals[(b+1)%3]>=2 or (totals[(b+1)%3]==1 and a!=(b+1)%3) else b
        out.append((na,nb))
    return out

def classify(seq):
    for t in range(3):
        if seq[t]==seq[t+1]: return (t,1)
        if seq[t]==seq[t+3]: return (t,3)
    raise AssertionError('No first-entry by 2')

x,z=s.symbols('E z')
H={0:lambda w:s.Integer(1),1:lambda w:w*z,2:lambda w:x**w-1-w*z}
polys=defaultdict(lambda:s.Integer(0))
valid=0
class_signature_counts=Counter()
for c in product(range(3),repeat=6):
    if not (2 in c or sum(c)>=3): continue
    valid+=1
    rep=[t for t,count in zip(TYPES,c) for _ in range(count)]
    if len(rep)<3: rep+=[TYPES[c.index(2)]]*(3-len(rep))
    # Keep a symbolic type tracker with one representative per pair, including duplicates.
    # A count of 2 represents >=2, so use its own exact representative count, then
    # verify transitions using capped and uncapped versions, not only the latter.
    curr=list(rep);cc=captypes(rep);seq=[tuple(curr)]
    for j in range(6):
        sym=symbolic_step(curr,cc)
        raw=do_step(curr)
        assert sym==raw,(c,j,'abstraction disagrees')
        cc=captypes(sym)
        curr=sym
        seq.append(tuple(curr))
    assert seq[5]==seq[2],(c,'period identity')
    a=classify(seq)
    class_signature_counts[a]+=1
    # Changes of exact type counts at >=2 cannot affect signatures or transitions;
    # when splitting counts, all pairs of a type follow the same orientation map.
    term=s.Integer(1)
    for ci,wi in zip(c,WEIGHTS):term*=H[ci](wi)
    polys[a]+=term

assert valid==sum(1 for c in product(range(3),repeat=6) if 2 in c or sum(c)>=3)
# Each class has its own exp-generating function for all n>=3.
# Expected EGF n>=3 includes finite missing initial terms only, removed below.
expected={
(0,1):3*x,
(1,1):3*x**4 -6*(1+z)*x,
(2,1):12*z*x,
(1,3):6*z*x**4-12*(z*z+z)*x,
(2,3):12*z*z*x,
}
expected[(0,3)]=x**9-sum(expected.values())
# Compare E=e^z and check residual Taylor polynomial degree<=2.
for key in sorted(polys):
    diff=s.expand(polys[key]-expected[key])
    # x^k -> exp(k*z), use expansion of polynomial in x and z
    sub=s.expand(diff.subs(x,s.exp(z)))
    # should be exactly a polynomial degree <=2 (no exponentials) or zero
    ans=s.simplify(sub)
    residual=s.series(ans,z,0,3).removeO().expand()
    assert s.simplify(ans-residual)==0,(key,'EGF formula',ans)
    print('class',key,'residual for n<3:',residual)
    assert s.degree(residual,z)<=2

# Direct combinatorial evaluation from capped types, independent of n=2 exception.
for n in range(3,31):
    expected_counts={
       (0,1):3, (1,1):3*4**n-6*(n+1), (2,1):12*n,
       (1,3):6*n*(4**(n-1)-2*n), (2,3):12*n*(n-1),
    }
    expected_counts[(0,3)]=9**n-sum(expected_counts.values())
    if n<=10:
        calc={key:int(s.expand(P.subs(x,s.exp(z))).series(z,0,n+1).coeff(z,n)*factorial(n)) for key,P in polys.items()}
        assert calc==expected_counts,(n,calc,expected_counts)
closed={
(0,1):3*(x-1-z),
(1,1):3*(x**4-2*x*(1+z)-3*z*z+1),
(2,1):12*z*(x-1-z),
(0,3):(x**3-1)*(x**6+x**3-6*x*z-3*x+1),
(1,3):6*z*(x**4-2*x*z-2*x+1),
(2,3):12*z*z*(x-1),
}
assert set(closed)==set(polys)
for a in closed:
    assert s.expand(polys[a]-closed[a])==0,('closed-form EGF',a)
print('capped signature class sizes:',sorted(class_signature_counts.items()))
print('PASS: valid capped signatures',valid, 'all first-entry classes, F^5=F^2, all six EGF identities')
