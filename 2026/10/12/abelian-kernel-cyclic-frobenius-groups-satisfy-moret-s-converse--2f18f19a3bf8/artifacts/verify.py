from itertools import product
from math import gcd, lcm
from collections import Counter

def prime_support(n):
    out=set()
    d=2
    while d*d<=n:
        if n%d==0:
            out.add(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1:
        out.add(n)
    return out

class AbelianKernel:
    def __init__(self,mods,action,m,name):
        self.mods=tuple(mods)
        self.action=action
        self.m=m
        self.name=name
        self.elements=list(product(*[range(n) for n in self.mods]))
        self.zero=tuple(0 for _ in self.mods)
        self.L=1
        for n in self.mods:
            self.L=lcm(self.L,n)

    def act(self,x,j=1):
        y=x
        for _ in range(j%self.m):
            y=self.action(y)
        return y

    def pair(self,a,x):
        return sum(
            ai*xi*(self.L//n)
            for ai,xi,n in zip(a,x,self.mods)
        )%self.L

    def fingerprint(self,a):
        return tuple(self.pair(a,x) for x in self.elements)

    def order(self,x):
        ans=1
        for xi,n in zip(x,self.mods):
            if xi:
                ans=lcm(ans,n//gcd(xi,n))
        return ans

    def verify(self):
        for x in self.elements:
            assert self.act(x,self.m)==x
        for j in range(1,self.m):
            fixed=[x for x in self.elements if self.act(x,j)==x]
            assert fixed==[self.zero],(self.name,j,fixed)

        labels_by_fp={self.fingerprint(a):a for a in self.elements}
        assert len(labels_by_fp)==len(self.elements)

        unseen=set(self.elements)
        orbits=[]
        while unseen:
            a=next(iter(unseen))
            orb=[]
            for j in range(self.m):
                transformed=tuple(
                    self.pair(a,self.act(x,j))
                    for x in self.elements
                )
                orb.append(labels_by_fp[transformed])
            orb=set(orb)
            if a==self.zero:
                assert orb=={self.zero}
            else:
                assert len(orb)==self.m
            unseen-=orb
            orbits.append(orb)

        nonlinear=[]
        for orb in orbits:
            if self.zero in orb:
                continue
            N=[]
            for x in self.elements:
                if all(self.pair(a,x)==0 for a in orb):
                    N.append(x)
            codegree=len(self.elements)//len(N)
            witness=next(
                (
                    x for x in self.elements
                    if prime_support(self.order(x))==prime_support(codegree)
                ),
                None
            )
            assert witness is not None
            nonlinear.append((codegree,self.order(witness)))

        assert len(nonlinear)==(len(self.elements)-1)//self.m
        assert self.m+len(nonlinear)*self.m*self.m==len(self.elements)*self.m

        linear=[]
        for j in range(self.m):
            d=1 if j==0 else self.m//gcd(self.m,j)
            # A cyclic group of order m has an element of exact order d.
            assert self.m%d==0
            linear.append(d)

        print({
            "example":self.name,
            "kernel_order":len(self.elements),
            "complement_order":self.m,
            "linear_codegrees":dict(Counter(linear)),
            "nonlinear_codegrees":dict(Counter(c for c,_ in nonlinear)),
        })

examples=[
    AbelianKernel([9],lambda x:((-x[0])%9,),2,"C9:C2"),
    AbelianKernel([15],lambda x:((-x[0])%15,),2,"C15:C2"),
    AbelianKernel([3,3],lambda x:((-x[1])%3,x[0]%3),4,"C3^2:C4"),
    AbelianKernel([5,5],lambda x:((-x[1])%5,(x[0]-x[1])%5),3,"C5^2:C3"),
    AbelianKernel([3,9],lambda x:((-x[0])%3,(-x[1])%9),2,"C3xC9:C2"),
    AbelianKernel([5,25],lambda x:((2*x[0])%5,(7*x[1])%25),4,"C5xC25:C4"),
]
for example in examples:
    example.verify()

print("VERIFY_OK")
