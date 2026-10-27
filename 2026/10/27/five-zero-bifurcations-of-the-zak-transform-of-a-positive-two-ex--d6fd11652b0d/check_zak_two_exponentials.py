"""Reproduce the Zak-zero formulas for e^{-|t|}-c e^{-2|t|}."""
import cmath
import math

u=math.exp(-1)
C0=(1+u*u)/(1+u)**2
C1=math.cosh(1)/(2*math.cosh(.5))
C2=math.exp(.5)*(1-u)/(1-u*u)*((1+u*u)/(1+u))**2
assert 0.5<C0<C1<C2<1

def direct(x,w,c,cutoff=90):
    return sum((math.exp(-abs(x-k))-c*math.exp(-2*abs(x-k)))*cmath.exp(2j*math.pi*k*w) for k in range(-cutoff,cutoff+1))

def formula(x,w,c):
    phi=2*math.pi*w
    def z(a):
        v=math.exp(-a*x);h=math.exp(-a*(1-x));v0=math.exp(-a)
        den=1-2*v0*math.cos(phi)+v0*v0
        return ((v-v0*h)+(h-v0*v)*cmath.exp(1j*phi))/den
    return z(1)-c*z(2)

def cos_phase(c,mid=False):
    r=(math.exp(.5)/(1+u)) if mid else 1/(1+u*u)
    return (r*(1+u**4)-c*(1+u*u))/(2*r*u*u-2*c*u)

def predicted(c):
    roots=[(.5,.5)]
    if c>=C0-1e-12:
        cs=cos_phase(c)
        assert -1-1e-10<=cs<=1+1e-10
        th=math.acos(max(-1,min(1,cs)))/(2*math.pi)
        roots.extend([(0.,th)] if abs(th-.5)<1e-8 else [(0.,th),(0.,1-th)])
    if C0+1e-10<c<C1-1e-10:
        delta=math.acosh(math.cosh(1)/(2*c*math.cosh(.5)))
        roots.extend([(.5-delta,.5),(.5+delta,.5)])
    if c>C2+1e-10:
        th=math.acos(cos_phase(c,True))/(2*math.pi)
        roots.extend([(.5,th),(.5,1-th)])
    return roots

maxdiff=0.0
for c in [0,.3,.61,.65,.68,.7,.82,.85,.9,1]:
    for x in [0,.13,.3,.5,.87,.99]:
        for w in [0,.11,.25,.39,.5,.73,.99]:
            diff=abs(direct(x,w,c)-formula(x,w,c))
            maxdiff=max(maxdiff,diff)
            assert diff<5e-13,(x,w,c,diff)
    for x,w in predicted(c):
        assert abs(direct(x,w,c))<5e-13,(c,x,w,direct(x,w,c))
    print(f'c={c:.4f} zeros={len(predicted(c))}: '+str([(round(x,7),round(w,7)) for x,w in predicted(c)]))
print('thresholds',C0,C1,C2)
print('maximum direct/analytic residual',maxdiff)
