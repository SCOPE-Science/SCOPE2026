#!/usr/bin/env python3
"""Finite exact checks for affine images of Gaussian norms."""
from math import isqrt

def prime(p):
    return p >= 2 and all(p%d for d in range(2,isqrt(p)+1))

def sum_two_squares(n):
    if n < 0:
        return False
    for x in range(isqrt(n)+1):
        y2=n-x*x
        if isqrt(y2)**2 == y2:
            return True
    return False

def local_count(a,b,q):
    mod=q*q
    out=0
    for x in range(mod):
        x2=(x*x)%mod
        for y in range(mod):
            v=(a*(x2+y*y)+b)%mod
            if v%q==0 and v!=0:
                out+=1
    return out

def run():
    qcases=0
    for q in (3,7,11,19):
        assert prime(q) and q%4==3
        for a,b in ((1,1),(2,3),(5,7),(13,17)):
            if a%q==0 or b%q==0:
                continue
            observed=local_count(a,b,q)
            expected=q*(q*q-1)
            assert observed==expected,(a,b,q,observed,expected)
            qcases+=1
    # Two fixed prime conditions are independent modulo 3^2*7^2.
    mod=9*49
    bad3=bad7=both=0
    for x in range(mod):
        x2=(x*x)%mod
        for y in range(mod):
            t=x2+y*y+1
            e3=(t%3==0 and t%9!=0)
            e7=(t%7==0 and t%49!=0)
            bad3+=e3
            bad7+=e7
            both+=e3 and e7
    assert bad3 * 27==8*mod*mod
    assert bad7 * 343==48*mod*mod
    assert both * (27*343)==(8*48)*mod*mod
    # Deterministic successful and unsuccessful affine representatives.
    sq={x*x+y*y for x in range(60) for y in range(60)}
    assert sum_two_squares(5)
    for a in (1,2,5,10,25):
        assert sum_two_squares(a)
        assert all(sum_two_squares(a*n) for n in sq if a*n<=15000)
    for a in (3,6,7,11,21):
        assert not sum_two_squares(a)
        assert all(not sum_two_squares(a*n) for n in sq if 0<n and a*n<=15000)
    for a,b in ((1,1),(2,1),(5,2),(3,1),(7,4),(10,3)):
        # Produce a direct small Gaussian norm whose image fails the two-square test.
        witness=next((x,y,a*(x*x+y*y)+b) for x in range(30) for y in range(30)
                     if not sum_two_squares(a*(x*x+y*y)+b))
        assert witness is not None
    print('VERIFY_OK local_q_cases=',qcases,'CRT_exact_pairs=',mod*mod,'direct_affine_witnesses=6')
    print('local_obstruction_density_q3=',8/27,'q7=',48/343,'CRT_both=',(8*48)/(27*343))

if __name__=='__main__': run()
