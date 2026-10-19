"""Exact finite consistency checks for polynomial circular-cycle synthesis.

Run: python3 verify.py
Standard library only. The all-parameter theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, sqrt, exp

checks = 0

def ok(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
        if not c[k]:
            del c[k]
    return c

def scale(a, k):
    return {idx: coeff*k for idx, coeff in a.items() if coeff*k}

def mul(a, b):
    c = {}
    for (i, j), v in a.items():
        for (h, k), w in b.items():
            c[(i+h,j+k)] = c.get((i+h,j+k), F(0)) + v*w
    return {idx:v for idx,v in c.items() if v}

def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def polyval(a,t):
    out=F(0)
    for v in a[::-1]:
        out=out*t+v
    return out

def poly_derivative(a,t):
    return sum((i*a[i]*t**(i-1) for i in range(1,len(a))),F(0))

def interpolate(nodes,vals):
    result=[F(0)]*len(nodes)
    for idx,t in enumerate(nodes):
        basis=[F(1)]; den=F(1)
        for j,z in enumerate(nodes):
            if idx == j: continue
            basis=poly_mul(basis,[-z,F(1)]);den*=t-z
        for j,val in enumerate(basis):
            result[j]+=vals[idx]*val/den
    return result

def compose_s(coeffs):
    """Build polynomial in x,y by substituting s=x*x+y*y."""
    s={(2,0):F(1),(0,2):F(1)}
    out={};power={(0,0):F(1)}
    for v in coeffs:
        out=add(out,scale(power,v));power=mul(power,s)
    return out

X={(1,0):F(1)};Y={(0,1):F(1)};X2=mul(X,X);Y2=mul(Y,Y)

nodes_all=[1,2,4,7,11]
for n in range(1,6):
    nodes=list(map(F,nodes_all[:n]))
    q=[F(1)]
    for a in nodes:
        q=poly_mul(q,[-a,F(1)])
    q0=q[0]
    qs=compose_s(q)
    radial=compose_s(q[1:])
    for signs in product((-1,1), repeat=n):
        beta=list(map(F,signs))
        b=interpolate(nodes,beta)
        for a, val in zip(nodes,beta):
            ok(polyval(b,a)==val,'Lagrange value')
        C=F(2+abs(q0)+sum(nodes))
        for a, val in zip(nodes,beta):
            ok(C*C > a*val*val+q0*q0/a, 'angular positivity')
        bw=compose_s(b)
        P=add(add(mul(mul(X,Y),radial),scale(Y,-C)),scale(mul(Y2,bw),-1))
        Q=add(add(add(mul(Y2,radial),{(0,0):q0}),scale(X,C)),mul(mul(X,Y),bw))
        ok(add(mul(X,P),mul(Y,Q))==mul(Y,qs),'radial polynomial identity')
        deg=max([sum(k) for k in P]+[sum(k) for k in Q])
        ok(deg==2*n,'exact polynomial degree')
        for a, val in zip(nodes,beta):
            derivative=poly_derivative(q,a)
            ok(derivative!=0,'simple radial root')
            D=sqrt(float(C*C-a*val*val-q0*q0/a))
            log_multiplier=(-4*pi*float(a*derivative*val))/(D*(float(C)+D))
            ok((log_multiplier<0)==(derivative*val>0),'prescribed Floquet sign')
            r=sqrt(float(a));cs=float(C);A=float(val)*r;B=float(q0)/r
            N=2048
            integral=(2*pi/N)*sum(sin(2*pi*(k+0.5)/N)/(cs+A*sin(2*pi*(k+0.5)/N)+B*cos(2*pi*(k+0.5)/N)) for k in range(N))
            approx=2*r*float(derivative)*integral
            ok(abs(log_multiplier-approx)<3e-11,'independent angular quadrature')
print(f'PASS: {checks} exact and numerical consistency assertions across all stability patterns for n=1..5')
