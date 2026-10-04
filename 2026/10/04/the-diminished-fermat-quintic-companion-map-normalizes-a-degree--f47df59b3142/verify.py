#!/usr/bin/env python3
# Exact integer-polynomial verification for the six quintics in the stated claim.

def clean(p):
    return {m:c for m,c in p.items() if c}
def add(p,q):
    r=dict(p)
    for m,c in q.items(): r[m]=r.get(m,0)+c
    return clean(r)
def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for (i,j),c in p.items():
        for (k,l),d in q.items(): r[(i+k,j+l)]=r.get((i+k,j+l),0)+c*d
    return clean(r)
def scale(p,s): return clean({m:s*c for m,c in p.items()})
def power(p,n):
    r={(0,0):1}
    for _ in range(n): r=mul(r,p)
    return r
def ev(p,a,b): return sum(c*(a**i)*(b**j) for (i,j),c in p.items())
ONE={(0,0):1}; A={(1,0):1}; B={(0,1):1}
A2=power(A,2); A3=power(A,3); A4=power(A,4); A5=power(A,5)
B2=power(B,2); B3=power(B,3); B5=power(B,5)
u=[
    sub(scale(A2,5),A5),
    sub(B5,scale(B2,5)),
    sub(ONE,scale(A3,5)),
    sub(scale(B3,5),ONE),
    scale(mul(B2,sub(A3,ONE)),5),
    scale(mul(A2,sub(ONE,B3)),5),
]
src=[ev(p,1,2) for p in u]
assert src == [4,12,-4,39,0,-35], src
cross=[sub(scale(u[i],src[2]), scale(u[2],src[i])) for i in [0,1,3,4,5]]
q=add(add(add(add(A4,A3),scale(A2,6)),A),ONE)
expected=[
    scale(mul(sub(A,ONE),q),4),
    scale(add(add(scale(A3,15),neg(B5)),add(scale(B2,5),{(0,0):-3})),4),
    scale(add(add(scale(A3,39),scale(B3,-4)),{(0,0):-7}),5),
    scale(mul(mul(B2,sub(A,ONE)),add(add(A2,A),ONE)),-20),
    scale(add(add(scale(A3,35),scale(mul(A2,B3),-4)),add(scale(A2,4),{(0,0):-7})),-5),
]
assert cross == expected
# The C=0 chart cannot contain the fiber because u3=0 there, while source u3=-4.
assert src[2] != 0
# Branch A!=1, B=0 would require both A^3=1/5 and A^3=7/39.
assert 1*39 != 7*5
# On A^2+A+1=0, q(A) reduces to -4(A+1); A=-1 is not a root of A^2+A+1.
assert ((-1)**2 + (-1) + 1) != 0
# At A=1: equations force B^3=8 and then B^2=4, hence B=2.
assert 2**3 == 8 and 2**2 == 4
# Jacobian of e1=(A-1)q(A), e3=39A^3-4B^3-7 at (1,2).
q_at_1=1+1+6+1+1
d_e3_dB=-12*(2**2)
det=q_at_1*d_e3_dB
assert det == -480
print('VERIFY_OK')
