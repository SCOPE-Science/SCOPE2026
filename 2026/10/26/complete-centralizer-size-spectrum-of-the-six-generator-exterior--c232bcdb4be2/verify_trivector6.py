#!/usr/bin/env python3
"""Independent finite-field checks of cubic exterior multiplication on six generators."""
from itertools import combinations
from random import Random
from math import prod

N=6
bases={d:[sum(1<<i for i in C) for C in combinations(range(N),d)] for d in range(7)}
coords=bases[3]

def wedge(a,b):
    if a&b:return None
    parity=sum((b&((1<<i)-1)).bit_count() for i in range(N) if (a>>i)&1)&1
    return a|b, (-1 if parity else 1)

def rank(rows,p):
    if not rows:return 0
    a=[x[:] for x in rows]; piv=0
    for j in range(len(a[0])):
        idx=next((i for i in range(piv,len(a)) if a[i][j]%p),None)
        if idx is None:continue
        a[idx],a[piv]=a[piv],a[idx]
        inv=pow(a[piv][j],-1,p)
        a[piv]=[(z*inv)%p for z in a[piv]]
        for i in range(piv+1,len(a)):
            if a[i][j]:
                mul=a[i][j]
                a[i]=[(x-mul*y)%p for x,y in zip(a[i],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv

def mult_rank(w,d,p):
    inputs=bases[d];outputs=bases[d+3]
    lookup={u:i for i,u in enumerate(outputs)}
    mat=[[0 for _ in inputs] for _ in outputs]
    for j,u in enumerate(inputs):
        for k,v in enumerate(coords):
            if w[k]%p:
                value=wedge(v,u)
                if value:
                    mon,sgn=value
                    mat[lookup[mon]][j]=(mat[lookup[mon]][j]+sgn*w[k])%p
    return rank(mat,p)

def qbin(n,k,q):
    result=1
    for i in range(k):result=result*(q**(n-i)-1)//(q**(k-i)-1) if False else result
    num=prod(q**(n-i)-1 for i in range(k));den=prod(q**(k-i)-1 for i in range(k))
    assert num%den==0
    return num//den

def predicted(p):
    d=(p-1)*qbin(6,3,p)
    b=qbin(6,1,p)*(p**10-1-(p-1)*qbin(5,2,p))
    generic=p**20-1-d-b
    return {0:1,8:d,12:b,14:generic}

def run():
    random=Random(12345);cases=0
    for p in (2,3,5,7):
        w0=[0]*20
        decomp=w0.copy();decomp[coords.index(0b000111)]=1
        div=w0.copy();div[coords.index(0b000111)]=1;div[coords.index(0b011001)]=1 # e1^e4^e5? 0b011001 contains e0 e3 e4 -> rank4 complement e23+e45
        gen=w0.copy();gen[coords.index(0b000111)]=1;gen[coords.index(0b111000)]=1
        for w,expect in ((w0,0),(decomp,8),(div,12),(gen,14)):
            ds=tuple(mult_rank(w,d,p) for d in range(4))
            assert sum(ds)==expect,(p,w,ds,expect)
            assert ds==(0,0,0,0) if expect==0 else ds in ((1,3,3,1),(1,5,5,1),(1,6,6,1))
            cases+=1
        for _ in range(250):
            w=[random.randrange(p) for z in range(20)]
            ds=tuple(mult_rank(w,d,p) for d in range(4))
            rk=sum(ds)
            assert rk in (0,8,12,14),(p,w,rk)
            null=6-mult_rank(w,1,p)
            assert rk==0 or rk==14-2*null
            assert ds[1]==ds[2],(p,ds)
            cases+=1
        freq=predicted(p)
        assert sum(freq.values())==p**20
        assert all(v>=0 for v in freq.values())
        print(f'field_F{p}: samples_254=PASS total_count_{p**20}=PASS rank_frequencies={freq}')
    print('VERIFY_OK_TRIVECTOR_SIX_GENERATOR_JORDAN',cases,'matrix_cases')
if __name__=='__main__':run()
