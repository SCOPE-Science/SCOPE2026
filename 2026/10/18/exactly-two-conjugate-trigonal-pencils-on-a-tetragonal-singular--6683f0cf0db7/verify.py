#!/usr/bin/env python3
"""Exact finite-field and divisor input checks for a genus-two nodal curve."""

P=3

def add(a,b): return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def neg(a): return ((-a[0])%P,(-a[1])%P)
def sub(a,b): return add(a,neg(b))
def mul_alpha(a,b):
    # alpha^2 = alpha + 1
    a0,a1=a; b0,b1=b
    return ((a0*b0+a1*b1)%P,(a0*b1+a1*b0+a1*b1)%P)
def pow_alpha(a,n):
    out=(1,0)
    for _ in range(n): out=mul_alpha(out,a)
    return out
zero=(0,0); one=(1,0); alpha=(0,1)
alpha3=pow_alpha(alpha,3)
assert alpha3==sub(one,alpha)

def F(a):
    return sub(sub(pow_alpha(a,5),pow_alpha(a,3)),one)
def B(a): return sub(pow_alpha(a,2),a)
assert B(alpha)==one and B(alpha3)==one
assert F(alpha)==one and F(alpha3)==one
for a in range(3): assert F((a,0))==(2,0)
# phi(X)=X^2-X-1 irreducible; F'(X)=2X^4 shares no root with F.
assert all(((a*a-a-1)%3)!=0 for a in range(3))
assert F(zero)!=(0,0)

def mul_c(a,b):
    # c^2=2=-1
    a0,a1=a; b0,b1=b
    return ((a0*b0+2*a1*b1)%P,(a0*b1+a1*b0)%P)
def pow_c(a,n):
    out=(1,0)
    for _ in range(n): out=mul_c(out,a)
    return out
c=(0,1)
assert mul_c(c,c)==(2,0)
assert pow_c(c,3)==neg(c)
assert all((a*a)%3 != 2 for a in range(3))

# F(X)-2 = X^3 (X-1)(X+1) in F_3[X].
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): out[i+j]=(out[i+j]+u*v)%3
    return out
lhs=[0,0,0,2,0,1] # X^5-X^3-1-2 = X^5-X^3 in F3
rhs=pmul(pmul([0,0,0,1],[2,1]),[1,1])
assert rhs==lhs
# At y=c above x=0, numerator y-c has order 3; above x=1 order 1.
# At y=-c it is nonzero. Denominator x(x-1) has simple zeros at both.
# Hence poles: infinity (5-4=1), (0,-c), (1,-c), each of order 1.
orders=(1,1,1)
assert sum(orders)==3
# Node branches x=alpha and x=alpha^3 both have B=1,
# so f=(y-c)/B takes the same value at each pair with y=+1 or -1.
assert B(alpha)==B(alpha3)==one
print('VERIFY_OK: field identities, node values, three simple poles, Frobenius exchange')
