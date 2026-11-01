#!/usr/bin/env python3
"""Independent finite polynomial certificate and coefficient test for colored quaternary partitions."""

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[i+j]+=u*v
    return c

def shift_difference(n):
    a=[0]*(n+1)
    a[0]=1
    a[n]=-1
    return a

def subtract(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]-=v
    return out

def degree_check():
    p=[0,8,4,24,8,8,12,24,16,8,20,24,24,8,28,24]
    u=shift_difference(16)
    v=shift_difference(4)
    w=shift_difference(1)
    w8=[1]
    for _ in range(8):w8=multiply(w8,w)
    top=multiply(u,multiply(v,v))
    lower=multiply(w8,[a+(p[i] if i<len(p) else 0) for i,a in enumerate(u)]+p[len(u):])
    delta=subtract(top,lower)
    while len(delta)>1 and delta[-1]==0:delta.pop()
    assert len(delta)==24
    assert all(t%32==0 for t in delta)
    return len(delta)

def valuation_mod_32(value):
    assert value%32!=0
    i=0
    while value%2==0:
        value//=2
        i+=1
    return i

def v2(n):
    assert n>0
    t=0
    while n%2==0:
        n//=2;t+=1
    return t

def coefficient_check(N=16384):
    # Independently compute the product (1-x)^-8 product_{j>=1}(1-x^(4^j))^-6.
    a=[0]*(N+1)
    a[0]=1
    d=1
    while d<=N:
        colors=8 if d==1 else 6
        for _ in range(colors):
            for n in range(d,N+1):
                a[n]=(a[n]+a[n-d])%32
        d*=4
    for n in range(1,N+1):
        t=v2(n)
        want=3 if n%2 else (2 if t%2 else 4)
        assert valuation_mod_32(a[n])==want,(n,a[n],want)
    assert a[0]==1
    assert a[1]==8 and a[2]==4 and a[4]==16
    b=lambda j:valuation_mod_32(a[j+1])//2
    relations=0
    for j in range((N-12)//16):
        assert b(4*j)==b(4*j+1)==b(4*j+2)==1
        assert b(8*j+7)==b(2*j+1)
        assert b(16*j+11)==b(16*j+3)==b(8*j+3)==2
        relations+=1
    return N,relations

if __name__=='__main__':
    cert=degree_check()
    count,relations=coefficient_check()
    print(f'VERIFY_OK polynomial_coefficients={cert} partition_indices={count} conjecture_relation_inputs={relations}')
