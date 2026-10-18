#!/usr/bin/env python3
"""Exact checks for the characteristic-five Picard-cover stratification.

Uses only the Python standard library. Polynomial identities are checked
coefficientwise in F_5[a,b,c]. Finite-field tests corroborate, but do not
replace, the proof for arbitrary algebraically closed fields.
"""
from itertools import product
from collections import Counter
P=5

def plus(x,y):
    r=dict(x)
    for k,v in y.items():
        r[k]=(r.get(k,0)+v)%P
        if not r[k]:del r[k]
    return r

def scale(x,n):
    return {k:(v*n)%P for k,v in x.items() if v*n%P}

def mul(x,y):
    r={}
    for (i,j,k),u in x.items():
        for (l,m,n),v in y.items():
            key=i+l,j+m,k+n
            r[key]=(r.get(key,0)+u*v)%P
            if not r[key]:del r[key]
    return r

def powp(x,n):
    r={(0,0,0):1}
    for _ in range(n): r=mul(r,x)
    return r

one={(0,0,0):1}; a={(1,0,0):1}; b={(0,1,0):1}; c={(0,0,1):1}
A=plus(plus(mul(powp(a,2),c),mul(a,powp(b,2))),powp(c,2))
D=plus(plus(plus(scale(mul(powp(a,4),c),16),scale(mul(powp(a,3),powp(b,2)),-4)),
            scale(mul(powp(a,2),powp(c,2)),-128)),
       plus(plus(scale(mul(mul(a,powp(b,2)),c),144),scale(powp(b,4),-27)),scale(powp(c,3),256)))
Dstar=plus(mul(plus(powp(a,2),c),A),scale(mul(powp(b,2),plus(mul(a,c),powp(b,2))),3))
assert D==Dstar, 'universal discriminant factorization failed'

# x^4+a*x^2+b*x+c; coefficients x^4 and x^9 in f^3.
def poly_mul(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,fi in enumerate(f):
        for j,gj in enumerate(g):h[i+j]=(h[i+j]+fi*gj)%P
    return h

# Check the universal coefficients by evaluation on every F_5 triple,
# then check the formal coefficient identity using a symbolic dictionary.
def poly_mul_formal(f,g):
    h={}
    for i,fi in f.items():
        for j,gj in g.items():
            h[i+j]=plus(h.get(i+j,{}),mul(fi,gj))
    return h
F={0:c,1:b,2:a,4:one}
F3=poly_mul_formal(poly_mul_formal(F,F),F)
assert F3.get(4,{})==scale(A,3)
assert F3.get(9,{})==scale(b,3)

counts=Counter(); examples={}
smooth_rankzero=[]
for av,bv,cv in product(range(P), repeat=3):
    fv=[cv,bv,av,0,1]
    cube=poly_mul(poly_mul(fv,fv),fv)
    alpha=(av*av*cv+av*bv*bv+cv*cv)%P
    beta=(3*bv)%P
    delta=(sum((coef*av**i*bv**j*cv**k for (i,j,k),coef in D.items()))%P)
    assert cube[4]==3*alpha%P and cube[9]==beta
    if not delta:continue
    assert bv != 0 or alpha != 0
    typ=(0,1) if alpha==0 else (2,1)
    counts[typ]+=1;examples.setdefault(typ,(av,bv,cv))
    if not alpha:smooth_rankzero.append((av,bv,cv))
assert counts == {(2,1):84,(0,1):16},counts

# Weighted scalings preserve monic depressed form over F_5.
classes=set(); orbit_sizes=[]; ts=set()
remaining=set(smooth_rankzero)
while remaining:
    a0,b0,c0=min(remaining)
    orb={((u*u*a0)%5,(u**3*b0)%5,(u**4*c0)%5) for u in range(1,5)}
    assert orb<=remaining
    orbit_sizes.append(len(orb));remaining-=orb;classes.add(min(orb))
    if a0 == 0: ts.add('infinity')
    else:ts.add(c0*pow((a0*a0)%5,-1,5)%5)
assert sorted(orbit_sizes)==[4]*4
assert ts=={1,2,3,'infinity'},ts
print('UNIVERSAL_IDENTITIES_OK')
print('FORMAL_CARTIER_COEFFICIENTS_OK')
print('SMOOTH_F5_TRIPLES',sum(counts.values()))
print('RANK_COUNTS',dict(counts))
print('NONORDINARY_SCALE_ORBITS',len(classes),sorted(orbit_sizes))
print('NONORDINARY_GEOMETRIC_MODULUS_F5',sorted(map(str,ts)))
print('VERIFY_OK')
