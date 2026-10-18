#!/usr/bin/env python3
"""Exact finite-stage birth/death scheduling checks with an independent CTMC calculation."""
import itertools
import json
import math
from fractions import Fraction as F


def stage(b, d, a=None, h=None):
    b, d = F(b), F(d)
    r = b - d
    if r == 0:
        assert a is None
        a, h = F(1), F(h)
    else:
        a = F(a)
        h = (1-a)/r
    assert b >= 0 and d >= 0 and a > 0 and h > 0
    return b, d, a, h


def params(items):
    A, B = F(1), F(0)
    for b, d, a, h in items:
        B += A*b*h
        A *= a
    return A, B


def prob_at_zero(A, B):
    return 1-F(1)/(A+B)


def stoploss(A, B, h):
    return F(1)/A * (B/(A+B))**h


def variance(A, B):
    return 2*B/A**2 + 1/A - 1/A**2


def ratio_desc(s):
    b,d,_,_=s
    return -float(b/d) if d else -float('inf')


def uniformization(b, d, duration, cutoff=110):
    # Independent CTMC forward solver; states cutoff+1 are aggregated.
    q = cutoff*(b+d)
    v=[0.]*(cutoff+1)
    v[1]=1.
    out=[0.]*(cutoff+1)
    w=math.exp(-q*duration)
    mean=q*duration
    niter=int(mean+16*math.sqrt(mean)+120)
    for k in range(niter):
        for n in range(cutoff+1):
            out[n] += w*v[n]
        new=[0.]*(cutoff+1)
        new[0]+=v[0]
        new[cutoff]+=v[cutoff]
        for n in range(1,cutoff):
            new[n] += (1-(b+d)*n/q)*v[n]
            new[n+1] += (b*n/q)*v[n]
            new[n-1] += (d*n/q)*v[n]
        v=new
        w*=mean/(k+1)
    return out


def uniformization_from(initial,b,d,duration):
    cutoff=len(initial)-1
    q=cutoff*(b+d)
    v=initial[:]
    out=[0.]*(cutoff+1)
    w=math.exp(-q*duration)
    mean=q*duration
    niter=int(mean+16*math.sqrt(mean)+120)
    for k in range(niter):
        for n in range(cutoff+1):
            out[n]+=w*v[n]
        new=[0.]*(cutoff+1)
        new[0]+=v[0]
        new[cutoff]+=v[cutoff]
        for n in range(1,cutoff):
            new[n]+=(1-(b+d)*n/q)*v[n]
            new[n+1]+=(b*n/q)*v[n]
            new[n-1]+=(d*n/q)*v[n]
        v=new
        w*=mean/(k+1)
    return out


def main():
    tests=0
    # Fractional exposure factors correspond to strictly positive physical durations.
    catalogue=[]
    for b in range(1,5):
        for d in range(1,5):
            for aa in (2,3):
                if b>d:
                    s=stage(b,d,a=F(1,aa))
                elif b<d:
                    s=stage(b,d,a=F(aa))
                else:
                    s=stage(b,d,h=F(1,aa))
                catalogue.append(s)
    # Exact adjacent interchange identity and strict sign.
    for x,y in itertools.product(catalogue,repeat=2):
        ax,bx=params((x,y)); ay,by=params((y,x))
        assert ax==ay
        b1,d1,_,h1=x; b2,d2,_,h2=y
        assert bx-by == (b2*d1-b1*d2)*h1*h2
        tests+=1
    # Four-phase assignments with distinct rate ratios, and all permutations.
    choices=[catalogue[i] for i in (1,8,13,17,24,30)]
    permutation_tests=0
    for chosen in itertools.combinations(choices,4):
        ordered=sorted(chosen,key=ratio_desc)
        reversed_order=ordered[::-1]
        amin,bmin=params(ordered)
        amax,bmax=params(reversed_order)
        for perm in itertools.permutations(chosen):
            A,B=params(perm)
            assert A==amin==amax
            assert bmin<=B<=bmax
            assert prob_at_zero(A,bmin)<=prob_at_zero(A,B)<=prob_at_zero(A,bmax)
            assert variance(A,bmin)<=variance(A,B)<=variance(A,bmax)
            for h in range(1,6):
                assert stoploss(A,bmin,h)<=stoploss(A,B,h)<=stoploss(A,bmax,h)
                tests+=1
            tests+=3
            permutation_tests+=1
    # A sharp exact arithmetic witness with common expected final abundance one.
    good=stage(3,1,a=F(1,2))
    bad=stage(1,2,a=F(2))
    A,B=params((good,bad))
    A_rev,B_rev=params((bad,good))
    assert (A,B,A_rev,B_rev)==(1,F(5,4),1,F(5,2))
    assert F(1)-prob_at_zero(A,B)==F(4,9)
    assert F(1)-prob_at_zero(A_rev,B_rev)==F(2,7)
    assert variance(A,B)==F(5,2)
    assert variance(A_rev,B_rev)==F(5)
    tests+=5
    # Numerically independent forward transition solution at the exact durations.
    tb=math.log(2)/2
    td=math.log(2)
    p0=[0.]*111; p0[1]=1.
    p_hi=uniformization_from(uniformization_from(p0,3.,1.,tb),1.,2.,td)
    p_lo=uniformization_from(uniformization_from(p0,1.,2.,td),3.,1.,tb)
    for probs, target_surv,target_var in ((p_hi,4/9,2.5),(p_lo,2/7,5.)):
        mass=sum(probs)
        m=sum(k*p for k,p in enumerate(probs))
        var=sum(k*k*p for k,p in enumerate(probs))-m*m
        assert abs(mass-1)<1e-10, mass
        assert abs(m-1)<1e-9, m
        assert abs(1-probs[0]-target_surv)<1e-9,(1-probs[0],target_surv)
        assert abs(var-target_var)<1e-8,(var,target_var)
        tests+=4
    output={
      'status':'passed',
      'exact_adjacent_swap_checks':len(catalogue)**2,
      'exact_permutation_checks':permutation_tests,
      'exact_assertions':tests,
      'independent_forward_ctmc_checks':8,
      'example':{
       'favorable_first':{'survival':'4/9','mean':'1','variance':'5/2'},
       'unfavorable_first':{'survival':'2/7','mean':'1','variance':'5'}
      },
      'limitations':'Finite checks corroborate the analytical all-stage proof, not replace it.'
    }
    print(json.dumps(output,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
