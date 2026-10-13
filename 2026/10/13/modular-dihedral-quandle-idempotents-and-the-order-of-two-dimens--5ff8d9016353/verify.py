"""Finite checks for modular dihedral-quandle idempotents.

The checker uses the basis of quandle elements for multiplication and
truncated-polynomial arithmetic for constructing predicted idempotents.
"""
from itertools import product
from math import comb
import random


def multiply(a, b, p):
    out = [0] * p
    for i, ai in enumerate(a):
        if ai % p:
            for j, bj in enumerate(b):
                if bj % p:
                    k = (2*j-i) % p
                    out[k] = (out[k] + ai*bj) % p
    return out


def trunc_mul(a, b, p):
    v=[0]*p
    for i, ai in enumerate(a):
        for j,bj in enumerate(b[:p-i]):
            v[i+j]=(v[i+j]+ai*bj)%p
    return v


def logarithm_x(p):
    y = [0,1]+[0]*(p-2)
    acc=[0]*p
    power=[1]+[0]*(p-1)
    for k in range(1,p):
        power=trunc_mul(power,y,p)
        factor=pow(k,-1,p)* (1 if k&1 else -1)
        acc=[(v+factor*w)%p for v,w in zip(acc,power)]
    return acc


def exponential(h,p):
    res=[1]+[0]*(p-1)
    term=[1]+[0]*(p-1)
    for k in range(1,p):
        term=trunc_mul(term,h,p)
        term=[(x*pow(k,-1,p))%p for x in term]
        res=[(x+y)%p for x,y in zip(res,term)]
    return res


def to_quandle_coordinates(poly_y,p):
    out=[0]*p
    for j, coef in enumerate(poly_y):
        for i in range(j+1):
            out[i]=(out[i]+coef*comb(j,i)*(-1)**(j-i))%p
    return out


def degrees(p):
    return [j for j in range(1,p) if (1-(-1)**j-pow(2,j,p))%p==0]


def predicted_idempotent(p,coeff):
    t=logarithm_x(p)
    h=[0]*p
    power=[1]+[0]*(p-1)
    coefficients=dict(zip(degrees(p),coeff))
    for j in range(1,p):
        power=trunc_mul(power,t,p)
        cj=coefficients.get(j,0)
        if cj:
            h=[(x+cj*y)%p for x,y in zip(h,power)]
    return to_quandle_coordinates(exponential(h,p),p)


def main():
    for p in (3,5):
        total=0; candidates={tuple([0]*p)}
        for coeff in product(range(p),repeat=len(degrees(p))):
            a=tuple(predicted_idempotent(p,coeff))
            assert multiply(a,a,p)==list(a),(p,coeff,'construct')
            candidates.add(a)
        for a in product(range(p), repeat=p):
            if multiply(a,a,p)==list(a):
                total+=1
                assert a in candidates,(p,a,'missing')
        assert total==len(candidates)==1+p**len(degrees(p))
        print('EXHAUSTIVE',p,'count',total,'degrees',degrees(p))
    for p in (7,11,17,31):
        m=len(degrees(p)); r=random.Random(p)
        for trial in range(60):
            coeff=[r.randrange(p) for _ in range(m)]
            a=predicted_idempotent(p,coeff)
            assert multiply(a,a,p)==a,(p,coeff)
        for trial in range(60):
            a=[r.randrange(p) for _ in range(p)]
            is_fixed=multiply(a,a,p)==a
            if is_fixed:
                assert tuple(a)==tuple([0]*p) or sum(a)%p==1
        print('SAMPLED',p,'degrees',degrees(p),'predicted_count',1+p**m)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
