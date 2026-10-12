#!/usr/bin/env python3
from itertools import product

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def sub(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]-=v
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def scale(a,k): return trim([k*x for x in a])
def shift(a,k): return [0]*k+a

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def power(a,n):
    r=[1]
    b=a[:]
    while n:
        if n&1: r=mul(r,b)
        b=mul(b,b); n//=2
    return r

def formula(n):
    one=[1,1]
    tri=[1,1,1]
    H=sub(sub(power(tri,n),power(one,n)),scale(shift(power(one,n-1),2),n))
    Q=sub(sub(mul([0,1,1],power(tri,n-1)),mul([0,1,1],power(one,n-1))),scale(shift(power(one,n-2),3),n-1))
    R=shift([1],2*n)
    R=add(R,scale(shift(power(one,n-1),n+2),2*n))
    inner=sub(sub(power(one,n),[1]),[0,n])
    R=add(R,scale(shift(mul(power(one,n),inner),n),2))
    R=add(R,scale(shift(power(one,2*n-2),4),n))
    R=add(R,scale(shift(power(one,2*n-4),6),n*(n-1)))
    R=add(R,scale(shift(mul(power(one,n-1),Q),2),2*n))
    R=add(R,mul(H,H))
    return trim(R)

def is_rdf(labels,n):
    # vertices 0..n-1 are a_i, n..2n-1 are b_i; a_i b_i is the deleted edge.
    for i,v in enumerate(labels):
        if v != 0: continue
        if i < n:
            if not any(labels[n+j]==2 for j in range(n) if j!=i): return False
        else:
            j=i-n
            if not any(labels[k]==2 for k in range(n) if k!=j): return False
    return True

def brute(n):
    c=[0]*(4*n+1)
    for lab in product((0,1,2), repeat=2*n):
        if is_rdf(lab,n): c[sum(lab)]+=1
    return trim(c)

labelings=0
coefficient_checks=0
minimum_checks=0
for n in range(3,7):
    b=brute(n); f=formula(n)
    labelings += 3**(2*n)
    L=max(len(b),len(f))
    bb=b+[0]*(L-len(b)); ff=f+[0]*(L-len(f))
    for i in range(L):
        assert bb[i]==ff[i], (n,i,bb[i],ff[i])
        coefficient_checks += 1
    nz=[i for i,v in enumerate(b) if v]
    assert nz[0]==4 and b[4]==n, (n,nz[0],b[4])
    minimum_checks += 1
print(f"VERIFY_OK n_range=3..6 labelings={labelings} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=12")
