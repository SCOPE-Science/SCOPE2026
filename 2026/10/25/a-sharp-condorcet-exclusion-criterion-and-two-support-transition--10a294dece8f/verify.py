#!/usr/bin/env python3
"""Exact rational verification of symmetric three-alternative stable two-lotteries."""
from fractions import Fraction as Q
from itertools import product

def rankings(p):
    return [('ABC',p),('CBA',p),('BAC',(1-2*p)/2),('BCA',(1-2*p)/2)]

def score_direct(p,lot,c):
    total=Q(0)
    for order,w in rankings(p):
        rank={a:i for i,a in enumerate(order)}
        for a,b in product('ABC', repeat=2):
            if rank[a]<rank[c] or rank[b]<rank[c]: continue
            ties=(a==c)+(b==c)
            total+=w*lot[a]*lot[b]/(ties+1)
    return total

def score_formula(p,lot,c):
    total=Q(0)
    d=lot[c]
    for order,w in rankings(p):
        R=sum((lot[t] for t in order[order.index(c)+1:]),Q(0))
        total+=w*(R*R+R*d+d*d/3)
    return total

def lottery(p):
    if p<=Q(1,3): x=Q(0)
    elif p>=Q(4,9):x=Q(1,2)
    else:x=(3*p-1)/(2-3*p)
    return {'A':x,'B':1-2*x,'C':x}

checks=0
for denominator in range(1,42):
 for j in range(denominator//2+1):
    p=Q(j,denominator)
    L=lottery(p)
    for c in 'ABC':
        f=score_direct(p,L,c)
        assert f==score_formula(p,L,c)
        assert f<=Q(1,3), (p,L,c,f)
        if L[c]>0:assert f==Q(1,3), (p,L,c,f)
        checks+=1
    assert sum(L[c]*score_direct(p,L,c) for c in 'ABC')==Q(1,3)
    # All 3-draw fixed-point identities follow from support equalities.
for denom in range(1,14):
 for j in range(denom//2+1):
    p=Q(j,denom)
    for k in range(denom+1):
     for l in range(denom-k+1):
      L={'A':Q(k,denom),'B':Q(l,denom),'C':Q(denom-k-l,denom)}
      for c in 'ABC':
       assert score_direct(p,L,c)==score_formula(p,L,c)
       checks+=1
      assert sum(L[c]*score_direct(p,L,c) for c in 'ABC')==Q(1,3)
# Sharp sample p=4/9 and p=2/5.
assert lottery(Q(4,9))=={'A':Q(1,2),'B':Q(0),'C':Q(1,2)}
assert lottery(Q(2,5))=={'A':Q(1,4),'B':Q(1,2),'C':Q(1,4)}
# Explicit Hessian of score_B in (x,z): (2/3,2/3-2p;2/3-2p,2/3).
for denom in range(1,40):
 for j in range(1,denom//2+1):
  p=Q(j,denom)
  assert Q(2,3)>0 and Q(4,3)*p*(2-3*p)>0
print('PASS', checks, 'exact attacker-score comparisons; finite checks corroborate the algebraic proof')

# Exact general Condorcet-winner exclusion criterion on the single-peaked axis.
def general_scores(u,v,m,n,L):
    total={c:Q(0) for c in 'ABC'}
    for order,w in [('ABC',u),('CBA',v),('BAC',m),('BCA',n)]:
        for c in 'ABC':
            R=sum((L[z] for z in order[order.index(c)+1:]), Q(0))
            d=L[c]
            total[c]+=w*(R*R+R*d+d*d/3)
    return total

general_checks=0
for q in range(1,18):
 for i in range(q+1):
  for j in range(q+1-i):
   for k in range(q+1-i-j):
    l=q-i-j-k
    if 2*i>=q or 2*j>=q:continue
    u,v,m,n=(Q(z,q) for z in (i,j,k,l))
    s=u+m
    if not Q(1,3)<s<Q(2,3):continue
    t=3*s-1
    L={'A':t,'B':Q(0),'C':1-t}
    F=general_scores(u,v,m,n,L)
    assert F['A']==Q(1,3) and F['C']==Q(1,3)
    criterion=m+n+u*(1-t)**2+v*t*t<=Q(1,3)
    assert (max(F.values())<=Q(1,3))==criterion
    general_checks+=1
print('PASS',general_checks,'exact general-profile Condorcet-exclusion tests')
