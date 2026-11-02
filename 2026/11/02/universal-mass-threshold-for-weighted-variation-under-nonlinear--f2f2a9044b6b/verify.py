"""Reproducibility checks for mass-weighted star p-heat variation generator."""
from fractions import Fraction as F
from itertools import product
import random


def phi(x, p):
    return 0 if x == 0 else (1 if x > 0 else -1) * abs(x)**(p-1)


def diniderivative(g, masses, c, w, p):
    m0=masses[0]
    r=[F(ci)*phi(gi,p) for ci,gi in zip(c,g)]
    S=sum(r)
    v=[-r[i]/masses[i+1]-S/m0 for i in range(len(g))]
    return sum(w[i]*((1 if g[i]>0 else -1)*v[i] if g[i]!=0 else abs(v[i])) for i in range(len(g)))


def beta(masses,w):
    W=sum(w);m0=masses[0]
    return [(W-2*w[i])/m0 - w[i]/masses[i+1] for i in range(len(w))]


def check():
    gen=random.Random(240817)
    count=0;sharp=0;stability=0
    for d in range(1,8):
        for _ in range(180):
            masses=[F(gen.randint(1,9)) for z in range(d+1)]
            c=[F(gen.randint(1,7)) for z in range(d)]
            w=[F(gen.randint(1,8)) for z in range(d)]
            b=beta(masses,w)
            for p in [2,3,4]:
                for _ in range(7):
                    g=[F(gen.randint(-4,4)) for z in range(d)]
                    if not any(g):g[gen.randrange(d)]=F(1)
                    derivative=diniderivative(g,masses,c,w,p)
                    flux=sum(c[i]*abs(g[i])**(p-1) for i in range(d))
                    assert derivative <= max(b)*flux, (d,p,masses,w,g,derivative,max(b)*flux)
                    count+=1
                for i in range(d):
                    g=[F(0)]*d;g[i]=F(1)
                    derivative=diniderivative(g,masses,c,w,p)
                    assert derivative == c[i]*b[i]
                    sharp+=1
            feasible=sum(1/(2+masses[0]/masses[i+1]) for i in range(d)) <= 1
            opt=[1/(2+masses[0]/masses[i+1]) for i in range(d)]
            if feasible:
                remainder=1-sum(opt)
                opt[0]+=remainder
                assert all(z<=0 for z in beta(masses,opt))
            else:
                # If each w_i/W >= 1/d_i, summation would contradict feasibility.
                assert sum(opt)>1
            stability+=1
    print('PASS exact rational derivative bounds:',count)
    print('PASS exact attained generators:',sharp)
    print('PASS sharp mass feasibility certificates:',stability)
    # Concrete high-degree p-independent stability witness.
    d=6; masses=[F(5)]+[F(1)]*d;c=[F(i+1) for i in range(d)];w=[F(1)]*d
    assert sum(1/(2+masses[0]/masses[i+1]) for i in range(d)) < 1
    assert all(z<0 for z in beta(masses,w))
    # Central mass 4 in a six-leaf star is the critical transition.
    masses[0]=F(4)
    assert sum(1/(2+masses[0]/masses[i+1]) for i in range(d))==1
    assert all(z==0 for z in beta(masses,w))
    masses[0]=F(3)
    assert sum(1/(2+masses[0]/masses[i+1]) for i in range(d))>1
    print('PASS six-leaf critical-mass phase diagram')

if __name__=='__main__': check()

# Float cross-checks for genuinely nonlinear exponents, including the non-Lipschitz range.
def fractional_and_flow_check():
    import math
    gen=random.Random(240819)
    ncases=0
    for d in range(1,8):
        for _ in range(190):
            m=[float(gen.randint(1,9)) for _ in range(d+1)]
            c=[float(gen.randint(1,8)) for _ in range(d)]
            w=[float(gen.randint(1,6)) for _ in range(d)]
            beta_num=beta(m,w)
            for p in (1.15,1.5,2.5,3.8):
                g=[float(gen.randint(-8,8)) for _ in range(d)]
                if not any(g):g[0]=1.0
                dv=diniderivative(g,m,c,w,p)
                flux=sum(c[i]*abs(g[i])**(p-1) for i in range(d))
                assert dv <= max(beta_num)*flux + 1e-8*max(1,abs(dv),abs(max(beta_num)*flux))
                ncases+=1
    print('PASS fractional-p Dini checks:',ncases)
    # Small-time Euler approximation of a stable six-leaf star, p=3.
    m=[5.0]+[1.0]*6;c=[1.0,2.0,1.5,0.5,3.0,0.8];w=[1.0]*6;p=3
    for k in range(25):
        g=[gen.uniform(-2,2) for _ in range(6)]
        last=sum(abs(x) for x in g)
        for t in range(600):
            ph=[math.copysign(abs(x)**(p-1),x) for x in g]
            S=sum(c[i]*ph[i] for i in range(6))/m[0]
            dt=.00012
            g=[g[i]-dt*(c[i]*ph[i]/m[i+1]+S) for i in range(6)]
            now=sum(abs(x) for x in g)
            assert now<=last+1e-9,(k,t,now,last)
            last=now
    print('PASS stable nonlinear flow Euler checks:',25*600)

if __name__=='__main__':fractional_and_flow_check()
