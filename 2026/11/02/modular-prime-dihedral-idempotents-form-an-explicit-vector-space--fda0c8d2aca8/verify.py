#!/usr/bin/env python3
"""Coefficient-level checks for modular dihedral-quandle idempotents.
Run: python3 verify.py  (requires numpy for exhaustive base-field tests).
"""
import itertools
import math
import numpy as np


def star(a, b, p):
    """Direct coefficient definition: e_i * e_j = e_(2j-i)."""
    out = [0] * p
    for i in range(p):
        for j in range(p):
            out[(2*j-i) % p] = (out[(2*j-i) % p] + a[i]*b[j]) % p
    return tuple(out)


def conv(a,b,p):
    out = [0]*p
    for i in range(p):
        for j in range(p):
            out[(i+j)%p] = (out[(i+j)%p]+a[i]*b[j])%p
    return out


def ord2(p):
    k=1
    v=2%p
    while v != 1:
        k+=1
        v=v*2%p
    return k


def w_basis(p):
    # Orbit generators for solutions of iota(w)=-w and sigma(w)=2w.
    h=ord2(p)
    unseen=set(range(1,p))
    basis=[]
    while unseen:
        seed=min(unseen)
        orbit={seed*pow(2,j,p)%p for j in range(h)}
        signs={(-x)%p for x in orbit}
        unseen.difference_update(orbit|signs)
        a=[0]*p
        for j in range(h):
            x=seed*pow(2,j,p)%p
            coef=pow(2,-j,p)
            a[x]=coef
            a[-x%p]=(-coef)%p
        assert all(a[-i%p]==(-a[i])%p for i in range(p))
        assert all(a[(i*2)%p]==a[i]*pow(2,-1,p)%p for i in range(p))
        basis.append(tuple(a))
    assert len(basis)==(p-1)//math.lcm(2,h)
    return basis


def exp_group(w,p):
    one=[1]+[0]*(p-1)
    out=one[:]
    power=one[:]
    invfac=1
    for k in range(1,p):
        power=conv(power,w,p)
        invfac=invfac*pow(k,-1,p)%p
        for i in range(p):
            out[i]=(out[i]+invfac*power[i])%p
    return tuple(out)


def linear_family(p):
    basis=w_basis(p)
    E={}
    for params in itertools.product(range(p),repeat=len(basis)):
        v=tuple(sum(a*b[i] for a,b in zip(params,basis))%p for i in range(p))
        f=exp_group(v,p)
        assert f not in E
        assert sum(f)%p==1
        assert star(f,f,p)==f
        E[f]=params
    return E


def exhaustive_prime(p):
    N=p**p
    hits=set()
    B=16000
    for start in range(0,N,B):
        z=np.arange(start,min(N,start+B),dtype=np.int64)
        A=np.stack([(z//p**i)%p for i in range(p)],axis=1)
        good=np.ones(len(A),dtype=bool)
        for k in range(p):
            terms=np.array([(2*j-k)%p for j in range(p)],dtype=np.int64)
            val=np.sum(A[:,terms]*A,axis=1)%p
            good &= (val==A[:,k])
        for row in A[good]:
            hits.add(tuple(int(x) for x in row))
    E=set(linear_family(p))
    assert hits==E|{(0,)*p},(p,len(hits),len(E))
    # Direct multiplication closure / right-translation permutations.
    for f in E:
        right={star(g,f,p) for g in E}
        assert right==E
        for g in E:
            assert star(g,f,p) in E
    print(f'EXHAUSTIVE F_{p}[R_{p}]: {N} elements, {len(hits)} idempotents, core size {len(E)}')


def exhaustive_f9_r3():
    # GF(9) = F_3[u]/(u*u+1); encode a+b*u by a+3*b.
    add=lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3)
    mul=lambda x,y: ((x%3)*(y%3)+2*(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
    ans=set()
    for z in itertools.product(range(9),repeat=3):
        out=[0,0,0]
        for i in range(3):
            for j in range(3):
                k=(2*j-i)%3
                out[k]=add(out[k],mul(z[i],z[j]))
        if tuple(out)==z:
            ans.add(z)
    assert len(ans)==10,len(ans)
    assert (0,0,0) in ans
    nonzero=ans-{(0,0,0)}
    for f in nonzero:
        image=[]
        for g in nonzero:
            out=[0,0,0]
            for i in range(3):
                for j in range(3):
                    k=(2*j-i)%3
                    out[k]=add(out[k],mul(g[i],f[j]))
            image.append(tuple(out))
        assert set(image)==nonzero
    print('EXHAUSTIVE F_9[R_3]: 729 elements, 10 idempotents, core size 9')


def larger_prime_checks():
    for p in [11,13,17,19,23,31,41,73,1093]:
        h=ord2(p)
        d=(p-1)//math.lcm(2,h)
        # For large p omit costly full basis, but verify arithmetic and orbit structure.
        seen=set()
        for i in range(1,p):
            if i not in seen:
                orb={i*pow(2,j,p)%p for j in range(h)}
                seen.update(orb | {(-x)%p for x in orb})
        assert len(seen)==p-1
        if p<=23:
            assert len(w_basis(p))==d
            E=linear_family(p) if d<=2 else {}
            for f in E:
                assert star(f,f,p)==f
            ee=list(E)
            for a in ee[:12]:
                for b in ee[:12]:
                    assert star(a,b,p) in E
        print(f'ORBIT p={p}: ord_p(2)={h}, dim={d}')

if __name__=='__main__':
    for prime in [3,5,7]:
        exhaustive_prime(prime)
    exhaustive_f9_r3()
    larger_prime_checks()
    print('VERIFY_OK: 3 exhaustive prime-field quandle algebras, GF(9) extension, 9 orbit dimensions')
