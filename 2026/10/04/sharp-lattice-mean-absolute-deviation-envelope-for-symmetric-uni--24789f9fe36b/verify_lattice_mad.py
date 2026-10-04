#!/usr/bin/env python3
from fractions import Fraction
import random, math

def vm(m): return Fraction(m*(m+1),3)
def dm(m): return Fraction(m*(m+1),2*m+1)
def slope(m): return (dm(m+1)-dm(m))/(vm(m+1)-vm(m))
def cell(v):
    m=0
    while vm(m+1)<v: m+=1
    return m

def upper(v):
    m=cell(v); a,b=vm(m),vm(m+1)
    th=(v-a)/(b-a)
    return (1-th)*dm(m)+th*dm(m+1)

def run():
    moment_checks=0; slope_checks=0; equality_checks=0; mix_checks=0; low_checks=0; phase_checks=0
    for m in range(0,1001):
        den=2*m+1
        e2=Fraction(sum(j*j for j in range(-m,m+1)),den)
        e1=Fraction(sum(abs(j) for j in range(-m,m+1)),den)
        assert e2==vm(m) and e1==dm(m)
        moment_checks+=2
    for m in range(0,1000):
        if m<999:
            assert slope(m)>slope(m+1)
            slope_checks+=1
        a,b=vm(m),vm(m+1)
        for num in range(21):
            th=Fraction(num,20); v=a+th*(b-a)
            d=(1-th)*dm(m)+th*dm(m+1)
            assert d==upper(v)
            equality_checks+=1
    rng=random.Random(33)
    for _ in range(30000):
        supp=sorted(set(rng.randrange(0,100) for __ in range(rng.randrange(2,8))))
        raw=[rng.randrange(1,30) for __ in supp]; tot=sum(raw)
        w=[Fraction(x,tot) for x in raw]
        v=sum(ww*vm(mm) for ww,mm in zip(w,supp))
        d=sum(ww*dm(mm) for ww,mm in zip(w,supp))
        assert d<=upper(v)
        mix_checks+=1
    for v in [Fraction(1,10),Fraction(2,3),Fraction(7,3),Fraction(25,4)]:
        prev=None
        for R in [20,50,100,200,500]:
            if vm(R)<v: continue
            d=v*dm(R)/vm(R)
            assert d==Fraction(3)*v/Fraction(2*R+1)
            if prev is not None: assert d<prev
            prev=d; low_checks+=1
    for th in [0,0.25,0.5,0.75,1.0]:
        target=math.sqrt(3)/48*(1+4*th*(1-th))
        prev=None
        for m in [100,300,1000,3000]:
            a=float(vm(m)); b=float(vm(m+1)); v=a+th*(b-a)
            d=(1-th)*float(dm(m))+th*float(dm(m+1))
            scaled=v*(math.sqrt(3)/2-d/math.sqrt(v))
            err=abs(scaled-target)
            if prev is not None: assert err<=prev+1e-9
            prev=err; phase_checks+=1
    print('VERIFY_OK '
          f'moment_checks={moment_checks} slope_checks={slope_checks} '
          f'equality_checks={equality_checks} random_mix_checks={mix_checks} '
          f'low_sequence_checks={low_checks} phase_checks={phase_checks}')
if __name__=='__main__': run()
