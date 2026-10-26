#!/usr/bin/env python3
"""Standalone moment-equation and exact sign checks for a two-state thermal harmonic trap.

Requires Python 3 and sympy; uses exact algebra and rational examples. Finite
checks are confirmations, not substitutes for the global analytic proof.
"""
from sympy import (symbols, Matrix, factor, diff, simplify, Rational, nroots)

a,b,k,D=symbols('a b k D', positive=True)
s=a+b; p=a*b
q2=Matrix([[2*a+k,-k],[-k,2*b+k]])
q4=Matrix([[4*a+k,-k],[-k,4*b+k]])
u=q2.inv()*Matrix([D,D]); v=q4.inv()*(12*D*u)
m2=factor(sum(u)); m4=factor(sum(v)); q=factor(m4/(3*m2**2)-1)
m2_claim=D*(s+2*k)/(2*p+s*k)
m4_claim=6*D**2*(2*(a*a+b*b)+3*s*k+2*k*k)/((2*p+s*k)*(4*p+s*k))
q_claim=(a-b)**2*(4*p+3*s*k+2*k*k)/((s+2*k)**2*(4*p+s*k))
P=4*p*(s*s-8*p)-16*p*s*k-5*s*s*k*k-2*s*k**3
assert simplify(m2-m2_claim)==0
assert simplify(m4-m4_claim)==0
assert simplify(q-q_claim)==0
assert simplify(diff(q,k)-2*(a-b)**2*P/((s+2*k)**3*(4*p+s*k)**2))==0
assert simplify(diff(m2,k)+D*(a-b)**2/(2*p+s*k)**2)==0
m4_der=-6*D**2*(a-b)**2*(12*p*s+4*(a*a+4*p+b*b)*k+3*s*k*k)/((2*p+s*k)**2*(4*p+s*k)**2)
assert simplify(diff(m4,k)-m4_der)==0
assert simplify(diff(P,k)+16*p*s+10*s*s*k+6*s*k*k)==0
num=P.subs({a:Rational(1),b:Rational(9)})
assert simplify(num-(1008-1440*k-500*k*k-20*k**3))==0
assert q.subs({a:1,b:9,k:0})==Rational(16,25)
assert q.subs({a:1,b:9,k:Rational(1,4)})==Rational(22336,33957)
assert q.subs({a:1,b:9,k:Rational(1,4)})>q.subs({a:1,b:9,k:0})
roots=nroots(num)
realpos=[float(x) for x in roots if abs(float(x.as_real_imag()[1]))<1.e-10 and float(x.as_real_imag()[0])>0]
assert len(realpos)==1 and abs(realpos[0]-0.580341977711327)<1.e-10
assert P.subs({a:1,b:4,k:0}) < 0
assert q.subs({a:2,b:2,k:Rational(2,3)})==0
print('PASS: exact second/fourth moments, derivatives, sign cubic, and rational examples')
