"""Direct finite-field checks of an additive-energy identity. Python 3 stdlib only."""
from collections import Counter

class Field:
    def __init__(self,p,mod=None):
        self.p=p; self.mod=mod or [0,1]; self.e=len(self.mod)-1; self.q=p**self.e
        self.ds=[[ (i//(p**j))%p for j in range(self.e)] for i in range(self.q)]
        self.add=[[self.encode([(x+y)%p for x,y in zip(self.ds[a],self.ds[b])]) for b in range(self.q)] for a in range(self.q)]
        self.mul=[[self.multiply(a,b) for b in range(self.q)] for a in range(self.q)]
        self.neg=[self.encode([(-x)%p for x in self.ds[a]]) for a in range(self.q)]
    def encode(self,c):return sum(a*self.p**i for i,a in enumerate(c))
    def multiply(self,a,b):
        c=[0]*(2*self.e-1)
        for i,x in enumerate(self.ds[a]):
            for j,y in enumerate(self.ds[b]): c[i+j]=(c[i+j]+x*y)%self.p
        for k in range(len(c)-1,self.e-1,-1):
            u=c[k]
            for j in range(self.e): c[k-self.e+j]=(c[k-self.e+j]-u*self.mod[j])%self.p
        return self.encode(c[:self.e])
    def plus(self,a,b):return self.add[a][b]
    def prod(self,a,b):return self.mul[a][b]
    def minus(self,a,b):return self.add[a][self.neg[b]]
    def power(self,a,k):
        r=1
        while k:
            if k&1:r=self.prod(r,a)
            a=self.prod(a,a); k//=2
        return r
    def character(self,a):
        if a==0:return 0
        return 1 if self.power(a,(self.q-1)//2)==1 else -1

def run(p, mod=None):
    F=Field(p,mod);q=F.q
    assert p%2==1
    d=next(i for i in range(1,q) if F.character(i)==-1)
    add=F.plus; sub=F.minus; mul=F.prod
    V={(sub(add(mul(a,a),a),mul(d,mul(b,b))),b)
       for a in range(q) for b in range(q)}
    assert len(V)==q*(q+1)//2
    sums=Counter((add(x[0],y[0]),add(x[1],y[1])) for x in V for y in V)
    energy=sum(k*k for k in sums.values())
    chi=F.character(F.neg[1])
    predicted=(q*q*(q+1)**4+q*(q-1)*((q+1)**2+2*q*(1+chi)))//16
    assert energy==predicted,(q,energy,predicted)
    return q,len(V),energy
if __name__=='__main__':
    cases=[(3,None),(5,None),(7,None),(11,None),(13,None),(17,None),(19,None),(3,[1,0,1]),(5,[2,0,1])]
    r=[run(*c) for c in cases]
    print('VERIFY_OK fields=',len(r),'total_image_points=',sum(x[1] for x in r),'total_energy=',sum(x[2] for x in r))
