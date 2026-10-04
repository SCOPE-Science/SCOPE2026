from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q in (2,4) else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0 | (c1<<1)

def mats(q):
    return list(product(range(q), repeat=4))

def addm(F,A,B):
    return tuple(F.add(a,b) for a,b in zip(A,B))

def negm(F,A):
    return tuple(F.neg(a) for a in A)

def mulm(F,A,B):
    a,b,c,d=A
    e,f,g,h=B
    return (
        F.add(F.mul(a,e),F.mul(b,g)),
        F.add(F.mul(a,f),F.mul(b,h)),
        F.add(F.mul(c,e),F.mul(d,g)),
        F.add(F.mul(c,f),F.mul(d,h)),
    )

def comm(F,A,B):
    return addm(F,mulm(F,A,B),negm(F,mulm(F,B,A)))

def tr(F,A):
    return F.add(A[0],A[3])

def trprod(F,A,B):
    return tr(F,mulm(F,A,B))

def is_scalar(A):
    return A[1]==0 and A[2]==0 and A[0]==A[3]

def histogram(F,r):
    M=mats(F.q)
    nr=negm(F,r)
    deg=[]
    for x in M:
        d=0
        for y in M:
            if x==y:
                continue
            c=comm(F,x,y)
            if c!=r and c!=nr:
                d+=1
        deg.append(d)
    return dict(Counter(deg))

def predicted(F,r):
    q=F.q
    q4=q**4
    if r==(0,0,0,0):
        return {0:q, q4-q*q:q4-q}
    if tr(F,r)!=0:
        return {q4-1:q4}
    lowcount=q**3-q
    highcount=q4-lowcount
    low=q4-q*q-1 if q in (2,4) else q4-2*q*q-1
    return {low:lowcount, q4-1:highcount}

def check_fiber_criterion(F,r):
    assert r!=(0,0,0,0) and tr(F,r)==0
    M=mats(F.q)
    for x in M:
        if is_scalar(x):
            continue
        attained=any(comm(F,x,y)==r for y in M)
        criterion=(trprod(F,r,x)==0)
        assert attained==criterion,(F.q,r,x,attained,criterion)

tests={
    2:[(0,0,0,0),(0,1,0,0),(1,0,0,1),(1,0,0,0)],
    3:[(0,0,0,0),(0,1,0,0),(1,0,0,2),(1,0,0,0)],
    4:[(0,0,0,0),(0,1,0,0),(1,0,0,1),(1,0,0,0)],
    5:[(0,0,0,0),(0,1,0,0),(1,0,0,4),(1,0,0,0)],
}

for q,rs in tests.items():
    F=Field(q)
    for r in rs:
        H=histogram(F,r)
        P=predicted(F,r)
        assert H==P,(q,r,H,P)
        if r!=(0,0,0,0) and tr(F,r)==0:
            check_fiber_criterion(F,r)
        print({'q':q,'r':r,'trace':tr(F,r),'degrees':dict(sorted(H.items()))})

print('VERIFY_OK')
