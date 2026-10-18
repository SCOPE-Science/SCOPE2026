#!/usr/bin/env python3
"""Standalone analytical-identity spot checks for rank-one matrix-function update laws."""
import sympy as S
from mpmath import mp

def symcheck():
    A=S.diag(1,4,9,9)
    u=S.ones(4,1)
    k=A+u*u.T
    I=S.eye(4)
    def rational_f(M,ts,b=S.Rational(0)):
        R=b*M
        for t in ts:
            R=R+M*(M+t*I).inv()
        return R
    cases=[([],0,0),([],1,1),([1],0,1),([1,2],0,2),([1,2,3],0,3),([1,2],1,3),([1,2,3,4],0,3)]
    checks=0
    for ts,b,r in cases:
        delta=rational_f(k,ts,S.Integer(b))-rational_f(A,ts,S.Integer(b))
        assert delta.rank()==r,(ts,b,delta.rank(),r)
        assert delta*S.Matrix([0,0,1,-1])==S.zeros(4,1)
        checks+=2
    # Negative updates retain exact rank for SPD matrices.
    eta=-S.Rational(1,10)
    k=A+eta*u*u.T
    assert k.det()>0
    for ts,b,r in cases:
        delta=rational_f(k,ts,S.Integer(b))-rational_f(A,ts,S.Integer(b))
        assert delta.rank()==r,(ts,b,delta.rank(),r)
        checks+=1
    # Exact Sherman-Morrison residual expression.
    for eta in [S.Rational(1),-S.Rational(1,10)]:
        B=A+eta*u*u.T
        for t in [S.Rational(1,2),2,7]:
            RA=(A+t*I).inv()
            d=(B+t*I).inv()-RA
            rhs=-eta/(1+eta*(u.T*RA*u)[0])*(RA*u)*(RA*u).T
            assert d==rhs
            checks+=1
    return checks

def mpcheck():
    mp.dps=70
    vals=[mp.mpf(1),mp.mpf(4),mp.mpf(9),mp.mpf(9)]
    A=mp.diag(vals)
    u=mp.matrix([1,1,1,1]); checks=0
    def power(M,p):
        w,Q=mp.eigsy(M)
        return Q*mp.diag([mp.power(x,p) for x in w])*Q.T
    for eta in [mp.mpf('0.01'),mp.mpf('0.4'),mp.mpf('-0.1')]:
        B=A+eta*u*u.T
        for p in [mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.8'),mp.mpf('-0.3'),mp.mpf('-0.5'),mp.mpf('-0.9')]:
            Delta=power(B,p)-power(A,p)
            w,Q=mp.eigsy(Delta)
            aa=sorted([abs(z) for z in w])
            assert aa[0]<mp.mpf('1e-58'),(eta,p,aa)
            assert aa[1]>mp.mpf('1e-13'),(eta,p,aa)
            sg=mp.sign(eta)*mp.sign(p)
            assert all(sg*e>mp.mpf('1e-13') for e in w if abs(e)>mp.mpf('1e-13'))
            checks+=3
    return checks

if __name__ == '__main__':
 print('Exact rational identity/rank checks:',symcheck())
 print('High-precision fractional power checks:',mpcheck())
 print('STATUS: PASS')
