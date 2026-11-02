#!/usr/bin/env python3
"""Exact checks for a weighted edge-TV contractivity characterization of K_{2,q}."""
from fractions import Fraction as F
from itertools import product
from random import Random


def normalized_generator_apply(data, q):
    u,v,*ys=data
    mean_right=sum(ys, F(0))/q
    mean_left=(u+v)/F(2)
    return (mean_right-u, mean_right-v, *(mean_left-y for y in ys))


def direct_cut_derivative(a,b, bits):
    q=len(a); data=tuple(F(t) for t in bits)
    dz=normalized_generator_apply(data,q)
    ans=F(0)
    for i,row in enumerate((a,b)):
        for j,w in enumerate(row):
            diff=data[i]-data[2+j]
            d_diff=dz[i]-dz[2+j]
            if diff: ans+=w * (d_diff if diff>0 else -d_diff)
            else: ans+=w*abs(d_diff)
    return ans


def sorted_certificate(a,b):
    q=len(a); W=sum(a)+sum(b); A=sum(a);B=sum(b)
    if not all((q+2)*(a[j]+b[j])>=W for j in range(q)):
        return False
    for s in range(q+1):
        d=F(1,2)-F(s,q)
        tau=sorted(((1+d+abs(d))*a[j]-(1-d+abs(d))*b[j]
                        for j in range(q)),reverse=True)
        if sum(tau[:s],F(0))>(1+d)*A-abs(d)*B:
            return False
    return True


def exhaustive_cut_certificate(a,b):
    q=len(a)
    return all(direct_cut_derivative(a,b,bits)<=0
               for bits in product((0,1), repeat=q+2))


def euler_step(data,q,step):
    dz=normalized_generator_apply(data,q)
    return tuple(x+step*y for x,y in zip(data,dz))


def tv(a,b,data):
    return sum((w*abs(data[i]-data[j+2])
            for i,row in enumerate((a,b))
            for j,w in enumerate(row)),F(0))


def run():
    random=Random(20261025); tests=0; cuts=0; euler=0
    for q in range(1,8):
        for sample in range(48 if q<=5 else 18):
            a=tuple(F(random.randrange(1,14)) for _ in range(q))
            b=tuple(F(random.randrange(1,14)) for _ in range(q))
            chk=sorted_certificate(a,b)
            brute=exhaustive_cut_certificate(a,b)
            assert chk==brute, (q,a,b,chk,brute)
            tests+=1; cuts+=2**(q+2)
            if chk:
                for t in range(8):
                    data=tuple(F(random.randrange(-7,8)) for _ in range(q+2))
                    J=tv(a,b,data)
                    for k in range(12):
                        data=euler_step(data,q,F(1,8))
                        assert tv(a,b,data)<=J
                        euler+=1
    a=(F(4),F(1),F(1)); b=(F(1),F(8),F(8))
    W=sum(a)+sum(b)
    assert W==23 and [a[j]+b[j] for j in range(3)]==[5,9,9]
    assert 3*sum(a)>=sum(b) and 3*sum(b)>=sum(a)
    assert all(5*(a[j]+b[j])>=W for j in range(3))
    bits=(1,0,1,0,0)
    assert tv(a,b,bits)==3
    assert direct_cut_derivative(a,b,bits)==F(1,6)
    assert not sorted_certificate(a,b)
    assert tv(a,b,euler_step(bits,3,F(1,16)))==F(3)+F(1,96)
    # q=1,2: all nontrivial cuts are singleton or balanced cuts with
    # zero derivative (up to complement), hence vertex tests suffice.
    print('PASS: certificate/exhaustive agreement:',tests,'weight profiles;',cuts,'binary cuts.')
    print('PASS: exact rational contractive Euler checks:',euler)
    print('PASS: 5-vertex witness: TV=3; positive derivative=1/6; one Euler step grows by 1/96.')

if __name__=='__main__': run()
