#!/usr/bin/env python3
"""Standalone exact certificate for a primitive-trinomial counterexample."""
P=41
Q=P*P
E=(Q**P-1)//83

def pair_mul(x,y):
    a,b=x;c,d=y
    return ((a*c+3*b*d)%P,(a*d+b*c)%P)

def pair_pow(x,n):
    v=(1,0)
    while n:
        if n&1:v=pair_mul(v,x)
        n>>=1
        if n:x=pair_mul(x,x)
    return v

lam=(2,16)
assert pow(3,20,41)==40  # u^2=3 defines a field
assert 1680==2**4*3*5*7
vals={l:pair_pow(lam,1680//l) for l in (2,3,5,7)}
assert all(v!=(1,0) for v in vals.values())
assert pow(Q,41,83)==1 and Q%83!=1
assert (Q**41-1)%83==0

def mul_mod(x,y):
    v=[0]*163
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:v[i+j]+=a*b
    for k in range(162,81,-1):
        c=v[k]%P
        if not c:continue
        t=k-82
        v[k]=0
        v[t]-=15*c
        v[t+1]-=4*c
        v[t+2]-=c
        v[t+41]-=4*c
        v[t+42]-=2*c
    return [z%P for z in v[:82]]

def pow_mod_z(n):
    acc=[1]+[0]*81
    z=[0,1]+[0]*80
    while n:
        if n&1:acc=mul_mod(acc,z)
        n>>=1
        if n:z=mul_mod(z,z)
    return acc

remainder=pow_mod_z(E)
assert remainder==[1]+[0]*81, (remainder[:20],len([x for x in remainder if x]))
print('PRIMITIVE_LAMBDA_TESTS',vals)
print('EXPONENT_DIGITS',len(str(E)),'EXPONENT_BITS',E.bit_length())
print('CERTIFICATE_OK', 'p=41', 'lambda=2+16u', 'u^2=3', 'irreducible_degree=41', 'nonprimitive_factor=83')
