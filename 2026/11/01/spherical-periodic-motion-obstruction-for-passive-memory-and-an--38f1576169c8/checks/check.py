"""Check exact frequency balances for a delayed-kernel circular solution and passive-kernel positivity."""
import sympy as s
I=s.I
rho=s.sqrt(10)/5
# e^{-i tau}=(-1+3i)/sqrt(10), tau=pi+arctan(3).
phase=(-1+3*I)/s.sqrt(10)
M=s.simplify(rho*phase/(1+I))
W=s.simplify(1/(2+I))
radial_force=s.simplify(4*(s.Rational(1,2)-W))
velocity_memory=s.simplify(I*M)
assert M==(1+2*I)/5
assert W==(2-I)/5
assert radial_force==(2+4*I)/5
assert velocity_memory==(-2+I)/5
assert s.simplify(velocity_memory+radial_force-I)==0
assert 0<rho<1
# On a circle of radius 1/2, every chord has length at most one: a(chord)=1.
# For any beta>0 the passive convolution u_beta satisfies u_beta'=u-beta u_beta,
# so integrating u dot u_beta' over a period gives integral |u_beta'|^2.
# Test exact example beta=2, u(t)=(cos t, sin t) using Fourier periodic response.
beta=s.Integer(2)
Q=1/(beta+I)
# Exact period-integrated passive contribution for unit-amplitude planar circle:
# 2*pi*Re(i Q)=2*pi*Im(-Q) = 2*pi/(beta^2+1).
assert s.simplify(s.re(I*Q)-s.Rational(1,5))==0
print('PASS: delayed complex response, positive kernel mass <1, bounded radial imprint construction, passive frequency sign')
print('M(i)=',M,'W(i)=',W,'sum=',velocity_memory+radial_force,'rho=',rho)
