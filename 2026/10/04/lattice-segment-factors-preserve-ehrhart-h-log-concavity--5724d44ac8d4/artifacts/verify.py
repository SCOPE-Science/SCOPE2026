#!/usr/bin/env python3
from math import comb


def lc(a):
    nz=[i for i,x in enumerate(a) if x]
    if not nz:
        return True
    lo,hi=min(nz),max(nz)
    if any(a[i]<=0 for i in range(lo,hi+1)):
        return False
    return all(a[i]*a[i] >= a[i-1]*a[i+1] for i in range(lo+1,hi))


def transform(h,d,m):
    hh=list(h)+[0]*(d+2-len(h))
    out=[]
    for i in range(d+2):
        him1=hh[i-1] if i else 0
        out.append((1+m*i)*hh[i] + (m*(d+2-i)-1)*him1)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def L_from_h(h,d,n):
    s=0
    for i,x in enumerate(h):
        top=n+d-i
        if top>=d:
            s += x*comb(top,d)
    return s


def recover_h(vals,D):
    # numerator coefficients of (1-t)^(D+1) * sum vals[n]t^n
    out=[]
    for j in range(D+2):
        v=0
        for q in range(j+1):
            n=j-q
            if n < len(vals):
                v += (-1)**q * comb(D+1,q) * vals[n]
        out.append(v)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def check_transform(h,d,m):
    g=transform(h,d,m)
    vals=[(m*n+1)*L_from_h(h,d,n) for n in range(d+3)]
    rec=recover_h(vals,d+1)
    assert rec==g,(h,d,m,g,rec)
    assert lc(h)
    assert lc(g),(h,d,m,g)

# Exact identity on a parameter grid.
for d in range(0,10):
    for m in range(1,8):
        for i in range(1,d+1):
            for x,y in [(1,1),(1,2),(2,1),(3,5),(8,3)]:
                A=lambda j: 1+m*j
                B=lambda j: m*(d+2-j)-1
                C=lambda j: A(j)*y+B(j)*x
                assert C(i)*C(i)-C(i-1)*C(i+1)==m*m*(y-x)*(y-x)

# Representative positive log-concave inputs of allowed lengths.
samples=[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1],
    [1,5,10,10,5,1],
    [1,2,2,1],
    [1,3,6,7,6,3,1],
    [1,4,12,20,20,12,4,1],
]
for h in samples:
    assert lc(h)
    d=max(len(h)-1,2)
    for extra in range(0,4):
        D=d+extra
        for m in range(1,8):
            check_transform(h,D,m)

# Repeated segment factors (box check) from several inputs.
for h0,d0 in [([1],0),([1,2,1],2),([1,3,3,1],3),([1,2,2,1],3)]:
    h=list(h0); d=d0
    for m in [1,2,5,3]:
        h=transform(h,d,m)
        d+=1
        assert lc(h)

print('VERIFY_OK')
