#!/usr/bin/env python3
from math import isclose

# Coefficients are in ascending powers.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def sub(a,b):
    return add(a,[-x for x in b])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def deriv(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])

def shift_one(a):
    # Return coefficients of a(1+s), exact integers.
    from math import comb
    out=[0]*len(a)
    for i,ai in enumerate(a):
        for j in range(i+1): out[j]+=ai*comb(i,j)
    return trim(out)

N=[2,1,1,1,1]          # t^4+t^3+t^2+t+2
Q=[0,1,1,1]            # t^3+t^2+t
D=[1,1,1,1]            # t^3+t^2+t+1
t=[0,1]
one=[1]
t4=[0,0,0,0,1]

assert sub(N,Q)==[2,0,0,0,1]
assert sub(N,mul(t,Q))==[2,1]
R=add(mul(add(t4,one),Q),N)
assert R==mul([2,0,0,0,1],D)

# Dominance identity t^3(t+2)-(t^4+2)=2(t-1)(t^2+t+1).
lhs=sub(mul([0,0,0,1],[2,1]),[2,0,0,0,1])
rhs=mul([-2,2],[1,1,1])
assert lhs==rhs

# Gap for lambda_b < 1/2 on t>1 and its positive-coefficient shift.
gap=sub(mul(mul([1,1],[1,0,1]),[2,0,0,0,1]), mul([0,0,0,2],[2,1]))
assert gap==[2,2,2,-2,-1,1,1,1]
assert shift_one(gap)==[6,14,36,59,54,28,8,1]

# Quotient-rule numerator of theta=N/Q.
num=sub(mul(deriv(N),Q),mul(N,deriv(Q)))
assert num==[-2,-4,-6,0,3,2,1]

# At a root of p=t^3+t^2+t-1, theta=2(1+t).
p=[-1,1,1,1]
assert sub(N,mul([2,2],Q))==mul([-2,-1],p)

# Numerical isolation only for display.
def poly(x): return x*x*x+x*x+x-1.0
lo,hi=0.0,1.0
for _ in range(120):
    mid=(lo+hi)/2
    if poly(mid)<0: lo=mid
    else: hi=mid
rho=(lo+hi)/2
assert 0.5436890126 < rho < 0.5436890128
print('VERIFY_OK', f'rho={rho:.15f}', f'theta_KS={2*(1+rho):.15f}', 'gap_shift=6,14,36,59,54,28,8,1')
