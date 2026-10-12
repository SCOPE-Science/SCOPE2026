#!/usr/bin/env python3
import sympy as sp

def check_n(n):
    lam, mu, beta, alpha = sp.symbols("lam mu beta alpha", positive=True)
    S, R = sp.symbols("S R", nonnegative=True)
    I = sp.symbols("I1:"+str(n+1), nonnegative=True)
    delta = sp.symbols("d1:"+str(n+1), positive=True)
    theta = sp.symbols("t1:"+str(n+1), positive=True)
    if n == 1:
        gamma = [sp.Integer(0)]
    else:
        gs = sp.symbols("g1:"+str(n), positive=True)
        gamma = list(gs)+[sp.Integer(0)]
    rhs = []
    rhs.append(lam + alpha*R - mu*S - beta*S*I[0])
    a = [mu+delta[j]+theta[j]+gamma[j] for j in range(n)]
    rhs.append(beta*S*I[0]-a[0]*I[0])
    for j in range(1,n):
        rhs.append(gamma[j-1]*I[j-1]-a[j]*I[j])
    rhs.append(sum(theta[j]*I[j] for j in range(n))-(alpha+mu)*R)
    Nprime = sp.expand(sum(rhs))
    target = sp.expand(lam-mu*(S+R+sum(I))-sum(delta[j]*I[j] for j in range(n)))
    assert sp.simplify(Nprime-target) == 0
    S0 = lam/mu
    R0 = beta*S0/a[0]
    factor = sp.expand(a[0]*(R0-1)+beta*(S-S0))
    assert sp.simplify(factor-(beta*S-a[0])) == 0
    for j in range(1,n):
        assert sp.simplify(rhs[1+j]-(gamma[j-1]*I[j-1]-a[j]*I[j])) == 0

for n in range(1,9):
    check_n(n)
print("VERIFY_OK")
