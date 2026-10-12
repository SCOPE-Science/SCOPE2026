#!/usr/bin/env python3
from math import comb


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def sub(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]-=x
    return trim(c)

def scale(a,s): return trim([s*x for x in a])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def deriv(a): return trim([i*a[i] for i in range(1,len(a))] or [0])

def qminus1_times(a): return sub([0]+a,a)

def shift(a,n): return [0]*n+list(a)

checked=0
for k in range(4,201):
    D=[1]*(k+1)
    E=[1]*k
    C=[0]+[1]*(k-1)
    dD,dE,dC=deriv(D),deriv(E),deriv(C)
    cross=sub(mul(dD,E),mul(D,dE))
    # N(theta=0): k(D'E-DE')C - C'DE
    N0=sub(scale(mul(cross,C),k),mul(dC,mul(D,E)))
    # N(theta=1), with H=C-D
    H1=sub(C,D); dH1=deriv(H1)
    N1=sub(scale(mul(cross,H1),k),mul(dH1,mul(D,E)))

    P=[0]*(2*k-3)
    for i in range(0,k-1): P[i]=comb(i+3,3)
    for i in range(k-1,2*k-3): P[i]=comb(2*k-1-i,3)
    R=[(j+1)*(k-1-j) for j in range(k-1)]
    extra=scale(shift(R,k-1),k)
    expect0=qminus1_times(add(mul(D,P),extra))
    expect1=qminus1_times(extra)
    assert trim(N0)==trim(expect0), ('theta0',k)
    assert trim(N1)==trim(expect1), ('theta1',k)
    assert all(x>0 for x in P), ('P positivity',k)
    assert all(x>0 for x in R), ('R positivity',k)
    checked+=1

# Reciprocal invariance and branch reconstruction, numerical corroboration only.
max_res=0.0
cases=0
for k in (4,5,6,8,12,20):
    theta_c=(k-1)/(k+1)
    for theta in (0.1*theta_c,0.5*theta_c,0.9*theta_c):
        for q in (1.05,1.2,1.7):
            D=sum(q**j for j in range(k+1))
            E=sum(q**j for j in range(k))
            C=sum(q**j for j in range(1,k))
            H=C-theta*D
            if H<=0: continue
            u=H**(-1.0/k); v=u*q
            a=u*D/E
            den=1+u**k+v**k
            r1=a*(1+u**k+theta*v**k)/den
            r2=a*(1+theta*u**k+v**k)/den
            lam=(D**k)/(E**k*H)
            qi=1.0/q
            Di=sum(qi**j for j in range(k+1))
            Ei=sum(qi**j for j in range(k))
            Ci=sum(qi**j for j in range(1,k))
            lami=(Di**k)/(Ei**k*(Ci-theta*Di))
            max_res=max(max_res,abs(r1/u-1),abs(r2/v-1),abs(lami/lam-1))
            cases+=1
assert max_res < 2e-11, max_res
print(f'VERIFY_OK derivative_identity_k=4..200 exact_orders={checked} branch_cases={cases} max_residual={max_res:.3e}')
