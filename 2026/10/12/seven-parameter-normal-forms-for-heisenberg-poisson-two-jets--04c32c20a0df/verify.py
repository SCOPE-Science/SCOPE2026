#!/usr/bin/env python3
"""Finite-dimensional verification of Poisson brackets on a cube-zero local algebra.
This script independently constructs the Jacobi and coordinate-change matrices
from truncated polynomial arithmetic. Requires Python 3 standard library only.
"""
from itertools import product
from random import Random

MON1 = [(1,0,0),(0,1,0),(0,0,1)]
MON2 = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
PAIRS = [(0,1),(0,2),(1,2)]


def add(a,b,p):
    z=dict(a)
    for k,v in b.items():
        z[k]=(z.get(k,0)+v)%p
        if z[k]==0: del z[k]
    return z


def scale(a,s,p):
    return {k:(v*s)%p for k,v in a.items() if (v*s)%p}


def prod(a,b,p):
    c={}
    for m,x in a.items():
        for n,y in b.items():
            k=tuple(i+j for i,j in zip(m,n))
            if sum(k)<3:
                c[k]=(c.get(k,0)+x*y)%p
    return {m:v for m,v in c.items() if v}


def unit(i):
    return {MON1[i]:1}


def bracket(a,b,gens,p):
    # Extend bracket on generators as alternating biderivation, allowing
    # arbitrary monomials of degree at most two in the algebra.
    out={}
    for am,ac in a.items():
        for bm,bc in b.items():
            for i in range(3):
                for j in range(3):
                    if i==j or am[i]==0 or bm[j]==0:continue
                    # derivation on two commutative monomials
                    e=[am[k]+bm[k] for k in range(3)]
                    e[i]-=1; e[j]-=1
                    d={tuple(e):am[i]*bm[j]*ac*bc % p}
                    if i<j: v=gens[PAIRS.index((i,j))]
                    else: v=scale(gens[PAIRS.index((j,i))],-1,p)
                    out=add(out,prod(d,v,p),p)
    return out


def gen_brackets(v,p):
    gens=[]
    for pair in range(3):
        z={}
        if pair==0:z[MON1[2]]=1
        for j,m in enumerate(MON2):
            u=v[pair*6+j]%p
            if u: z[m]=u
        gens.append(z)
    return gens


def jacobi(v,p):
    gens=gen_brackets(v,p)
    x,y,z=map(unit,range(3))
    q={}
    for a,b,c in [(x,y,z),(y,z,x),(z,x,y)]:
        q=add(q,bracket(a,bracket(b,c,gens,p),gens,p),p)
    return tuple(q.get(m,0)%p for m in MON2)


def substitution_gauge(h,p):
    # Differential of pullback of Poisson structure by x_i -> x_i+H_i.
    l=[unit(i) for i in range(3)]
    H=[{m:h[6*i+j]%p for j,m in enumerate(MON2) if h[6*i+j]%p}
       for i in range(3)]
    g0=gen_brackets([0]*18,p)
    res=[]
    for i,j in PAIRS:
        a=add(l[i],H[i],p); b=add(l[j],H[j],p)
        raw=bracket(a,b,g0,p)
        # change of coordinate back: linear z in {x,y} gives -H_z
        if (i,j)==(0,1):raw=add(raw,scale(H[2],-1,p),p)
        res.extend(raw.get(m,0) for m in MON2)
    return tuple(res)


def rank(matrix,p):
    a=[list(map(lambda v:v%p,r)) for r in matrix]
    j=0
    for k in range(len(a[0])):
        pivot=next((r for r in range(j,len(a)) if a[r][k]),None)
        if pivot is None:continue
        a[j],a[pivot]=a[pivot],a[j]
        t=pow(a[j][k],-1,p)
        a[j]=[x*t%p for x in a[j]]
        for r in range(len(a)):
            if r==j:continue
            u=a[r][k]
            if u:a[r]=[(x-u*y)%p for x,y in zip(a[r],a[j])]
        j+=1
        if j==len(a):break
    return j


def columns_to_rows(cols):
    return [list(row) for row in zip(*cols)]


def expected_normal(f,p):
    # f is 7 parameters a,b,c,d,e,f,g
    a,b,c,d,e,ff,g=f
    A=[0]*6
    B=[a,-2*g,b,c,d,0]
    C=[e,-2*a,ff,g,-b,0]
    return tuple(x%p for x in A+B+C)


def main():
    rng=Random(123456)
    for p in (2,3,5,7,11):
        jacmat=columns_to_rows([jacobi([int(i==k) for i in range(18)],p) for k in range(18)])
        gaugemat=columns_to_rows([substitution_gauge([int(i==k) for i in range(18)],p) for k in range(18)])
        rj=rank(jacmat,p);rg=rank(gaugemat,p)
        assert (rj,rg)==(3,8),(p,rj,rg)
        for c in zip(*gaugemat):assert all(sum(row[i]*c[i] for i in range(18))%p==0 for row in jacmat)
        for _ in range(500):
            f=[rng.randrange(p) for i in range(7)]
            assert jacobi(expected_normal(f,p),p)==(0,)*6
            h=[rng.randrange(p) for i in range(18)]
            vg=substitution_gauge(h,p)
            assert jacobi(vg,p)==(0,)*6
            # Gauge changes preserve Jacobi in the coset of every normal form.
            assert jacobi(tuple((u+v)%p for u,v in zip(expected_normal(f,p),vg)),p)==(0,)*6
        print('field',p,'Jacobi rank',rj,'gauge rank',rg,'framed dimension',18-rj,'moduli dimension',18-rj-rg)
    # Exhaustive 2^18 enumeration of the full coefficient space, using independently constructed Jacobi columns.
    jcols=[jacobi([int(i==k) for i in range(18)],2) for k in range(18)]
    count=0
    for v in range(1<<18):
        js=[0]*6
        a=v
        while a:
            bit=(a & -a).bit_length()-1
            a &= a-1
            for i in range(6):js[i]^=jcols[bit][i]
        if not any(js):count+=1
    assert count==2**15,count
    # All normal-form classes over F2 are distinct mod gauge: their 7 columns
    # are linearly independent modulo the 8-dimensional gauge image.
    gg=columns_to_rows([substitution_gauge([int(i==k) for i in range(18)],2) for k in range(18)])
    norms=[expected_normal([int(i==k) for i in range(7)],2) for k in range(7)]
    assert rank([row+list(nrow) for row,nrow in zip(gg,columns_to_rows(norms))],2)==15
    print('F2 exhaustive cocycles',count,'gauge orbits',2**7,'uniform orbit size',2**8)
    print('VERIFY_OK')


if __name__=='__main__':main()
