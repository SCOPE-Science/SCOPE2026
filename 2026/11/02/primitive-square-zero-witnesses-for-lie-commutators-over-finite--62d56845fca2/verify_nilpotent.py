#!/usr/bin/env python3
"""Checks primitive square-zero witness commutator fibers in sl2 of finite local rings.
Run alongside verify.py: python verify_nilpotent.py. Only Python standard library.
"""
from itertools import product
from collections import Counter
from verify import make_ring

def finite_ring(q,n):
    elems,add,sub,mul,v,z,two,p=make_ring(q,n)
    return (elems,add,sub,mul,v,z,two,p,lambda i:elems[i])

def integer_ring(p,n):
    m=p**n; elems=list(range(m)); z=0
    add=[[(a+b)%m for b in elems] for a in elems]
    sub=[[(a-b)%m for b in elems] for a in elems]
    mul=[[(a*b)%m for b in elems] for a in elems]
    def val(a):
        if a==0:return n
        v=0
        while a%p==0:a//=p;v+=1
        return v
    return (elems,add,sub,mul,[val(a) for a in elems],z,2,p,lambda i:(i,))

def roots_count_by_discriminant(ring,q,n,z):
    elems,plus,sub,times,val,zero,two,p,coords=ring
    a,b,c=z
    s=min(val[t] for t in z)
    if s==n:return q**n+q**(n-1)
    r=n-s
    # In a chain ring, divide modulo the annihilator of pi^s; reduce to length r.
    if isinstance(elems[0],int):
        mod=p**r
        a0=(a//(p**s))%mod;b0=(b//(p**s))%mod;c0=(c//(p**s))%mod
        delta=(c0*c0+a0*b0)%mod
        def residue(t):return t%p
        def vd(t):
            if t==0:return r
            i=0
            while t%p==0:i+=1;t//=p
            return i
        def leading(t,h):return (t//p**h)%p
    else:
        def divide(t):
            return coords(t)[s:]
        a0=divide(a);b0=divide(b);c0=divide(c)
        # field arithmetic from verify.py
        from verify import field_ops
        _,_,fm,_=field_ops(q)
        delta=[0]*r
        for k in range(r):
            for j in range(k+1):
                delta[k]=(delta[k]+0) if False else delta[k]
        fadd,_,fm,_=field_ops(q)
        delta=[0]*r
        for k in range(r):
            for j in range(k+1):delta[k]=fadd(delta[k],fadd(fm(c0[j],c0[k-j]),fm(a0[j],b0[k-j])))
        def vd(t):return next((i for i,d in enumerate(t) if d),r)
        def leading(t,h):return t[h]
    d=vd(delta)
    if d==r:return q**(r//2)
    if d%2:return 0
    u=leading(delta,d)
    from verify import field_ops
    _,_,fm,_=field_ops(q)
    squares={fm(i,i) for i in range(1,q)}
    return 2*q**(d//2) if u in squares else 0

def validate(q,n,mixed=False):
    ring=integer_ring(q,n) if mixed else finite_ring(q,n)
    es,add,sub,mul,v,z,two,p,_=ring
    assert p!=2
    R=len(es)
    all3=list(product(range(R),repeat=3))
    hist=Counter();nilx=0
    for a,b,c in all3:
        if min(v[a],v[b],v[c])!=0 or add[mul[c][c]][mul[a][b]]!=z: continue
        nilx+=1
        for A,B,C in all3:
            E=mul[two][sub[mul[c][A]][mul[a][C]]]
            F=mul[two][sub[mul[b][C]][mul[c][B]]]
            H=sub[mul[a][B]][mul[b][A]]
            hist[E,F,H]+=1
    assert nilx==q**(2*n)-q**(2*n-2),(q,n,nilx)
    for target in all3:
        s=min(v[t] for t in target)
        expected=q**n*(q**n-q**(n-1))*(q**s if s<n else 1)*roots_count_by_discriminant(ring,q,n,target)
        assert hist[target]==expected,(q,n,mixed,target,hist[target],expected)
    print(f'PASS q={q} length={n} mixed={mixed} nilpotent_X={nilx} tested_pairs={nilx*len(all3)} images={len(hist)}')

def main():
    for q,n in ((3,1),(3,2),(5,1),(9,1)):
        validate(q,n)
    validate(3,2,True)
    print('PRIMITIVE_NILPOTENT_SL2_FIBERS_OK')
if __name__=='__main__':main()
