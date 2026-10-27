import math,numpy as np
h=math.acos(1/4);delta=h-2*math.pi/5
A=160/243*(delta+math.sin(5*delta)/5)
assert 0<delta<0.1
assert abs(A-(160/243*delta+5*math.sqrt(15)/486))<1e-14
# Verify exact boundary endpoints and polar-angle speed, numerical finite checks only.
def C(t):return (8/27)*np.exp(3j*t)-(4/9)*np.exp(-2j*t)
for k in range(5):
 a=2*math.pi*k/5; z1=C(a-delta);z2=C(a+delta)
 assert abs(abs(z1)-5/27)<1e-12 and abs(abs(z2)-5/27)<1e-12
 assert abs(C(a+delta)-C(a-2*math.pi/5+h))<1e-12
for t in np.linspace(-delta,delta,300):
 cp=1j*((8/9)*np.exp(3j*t)+(8/9)*np.exp(-2j*t))
 den=np.imag(np.conj(C(t))*cp)
 assert abs(den+32/243*(1+np.cos(5*t)))<1e-12
# Monte Carlo integration polar region, deterministic integration of min radial boundary via winding.
T=np.linspace(0,2*math.pi,10001,endpoint=False)
Z=C(T)
# For each angle, choose two solutions using monotone argument of C, inversion by interpolation.
angle=np.unwrap(np.angle(Z))
assert abs((angle[-1]-angle[0])+4*math.pi)<0.01
# parameter t maps twice over angle; build radial minimum function, interpolate all corresponding angle branches
ang=-angle
# unwrap starts pi to pi+4pi
phi_grid=np.linspace(-math.pi,math.pi,40001)
r1=np.interp(phi_grid,ang,np.abs(Z))
r2=np.interp(phi_grid+2*math.pi,ang,np.abs(Z))
area_numeric=0.5*np.trapezoid(np.minimum(r1,r2)**2,phi_grid)
print('h',h,'delta',delta,'area_theory',A,'area_polar_numerical',area_numeric,'diff',area_numeric-A)
assert abs(area_numeric-A)<1e-5
print('PASS sampled polar boundary and numerical area comparison')
