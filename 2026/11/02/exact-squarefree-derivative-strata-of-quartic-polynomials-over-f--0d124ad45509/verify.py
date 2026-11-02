#!/usr/bin/env python3
"""Exact enumeration of quartics with squarefree derivative over small finite fields.

Uses polynomial-basis finite fields and Euclidean polynomial gcds. The formulas
being tested are independent of the enumeration method.
"""
from itertools import product

# Each monic modulus is irreducible in its stated prime field; coefficients low first.
FIELDS = {
    2: (2, (0, 1)),      # degree one, field F_2
    3: (3, (0, 1)),
    4: (2, (1, 1, 1)),    # t^2+t+1
    5: (5, (0, 1)),
    7: (7, (0, 1)),
    8: (2, (1, 1, 0, 1)), # t^3+t+1
    9: (3, (1, 0, 1)),    # t^2+1
    11: (11, (0, 1)),
    16: (2, (1, 1, 0, 0, 1)), # t^4+t+1
}

class Field:
    def __init__(self, q, p, modulus):
        self.q, self.p, self.modulus = q, p, modulus
        self.degree = len(modulus) - 1
        assert p ** self.degree == q and modulus[-1] == 1
        self.digits = []
        for v in range(q):
            ds=[]
            for _ in range(self.degree):
                ds.append(v % p);v //= p
            self.digits.append(tuple(ds))
        self.add_table=[[0]*q for _ in range(q)]
        self.mul_table=[[0]*q for _ in range(q)]
        weights=[p**i for i in range(self.degree)]
        for a in range(q):
            for b in range(q):
                da=self.digits[a]; db=self.digits[b]
                self.add_table[a][b]=sum(((da[i]+db[i])%p)*weights[i] for i in range(self.degree))
                prod=[0]*(2*self.degree-1)
                for i,ai in enumerate(da):
                    for j,bj in enumerate(db): prod[i+j]=(prod[i+j]+ai*bj)%p
                for k in range(len(prod)-1,self.degree-1,-1):
                    c=prod[k]
                    if c:
                        for j in range(self.degree):
                            prod[k-self.degree+j]=(prod[k-self.degree+j]-c*modulus[j])%p
                self.mul_table[a][b]=sum(prod[i]*weights[i] for i in range(self.degree))
        self.neg=[next(i for i in range(q) if self.add_table[i][a]==0) for a in range(q)]
        self.inv=[None]+[next(i for i in range(1,q) if self.mul_table[a][i]==1) for a in range(1,q)]
    def add(self,a,b):return self.add_table[a][b]
    def sub(self,a,b):return self.add_table[a][self.neg[b]]
    def mul(self,a,b):return self.mul_table[a][b]
    def trim(self,poly):
        poly=list(poly)
        while poly and poly[-1]==0:poly.pop()
        return poly
    def rem(self,a,b):
        a=self.trim(a); b=self.trim(b)
        assert b
        inv=self.inv[b[-1]]
        while len(a)>=len(b):
            fac=self.mul(a[-1],inv);pos=len(a)-len(b)
            for i,coef in enumerate(b):
                a[pos+i]=self.sub(a[pos+i],self.mul(fac,coef))
            a=self.trim(a)
        return a
    def gcd(self,a,b):
        a=self.trim(a);b=self.trim(b)
        while b:a,b=b,self.rem(a,b)
        return a
    def derivative(self,poly):
        out=[]
        for i in range(1,len(poly)):
            scale=i%self.p
            out.append(self.mul(poly[i],scale))
        return self.trim(out)
    def is_squarefree(self,poly):
        p=self.trim(poly)
        return bool(p) and len(self.gcd(p,self.derivative(p)))==1

def expected(q,p):
    if p==2:return (q*q*(q-1),0,0)
    if p==3:return (q*q*(q-1)**2,q*(q-1)**2,q*(q-1))
    return (q*(q-1)*(q*q-q+1),q*(q-1)*(q-2),q*(q-1))

def verify():
    trials=0
    for q,(p,modulus) in FIELDS.items():
        fld=Field(q,p,modulus)
        counts=[0,0,0]
        tested=0
        for a,b,c,d in product(range(q),repeat=4):
            f=[d,c,b,a,1]
            df=fld.derivative(f)
            if fld.is_squarefree(df):
                g=fld.gcd(f,df)
                degree=len(g)-1
                assert degree in (0,1,2), (q,a,b,c,d,degree)
                counts[degree]+=1
            tested+=1
        assert tuple(counts)==expected(q,p), (q,counts,expected(q,p))
        print('PASS q=%d p=%d degree_counts=%r quartics=%d'%(q,p,tuple(counts),tested))
        trials+=tested
    print('VERIFY_OK fields=%d quartics=%d'%(len(FIELDS),trials))

if __name__=='__main__':verify()
