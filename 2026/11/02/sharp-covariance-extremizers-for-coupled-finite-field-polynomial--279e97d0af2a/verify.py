#!/usr/bin/env python3
"""Independent exact arithmetic for joint polynomial-function value-set sizes.

All maps on a finite field are polynomial functions of degree below q.
The finite fields checked are F_2,F_3,F_4,F_5; F_4 uses F_2[t]/(t^2+t+1).
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import prod

def field_add(q,a,b):
    return a ^ b if q == 4 else (a+b) % q

def exact_predicted(q,h):
    counts=Counter(h)
    A=Fraction(q-1,q)
    B=Fraction(q-2,q)
    return q*sum(A**counts[c] * B**(q-counts[c]) for c in range(q))-q*q*A**(2*q)

def exact_direct(q,h,functions):
    n=0; sx=sy=sxy=0
    for f in functions:
        x=len(set(f))
        y=len({field_add(q,f[i],h[i]) for i in range(q)})
        sx+=x; sy+=y; sxy+=x*y; n+=1
    return Fraction(sxy,n)-Fraction(sx*sy,n*n)

def check(q, all_h=True):
    funcs=list(product(range(q),repeat=q))
    if all_h:
        H=funcs
    else:
        H=[tuple([0]*q),tuple(range(q)),tuple([0]*(q-1)+[1]),tuple([0,0]+list(range(2,q))), tuple([0,0,1,1,2])]
    tested=0
    vals_by_h={}
    A=Fraction(q-1,q); B=Fraction(q-2,q)
    lo=q*q*A*B**(q-1)-q*q*A**(2*q)
    hi=q*A**q+q*(q-1)*B**q-q*q*A**(2*q)
    for h in H:
        a=exact_direct(q,h,funcs)
        b=exact_predicted(q,h)
        assert a==b,(q,h,a,b)
        profile=tuple(sorted(Counter(h).values(), reverse=True))
        # profiles are positive r only, so (1,...,1) iff h perm, (q,) iff constant.
        assert lo<=a<=hi,(q,h,a,lo,hi)
        assert (a==lo)==(profile==tuple([1]*q)),(q,h,a,profile)
        assert (a==hi)==(profile==(q,)),(q,h,a,profile)
        if q>=3:
            if profile!=tuple([1]*q):
                assert a>=lo+B**(q-2)/q,(q,h,a)
                if a==lo+B**(q-2)/q:
                    assert profile==(2,)+tuple([1]*(q-2)),(q,h,profile)
            if profile!=(q,):
                assert a<=hi-(A**(q-1)-B**(q-1)),(q,h,a)
                if a==hi-(A**(q-1)-B**(q-1)):
                    assert profile==(q-1,1),(q,h,profile)
        tested+=1
        vals_by_h[profile]=a
    print(f'FIELD_OK q={q} functions={len(funcs)} perturbations={tested} unique_profiles={len(vals_by_h)} min={lo} max={hi}')
    if all_h:
        if q>=3:
            assert vals_by_h[(2,)+tuple([1]*(q-2))]==lo+B**(q-2)/q
            assert vals_by_h[(q-1,1)]==hi-(A**(q-1)-B**(q-1))

if __name__=='__main__':
    for q in (2,3,4): check(q)
    check(5,all_h=False)
    print('VERIFY_OK exact_joint_covariance_and_extremal_profiles=True')
