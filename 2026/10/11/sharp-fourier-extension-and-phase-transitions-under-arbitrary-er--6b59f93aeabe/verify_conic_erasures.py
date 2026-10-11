"""Standalone exact checks for Fourier fourth moments on erased binary conics.
No external packages; finite cases corroborate the general algebraic argument.
"""
from fractions import Fraction
from itertools import combinations
from random import Random

RNG=Random(424242)

class Field:
    def __init__(self,p,degree=1):
        self.p=p; self.degree=degree
        assert degree==1 or (p==3 and degree==2)
        self.elements=list(range(p)) if degree==1 else [(a,b) for a in range(p) for b in range(p)]
        self.zero=0 if degree==1 else (0,0)
        self.one=1 if degree==1 else (1,0)
    def add(self,a,b):
        p=self.p
        return (a+b)%p if self.degree==1 else ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def neg(self,a):
        p=self.p
        return (-a)%p if self.degree==1 else ((-a[0])%p,(-a[1])%p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        return (a*b)%p if self.degree==1 else ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def square(self,a):return self.mul(a,a)
    def nonsquare(self):
        squares={self.square(a) for a in self.elements if a!=self.zero}
        return next(a for a in self.elements if a!=self.zero and a not in squares)

def run_case(F,delta,all_masks=True):
    q=len(F.elements)
    Q=lambda x,y:F.sub(F.square(x),F.mul(delta,F.square(y)))
    C=[(x,y) for x in F.elements for y in F.elements if Q(x,y)==F.one]
    assert len(C) in (q-1,q+1)
    add=lambda u,v:(F.add(u[0],v[0]),F.add(u[1],v[1]))
    neg=lambda u:(F.neg(u[0]),F.neg(u[1]))
    pairs={}
    for i,u in enumerate(C):
        for j in range(i,len(C)):
            s=add(u,C[j]);pairs.setdefault(s,[]).append((i,j))
    assert all(s==(F.zero,F.zero) or len(v)==1 for s,v in pairs.items())
    assert all(i!=j for i,j in pairs.get((F.zero,F.zero),[]))
    m_total=len(C)
    masks=(range(1,1<<m_total) if all_masks else
            [((1<<m_total)-1)]+[sum(1<<j for j in RNG.sample(range(m_total),RNG.randint(1,m_total))) for _ in range(180)])
    checked=0; equalities=0; random_tests=0
    for mask in masks:
        A=[i for i in range(m_total) if mask>>i&1];m=len(A)
        pair_list=[(i,j) for i,j in pairs.get((F.zero,F.zero),[]) if i in A and j in A]
        p=len(pair_list)
        Csharp=Fraction(2*m-1,m) if p<=1 else Fraction(6*p-3,2*p)
        f={i:complex(RNG.randint(-2,2), RNG.randint(-2,2)) for i in A}
        def moment(g):
            conv={}
            for i,v in g.items():
                for j,w in g.items():
                    s=add(C[i],C[j]); conv[s]=conv.get(s,0)+v*w
            return sum(round(abs(v)**2) for v in conv.values())
        E=moment(f)
        S=sum(round(abs(v)**2) for v in f.values())
        # Exact pair-collision formula (Gaussian integer vectors)
        baseline=2*S*S-sum(round(abs(v)**4) for v in f.values())
        z=[f[i]*f[j] for i,j in pair_list]
        rhs=baseline+4*(round(abs(sum(z))**2)-sum(round(abs(w)**2) for w in z))
        assert E==rhs,(q,delta,mask,E,rhs)
        assert E*Csharp.denominator<=Csharp.numerator*S*S,(q,delta,mask)
        random_tests+=1
        if p<=1:
            g={i:1 for i in A}
        else:
            g={i:0 for i in A}
            for k,(i,j) in enumerate(pair_list):
                phase=(1,-1,1j,-1j)[k%4]; g[i]=phase;g[j]=phase.conjugate()
        G=moment(g); T=sum(round(abs(w)**2) for w in g.values())
        assert G*Csharp.denominator==Csharp.numerator*T*T,(q,delta,mask,p,G,T)
        checked+=1;equalities+=1
    print('q=%s delta=%s conic_size=%s all_masks=%s tested=%s random_moments=%s sharp_equalities=%s'%(q,delta,m_total,all_masks,checked,random_tests,equalities))

if __name__=='__main__':
    for q in (3,5,7,11):
        F=Field(q)
        for d in (F.one,F.nonsquare()):run_case(F,d,all_masks=True)
    F=Field(3,2)
    for d in (F.one,F.nonsquare()):run_case(F,d,all_masks=True)
    print('VERIFY_OK')
