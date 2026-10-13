#!/usr/bin/env python3
import math
k=1.0
c=1.0
Lam=0.2
T=1.0
E=math.exp(-c*T)
Y=Lam/(1-E)
X=k*Lam*T*E/(1-E)**2
assert abs(Y-(E*Y+Lam)) < 1e-14
assert abs(X-E*(X+k*Y*T)) < 1e-14
def te(t):
    return Y*math.exp(-c*t)
def t0(t):
    return math.exp(-c*t)*(X+k*Y*t)
assert abs(t0(T)-X) < 1e-14
assert abs(te(T)+Lam-Y) < 1e-14
mean=k*Lam/(c*c*T)
assert abs(mean-0.2) < 1e-15
int_tau=(1-E*(1+c*T))/(c*c)
integral=X*(1-E)/c+k*Y*int_tau
assert abs(integral/T-mean) < 1e-14
def nonres_x(g, v=c):
    return k*Lam*(math.exp(-v*T)-math.exp(-g*T))/((g-v)*(1-math.exp(-v*T))*(1-math.exp(-g*T)))
for eps in (1e-3,1e-4,1e-5,1e-6):
    assert abs(nonres_x(c+eps)-X) < 2*eps
print("VERIFY_OK")
print("T0_periodic_initial", X)
print("Te_postpulse", Y)
print("mean_T0", mean)
