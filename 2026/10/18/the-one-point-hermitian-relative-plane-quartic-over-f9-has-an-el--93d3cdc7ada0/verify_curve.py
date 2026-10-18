#!/usr/bin/env python3
"""Exact, dependency-free finite-field point counts for a smooth plane quartic."""
from collections import Counter
from itertools import product

P = 3
MODULI = {2: (1,0,1), 4: (1,0,1,1,1), 6: (1,0,0,0,1,1,1)}

def divides(f, g):
    r=list(f)
    while len(r)>=len(g):
        t=r[-1]
        if t:
            start=len(r)-len(g)
            for j,u in enumerate(g):r[start+j]=(r[start+j]-t*u)%P
        while r and r[-1]==0:r.pop()
    return not r

def check_irreducible(f):
    deg=len(f)-1
    for n in range(1,deg//2+1):
        for a in product(range(P),repeat=n):
            if divides(f,(*a,1)):
                return False
    return True

class Field:
    def __init__(self,m):
        self.m=m
        self.mod=MODULI[m]
        assert check_irreducible(self.mod), self.mod
        self.order=P**m
        self.digits=[tuple((a//(P**i))%P for i in range(m)) for a in range(self.order)]
        self.memo={}
    def enc(self,a):return sum((v%P)*(P**i) for i,v in enumerate(a))
    def add(self,a,b):return self.enc([(u+v)%P for u,v in zip(self.digits[a],self.digits[b])])
    def neg(self,a):return self.enc([-u for u in self.digits[a]])
    def mul(self,a,b):
        if a>b:a,b=b,a
        key=(a,b)
        if key in self.memo:return self.memo[key]
        c=[0]*(2*self.m-1)
        for i,u in enumerate(self.digits[a]):
            for j,v in enumerate(self.digits[b]):c[i+j]+=u*v
        for k in range(2*self.m-2,self.m-1,-1):
            t=c[k]%P
            for j in range(self.m):c[k-self.m+j]-=t*self.mod[j]
        value=self.enc(c[:self.m]);self.memo[key]=value
        return value
    def pow(self,a,n):
        v=1
        while n:
            if n&1:v=self.mul(v,a)
            a=self.mul(a,a);n//=2
        return v

def count_curve(m):
    f=Field(m); q=f.order
    eta=next(u for u in range(q) if f.mul(u,u)==2)
    assert eta not in (0,1,2)
    fourth=[f.pow(u,4) for u in range(q)]
    cubic=[f.pow(u,3) for u in range(q)]
    rhs=[f.neg(f.add(f.mul(eta,fourth[y]),f.add(cubic[y],y))) for y in range(q)]
    freq=Counter(fourth)
    affine=sum(freq[a] for a in rhs)
    infinity=freq[f.neg(eta)]
    counted=affine+infinity
    # Independent projective enumeration: every projective point has
    # a unique representative [x:y:1] or [x:1:0] or [1:0:0].
    brute=sum(1 for y in range(q) for x in range(q) if fourth[x]==rhs[y])
    brute+=sum(1 for x in range(q) if fourth[x]==f.neg(eta))
    assert brute==counted, (m,brute,counted)
    assert f.add(1,2)==0 and f.mul(eta,eta)==2
    return counted,affine,infinity,f.mod

def poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def main():
    expected={2:(1,1,0),4:(109,105,4),6:(892,892,0)}
    for m in (2,4,6):
        n,aff,inf,mod=count_curve(m)
        assert (n,aff,inf)==expected[m],(m,n,aff,inf)
        print('F_3^%s'%m,'polynomial',mod,'points',n,'affine',aff,'infinity',inf)
    q=9
    power_sums=[None]+[q**k+1-expected[2*k][0] for k in (1,2,3)]
    coeff=[1]
    for k in (1,2,3):
        s=sum(coeff[k-i]*power_sums[i] for i in range(1,k+1))
        assert s%k==0
        coeff.append(-s//k)
    coeff.extend([q*coeff[2],q*q*coeff[1],q**3])
    target=poly_mul(poly_mul([1,-3,9],[1,-3,9]),[1,-3,9])
    assert coeff==target,(coeff,target)
    assert sum(coeff)==343
    E=1+sum(sum(y*y%3==((x*x*x-x+1)%3) for y in range(3)) for x in range(3))
    assert E==7
    trace_f3=3+1-E
    trace_f9=trace_f3**2-2*3
    assert trace_f3==-3 and trace_f9==3
    print('L(T) coefficients',coeff,'= (1-3T+9T^2)^3')
    print('Jacobian cardinality',sum(coeff),'elliptic trace F3/F9',trace_f3,trace_f9)
    print('VERIFICATION_OK')
if __name__=='__main__':main()
