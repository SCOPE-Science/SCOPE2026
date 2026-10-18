"""Reproduce spherical shadow moments, exact rectangle specialization, and sharp optimizer.
Standard Python library only; midpoint quadrature is diagnostic, not a proof.
"""
import math
from fractions import Fraction
from random import Random

pi=math.pi
q=pi/4-2/3
g=2/3-pi*pi/16
assert q>0 and g>0
C=1/12-q*q/(4*g)
assert 0<C<1/12

# A square of side one: its directional width is |cos theta|+|sin theta|.
mu_sq=4/pi
nu_sq=1+2/pi
A_sq=1.0
alpha_sq=2*nu_sq/3-pi*pi*mu_sq*mu_sq/16
h_sq=A_sq*mu_sq*q/(2*alpha_sq)

# An entirely separate polyhedral brightness identity: Cauchy's projection formula
# for a rectangular box with sides (1,1,h).
def box_moment2(h):
    return (1+2*h*h)/3+4*h*(2+h)/(3*pi)
def prism_moment2(h):
    return 1/3+2*h*mu_sq/3+2*h*h*nu_sq/3
for h in (0.04,0.3,1.,2.,3.9):
    assert abs(box_moment2(h)-prism_moment2(h))<1e-13

# Independent integration over a circle of azimuths and zenith-absolute values.
# This uses no closed-form angular/spherical moments.
N=460; M=440
sum_a=sum_a2=0.0
for i in range(N):
    z=(i+.5)/N
    sz=math.sqrt(1-z*z)
    for j in range(M):
        phi=(j+.5)*2*pi/M
        w=abs(math.cos(phi))+abs(math.sin(phi))
        b=z+h_sq*sz*w
        sum_a+=b
        sum_a2+=b*b
mean_num=sum_a/(N*M)
var_num=sum_a2/(N*M)-mean_num**2
mean_exact=1/2+pi*mu_sq*h_sq/4
var_exact=1/12-A_sq*mu_sq*q*h_sq+alpha_sq*h_sq*h_sq
assert abs(mean_num-mean_exact)<2e-5,(mean_num,mean_exact)
assert abs(var_num-var_exact)<2e-5,(var_num,var_exact)

# Rigidity profile for anisotropic square and constant-width disk.
mu_disk=2.0 # unit-radius disk
A_disk=pi
nu_disk=mu_disk**2
h_disk=A_disk*mu_disk*q/(2*g*mu_disk**2)
V_disk=A_disk**2*C

def min_v(A,mu,nu):
    alpha=2*nu/3-pi*pi*mu**2/16
    h=A*mu*q/(2*alpha)
    value=A*A/12-(A*mu*q)**2/(4*alpha)
    return h,value
assert abs(min_v(A_disk,mu_disk,nu_disk)[0]-h_disk)<1e-13
assert abs(min_v(A_disk,mu_disk,nu_disk)[1]-V_disk)<1e-13
assert min_v(A_sq,mu_sq,nu_sq)[1]/A_sq**2>C

for s in (0,1e-6,.005,.1,1,20):
    alpha=g+2*s/3
    v=1/12-q*q/(4*alpha)
    exact_gap=q*q*s/(6*g*alpha)
    assert abs(v-C-exact_gap)<3e-14

print('VERIFY_OK')
print('q=',q,'gamma=',g,'sharp_constant=',C)
print('disk_height_over_radius=',h_disk,'square_opt_height=',h_sq)
print('square_opt_var_over_A2=',min_v(A_sq,mu_sq,nu_sq)[1])
print('quadrature_squared_moment=',sum_a2/(N*M),'exact=',prism_moment2(h_sq))
