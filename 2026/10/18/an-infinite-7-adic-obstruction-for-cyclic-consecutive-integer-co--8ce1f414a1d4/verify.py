#!/usr/bin/env python3
"""Exact arithmetic certificate for a periodic decimal concatenation obstruction."""
MOD = 49

def followed(first, second):
    """Compose transformations (a,b,c,n): (v,k) -> (a*v+b*k+c,k+n)."""
    a,b,c,n=first
    A,B,C,N=second
    return ((A*a)%MOD,(A*b+B)%MOD,(A*c+B*n+C)%MOD,(n+N)%MOD)

def power_step(base, exponent):
    val=(1,0,0,0)
    while exponent:
        if exponent&1:val=followed(val,base)
        base=followed(base,base)
        exponent//=2
    return val

def block(d):
    first=10**(d-1)
    N=9*first
    r=pow(10,d,MOD)
    a,b,c,_=power_step((r,1,0,1),N)
    return (a,(b*first+c)%MOD,(d*N)%42)

def append_blocks(x,y):
    a,b,l=x
    A,B,L=y
    return ((A*a)%MOD,(A*b+B)%MOD,(l+L)%42)

I=(1,0,0)
blocks=[block(d) for d in range(2,86)]
for d in range(2,44):
    assert block(d)==block(d+42),(d,block(d),block(d+42))
monodromy=I
for d in range(2,44):
    monodromy=append_blocks(monodromy,block(d))
assert monodromy==I,monodromy
# State after all one- to four-digit numbers.
v=0;length=0
for d in range(1,5):
    a,b,l=block(d)
    v=(a*v+b)%MOD
    length=(length+l)%42
# Append the first nine five-digit integers, 10000 through 10008.
r=pow(10,5,MOD)
a,b,c,_=power_step((r,1,0,1),9)
v=(a*v+b*10000+c)%MOD
length=(length+45)%42
assert (v,length)==(14,0),(v,length)
# Independent direct decimal streaming for the initial case.
v2=0;L2=0
for k in range(1,10009):
    word=str(k)
    for digit in word:
        v2=(10*v2+int(digit))%MOD
        L2=(L2+1)%42
assert (v2,L2)==(14,0)
# Verify the sequence of 42 digit-tier maps leaves every boundary state unchanged.
assert len(blocks)==84
print('PASS: period-42 blocks; identity 42-tier transfer; base residues (14,0); independent digit streaming')
