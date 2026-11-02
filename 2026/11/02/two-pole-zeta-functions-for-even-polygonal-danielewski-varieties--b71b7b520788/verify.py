#!/usr/bin/env python3
"""Direct extension-field associated-zero enumerator for polygonal polynomial families.

Independent finite arithmetic check; not a substitute for the general proof.
"""
from itertools import product

class Field:
    def __init__(self,p,mod):
        self.p=p
        self.mod=mod
        self.d=len(mod)-1
        self.size=p**self.d
        self.addtab=[[0]*self.size for _ in range(self.size)]
        self.multab=[[0]*self.size for _ in range(self.size)]
        def digits(a):
            out=[]
            for _ in range(self.d):out.append(a%p);a//=p
            return out
        def encode(v):return sum((z%p)*p**i for i,z in enumerate(v))
        vals=[digits(i) for i in range(self.size)]
        for a in range(self.size):
            for b in range(self.size):
                self.addtab[a][b]=encode([(x+y)%p for x,y in zip(vals[a],vals[b])])
                prod=[0]*(2*self.d-1)
                for i,x in enumerate(vals[a]):
                    for j,y in enumerate(vals[b]): prod[i+j]=(prod[i+j]+x*y)%p
                for k in range(len(prod)-1,self.d-1,-1):
                    coef=prod[k]
                    for j in range(self.d):prod[k-self.d+j]=(prod[k-self.d+j]-coef*self.mod[j])%p
                self.multab[a][b]=encode(prod[:self.d])
        self.negtab=[encode([(-v)%p for v in x]) for x in vals]
    def add(self,a,b):return self.addtab[a][b]
    def mul(self,a,b):return self.multab[a][b]
    def sub(self,a,b):return self.addtab[a][self.negtab[b]]
    def pow(self,a,n):
        ans=1
        while n:
            if n&1:ans=self.mul(ans,a)
            a=self.mul(a,a)
            n//=2
        return ans

def make_family(m,q,F):
    def de(u):return F.pow(u,q-1)
    def gamma(u):return F.sub(1,de(u))
    def alpha(u,t):return F.mul(de(u),F.mul(t,F.add(t,u)))
    def beta(u,t):return F.add(alpha(u,t),F.mul(gamma(u),t))
    def omega(u,t):return F.sub(F.add(de(u),de(t)), F.mul(de(u),de(t)))
    if m in (4,6,8,10):
        def first(y):return F.sub(F.pow(y[0],q),y[0])
        def second(y):
            u,t=y
            vals=[1,t,u,F.add(u,t)]
            ans=omega(u,t)
            for v in vals[:(m-4)//2+1]:ans=F.mul(ans,v)
            return ans
        return [first,second]
    n=(m-4).bit_length()-1
    parent=m-2**n
    old=make_family(parent,q,F)
    r=len(old)
    ell=n-r-1
    assert ell>=0, (m,parent,n,r,ell)
    new=[lambda y:F.sub(F.pow(y[0],q),y[0])]
    for i in range(r):
        f=old[i]
        new.append(lambda y,i=i,f=f:F.add(alpha(y[0],y[i+1]), F.mul(gamma(y[0]),f(y[1:i+2]))))
    for i in range(ell):
        new.append(lambda y,i=i,r=r:beta(y[0],y[r+1+i]))
    return new

def coeff(m,q):
    residue={4:4,6:6,0:8,2:10}[m%8]
    h=(m-residue)//2
    if residue==4: return 0,1+h*(q-1)
    if residue==6: return 0,q+h*(q-1)
    if residue==8: return 1,(h+1)*(q-1)
    return 1,(h+2)*(q-1)

def run():
    samples=[(2,[0,1],2),(2,[1,1,1],2),(2,[1,1,0,1],2),(3,[0,1],3),(3,[1,0,1],3),(3,[1,2,0,1],3),(2,[1,1,1],4),(2,[1,1,0,0,1],4),(3,[1,0,1],9)]
    checks=0; points=0
    for p,poly,q in samples:
        F=Field(p,poly)
        Q=F.size
        assert all(F.pow(a,Q)==a for a in range(Q))
        mrange=[4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34]
        for m in mrange:
            fs=make_family(m,q,F)
            n=len(fs)
            if Q**n>16000: continue
            tot=0
            for y in product(range(Q),repeat=n):
                points+=1
                if all(f(y)==0 for f in fs):tot+=1
            k,c=coeff(m,q)
            pred=k*Q+c
            assert tot==pred, (p,F.d,m,Q,n,tot,pred)
            count=Q*(Q-1)+Q*tot
            assert count==(1+k)*Q*Q+(c-1)*Q
            if Q==q: assert count==((m-2)*q*q-(m-4)*q)//2
            checks+=1
    print('VERIFY_OK direct_extension_field_cases=%d associated_tuples_checked=%d'%(checks,points))
if __name__=='__main__':run()
