#!/usr/bin/env python3
"""Exact finite-field checks for the normalized genus-two bielliptic family."""
P=5

def poladd(A,B):
    C=[0]*max(len(A),len(B))
    for i,x in enumerate(A): C[i]=(C[i]+x)%P
    for i,x in enumerate(B): C[i]=(C[i]+x)%P
    return C

def polymul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B): C[i+j]=(C[i+j]+x*y)%P
    return C

def eqpoly(A,B):
    n=max(len(A),len(B))
    return all((A[i] if i<len(A) else 0)%P == (B[i] if i<len(B) else 0)%P for i in range(n))

def scalar(A,n): return [(n*x)%P for x in A]

# Discriminant of u^3+a*u^2+b*u+1, modulo five.
# Restrict to H_1=0 by b=2*a^2, and verify the exact polynomial identity.
def discr_univariate_h1():
    A=[0,1]; B=[0,0,2]; one=[1]
    term=lambda *xs: __import__('functools').reduce(polymul,xs,one)
    D=poladd(term(A,A,B,B), scalar(term(B,B,B),-4))
    D=poladd(D, scalar(term(A,A,A),-4))
    D=poladd(D,[-27])
    D=poladd(D, scalar(term(A,B),18))
    rhs=scalar(term(poladd(term(A,A,A),[-2]),poladd(term(A,A,A),[-2])),2)
    assert eqpoly(D,rhs), (D,rhs)
    return True

class Field:
 def __init__(self,n):
    self.n=n;self.q=P**n
    # t^2+2 and t^3+t+1 are irreducible over F_5.
    self.mod={1:[0,1],2:[2,0,1],3:[1,1,0,1]}[n]
    self.tuples=[tuple((k//(P**i))%P for i in range(n)) for k in range(self.q)]
    self.to_num={t:i for i,t in enumerate(self.tuples)}
    self.add=[[self.to_num[tuple((x+y)%P for x,y in zip(s,t))] for t in self.tuples] for s in self.tuples]
    self.mul=[[self.product(s,t) for t in self.tuples] for s in self.tuples]
    self.zero=0;self.one=1
    self.inverse=[0]*self.q
    for x in range(1,self.q):
      self.inverse[x]=self.pow(x,self.q-2)
      assert self.mul[x][self.inverse[x]]==1
 def product(self,s,t):
    out=[0]*(2*self.n-1)
    for i,x in enumerate(s):
      for j,y in enumerate(t):out[i+j]=(out[i+j]+x*y)%P
    for i in range(len(out)-1,self.n-1,-1):
      c=out[i]
      for j in range(self.n):out[i-self.n+j]=(out[i-self.n+j]-c*self.mod[j])%P
    return self.to_num[tuple(out[:self.n])]
 def A(self,x,y):return self.add[x][y]
 def M(self,x,y):return self.mul[x][y]
 def neg(self,x):return self.to_num[tuple((-u)%P for u in self.tuples[x])]
 def sub(self,x,y):return self.A(x,self.neg(y))
 def pow(self,a,n):
    z=1
    while n:
      if n&1:z=self.M(z,a)
      a=self.M(a,a);n//=2
    return z
 def c(self,i):return i%P
 def discriminant(self,a,b):
    add=self.A;mul=self.M;sub=self.sub
    # a^2 b^2 - 4 b^3 - 4 a^3 - 27 + 18 a b
    return sub(add(sub(sub(mul(mul(a,a),mul(b,b)),mul(self.c(4),self.pow(b,3))),mul(self.c(4),self.pow(a,3))),mul(self.c(18),mul(a,b))),self.c(27))
 def rank(self,a,b):
    # Compute coefficients of f(x)^2, not just the two stated Hasse formulas.
    ff=[1,0,b,0,a,0,1]
    cs=[0]*13
    for i,v in enumerate(ff):
      for j,w in enumerate(ff):cs[i+j]=self.A(cs[i+j],self.M(v,w))
    assert cs[3]==0 and cs[9]==0
    assert cs[4]==self.A(self.M(b,b),self.M(2,a))
    assert cs[8]==self.A(self.M(a,a),self.M(2,b))
    return (cs[4]!=0)+(cs[8]!=0)

def run(n):
    F=Field(n);q=F.q
    counts=[0,0,0];sing=[];inter=[]
    for a in range(q):
      for b in range(q):
        h1=F.A(F.M(a,a),F.M(2,b))
        h2=F.A(F.M(b,b),F.M(2,a))
        D=F.discriminant(a,b)
        if h1==h2==0:inter.append((a,b,D))
        if D==0:sing.append((a,b));continue
        counts[F.rank(a,b)]+=1
    t=sum(F.pow(a,3)==2 for a in range(q))
    target=[1,2*(q-t-1),q*q-3*q+2*t+2]
    assert counts==target,(n,counts,target)
    assert len(sing)==q-1,(n,len(sing))
    assert len(inter)==1+t,(n,len(inter),t)
    assert sum(D!=0 for _,_,D in inter)==1
    assert (0,0,F.discriminant(0,0)) in inter
    print('F_%s  ranks_0_1_2=%s  singular=%s  triple_boundaries=%s'%(q,counts,len(sing),t))

if __name__=='__main__':
    assert discr_univariate_h1()
    for n in (1,2,3):run(n)
    print('VERIFY_OK')
