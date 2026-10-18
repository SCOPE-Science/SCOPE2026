#!/usr/bin/env python3
"""Standalone finite-n checks for Chebyshev--Lobatto single-node erasure.

Only Python's standard library is required. These checks support but do not
prove the infinite-degree assertions in the accompanying analytical proof.
"""
import math

PI = math.pi
N_ASSERT = 0

def ck(condition, message):
    global N_ASSERT
    N_ASSERT += 1
    if not condition:
        raise AssertionError(message)

def nodes_weights(n):
    x = [math.cos(j*PI/n) for j in range(n+1)]
    w = [((-1)**j)*(0.5 if j in (0,n) else 1.0) for j in range(n+1)]
    return x,w

def cards(x,w,t):
    for j,z in enumerate(x):
        if abs(t-z)<1e-13:
            return [1.0 if i==j else 0.0 for i in range(len(x))]
    a=[v/(t-z) for v,z in zip(w,x)]
    total=sum(a)
    return [v/total for v in a]

def deleted_cards(n,k,t):
    x,w=nodes_weights(n)
    xx=[z for j,z in enumerate(x) if j!=k]
    ww=[w[j]*(x[j]-x[k]) for j in range(n+1) if j!=k]
    return cards(xx,ww,t)

def sinc(y):
    return math.sin(y)/y if abs(y)>1.e-12 else 1.0-y*y/6.0

def limit_mode(k,z):
    a=k*PI
    d=z-a
    return abs(sinc(d)*2*z/(z+a))

def golden_max(f,lo,hi):
    gr=(math.sqrt(5.0)-1.0)/2.0
    c=hi-gr*(hi-lo); d=lo+gr*(hi-lo)
    for _ in range(90):
        if f(c)<f(d): lo=c; c=d; d=lo+gr*(hi-lo)
        else: hi=d; d=c; c=hi-gr*(hi-lo)
    return f((hi+lo)/2.0),(hi+lo)/2.0

for n in [3,4,5,8,12,20,40]:
    x,w=nodes_weights(n)
    ck(abs(sum(w))<1.e-13, f'weights sum, n={n}')
    for k in sorted(set([0,1,n//2,n-1,n])):
        A=(n-1 if k not in (0,n) else 2*n-1)
        vec=deleted_cards(n,k,x[k])
        ck(abs(sum(map(abs,vec))-A)<3.e-7, f'node-loss evaluation, n={n}, k={k}')
        for j,q in enumerate([jj for jj in range(n+1) if jj!=k]):
            ck(abs(vec[j]+w[q]/w[k])<5.e-7, f'node-loss signs, n={n}, k={k}, j={j}')
        for m in range(10):
            theta=(m+0.319)*PI/10
            t=math.cos(theta)
            full=cards(x,w,t)
            red=deleted_cards(n,k,t)
            corrected=[full[j]-w[j]/w[k]*full[k] for j in range(n+1) if j!=k]
            ck(max(abs(a-b) for a,b in zip(red,corrected))<1.e-7,
               f'exact erasure identity, n={n}, k={k}, m={m}')
            err=abs(sum(map(abs,red))-A*abs(full[k]))
            ck(err<=sum(map(abs,full))+1.e-7,
               f'pointwise norm comparison, n={n}, k={k}, m={m}')

for k in range(1,9):
    a=k*PI
    f=lambda z: limit_mode(k,z)
    rho,z=golden_max(f,a,a+0.7)
    ck(rho>1.0, f'positive overshoot k={k}')
    ck(abs(limit_mode(k,a)-1.0)<1.e-12,f'removable value k={k}')
    if k>=3:
        ck(abs((rho-1)*a*a - .375)<.12,f'large k correction k={k}')

# Finite-degree grids, which only corroborate convergence.
for n in [64,128,256]:
    x,w=nodes_weights(n)
    for k in [0,1,2,n//2,n-2,n-1,n]:
        A=(n-1 if k not in(0,n) else 2*n-1)
        m=sum(map(abs,deleted_cards(n,k,x[k])))
        for i in range(3201):
            t=math.cos((i+0.418)*PI/3201.0)
            v=deleted_cards(n,k,t)
            m=max(m,sum(map(abs,v)))
        ck(m>=A-1.e-4,f'finite lower bound n={n}, k={k}')
        if k in(0,n):
            ck(abs(m/n-2)<.12,f'endpoint regime n={n}')
        elif k==n//2:
            ck(abs(m/n-1)<.08,f'bulk regime n={n}')
        elif k in(1,n-1):
            rho=golden_max(lambda z:limit_mode(1,z),PI,PI+.7)[0]
            ck(abs(m/n-rho)<.07,f'first boundary regime n={n}')
        else:
            rho=golden_max(lambda z:limit_mode(2,z),2*PI,2*PI+.7)[0]
            ck(abs(m/n-rho)<.07,f'second boundary regime n={n}')

print('PASS:', N_ASSERT, 'deterministic finite comparisons')
print('Boundary mode k=1:',golden_max(lambda z:limit_mode(1,z),PI,PI+.7))
print('Boundary mode k=2:',golden_max(lambda z:limit_mode(2,z),2*PI,2*PI+.7))
print('No infinite statement is inferred from finite checks.')
