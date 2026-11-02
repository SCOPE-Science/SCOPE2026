#!/usr/bin/env python3
"""Reproduce local algebra and second-sheet resonance diagnostics.
Requires sympy and mpmath. No network access or external data.
"""
import sympy as sp
import mpmath as mp


def p_polys(n, x):
    ps = [sp.S.Zero, sp.S.One]
    for k in range(1, n + 1):
        ps.append(sp.expand(x * ps[-1] - ps[-2]))
    return ps


def numeric_p(n, e):
    prev, cur = 0, 1
    for _ in range(n - 1):
        prev, cur = cur, e * cur - prev
    return cur


def secular(e, eps, g, m):
    N = 3*m+1
    coupling2 = (1+eps)**2
    sigma = (e-1j*mp.sqrt(4*g*g-e*e))/(2*g*g)
    return (e+coupling2)*((e-sigma)*numeric_p(N+1,e)-numeric_p(N,e))-coupling2*(e-sigma+1)*(numeric_p(N,e)+numeric_p(N+1,e))


def pole(m,g,eps):
    predicted = -1-eps/(m+1)
    guess = predicted + mp.mpf('0.42')*eps**2-mp.mpf('0.3')*1j*eps**2
    return mp.findroot(lambda z:secular(z,eps,g,m), (guess, guess+mp.mpf('0.0000002')),
                       tol=mp.mpf('1e-35'), maxsteps=100)


def run():
    mp.mp.dps=60
    x, z, sig, sigprime, A, B = sp.symbols('x z sig sigprime A B')
    sym_count = 0
    for m in range(1, 7):
        N=3*m+1
        ps=p_polys(N+1,x)
        expected=[(ps[N],1,m,-3*m*(m+1)),
                  (ps[N+1],-1,m+1,3*m*(m+1))]
        for poly,v,d,d2 in expected:
            assert sp.simplify(poly.subs(x,-1)-v)==0
            assert sp.simplify(sp.diff(poly,x).subs(x,-1)-d)==0
            assert sp.simplify(sp.diff(poly,x,2).subs(x,-1)-d2)==0
            sym_count+=3
        e=-1+A*z+B*z*z
        v=(1+z)**2
        sigma=sig+sigprime*(e+1)
        F=(e+v)*((e-sigma)*ps[N+1].subs(x,e)-ps[N].subs(x,e))-v*(e-sigma+1)*(ps[N].subs(x,e)+ps[N+1].subs(x,e))
        sF=sp.series(F,z,0,3).removeO().expand()
        a=-sp.Rational(1,m+1)
        b=sp.Rational(m,2*(m+1)**2)-sp.Rational((2*m+1)**2,2*(m+1)**3)/sig
        assert sp.simplify(sF.coeff(z).subs(A,a))==0
        assert sp.simplify(sF.coeff(z,2).subs({A:a,B:b}))==0
        sym_count+=2
    num_count=0
    for g in ('0.51','0.7','1','2'):
        g=mp.mpf(g)
        for m in (1,2,4):
            eps=mp.mpf('0.0005')
            e=pole(m,g,eps)
            coeff=mp.mpf((2*m+1)**2)*mp.sqrt(4*g*g-1)/(4*(m+1)**3)
            measured=-mp.im(e)/eps**2
            assert coeff>0 and abs(measured/coeff-1)<mp.mpf('0.025')
            assert abs(secular(e,eps,g,m))<mp.mpf('1e-34')
            num_count+=2
    for m in (1,2,4):
        for t in ('0.001','0.0003'):
            t=mp.mpf(t)
            e=pole(m,mp.mpf('0.5'),-t)
            coeff=(2*m+1)**2*mp.sqrt(2)/(4*mp.power(m+1,mp.mpf('3.5')))
            measured=-mp.im(e)/t**mp.mpf('2.5')
            assert abs(measured/coeff-1)<mp.mpf('0.025')
            assert mp.im(e)<0 and abs(secular(e,-t,mp.mpf('0.5'),m))<mp.mpf('1e-34')
            num_count+=2
    for m in (1,2,4):
        eps=mp.mpf('0.001')
        predicted=-1-eps/(m+1)
        e=mp.findroot(lambda z: secular(z,eps,mp.mpf('0.5'),m), (predicted, predicted+eps*mp.mpf('0.00001')), tol=mp.mpf('1e-35'), maxsteps=100)
        assert abs(mp.im(e))<mp.mpf('1e-35')
        assert mp.re(e)<-1
        assert abs(secular(e,eps,mp.mpf('0.5'),m))<mp.mpf('1e-34')
        num_count+=3
    print('PASS: %d exact symbolic identities; %d high-precision resonance tests'%(sym_count,num_count))

if __name__=='__main__': run()
