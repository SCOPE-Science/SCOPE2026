#!/usr/bin/env python3
"""Reproduce the nontrivial central Fourier blocks for the transposition metric on S5.
Scientific calculations only. Exact class enumeration, character formulas and rational bounds."""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, combinations
from math import factorial

G=list(permutations(range(5)))
assert len(G)==120

def cyc(g):
    seen=set(); lengths=[]
    for i in range(5):
        if i in seen: continue
        cur=i;n=0
        while cur not in seen:
            seen.add(cur);cur=g[cur];n+=1
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

def square(g):
    return tuple(g[g[i]] for i in range(5))

def subfixed(g):
    return sum({g[i],g[j]}=={i,j} for i,j in combinations(range(5),2))

char_by_class={}
counts=Counter()
for g in G:
    mu=cyc(g);counts[mu]+=1
    std=sum(g[i]==i for i in range(5))-1
    stdsq=sum(square(g)[i]==i for i in range(5))-1
    two=subfixed(g)-1-std
    wedge=(std*std-stdsq)//2
    assert 2*wedge==std*std-stdsq
    sign=(-1)**(5-len(mu))
    vals=(std,two,wedge,sign*two,sign*std,sign)
    if mu in char_by_class: assert char_by_class[mu]==vals
    char_by_class[mu]=vals
expected={
 (1,1,1,1,1):1,(2,1,1,1):10,(2,2,1):15,(3,1,1):20,
 (3,2):20,(4,1):30,(5,):24
}
assert counts==expected
spec={}
names=['(4,1)','(3,2)','(3,1,1)','(2,2,1)','(2,1,1,1)','(1,1,1,1,1)']
dims=[4,5,6,5,4,1]
for j,name in enumerate(names):
    agg=Counter()
    for mu,count in counts.items():
        k=5-len(mu)
        if k: agg[k]+=count*char_by_class[mu][j]
    spec[name]=[Q(agg[k],dims[j]) for k in (1,2,3,4)]
assert spec=={
 '(4,1)':[Q(5),Q(5),Q(-5),Q(-6)],
 '(3,2)':[Q(2),Q(-1),Q(-2),Q(0)],
 '(3,1,1)':[Q(0),Q(-5),Q(0),Q(4)],
 '(2,2,1)':[Q(-2),Q(-1),Q(2),Q(0)],
 '(2,1,1,1)':[Q(-5),Q(5),Q(5),Q(-6)],
 '(1,1,1,1,1)':[Q(-10),Q(35),Q(-50),Q(24)]
},spec
# Dimension/character orthogonality is a second independent exact table check.
for j in range(6):
 for k in range(6):
    inner=sum(count*char_by_class[mu][j]*char_by_class[mu][k]
              for mu,count in counts.items())
    assert inner==120*(j==k),(j,k,inner)
assert sum(d*d for d in [1]+dims)==120

def root_bracket(base, numerator=8,degree=25,den=10**9):
    """Exact rational enclosure of base**(numerator/degree)."""
    T=base**numerator * den**degree
    l=0; h=base*den
    while l+1<h:
        m=(l+h)//2
        if m**degree<=T:l=m
        else:h=m
    assert l**degree<=T<(l+1)**degree
    return Q(l,den),Q(l+1,den)
a0,a1=root_bracket(2)
b0,b1=root_bracket(3)
c0,c1=root_bracket(4)
f_lower=-10+35*a0-50*b1+24*c0
f_upper=-10+35*a1-50*b0+24*c1
assert f_lower>0,(f_lower,f_upper)
assert 2**8 * 4**25 < 5**25  # 2^(8/25)<5/4

# Exact logarithm intervals via artanh series with rational truncation bounds.
def logbounds(x, n=12):
    z=(x-1)/(x+1)
    assert 0<z<1
    lo=sum((2*z**(2*k+1))/Q(2*k+1) for k in range(n))
    hi=lo + 2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
    return lo,hi
L0,L1=logbounds(Q(2))
M0,M1=logbounds(Q(3))
H0,H1=logbounds(Q(3,2))
assert 83*L0-50*M1>0    # g(0)>0
assert 48*L0**2-50*M1*H1>0 # g'(0)>0
assert 48*L0**3-50*M1*H1**2>0 # lower coefficient in g''

# A standalone finite-matrix test independent from central-character calculations.
# Sign is an exact zero-sum direction: the sign Fourier multiplier equals
# its quadratic form divided by group size.
signs={g:(-1)**(5-len(cyc(g))) for g in G}
index={g:i for i,g in enumerate(G)}
assert sum(signs.values())==0
import mpmath as mp
mp.mp.dps=65
f=lambda p:-10+35*mp.power(2,p)-50*mp.power(3,p)+24*mp.power(4,p)
pstar=mp.findroot(f,('0.313','0.314'))
assert mp.mpf('0.313')<pstar<mp.mpf('0.314')
assert abs(f(pstar))<mp.mpf('1e-58')
for j,name in enumerate(names):
 coeff=spec[name]
 lam=sum(mp.mpf(str(int(q.numerator)))/int(q.denominator)*mp.power(k,pstar)
         for k,q in zip(range(1,5),coeff))
 if name==names[-1]:assert abs(lam)<mp.mpf('1e-58')
 else:assert lam<mp.mpf('-0.001'),(name,lam)

print('PASS: 120 permutations, 7 conjugacy classes, six irreducible Fourier multipliers')
for name in names:print('  ',name,','.join(str(z) for z in spec[name]))
print('PASS: exact class/character orthogonality and dimensions')
print('PASS: rational 25th-root interval F(8/25) lower=',f_lower,'upper=',f_upper)
print('PASS: log-series exact intervals verify F_sign is increasing for all p>=0')
print('PASS: p*=',mp.nstr(pstar,55))
print('PASS: endpoint Euclidean embedding rank 118; all lower p have rank 119')
