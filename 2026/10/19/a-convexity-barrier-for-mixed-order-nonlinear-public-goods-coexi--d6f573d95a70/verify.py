#!/usr/bin/env python3
"""Exact-arithmetic validation of the three-order geometric public-goods example.

This checks one finite example, not the universal theorem, which is mathematical.
"""
from fractions import Fraction as F


def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]+=ai*bj
    return out


def polynomial_power(a,n):
    result=[F(1)]
    for _ in range(n):
        result=multiply(result,a)
    return result


def eval_polynomial(coeffs,x):
    value=F(0)
    for a in reversed(coeffs):
        value=value*x+a
    return value


def derivative(coeffs):
    return [F(i)*v for i,v in enumerate(coeffs)][1:]


def main():
    data=[(2,F(1,2),F(1,5)),(3,F(1,4),F(1,4)),(4,F(1,4),F(2))]
    Q=[F(0)]*4
    for ell,weight,delta in data:
        term=polynomial_power([F(1),delta-1],ell-1)
        for j,t in enumerate(term): Q[j]+=weight/F(ell)*t
    assert Q==[F(19,48),-F(11,80),F(15,64),F(1,16)],Q
    assert derivative(derivative(Q))==[F(15,32),F(3,8)]
    assert eval_polynomial(Q,F(0))==F(19,48)>F(77,200)
    assert eval_polynomial(Q,F(1,4))==F(181,480)<F(77,200)
    assert eval_polynomial(Q,F(1))==F(533,960)>F(77,200)
    scaled=[960*c for c in Q]
    assert scaled==[380,-132,225,60]
    cub=[int((v-(F(77,200) if i==0 else F(0)))*4800) for i,v in enumerate(Q)]
    assert cub==[52,-660,1125,300],cub
    # Convexity and signs guarantee exactly one crossing in each interval.
    assert derivative(derivative(Q))[0]>0
    print('PASS: exact polynomial, derivatives, threshold signs and two-root classification.')

if __name__=='__main__': main()
