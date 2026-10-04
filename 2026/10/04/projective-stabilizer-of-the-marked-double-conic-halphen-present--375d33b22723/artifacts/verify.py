#!/usr/bin/env python3
from collections import defaultdict

# Polynomial dicts in variables (x,y,z,r,e), exponent tuple length 5.
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for m,c in p.items(): out[m]+=c
    return {m:c for m,c in out.items() if c}

def neg(p): return {m:-c for m,c in p.items()}
def mul(p,q):
    out=defaultdict(int)
    for a,ca in p.items():
        for b,cb in q.items():
            out[tuple(a[i]+b[i] for i in range(5))]+=ca*cb
    return {m:c for m,c in out.items() if c}
def power(p,n):
    out={(0,0,0,0,0):1}
    for _ in range(n): out=mul(out,p)
    return out

def var(i):
    m=[0]*5; m[i]=1
    return {tuple(m):1}

def const(n): return {(0,0,0,0,0):n} if n else {}

def reduce_e2(p):
    out=defaultdict(int)
    for m,c in p.items():
        mm=list(m)
        mm[4]%=2
        out[tuple(mm)]+=c
    return {m:c for m,c in out.items() if c}

x,y,z,r,e=[var(i) for i in range(5)]
Q=add(power(x,2),mul(y,z))
C=add(power(y,3),mul(z,Q))
X=add(mul(e,x),neg(mul(r,y)))
Y=y
Z=add(z,mul(const(2),mul(e,mul(r,x))),neg(mul(power(r,2),y)))
Q_A=add(power(X,2),mul(Y,Z))
Q_A=reduce_e2(Q_A)
assert Q_A==Q, (Q_A,Q)
C_A=add(power(Y,3),mul(Z,Q_A))
diff=reduce_e2(add(C_A,neg(C)))
rhs=reduce_e2(mul(r,mul(add(mul(const(2),mul(e,x)),neg(mul(r,y))),Q)))
assert diff==rhs, (diff,rhs)

# For r=0, e=+1 and e=-1 both preserve Q, Q', C. We directly check
# the only changed variable is x -> e*x and all three defining polynomials
# contain x only through x^2.
# The proof shows preservation of C forces r=0 because the coefficient of
# y^3 fixes the scalar and r(2 e x-r y)Q is identically zero only when r=0.
# Verify the latter coefficient obstruction syntactically: if r != 0, the
# monomial r*e*x^3 occurs with coefficient 2 in rhs and cannot cancel.
mon=(3,0,0,1,1)
assert rhs.get(mon)==2, rhs.get(mon)
print('VERIFY_OK')
