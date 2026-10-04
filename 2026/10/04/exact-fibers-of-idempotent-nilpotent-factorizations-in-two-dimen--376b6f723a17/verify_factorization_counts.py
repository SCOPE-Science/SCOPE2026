#!/usr/bin/env python3
from collections import Counter, defaultdict

class Field:
    def __init__(self,q):
        self.q=q
        if q in (2,3,5,7):
            self.kind='prime'; self.p=q
        elif q==4:
            self.kind='gf4'
        else: raise ValueError(q)
    def add(self,a,b):
        if self.kind=='prime': return (a+b)%self.p
        return a^b
    def neg(self,a):
        if self.kind=='prime': return (-a)%self.p
        return a
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.kind=='prime': return (a*b)%self.p
        # GF(4)=F2[t]/(t^2+t+1), bits encode a0+a1 t
        a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)  # t^2=t+1 -> constant contribution 1
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)
    def eq0(self,a): return a==0


def mm(F,A,B):
    a,b,c,d=A; e,f,g,h=B
    return (F.add(F.mul(a,e),F.mul(b,g)),
            F.add(F.mul(a,f),F.mul(b,h)),
            F.add(F.mul(c,e),F.mul(d,g)),
            F.add(F.mul(c,f),F.mul(d,h)))

def tr(F,A): return F.add(A[0],A[3])
def det(F,A): return F.sub(F.mul(A[0],A[3]),F.mul(A[1],A[2]))
def classify(F,A):
    if A==(0,0,0,0): return 'zero'
    if det(F,A)!=0: return 'invertible'
    if tr(F,A)==0: return 'nonzero_nilpotent'
    return 'rank1_nonnilpotent'

def check(q):
    F=Field(q); els=range(q)
    mats=[(a,b,c,d) for a in els for b in els for c in els for d in els]
    idem=[A for A in mats if mm(F,A,A)==A]
    zero=(0,0,0,0)
    nil=[A for A in mats if mm(F,mm(F,A,A),A)==zero or mm(F,A,A)==zero] # 2x2 nilpotency <=2, zero included
    # Correct by trace/det criterion, also cross-check against square zero in 2x2 over a field.
    nil2=[A for A in mats if tr(F,A)==0 and det(F,A)==0]
    assert set(nil)==set(nil2), (q,len(nil),len(nil2), set(nil)^set(nil2))
    fibers=Counter()
    for E in idem:
        for N in nil2:
            fibers[mm(F,E,N)] += 1
    strata=defaultdict(set)
    counts=Counter()
    for A in mats:
        s=classify(F,A); counts[s]+=1; strata[s].add(fibers[A])
    expect={
      'zero': q**3+2*q**2+1,
      'nonzero_nilpotent': q+1,
      'rank1_nonnilpotent': q-1,
      'invertible': 0,
    }
    for s,v in expect.items():
        assert strata[s]=={v}, (q,s,strata[s],v)
    assert len(idem)==q*q+q+2
    assert len(nil2)==q*q
    print(f'q={q}: idempotents={len(idem)}, nilpotents={len(nil2)}, strata={dict(counts)}, fibers={expect}')

for q in (2,3,4,5,7): check(q)
print('VERIFY_OK')
