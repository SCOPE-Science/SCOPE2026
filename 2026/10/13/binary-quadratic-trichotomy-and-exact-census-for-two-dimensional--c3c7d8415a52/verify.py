"""Finite-field enumeration for perfect 2D commutative algebras.
Run: python verify.py
"""
from itertools import product, combinations

def finite_field(q):
    if q == 4:
        def add(a,b): return a^b
        def mul(a,b):
            z=0
            while b:
                if b&1: z ^= a
                b >>= 1
                a <<= 1
                if a&4: a ^= 7 # t^2=t+1
            return z
        return add,mul
    def add(a,b): return (a+b)%q
    def mul(a,b): return a*b%q
    return add,mul

def work(q):
    add,mul=finite_field(q)
    sub=lambda x,y: add(x, next(z for z in range(q) if add(z,y)==0))
    neg=lambda x:next(z for z in range(q) if add(x,z)==0)
    V=list(product(range(q),repeat=2))
    zero=(0,0)
    va=lambda a,b:(add(a[0],b[0]),add(a[1],b[1]))
    vm=lambda a,b:(mul(a,b[0]),mul(a,b[1]))
    cross=lambda a,b:sub(mul(a[0],b[1]),mul(a[1],b[0]))
    lines=[]
    for x in V:
        if x==zero: continue
        if not any(cross(x,y)==0 for y in lines):lines.append(x)
    assert len(lines)==q+1
    relation_types={}
    def canon(z):
        assert z!=(0,0,0)
        first=next(x for x in z if x)
        inv=next(i for i in range(1,q) if mul(i,first)==1)
        return tuple(mul(inv,x) for x in z)
    def coeff(x,y): return (mul(x[0],y[0]),add(mul(x[0],y[1]),mul(x[1],y[0])),mul(x[1],y[1]))
    for x in lines:
        relation_types[canon(coeff(x,x))]='double'
    for x,y in combinations(lines,2):
        z=canon(coeff(x,y))
        assert z not in relation_types
        relation_types[z]='split'
    assert len(relation_types)==q+1+q*(q+1)//2
    assert len({canon(x) for x in product(range(q),repeat=3) if x!=(0,0,0)})==q*q+q+1
    all_GL=[(x,y) for x in V for y in V if cross(x,y)!=0]
    assert len(all_GL)==(q*q-1)*(q*q-q)
    counts=dict(split=0,double=0,irreducible=0)
    for A,B,C in product(V,repeat=3):
        # Surjectivity of Sym^2 V -> V.
        if not any(cross(x,y)!=0 for x,y in ((A,B),(A,C),(B,C))): continue
        ker=next((a,b,c) for a,b,c in product(range(q),repeat=3) if (a,b,c)!=(0,0,0)
            and va(va(vm(a,A),vm(b,B)),vm(c,C))==zero)
        kind=relation_types.get(canon(ker),'irreducible')
        counts[kind]+=1
        # Independent brute-force natural-basis test, with no use of the kernel.
        def prod(x,y):
            t1=vm(mul(x[0],y[0]),A)
            t2=vm(add(mul(x[0],y[1]),mul(x[1],y[0])),B)
            t3=vm(mul(x[1],y[1]),C)
            return va(va(t1,t2),t3)
        nats=sum(prod(x,y)==zero for x,y in all_GL)
        assert nats==(2*(q-1)**2 if kind=='split' else 0),(q,A,B,C,kind,nats)
        # Exact 3D evolution envelope. U=f1+f3, V=f2+f3.
        w1=va(A,vm(neg(1),B)); w2=va(C,vm(neg(1),B)); w3=B
        assert va(w1,w3)==A and va(w2,w3)==C
        assert any(cross(x,y)!=0 for x,y in ((w1,w2),(w1,w3),(w2,w3)))
    G=(q*q-1)*(q*q-q)
    expected={'split':G*q*(q+1)//2,'double':G*(q+1),'irreducible':G*q*(q-1)//2}
    assert counts==expected,(q,counts,expected)
    print(f'q={q}: all_perfect={sum(counts.values())} split={counts["split"]} double={counts["double"]} irreducible={counts["irreducible"]}; natural_bases_checked=YES; three_dimensional_realization_checked=YES')

for q in (2,3,4,5):work(q)
print('VERIFY_OK')
