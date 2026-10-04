#!/usr/bin/env python3
import math

d=math.asin(0.25)

def raw_gc2(x,beta):
    sx=math.sin(x); s2=math.sin(2*x)
    if abs(sx)<1e-12 or abs(s2)<1e-12:
        return False
    return 1/abs(s2)-2/abs(sx) > abs(math.cos(2*x)/s2 + 2*math.cos(x)/sx + beta/x)

def reduced(t,m,beta):
    if beta==0 or not (0<t<0.25): return False
    eps=1 if beta>0 else -1
    x=(m+0.5)*math.pi-eps*math.asin(t)
    s=math.sqrt(1-t*t)
    F=x*(2-3*t)/s
    G=x*(1+t)*(1-3*t)/(t*s)
    return F < abs(beta) < G

def threshold(m,eps):
    return math.sqrt(5/3)*((m+0.5)*math.pi-eps*d)

def count_formula(beta):
    if beta==0: return 0
    eps=1 if beta>0 else -1
    R=(math.sqrt(3/5)*abs(beta)+eps*d)/math.pi-0.5
    return max(0,math.ceil(R-1e-14))

def count_grid(beta, mmax=20, N=4000):
    eps=1 if beta>0 else -1 if beta<0 else 0
    if eps==0: return 0
    count=0
    for m in range(mmax):
        vals=[]
        for j in range(1,N):
            t=0.25*j/N
            x=(m+0.5)*math.pi-eps*math.asin(t)
            vals.append(raw_gc2(x,beta))
            assert vals[-1]==reduced(t,m,beta)
        # exactly one component if present
        comp=0; prev=False
        for v in vals:
            if v and not prev: comp+=1
            prev=v
        assert comp in (0,1)
        count += comp
    return count

def check_monotone():
    for eps in (1,-1):
        for m in range(5):
            Fs=[]; Gs=[]
            for j in range(1,2000):
                t=0.25*j/2000
                x=(m+0.5)*math.pi-eps*math.asin(t)
                s=math.sqrt(1-t*t)
                F=x*(2-3*t)/s
                G=x*(1+t)*(1-3*t)/(t*s)
                assert G>F
                Fs.append(F); Gs.append(G)
            assert all(Fs[i+1]<Fs[i] for i in range(len(Fs)-1))
            assert all(Gs[i+1]<Gs[i] for i in range(len(Gs)-1))

check_monotone()
for beta in (2.0,5.0,5.8,10.0,20.0,-2.0,-2.36,-5.0,-6.5,-10.0,-20.0):
    cg=count_grid(beta)
    cf=count_formula(beta)
    assert cg==cf,(beta,cg,cf)
# equality threshold is excluded; values just above are included.
for eps in (1,-1):
    for m in range(4):
        th=threshold(m,eps)
        assert not any(reduced(0.25*j/5000,m,eps*th) for j in range(1,5000))
        assert any(reduced(0.25*j/5000,m,eps*(th+0.05)) for j in range(1,5000))
print('VERIFY_OK')
print('thresholds_positive =', [threshold(m,1) for m in range(3)])
print('thresholds_negative_abs =', [threshold(m,-1) for m in range(3)])
