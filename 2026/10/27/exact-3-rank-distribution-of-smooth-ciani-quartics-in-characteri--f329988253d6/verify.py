#!/usr/bin/env python3
"""Exact tests for Ciani-quartic p-rank counts in characteristic three.

Works over F_3 and F_9 without external packages. This verification is
supplementary to the symbolic all-q proof, not a substitute for that proof.
"""
from itertools import product
from collections import Counter


def add(a,b,q):
    if q == 3:
        return (a+b)%3
    return ((a%3+b%3)%3)+3*((a//3+b//3)%3)


def neg(a,q):
    return add(0, (3-a)%3 if q==3 else ((3-a%3)%3)+3*((3-a//3)%3), q)


def mul(a,b,q):
    if q==3:
        return (a*b)%3
    a0,a1=a%3,a//3
    b0,b1=b%3,b//3
    # F_9=F_3[u]/(u^2+1)
    return ((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)


def sq(a,q):return mul(a,a,q)

def fm(q):
    z=Counter()
    for b,c in product(range(1,q),repeat=2):
        bc=mul(b,c,q)
        for d,e,f in product(range(q),repeat=3):
            d2,e2,f2=sq(d,q),sq(e,q),sq(f,q)
            if d2==b or e2==c or f2==bc: continue
            # det M for [[a,-d,-e],[-d,b,-f],[-e,-f,c]] with a=1
            # delta=(b-d^2)(c-e^2)-(f+de)^2
            t=add(f,mul(d,e,q),q)
            T=mul(add(b,neg(d2,q),q),add(c,neg(e2,q),q),q)
            if sq(t,q)==T: continue
            hx=t
            hy=add(mul(b,e,q),mul(d,f,q),q)
            hz=add(mul(c,d,q),mul(e,f,q),q)
            rank=sum(h!=0 for h in (hx,hy,hz))
            z[rank]+=1
    return tuple(z[i] for i in range(4))


def predicted(q):
    s=(q-1)**2
    return (s,3*s*(q-2),3*s*(q-2)*(q-3),s*(q**3-7*q**2+18*q-18))


def check_matrix_coefficients():
    # Produce F^2 as a polynomial of six formal coefficient labels;
    # all monomials of F have even exponents, so every off-diagonal
    # Hasse-Witt entry (which needs an odd exponent) vanishes.
    mons=[((4,0,0),'A'),((0,4,0),'B'),((0,0,4),'C'),
          ((2,2,0),'D'),((2,0,2),'E'),((0,2,2),'F')]
    exp_targets=[(4,2,2),(2,4,2),(2,2,4)]
    coeff=[]
    for v in exp_targets:
        pairs=Counter()
        for t1,c1 in mons:
            for t2,c2 in mons:
                if all(t1[i]+t2[i]==v[i] for i in range(3)):
                    pairs[''.join(sorted((c1,c2)))]+=1
        coeff.append(dict(pairs))
    assert coeff==[{'AF':2,'DE':2},{'BE':2,'DF':2},{'CD':2,'EF':2}],coeff
    # Off diagonal Frobenius basis transitions require odd exponents;
    # this assertion checks the parity argument independent of q.
    source=[(2,1,1),(1,2,1),(1,1,2)]
    for i in range(3):
        for j in range(3):
            if i!=j:
                ex=[3*source[i][k]-source[j][k] for k in range(3)]
                assert any(e%2 for e in ex)
    return coeff


if __name__=='__main__':
    print('Hasse-Witt coefficient pairs:',check_matrix_coefficients())
    for q in (3,9):
        out=fm(q)
        ref=predicted(q)
        print('q',q,'computed',out,'predicted',ref,'total',sum(out))
        assert out==ref,(q,out,ref)
        assert sum(out)==(q-1)**2*(q**3-4*q**2+6*q-5)
    for q in (3,9,27,81):
        assert sum(predicted(q))==(q-1)**2*(q**3-4*q**2+6*q-5)
    print('VERIFY_OK')
