#!/usr/bin/env python3
"""Reproduce exact two-stage recurrence and sample the proved positivity law.
Standard-library-only numerical checks; the analytic proof establishes the infinite statement.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import math

N = 0
def ck(cond, label):
    global N
    if not cond: raise AssertionError(label)
    N += 1

# Stage scheme v0=(16 yn-7 yprev)/9; v1=v0+(4/9) z v0;
# v2=(7/4) v1-(3/4) v0+(7/9) z v1;
# ynext=(4/7) yn+(3/7) v2.
S = [F(1), F(14,9), F(28,81)] # v2/v0 for scalar y'=lambda*y
A = [F(4,7)+F(3,7)*F(16,9)*S[0], F(3,7)*F(16,9)*S[1], F(3,7)*F(16,9)*S[2]]
B = [-F(3,7)*F(7,9)*u for u in S]
T = [F(4,3), F(56,27), F(112,243)]
ck(A == [F(4,3),F(32,27),F(64,243)], 'stage A')
ck(B == [-F(1,3),-F(14,27),-F(28,243)], 'stage B')
ck(A == [F(4,7)*(1+T[0]), F(4,7)*T[1], F(4,7)*T[2]], 'Chebyshev A')
ck(B == [-F(1,4)*u for u in T], 'Chebyshev B')
ck(1-A[0]-B[0] == 0, 'order 0')
ck(2-A[0]-A[1]-B[1] == 0, 'order 1')
ck(2-A[0]/2-A[1]-A[2]-B[2] == 0, 'order 2')
ck(F(12,28)-F(9,28)*F(4,3) == 0, 'left Jury endpoint')

with localcontext() as ctx:
    ctx.prec=70
    D=Decimal
    a=D(4)/7
    zleft=D(-9)/2
    zr=D(-9)/4*(1-(D(3)/7).sqrt())
    zl=D(-9)/4*(1+(D(3)/7).sqrt())
    def t(z): return D(112)/243*z*z+D(56)/27*z+D(4)/3
    def roots(z):
        q=t(z)
        delta=a*a*(1+q)**2-q
        ck(delta>0, 'positive discriminant')
        return ((a*(1+q)-delta.sqrt())/2,(a*(1+q)+delta.sqrt())/2)
    def f(z): return roots(z)[0]-z.exp()
    ck(f(zleft)>0 and f(zl)<0, 'threshold bracket')
    lo,hi=zleft,zl
    for _ in range(210):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    root=(lo+hi)/2
    ck(D('-3.762081')<root<D('-3.762079'), 'root numerical enclosure')
    ck(zr> D(-1) and zl<D(-3), 'zero boundaries')
    for j in range(1,601):
        z=zleft+(D(j)/D(601))*(D(0)-zleft)
        sm,sp=roots(z)
        ck(-1<=t(z)<D(4)/3 and abs(sm)<1 and abs(sp)<1, 'Jury/spectrum sample')
        E=z.exp()
        if z<=zl or z>=zr:
            predicted=(E>=sm) if t(z)>0 else True
        else: predicted=True
        ck(predicted == (z>=root), 'sharp global positivity zone sample')
        if z<root:
            ck(D(0)<E<sm<sp, 'negative dominant weight')
            num=((sp-E)/(sm-E)).ln()
            den=(sp/sm).ln()
            nu=num/den
            # The sign of each iterate changes once at the threshold n=nu.
            nbelow=max(1,int(nu))
            nup=nbelow+1
            ybelow=((E-sm)*(sp**nbelow)+(sp-E)*(sm**nbelow))/(sp-sm)
            yup=((E-sm)*(sp**nup)+(sp-E)*(sm**nup))/(sp-sm)
            ck(ybelow>=0 and yup<0, 'first negative index')
    # Selected exact-startup resonant cases (a scalar e^(n*z) orbit at the threshold).
    sm,sp=roots(root)
    ck(abs(sm-root.exp())<D('1e-64'), 'exactness resonance')
    for delta in ['1e-3','1e-5','1e-7','1e-9']:
        z=root-D(delta)
        l,L=roots(z)
        nu=((L-z.exp())/(l-z.exp())).ln()/(L/l).ln()
        ck(nu>1, 'delayed loss')
    print('VERIFY_OK',N)
    print('critical_z', format(root,'.45f'))
    print('stability_interval', '(-4.5, 0)')
    print('left_Chebyshev_zero', format(zl,'.35f'))
    print('right_Chebyshev_zero', format(zr,'.35f'))
