#!/usr/bin/env python3
"""Independent finite-state checks of a Haar-coin averaged walk's capacity formulas.

Standard-library only; numerical tests are checks, not substitutes for the proof.
"""
import math

CHECKS = 0

def close(a, b, tol=2e-11):
    global CHECKS
    CHECKS += 1
    assert abs(a-b) < tol, (a,b,tol)

def walk(d,t):
    n=1<<d
    p=[0.0]*n
    p[0]=1.0
    for _ in range(t):
        p=[sum(p[x^(1<<k)] for k in range(d))/d for x in range(n)]
    return p

def signed_spectrum(d,t):
    n=1<<d
    lamb=[1.0-2.0*u.bit_count()/d for u in range(n)]
    return [sum(((-1 if (u & x).bit_count()%2 else 1))*lamb[u]**t for u in range(n))/n for x in range(n)]

def capacity(d,t):
    p=walk(d,t)
    return d+sum(z*math.log2(z) for z in p if z>0)

def capacity_excess(d,t):
    n=1<<d
    p=walk(d,t)
    base=2.0/n
    acc=0.0
    for x,px in enumerate(p):
        if x.bit_count()%2!=t%2:
            close(px,0)
        else:
            delta=px/base-1
            if abs(delta)<1e-4:
                term=0.5*delta**2-(delta**3)/6+delta**4/12-delta**5/20
            else:
                term=(1+delta)*math.log1p(delta)-delta
            acc+=base*term
    return acc/math.log(2)

def partial_trace_coin(rho,d,n):
    return [[sum(rho[a*n+x][a*n+y] for a in range(d)) for y in range(n)] for x in range(n)]

def one_step_full(rho,d):
    n=1<<d
    reduced=partial_trace_coin(rho,d,n)
    out=[[0j]*(d*n) for _ in range(d*n)]
    for k in range(d):
        shift=1<<k
        for x in range(n):
            for y in range(n):
                out[k*n+(x^shift)][k*n+(y^shift)]=reduced[x][y]/d
    return out

def vertex_step(rho,d):
    n=1<<d
    return [[sum(rho[x^(1<<k)][y^(1<<k)] for k in range(d))/d for y in range(n)] for x in range(n)]

def predicted_full(rho,d,t):
    n=1<<d
    reduced=partial_trace_coin(rho,d,n)
    for _ in range(t-1):
        reduced=vertex_step(reduced,d)
    out=[[0j]*(d*n) for _ in range(d*n)]
    for k in range(d):
        shift=1<<k
        for x in range(n):
            for y in range(n):
                out[k*n+(x^shift)][k*n+(y^shift)]=reduced[x][y]/d
    return out

for d in range(2,8):
    n=1<<d
    for t in range(0,9):
        p=walk(d,t)
        ps=signed_spectrum(d,t)
        close(sum(p),1)
        for a,b in zip(p,ps):
            close(a,b,3e-12)
        for x in range(n):
            if x.bit_count()%2!=t%2:
                close(p[x],0)
        c=capacity(d,t)
        assert 1-1e-11<=c<=d+1e-11
        if t>0:
            assert capacity(d,t-1)+1e-12>=c
for t in range(1,16):
    close(capacity(2,t),1.0,1e-10)
for d,t in [(3,8),(4,9),(5,13),(6,16),(7,18)]:
    alpha=1-2/d
    observed=capacity_excess(d,t)/alpha**(2*t)
    expected=d/(2*math.log(2))
    assert abs(observed/expected-1)<0.035,(d,t,observed,expected)
    CHECKS+=1
for d in (2,3):
    n=1<<d
    size=d*n
    v=[(math.sin(i+.5)+1j*math.cos(2*i+.3))/math.sqrt(size) for i in range(size)]
    norm=sum(abs(z)**2 for z in v)
    v=[z/math.sqrt(norm) for z in v]
    rho=[[v[i]*v[j].conjugate() for j in range(size)] for i in range(size)]
    for t in range(1,6):
        rho=one_step_full(rho,d)
        target=predicted_full([[v[i]*v[j].conjugate() for j in range(size)] for i in range(size)],d,t)
        for i in range(size):
            for j in range(size):
                close(rho[i][j],target[i][j],3e-12)
print('CHECKS_PASSED',CHECKS)
# Additional non-hypercube Abelian examples: cycles with symmetric steps.
for n in (3,4,5,6,7,8):
    steps=(1,n-1)
    p=[0.0]*n
    p[0]=1.0
    for t in range(1,19):
        p=[(p[(i-1)%n]+p[(i+1)%n])/2 for i in range(n)]
        eigen=[math.cos(2*math.pi*k/n) for k in range(n)]
        pf=[sum(eigen[k]**t*math.cos(2*math.pi*k*x/n) for k in range(n))/n for x in range(n)]
        for x in range(n):
            close(p[x],pf[x],2e-12)
        h=2 if n%2==0 else 1
        baseline=math.log2(h)
        c=math.log2(n)+sum(z*math.log2(z) for z in p if z>0)
        assert c+1e-12>=baseline
        if n==4 and t>=1:
            close(c,1,1e-11)
        if n in (3,5,6,7,8) and t==15:
            exclude={0}
            if n%2==0:
                exclude.add(n//2)
            others=[abs(eigen[k]) for k in range(n) if k not in exclude]
            r=max(others)
            mult=sum(abs(z-r)<1e-12 for z in others)
            expected=mult/(2*h*math.log(2))
            # High-precision direct KL expression would be preferable for tiny differences.
            if r**30>1e-12:
                ratio=(c-baseline)/(r**(2*t))
                assert abs(ratio/expected-1)<0.05,(n,ratio,expected)
                CHECKS+=1
print('CHECKS_PASSED_FINAL',CHECKS)
