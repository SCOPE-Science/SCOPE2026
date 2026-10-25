#!/usr/bin/env python3
"""Independent symbolic and numerical diagnostics for paired implicit random stages."""
import sympy as S
import mpmath as mp
import numpy as np
z,u,s=S.symbols('z u s',real=True)
v=1-u; c=u*v
R=lambda z,t:(1+(1-t)*z)/(1-t*z)
P=S.factor(R(z,u)*R(z,v))
assert S.factor(P-(1+z+c*z*z)/(1-z+c*z*z))==0
assert S.diff(P,z).subs(z,0)==2
assert S.simplify(S.diff(P,z,2).subs(z,0))==4
D=1+s+s*s*c
I1=S.simplify(2*S.log(1+s)/(s*(s+2)))
I2=S.simplify(2/((s+2)**2*(s+1))+2*I1/(s+2)**2)
delta=S.simplify(4*s*I1-4*s*s*I2)
expected=8*(s*s+2*s+4)*S.log(1+s)/(s+2)**3-8*s*s/((s+2)**2*(s+1))
assert S.simplify(delta-expected)==0
assert S.limit(s*delta/S.log(s),s,S.oo)==8
assert S.limit(s*delta-8*S.log(s),s,S.oo)==-8
mp.mp.dps=55
for ss in (mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('1'),mp.mpf('2'),mp.mpf('10'),mp.mpf('100'),mp.mpf('1000')):
    f=lambda t:1-((1-ss+ss*ss*t*(1-t))/(1+ss+ss*ss*t*(1-t)))**2
    integral=mp.quad(f,[0,mp.mpf('.5'),1]); exact=8*(ss*ss+2*ss+4)*mp.log(1+ss)/(ss+2)**3-8*ss*ss/((ss+2)**2*(ss+1))
    assert abs(integral-exact)<mp.mpf('1e-45'),(ss,integral,exact)
# Check nonnormal dissipative matrices: A+A^* negative semidefinite; no diagonalizability assumptions.
rng=np.random.default_rng(1033)
for i in range(48):
    K=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); H=-(K.conj().T@K)-.1*np.eye(4)
    J=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); A=H+(J-J.conj().T)
    for hh in (0.0001,.1,1,10,100):
        for uu in (.001,.02,.2,.5,.8,.98,.999):
            cc=uu*(1-uu); eye=np.eye(4)
            den=eye-hh*A+cc*hh**2*(A@A)
            num=eye+hh*A+cc*hh**2*(A@A)
            transfer=np.linalg.solve(den.T,num.T).T # num @ den^-1
            assert np.linalg.norm(transfer,2)<=1+3e-10, (i,hh,uu,np.linalg.norm(transfer,2))
# Formal rigidity argument reduces to u+v>=1; this scan is only a diagnostic.
for uu,vv in ((.1,.3),(.2,.6),(.45,.7),(.3,.7),(.05,.95)):
    large=1e8
    rr=lambda t:(1-(1-t)*large)/(1+t*large)
    product=abs(rr(uu)*rr(vv))
    target=(1-uu)*(1-vv)/(uu*vv)
    assert abs(product-target)<2e-5
print('VERIFY_OK symbolic transfer, exact gap and two-term stiff asymptotic; 7 numerical integrals; 1680 nonnormal dissipative matrix checks; rigidity limits')
