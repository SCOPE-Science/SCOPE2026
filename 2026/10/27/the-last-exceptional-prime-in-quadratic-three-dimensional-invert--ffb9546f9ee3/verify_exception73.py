#!/usr/bin/env python3
"""Exact finite checks for the quadratic inverted-Kloosterman p=73 exception."""
from fractions import Fraction
from math import factorial
P=73
D4=2*5**4-70**2
assert D4==-3650 and D4%73==0 and (P-1)//4==18

def coeffs_fraction(n):
    a=[Fraction(1)]
    rising=Fraction(1)
    for j in range(1,n+1):
        rising *= Fraction(4*j-3,4)
        a.append(rising**4/Fraction(factorial(4*j)**2))
    lam=[Fraction(0)]*(n+1)
    # T f'(T) = f(T) T (log f)'(T)
    for k in range(1,n+1):
        lam[k]=k*a[k]
        for j in range(1,k): lam[k]-=j*lam[j]*a[k-j]
        lam[k]/=k
    return a,lam

def modfrac(v): return v.numerator%P*pow(v.denominator%P,-1,P)%P
A,L=coeffs_fraction(6)
assert [modfrac(x) for x in L] == [0,18,0,49,25,52,56], [modfrac(x) for x in L]
print('COEFFS_OK',*[f'lambda_{i}={modfrac(L[i])}' for i in [1,2,3,4,5,6]])
# independent modular-coefficient recurrence
am=[1]; rising=1
for j in range(1,7):
    rising=rising*(4*j-3)*pow(4,-1,P)%P
    am.append(rising**4*pow(factorial(4*j),-2,P)%P)
lm=[0]*7
for k in range(1,7):
    lm[k]=(k*am[k]-sum(j*lm[j]*am[k-j] for j in range(1,k)))*pow(k,-1,P)%P
assert lm==[modfrac(x) for x in L]
assert pow(5,(P-1)//2,P)==P-1 # irreducibility of u^2-5

def mul(x,y):
    a,b=x;c,d=y
    return ((a*c+5*b*d)%P,(a*d+b*c)%P)
def tr(x):return 2*x[0]%P
sigs={}
for a in range(P):
    for b in range(P):
        if (a,b)==(0,0): continue
        x=a,b
        x2=mul(x,x);x3=mul(x2,x);x4=mul(x2,x2);x6=mul(x3,x3)
        sig=tr(x),tr(x3),tr(x4),tr(x6)
        sigs.setdefault(sig,[]).append(x)
assert len(sigs)==(P**2+P-2)//2,len(sigs)
for block in sigs.values():
    x=block[0]
    assert set(block)=={x,(x[0],(-x[1])%P)},(x,block)
assert sum(len(s) for s in sigs.values())==P**2-1
assert sum(len(s)==1 for s in sigs.values())==P-1
print('TRACE_ORBITS_OK', 'nonzero_parameters='+str(P**2-1),'Frobenius_orbits='+str(len(sigs)), 'singleton_orbits='+str(P-1))
# direct Galois-stabilizer cardinalities by exhaustive base-field scaling
for tr0 in (False,True):
    x=next((a,b) for a in range(P) for b in range(P) if (a,b)!=(0,0) and ((a==0)==tr0))
    conjugates={x,(x[0],-x[1]%P)}
    stabilizer=[t for t in range(1,P) if (x[0]*pow(t,-4,P)%P,x[1]*pow(t,-4,P)%P) in conjugates]
    assert len(stabilizer)==(8 if tr0 else 4),(tr0,stabilizer)
    print('STABILIZER_OK', 'trace_zero='+str(tr0),'size='+str(len(stabilizer)),'algebraic_degree='+str(72//len(stabilizer)))
print('CERTIFICATE_OK')
