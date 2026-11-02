#!/usr/bin/env python3
"""Independent finite-field point count checks for a singular hyperelliptic family.
Uses pure-Python polynomial-basis finite fields, without third-party libraries.
Finite tests supplement, but do not prove, the general geometric argument.
"""
from itertools import product

MODULI = {1:[0,1],2:[2,1,1],3:[2,0,1,1],4:[2,0,0,1]}

class GF:
    def __init__(self,m):
        self.m=m; self.q=3**m; self.mod=MODULI[m]
        self.coef=[self.unpack(z) for z in range(self.q)]
        self.table=[[self.pack([(a+b)%3 for a,b in zip(self.coef[i],self.coef[j])]) for j in range(self.q)] for i in range(self.q)]
        self.mul_table=[[self.mul_raw(i,j) for j in range(self.q)] for i in range(self.q)]
        self.squares={self.mul(a,a) for a in range(self.q)}
        self.one=1
    def unpack(self,z):
        return [z//3**i%3 for i in range(self.m)]
    def pack(self,c):return sum((t%3)*3**i for i,t in enumerate(c))
    def add(self,x,y):return self.table[x][y]
    def sub(self,x,y):return self.add(x,self.neg(y))
    def neg(self,x):return self.pack([-z for z in self.coef[x]])
    def mul_raw(self,x,y):
        n=self.m; a=self.coef[x];b=self.coef[y];v=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):v[i+j]=(v[i+j]+a[i]*b[j])%3
        for k in range(2*n-2,n-1,-1):
            u=v[k]
            for j in range(n):v[k-n+j]=(v[k-n+j]-u*self.mod[j])%3
        return self.pack(v[:n])
    def mul(self,x,y):return self.mul_table[x][y]
    def power(self,a,n):
        o=1
        while n:
            if n&1:o=self.mul(o,a)
            a=self.mul(a,a);n>>=1
        return o
    def chi(self,x):return 0 if x==0 else (1 if x in self.squares else -1)

def check_field(m,limit=None):
    k=GF(m);q=k.q;totals={'elliptic_ordinary':0,'elliptic_supersingular':0,'nodal':0,'cuspidal':0,'reducible':0}
    pairs=product(range(q),repeat=2)
    for index,(a,b) in enumerate(pairs):
        if limit is not None and index>=limit:break
        c=k.power(a,3**(m-1)); d=k.power(b,3**(m-1))
        assert k.power(c,3)==a and k.power(d,3)==b
        critical=k.sub(k.mul(a,a),k.power(a,3))
        x_counts_H=0;x_counts_quartic=0
        for x in range(q):
            x2=k.mul(x,x);x3=k.mul(x2,x)
            h=k.add(k.add(x3,x2),k.add(k.mul(c,x),d))
            f=k.mul(x,k.power(h,3));g=k.mul(x,h)
            x_counts_H+=k.chi(f)
            x_counts_quartic+=k.chi(g)
        assert x_counts_H==x_counts_quartic,(m,a,b)
        num=q+2+x_counts_H
        if b!=0 and b!=critical:
            label='elliptic_supersingular' if a==0 else 'elliptic_ordinary'
        elif a==0 and b==0:
            label='cuspidal';assert num==q+1,(m,a,b,num,q+1)
        elif a==1 and b==0:
            label='reducible';assert num==2*q,(m,a,b,num,2*q)
        else:
            label='nodal';expected=q+1-k.chi(a)
            assert num==expected,(m,a,b,num,expected)
        totals[label]+=1
    if limit is None:
        assert totals == {'elliptic_ordinary':q*q-3*q+3,
                          'elliptic_supersingular':q-1,
                          'nodal':2*(q-2),
                          'cuspidal':1,'reducible':1},(q,totals)
    print('GF(3^%d), q=%d, checked=%d, strata=%s'%(m,q,sum(totals.values()),totals))

if __name__=='__main__':
    for m in (1,2,3):check_field(m)
    check_field(4,limit=500)
    print('CHAR3_C6_FIBER_ZETA_CLASSIFICATION_PASS')
