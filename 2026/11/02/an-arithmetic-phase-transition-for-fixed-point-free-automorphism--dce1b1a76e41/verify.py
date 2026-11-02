#!/usr/bin/env python3
"""Standalone exhaustive finite-field checks for fixed-point-free automorphisms.

Constructs the original Lie bracket, all automorphism parameters in selected
small configurations, and independent matrix ranks over finite fields.
"""
from itertools import product
from math import gcd

class Field:
    def __init__(self, q):
        self.q=q
        self.polynomial={4:0b111,8:0b1011}.get(q)
        if self.polynomial is None and q not in (2,3,5,7,11):
            raise ValueError('unsupported field')
        self.bits={4:2,8:3}.get(q)
    def add(self,a,b):
        return (a^b) if self.bits else ((a+b)%self.q)
    def neg(self,a):
        return a if self.bits else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if not self.bits:
            return (a*b)%self.q
        value=0
        for i in range(self.bits):
            if (b>>i)&1:
                value ^= a<<i
        for i in range(2*self.bits-2,self.bits-1,-1):
            if (value>>i)&1:
                value ^= self.polynomial <<(i-self.bits)
        return value
    def inv(self,a):
        if not a:raise ZeroDivisionError
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise AssertionError('not field')
    def pow(self,a,k):
        out=1
        for _ in range(k):out=self.mul(out,a)
        return out

def bracket(x,y,F):
    n=len(x); out=[0]*n
    for j in range(1,n-1):
        out[j+1]=F.sub(F.mul(x[0],y[j]),F.mul(y[0],x[j]))
    return out

def images_from_generators(a,d,b_tail,c_tail,F,n):
    e1=[a]+list(b_tail)
    e2=[0,d]+list(c_tail)
    out=[e1,e2]
    for _ in range(2,n):
        out.append(bracket(e1,out[-1],F))
    return out

def rank_cols(cols,F,shift_identity=False):
    n=len(cols)
    m=[[F.sub(cols[j][i],1 if shift_identity and i==j else 0)
        for j in range(n)] for i in range(n)]
    rr=0
    for j in range(n):
        ix=next((i for i in range(rr,n) if m[i][j]),None)
        if ix is None:continue
        m[rr],m[ix]=m[ix],m[rr]
        fac=F.inv(m[rr][j]);m[rr]=[F.mul(fac,x) for x in m[rr]]
        for i in range(n):
            if i==rr or not m[i][j]:continue
            coeff=m[i][j]
            m[i]=[F.sub(x,F.mul(coeff,y)) for x,y in zip(m[i],m[rr])]
        rr+=1
        if rr==n:break
    return rr

def predicted_fpf(n,F):
    q=F.q; ans=0
    for a in range(1,q):
        for d in range(1,q):
            vals=[a,d]
            for j in range(1,n-1):
                vals.append(F.mul(d,F.pow(a,j)))
            ans += (1 if 1 not in vals else 0)
    return ans * q**(2*n-3)

def divisor_formula(n,q):
    order=q-1
    ans=0
    for t in range(2,order+1):
        if order%t==0:
            tot=sum(gcd(i,t)==1 for i in range(1,t+1))
            ans+=tot*(order-min(t,n-1))
    return q**(2*n-3)*ans

def check(n,q):
    F=Field(q)
    assert predicted_fpf(n,F)==divisor_formula(n,q)
    seen=0; fpf=0
    for a in range(1,q):
        for d in range(1,q):
            for tail in product(range(q),repeat=2*n-3):
                cols=images_from_generators(a,d,tail[:n-1],tail[n-1:],F,n)
                assert rank_cols(cols,F)==n
                # Check every defining and zero bracket independently from the original law.
                for i in range(n):
                    for j in range(i+1,n):
                        input_i=[int(z==i) for z in range(n)]
                        input_j=[int(z==j) for z in range(n)]
                        lhs=bracket(cols[i],cols[j],F)
                        orig=bracket(input_i,input_j,F)
                        rhs=[0]*n
                        for h,coef in enumerate(orig):
                            for r in range(n):
                                rhs[r]=F.add(rhs[r],F.mul(coef,cols[h][r]))
                        assert lhs==rhs,(n,q,a,d,tail,i,j)
                fpf+=(rank_cols(cols,F,True)==n)
                seen+=1
    expected=divisor_formula(n,q)
    assert fpf==expected,(n,q,seen,fpf,expected)
    return f'n={n} q={q} tested={seen} fixed_point_free={fpf}'

def sampled_check(n,q):
    F=Field(q)
    assert predicted_fpf(n,F)==divisor_formula(n,q)
    for a in range(1,q):
        for d in range(1,q):
            for trial in range(4):
                tail=[(trial+2*j+a*d)%q for j in range(2*n-3)]
                cols=images_from_generators(a,d,tail[:n-1],tail[n-1:],F,n)
                assert rank_cols(cols,F)==n
                eig=[a,d]+[F.mul(d,F.pow(a,j)) for j in range(1,n-1)]
                assert (rank_cols(cols,F,True)==n)==(1 not in eig)
    return f'n={n} q={q} sampled_pairs={(q-1)**2} expected_total={divisor_formula(n,q)}'

if __name__=='__main__':
    results=[]
    for n,q in [(4,2),(5,2),(4,3),(4,4),(4,5)]:
        results.append(check(n,q))
    for n,q in [(5,3),(6,4),(5,5),(8,7),(8,8),(5,8),(12,7),(8,11)]:
        results.append(sampled_check(n,q))
    for item in results:print(item)
    print(f'FILIFORM_FIXED_POINT_FREE_COUNTS_OK {len(results)}_CONFIGURATIONS')
