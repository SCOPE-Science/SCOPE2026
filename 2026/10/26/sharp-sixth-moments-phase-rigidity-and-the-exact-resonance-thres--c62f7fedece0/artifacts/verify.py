#!/usr/bin/env python3
"""Exact coefficient tests for a sharp sixth moment of two real dihedral characters.

Scientific companion: finite tests check constants and computations; the
all-order assertion follows from the separately supplied algebraic proof.
"""
from itertools import product
from math import comb, sqrt
from random import Random
from collections import defaultdict

checks=0

def confirm(test, detail):
    global checks
    checks += 1
    if not test:
        raise AssertionError(detail)

def mult(p,q):
    r=defaultdict(int)
    for i,a in p.items():
        for j,b in q.items(): r[i+j]+=a*b
    return dict(r)

def sixth(a,b,n=None):
    # F(z)=a(z+z^-1)+b(z^2+z^-2); its |F|^6 Fourier coefficients
    f={-2:b,-1:a,1:a,2:b}
    conjugate={k:complex(v).conjugate() for k,v in f.items()}
    g=mult(f,conjugate)
    cube=mult(mult(g,g),g)
    if n is None:
        return cube.get(0,0)/2
    return sum(v for k,v in cube.items() if k % n ==0)/2

def algebraic_expression(a,b):
    # Complex integer coefficient tests yield integer-valued expressions.
    p=(a*complex(a).conjugate()).real
    q=(b*complex(b).conjugate()).real
    w=(a*complex(b).conjugate()).real
    return 10*(p**3+q**3)+21*p*p*q+18*p*q*q+(84*p+72*q)*w*w

# Independently enumerate constant Laurent coefficients and mixed trace moments.
for exponent_b, target in enumerate([10,0,7,0,6,0,10]):
    exponent_a=6-exponent_b
    poly={0:1}
    for shift in [1]*exponent_a + [2]*exponent_b:
        poly=mult(poly,{-shift:1,shift:1})
    confirm(poly.get(0,0)/2 == target, 'mixed moment ' + str(exponent_b))
    for n in [13,14,17,29]:
        confirm(sum(v for k,v in poly.items() if k%n==0)/2==target,'stable mixed moment')

for n in range(5,13):
    evidence=[]
    for num_twos in range(7):
        poly={0:1}
        for shift in [1]*(6-num_twos) + [2]*num_twos:
            poly=mult(poly,{-shift:1,shift:1})
        if poly.get(n,0).real > 0:
            evidence.append((num_twos,poly[n]))
    confirm(bool(evidence), 'strict alias at index ' + str(n))

rng=Random(87261)
for sample in range(850):
    a=complex(rng.randint(-5,5), rng.randint(-5,5))
    b=complex(rng.randint(-5,5), rng.randint(-5,5))
    if not a and not b:
        continue
    exact=algebraic_expression(a,b)
    for n in [13,14,17,31]:
        val=sixth(a,b,n)
        confirm(abs(val-exact)<1e-6,'complex moment n='+str(n))
    confirm(abs(sixth(a,b,None)-exact)<1e-6,'continuous moment')

# Positivity of the exact analytical deficit for sampled points.
xstar=-1+sqrt(21)/3
K=70*sqrt(21)/3-80
for j in range(700):
    a=complex(rng.randint(-20,20),rng.randint(-20,20))
    b=complex(rng.randint(-20,20),rng.randint(-20,20))
    if not a and not b:continue
    p=abs(a)**2;q=abs(b)**2;S=p+q;x=p/S
    w=a*b.conjugate()
    lhs=K*S**3-sixth(a,b,13).real
    rhs=15*S**3*(x-xstar)**2*(1+x+2*sqrt(21)/3) + 12*S*(6+x)*w.imag**2
    confirm(abs(lhs-rhs)<1e-7*max(1,S**3), 'deficit identity')
    confirm(lhs>-1e-7*max(1,S**3),'nonnegative deficit')

# Independent direct finite-group quadrature for low and stable cyclic orders.
from cmath import exp,pi
for n in range(5,23):
    for a,b in [(1.0,1.0),(1+2j,-2+1j),(0.5,-1j)]:
        averaged=sum(abs(a*2*__import__('math').cos(2*pi*k/n)
                         +b*2*__import__('math').cos(4*pi*k/n))**6
                         for k in range(n))/(2*n)
        predicted=sixth(a,b,n)
        confirm(abs(averaged-predicted)<1e-7*max(1,abs(predicted)),'dihedral group quadrature')

# Exact polynomial identity in Q[sqrt(21)] with rational coefficients.
from fractions import Fraction

def quad(a=0,b=0): return (Fraction(a),Fraction(b))
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qm(x,y): return (x[0]*y[0]+21*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def padd(p,q):
    z=[quad()] * max(len(p),len(q))
    for j,x in enumerate(p): z[j]=qa(z[j],x)
    for j,y in enumerate(q): z[j]=qa(z[j],y)
    return z

def pmult(p,q):
    z=[quad()] * (len(p)+len(q)-1)
    for j,x in enumerate(p):
        for k,y in enumerate(q): z[j+k]=qa(z[j+k],qm(x,y))
    return z

xx=quad(-1,Fraction(1,3))
Kexact=quad(-80,Fraction(70,3))
Pexact=[quad(10),quad(60),quad(-45),quad(-15)]
# K - P, expressed coefficientwise.
left=padd([Kexact],[quad(-10),quad(-60),quad(45),quad(15)])
# 15(x-x*)^2(1+x+2sqrt(21)/3).
neg_xstar=quad(1,Fraction(-1,3))
right=pmult(pmult([neg_xstar,quad(1)],[neg_xstar,quad(1)]),[quad(1,Fraction(2,3)),quad(1)])
right=[qm(quad(15),v) for v in right]
confirm(left==right, 'exact Q(sqrt21) stability factorization')
# Critical point equation 3x^2+6x-4=0.
confirm(qa(qa(qm(quad(3),qm(xx,xx)),qm(quad(6),xx)),quad(-4))==quad(), 'exact critical point')
# Maximum polynomial evaluation equals K.
power=quad(1); calc=quad()
for c in Pexact:
    calc=qa(calc,qm(c,power));power=qm(power,xx)
confirm(calc==Kexact,'exact sharp algebraic constant')

print('VERIFY_OK')
print('Assertions:',checks)
print('Stable sixth-moment polynomial: 10(p^3+q^3)+21p^2q+18pq^2+(84p+72q)Re(a*conj(b))^2')
print('Normalized real-phase maximum:',round(K,12),'at x=',round(xstar,12))
print('Stable-order threshold n>=13: checked; low orders 5..12 have positive aliased terms')
