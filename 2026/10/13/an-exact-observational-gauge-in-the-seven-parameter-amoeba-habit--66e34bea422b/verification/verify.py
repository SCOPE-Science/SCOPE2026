#!/usr/bin/env python3
"""Exact identity checks for pressure-response observational equivalence."""
import sympy as sp
from fractions import Fraction

p_f,p_r=sp.symbols('p_f p_r',real=True)
a,a_s,d,r,g_f,g_s,g_r,gamma,c,h=sp.symbols('a a_s d r g_f g_s g_r gamma c h', positive=True)
a_h=(1-h)*a+h*a_s
g_h=(1-h)*g_f+h*g_s
orig_f=d*(p_r-p_f)-a_h*p_f+g_h
orig_r=r*d*(p_f-p_r)-a*p_r+g_r
b=(1-c)*g_r/a
F=c*p_f+b
R=c*p_r+b
G_f=c*g_f+a*b
G_s=c*g_s+a_s*b
G_r=c*g_r+a*b
Gamma=gamma/c
G_h=(1-h)*G_f+h*G_s
trans_f=d*(R-F)-a_h*F+G_h
trans_r=r*d*(F-R)-a*R+G_r
assert sp.factor(trans_f-c*orig_f)==0
assert sp.factor(trans_r-c*orig_r)==0
assert sp.factor(Gamma*(R-F)-gamma*(p_r-p_f))==0
assert sp.factor(G_r-g_r)==0

# Exact six-combination observable normal form.
q_f=gamma*(p_f-g_r/a)
q_r=gamma*(p_r-g_r/a)
k0=gamma*(g_f-g_r)
k1=gamma*(g_s-a_s*g_r/a)
assert sp.factor(gamma*orig_f-(d*(q_r-q_f)-a_h*q_f+(1-h)*k0+h*k1))==0
assert sp.factor(gamma*orig_r-(r*d*(q_f-q_r)-a*q_r))==0
assert sp.factor((q_r-q_f)-gamma*(p_r-p_f))==0
assert sp.simplify(Gamma*(G_f-G_r)-k0)==0
assert sp.simplify(Gamma*(G_s-a_s*G_r/a)-k1)==0

# The tangent to the exactly indistinguishable parameter curve.
curve=sp.Matrix([G_f,G_s,a,a_s,d,Gamma,r]).subs(g_r,1)
tangent=sp.simplify(curve.diff(c).subs(c,1))
assert tangent==sp.Matrix([g_f-1,g_s-a_s/a,0,0,0,-gamma,0])

# Table S4 (seed 308) from the published supplementary material.
nums={g_r:sp.Integer(1),g_f:sp.Rational(1001,10**6),g_s:sp.Rational(1197,100),
      a:sp.Rational(2244,10**5),a_s:sp.Rational(2866,10**4),
      d:sp.Rational(4909,10**4), gamma:sp.Rational(5782,10**6),
      r:sp.Rational(7088,10**5), c:sp.Rational(9,10)}
alt_gf=sp.factor(G_f.subs(nums))
alt_gs=sp.factor(G_s.subs(nums))
alt_gamma=sp.factor(Gamma.subs(nums))
assert alt_gf==sp.Rational(1009009,10**7)
for val in (alt_gf, alt_gs, alt_gamma, nums[g_s], nums[g_f], nums[gamma]):
    assert sp.Rational(1,1000)<=val<=100
assert sp.Rational(1,1000)<=nums[r]<=1
assert alt_gf != nums[g_f] and alt_gs != nums[g_s] and alt_gamma!=nums[gamma]

# Both positive-equilibrium initial conditions map exactly.
Af=sp.Matrix([[-a-d,d],[r*d,-a-r*d]])
As=sp.Matrix([[-a_s-d,d],[r*d,-a-r*d]])
base=sp.Matrix([g_f,g_r]); stim=sp.Matrix([g_s,g_r]);
P0=-Af.inv()*base
P1=-As.inv()*stim
P0c=sp.simplify(c*P0+sp.Matrix([b,b]))
P1c=sp.simplify(c*P1+sp.Matrix([b,b]))
assert all(sp.simplify(x)==0 for x in (-Af.inv()*sp.Matrix([G_f,G_r])-P0c))
assert all(sp.simplify(x)==0 for x in (-As.inv()*sp.Matrix([G_s,G_r])-P1c))

# A switched physical trajectory is also checked at representative times.
# This finite test confirms implementation, not the universal identity proved above.
from scipy.linalg import expm
import numpy as np
sub={s:float(t) for s,t in nums.items() if s!=c}
scc=float(nums[c]); shift=float(b.subs(nums))
Pf=np.asarray(P0.subs(nums),dtype=float).reshape(2)
Pf2=scc*Pf+shift
l1=l2=0.
alt_sub=dict(sub)
alt_sub[g_f]=float(alt_gf);alt_sub[g_s]=float(alt_gs)
alt_sub[gamma]=float(alt_gamma)
def flow(P,l,stim_on,dt,params):
    aa=params[a_s] if stim_on else params[a]
    gg=params[g_s] if stim_on else params[g_f]
    M=np.array([[-aa-params[d],params[d]],
                [params[r]*params[d],-params[a]-params[r]*params[d]]])
    # Augmented affine system and velocity-integral state.
    Z=np.zeros((4,4)); Z[:2,:2]=M;Z[0,3]=gg;Z[1,3]=params[g_r]
    Z[2,0]=-params[gamma];Z[2,1]=params[gamma]
    st=np.array([P[0],P[1],l,1.])
    en=expm(dt*Z)@st
    return en[:2],en[2]
for day in range(1,10):
    # Fixed (Q) schedule with stimulation on days 1-6 and 9.
    on=day<=6 or day==9
    for sw,dt in ([(True,8.),(False,16.)] if on else [(False,24.)]):
        Pf,l1=flow(Pf,l1,sw,dt,sub)
        Pf2,l2=flow(Pf2,l2,sw,dt,alt_sub)
        assert np.allclose(Pf2,scc*Pf+shift,rtol=1e-10,atol=2e-10)
        assert abs(l1-l2)<2e-11
    l1=l2=0.
print('VERIFY_OK')
print('parameter_pair',alt_gf,alt_gs,alt_gamma)
print('parameter_pair_decimal',*[sp.N(v,11) for v in (alt_gf,alt_gs,alt_gamma)])
