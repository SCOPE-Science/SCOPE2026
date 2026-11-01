"""Standalone numerical/exact checks for sharp directional p-heat smoothing.

Requires Python standard library. All exact checks use fractions. Finite tests
corroborate, but cannot replace, the general comparison proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
from math import isclose, sqrt


def vertices(qs):
    return list(product(*(range(q) for q in qs)))


def flux(z, p):
    if p == 2:
        return z
    if p == 3:
        return z * abs(z)
    if p == 4:
        return z ** 3
    return abs(z)**(p-2)*z if z else 0


def vector_field(qs, cs, p, u):
    out = {}
    for x in vertices(qs):
        val = 0
        for i, q in enumerate(qs):
            for a in range(q):
                if a != x[i]:
                    y = x[:i]+(a,)+x[i+1:]
                    val += cs[i] * flux(u[y]-u[x], p)
        out[x] = val
    return out


def active_derivatives(qs, i, u, du):
    li = 0
    derivatives = []
    for x in vertices(qs):
        for a in range(x[i]):
            y = x[:i]+(a,)+x[i+1:]
            diff = u[x]-u[y]
            if abs(diff)>li:
                li=abs(diff)
    if li == 0:
        return li, 0
    for x in vertices(qs):
        for a in range(x[i]):
            y = x[:i]+(a,)+x[i+1:]
            diff = u[x]-u[y]
            if abs(diff)==li:
                derivatives.append((1 if diff>0 else -1)*(du[x]-du[y]))
    return li, max(derivatives)


def kappa(q, c, p):
    ap = 1 if p <= 2 else 2**(2-p)
    return c * (2 + (q-2)*ap)


def extremizer(qs, cs, p, scales):
    axes = []
    for q, s in zip(qs, scales):
        if p <= 2:
            axes.append([s]+[F(0)]*(q-1))
        else:
            axes.append([s/F(2),-s/F(2)]+[F(0)]*(q-2))
    u = {x:sum((axes[i][xi] for i,xi in enumerate(x)),F(0)) for x in vertices(qs)}
    du = vector_field(qs,cs,p,u)
    for i in range(len(qs)):
        li, rate = active_derivatives(qs,i,u,du)
        target = -F(cs[i])*F(kappa(qs[i],1,p))*scales[i]**(p-1)
        assert li == scales[i] and rate == target, (qs,cs,p,i,li,rate,target)


def exact_tests():
    rng=Random(871443)
    checks=0
    extremal_checks=0
    for qs in [(2,), (3,), (5,), (2,2), (2,3), (3,3), (2,2,2), (2,3,2), (3,2,3)]:
        cs = tuple(F(j+2,j+1) for j in range(len(qs)))
        for p in [2,3,4]:
            for _ in range(42):
                u={x:F(rng.randrange(-8,9),rng.randrange(1,5)) for x in vertices(qs)}
                du=vector_field(qs,cs,p,u)
                for i in range(len(qs)):
                    li,rate=active_derivatives(qs,i,u,du)
                    if li>0:
                        assert rate <= -F(kappa(qs[i],cs[i],p))*(li**(p-1)), (qs,p,i,li,rate)
                        checks+=1
            scales=tuple(F(i+2,i+1) for i in range(len(qs)))
            extremizer(qs,cs,p,scales)
            extremal_checks +=len(qs)
    print('EXACT_DIRECTIONAL_DINI_INEQUALITIES_OK',checks)
    print('EXACT_SIMULTANEOUS_EXTREMIZERS_OK',extremal_checks)


def envelope(c,q,p,t,a):
    kk=kappa(q,c,p)
    if a<=0:return 0
    if p==2:return a*__import__('math').exp(-kk*t)
    if p>2:return (a**(2-p)+(p-2)*kk*t)**(1/(2-p))
    return max(0.0,a**(2-p)-(2-p)*kk*t)**(1/(2-p))


def analytic_diagnostics():
    for p in [1.25,1.5,1.95,2.0,2.5,3.0,4.0,6.0]:
        for qs in [(2,2,2),(3,5),(2,3,4)]:
            cs=[1,0.6,2][:len(qs)]
            scales=[1.5,0.8,2][:len(qs)]
            for i,q in enumerate(qs):
                a=scales[i]
                for t in [0,0.025,0.1,0.3]:
                    val=envelope(cs[i],q,p,t,a)
                    assert val>=0 and val<=a+1e-12
                    if t>0:assert val <=envelope(cs[i],q,p,t/2,a)
    for p in [1.4,1.7]:
        q=5;c=F(3,2);a=F(9,7)
        extinction=float(a**(2-p))/((2-p)*kappa(q,c,p))
        assert envelope(float(c),q,p,extinction+1e-6,float(a))==0
        assert envelope(float(c),q,p,extinction-1e-6,float(a))>0
    print('SCALAR_FLOW_AND_EXTINCTION_DIAGNOSTICS_OK')


def independent_flow_check():
    # Advance a 3x2 graph by RK4, verifying the sharp directional bound.
    qs=(3,2);cs=(1.1,0.8)
    rng=Random(6675)
    vv=vertices(qs)
    for p in [1.5,2.0,3.0,4.0]:
        for trial in range(10):
            state={x:rng.uniform(-1,1) for x in vv}
            initial=[]
            for i in range(2):
                init,_=active_derivatives(qs,i,state,{x:0 for x in vv})
                initial.append(init)
            def add(a,b,s):return {x:a[x]+s*b[x] for x in vv}
            h=2.e-5
            for step in range(300):
                k1=vector_field(qs,cs,p,state)
                k2=vector_field(qs,cs,p,add(state,k1,h/2))
                k3=vector_field(qs,cs,p,add(state,k2,h/2))
                k4=vector_field(qs,cs,p,add(state,k3,h))
                state={x:state[x]+h*(k1[x]+2*k2[x]+2*k3[x]+k4[x])/6 for x in vv}
            for i,q in enumerate(qs):
                actual,_=active_derivatives(qs,i,state,{x:0 for x in vv})
                upper=envelope(cs[i],q,p,h*300,initial[i])
                assert actual <= upper + 2.e-8, (p,trial,i,actual,upper)
    print('NONLINEAR_FLOW_ENVELOPES_OK',4*10*2)


if __name__=='__main__':
    exact_tests()
    analytic_diagnostics()
    independent_flow_check()
    print('ALL_HAMMING_PHEAT_TESTS_OK')
