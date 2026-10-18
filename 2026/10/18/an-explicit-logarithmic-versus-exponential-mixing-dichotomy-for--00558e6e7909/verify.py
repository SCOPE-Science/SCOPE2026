#!/usr/bin/env python3
"""Standalone finite-state checks for the stated synchronous opinion model."""
import math
from math import comb

def sig(z):
    return 1/(1+math.exp(-z))

def kernel(n,beta,gamma,p):
    out=[]
    for k in range(n+1):
        a=sig(beta*(gamma*(2*k/n-1)+2*(1-gamma)))
        b=sig(beta*(gamma*(2*k/n-1)-2*(1-gamma)))
        row=[comb(n,l)*(p*a**l*(1-a)**(n-l)+(1-p)*b**l*(1-b)**(n-l)) for l in range(n+1)]
        assert all(v>0 for v in row)
        assert abs(sum(row)-1)<1e-10
        out.append(row)
    return out

for n in (2,4,7):
    for p in (0,.25,.5,.8,1):
        gamma=.4
        beta=2
        ker=kernel(n,beta,gamma,p)
        c=beta*gamma/2
        for k in range(n+1):
            for l in range(n+1):
                for x in (-1,1):
                    aa=sig(beta*(gamma*(2*k/n-1)+2*(1-gamma)*x))
                    bb=sig(beta*(gamma*(2*l/n-1)+2*(1-gamma)*x))
                    assert n*abs(aa-bb)<=c*abs(k-l)+1e-12
        if p==.5 and n==4:
            assert len(ker)==5

gamma=.8; beta=20; delta=.1
h=gamma*(1-2*delta)-2*(1-gamma)
q=sig(-beta*h)
assert h>0 and 0<q<delta
D=delta*math.log(delta/q)+(1-delta)*math.log((1-delta)/(1-q))
assert D>.16
for n in (2,5,10,20):
    K=kernel(n,beta,gamma,.3)
    hi=[k for k in range(n+1) if k/n>=1-delta]
    lo=[k for k in range(n+1) if k/n<=delta]
    for k in hi:
        exit_prob=sum(K[k][j] for j in range(n+1) if j not in hi)
        assert exit_prob <= math.exp(-n*D)+1e-11
    for k in lo:
        exit_prob=sum(K[k][j] for j in range(n+1) if j not in lo)
        assert exit_prob <= math.exp(-n*D)+1e-11
print('PASS: positive transition kernels, contraction checks, two metastable regions; N=2,4,5,7,10,20')
print('admissible barrier and rate:',h,q,D)
