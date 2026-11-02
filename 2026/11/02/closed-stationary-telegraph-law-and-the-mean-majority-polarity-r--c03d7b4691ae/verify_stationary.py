#!/usr/bin/env python3
"""Deterministic checks for a two-speed telegraph process with Bernoulli resets.

This program supplements, but does not replace, the proof. It uses only the
Python standard library and checks the stationary law against a distinct
geometric-excursion representation.
"""
import cmath
import math
from fractions import Fraction

nchecks = 0

def check(condition, label):
    global nchecks
    if not condition:
        raise AssertionError(label)
    nchecks += 1

def close(a, b, label, tol=2.0e-10):
    check(abs(a-b) <= tol * (1.0+abs(a)+abs(b)), label)

def parameters(lam, c, v, theta):
    disc=math.sqrt((v-c)**2 + 4.0*c*v*theta*(2.0-theta))
    plus=lam*(disc+v-c)/(2.0*c*v)
    minus=lam*(disc-v+c)/(2.0*c*v)
    reset=lam*theta
    A=plus*(minus+reset/c)/(plus+minus)
    B=minus*(plus-reset/c)/(plus+minus)
    return disc, plus, minus, A, B

def resolvent_fourier(lam,c,v,theta,k):
    r=lam*theta
    a=lam*(1-theta)
    return r*(r+2*a+1j*k*v)/(c*v*k*k+1j*k*(r+a)*(v-c)+r*(r+2*a))

def law_fourier(lam,c,v,theta,k):
    _,plus,minus,A,B=parameters(lam,c,v,theta)
    return A/(plus-1j*k)+B/(minus+1j*k)

def excursion_fourier(lam,c,v,theta,k):
    # Number of flips before the next reset is geometric(theta); all
    # independent holding times conditional on a marked event are Exp(lam).
    q=1-theta
    hp=lam/(lam-1j*k*c)
    hm=lam/(lam+1j*k*v)
    return theta*hp*(1+q*hm)/(1-q*q*hp*hm)

def truncated_excursion_fourier(lam,c,v,theta,k):
    # Direct geometric-series truncation, without using the rational formula.
    q=1-theta
    hp=lam/(lam-1j*k*c)
    hm=lam/(lam+1j*k*v)
    weight=theta
    product=1+0j
    total=0+0j
    for n in range(10000):
        product *= hp if n%2==0 else hm
        total += weight*product
        weight *= q
        if weight < 1e-14:
            break
    return total

for lam in (0.7, 1.0, 2.3):
    for c in (0.8, 1.0, 2.7):
        for v in (0.6, 1.0, 2.1, 8.0):
            for theta in (0.05, 0.2, 0.41, 0.5, 0.8, 0.99, 1.0):
                D, plus, minus, A, B=parameters(lam,c,v,theta)
                check(D>0 and plus>0 and minus>0, 'decay rates')
                check(A>0 and B>=-1e-13, 'density positivity')
                close(A/plus+B/minus,1.0,'normalization')
                close(A-B,lam*theta/c,'origin jump')
                close(plus*minus,lam*lam*theta*(2-theta)/(c*v),'rate product')
                close(plus-minus,lam*(v-c)/(c*v),'rate difference')
                pminus=B/minus
                close(pminus, 0.5+(v*(1-2*theta)-c)/(2*D),'negative mass')
                close(A/plus**2-B/minus**2,(c-v*(1-theta))/(lam*theta*(2-theta)), 'stationary mean')
                check(-1e-12 < pminus < 1+1e-12,'signed probability bounds')
                check((pminus>0.5+1e-10)==(v*(1-2*theta)>c+1e-9),'polarity')
                for k in (-2.0,-0.2,0.0,0.3,1.7):
                    target=law_fourier(lam,c,v,theta,k)
                    close(target,resolvent_fourier(lam,c,v,theta,k),'matrix resolvent')
                    close(target,excursion_fourier(lam,c,v,theta,k),'geometric sum')
                for k in (-1.3,0.37,2.4):
                    close(law_fourier(lam,c,v,theta,k),truncated_excursion_fourier(lam,c,v,theta,k),'independent truncated excursion series')

for theta in (0.1, 0.3, 0.49):
    for c in (0.5, 1., 3.):
        v=c/(1-2*theta)
        D,plus,minus,A,B=parameters(1.3,c,v,theta)
        close(B/minus,0.5,'exact majority boundary')
        # Strict mean/median disagreement in the nonempty interval.
        v=0.5*(c/(1-theta)+c/(1-2*theta))
        D,plus,minus,A,B=parameters(1.3,c,v,theta)
        check(A/plus > 0.5 and A/plus**2-B/minus**2 < 0.,'mean-majority disagreement')

# Exact rational checks of the two competing sign tests, without float dependence.
for numerator in range(1,10):
    theta=Fraction(numerator,10)
    for v in range(1,50):
        c=Fraction(3,2)
        mean_negative = v*(1-theta)>c
        minus_majority = v*(1-2*theta)>c
        check(not minus_majority or mean_negative, 'one-sided sign disagreement')

print(f'PASS: {nchecks} deterministic numeric and exact-rational assertions')
print('Critical example: lambda=1, c=1, v=2, theta=0.4')
D,plus,minus,A,B=parameters(1,1,2,0.4)
print(f'delta_plus={plus:.12f} delta_minus={minus:.12f} A={A:.12f} B={B:.12f}')
print(f'P(X<0)={B/minus:.12f}; stationary_mean={A/plus**2-B/minus**2:.12f}')
