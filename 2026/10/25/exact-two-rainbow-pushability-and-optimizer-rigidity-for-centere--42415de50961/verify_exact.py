"""Exact rational-quadratic enumeration for regular pentagon pushability.
Requires Python 3.10+ standard library only. All operations use Q(sqrt(5))."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict

class K:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    @staticmethod
    def cv(x):return x if isinstance(x,K) else K(x)
    def __add__(self,o):o=K.cv(o);return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,o):return self+-K.cv(o)
    def __rsub__(self,o):return K.cv(o)+-self
    def __mul__(self,o):o=K.cv(o);return K(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=K.cv(o); d=o.a*o.a-5*o.b*o.b
        assert d
        return K((self.a*o.a-5*self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
    def __eq__(self,o):o=K.cv(o);return self.a==o.a and self.b==o.b
    def __bool__(self):return self.a!=0 or self.b!=0
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        assert d!=0
        return ((a>0)-(a<0)) * ((d>0)-(d<0))
    def __gt__(self,o):return (self-K.cv(o)).sign()>0
    def __lt__(self,o):return (self-K.cv(o)).sign()<0
    def __repr__(self):return f'({self.a})+({self.b})sqrt5'

Z=K(0); ONE=K(1); t=K(F(-1,2),F(1,2))
u=[(ONE,Z),(Z,ONE),(-ONE,t),(-t,-t),(t,-ONE)]
B=[[K(int(min((i-j)%5,(j-i)%5)<=1)) for j in range(5)] for i in range(5)]
H=[[B[i][j-5] if i<5 and j>=5 else B[j][i-5] if j<5 and i>=5 else Z for j in range(10)] for i in range(10)]
A=[[K(int(i<5)) for i in range(10)], [K(int(i>=5)) for i in range(10)], [u[i%5][0] for i in range(10)], [u[i%5][1] for i in range(10)]]
b=[ONE,ONE,Z,Z]

def rref(M, rhs=None):
    n=len(M); m=len(M[0]); W=[list(row)+([rhs[i]] if rhs is not None else []) for i,row in enumerate(M)]
    piv=[];row=0
    for j in range(m):
        i=next((i for i in range(row,n) if W[i][j]),None)
        if i is None: continue
        W[row],W[i]=W[i],W[row]
        q=W[row][j];W[row]=[x/q for x in W[row]]
        for k in range(n):
            if k!=row and W[k][j]:
                q=W[k][j];W[k]=[a-q*b for a,b in zip(W[k],W[row])]
        piv.append(j);row+=1
        if row==n:break
    if rhs is not None:
        for k in range(row,n):
            if W[k][-1]: return None
    return W,piv

def solve_affine(M,rhs):
    n=len(M[0]); rr=rref(M,rhs)
    if rr is None:return None
    W,p=rr
    x=[Z]*n
    for i,j in enumerate(p):x[j]=W[i][-1]
    N=[]
    for free in range(n):
        if free in p:continue
        z=[Z]*n;z[free]=ONE
        for i,j in enumerate(p):z[j]=-W[i][free]
        N.append(z)
    return x,N

def det(M):
    n=len(M)
    if n==0:return ONE
    W=[list(row) for row in M];d=ONE
    for j in range(n):
        k=next((i for i in range(j,n) if W[i][j]),None)
        if k is None:return Z
        if k!=j:W[k],W[j]=W[j],W[k];d=-d
        pivot=W[j][j];d=d*pivot
        for i in range(j+1,n):
            q=W[i][j]/pivot
            for l in range(j+1,n):W[i][l]=W[i][l]-q*W[j][l]
    return d

def quad(G,x,y):return sum((x[i]*G[i][j]*y[j] for i in range(len(x)) for j in range(len(y))),Z)

def transform(m,s,flip,swap):
 out=0
 for i in range(10):
  if m>>i & 1:
   j=(((-i%5 if flip else i%5)+s)%5)+5*((i//5)^swap)
   out |=1<<j
 return out

def representative(m):return min(transform(m,s,f,w) for s in range(5) for f in (False,True) for w in (False,True))

def analyze_support(mask):
 ids=[i for i in range(10) if mask>>i&1]
 C=[[row[i] for i in ids] for row in A]
 sol=solve_affine(C,b)
 if sol is None:return None
 x,N=sol;k=len(ids); d=len(N)
 Q=[[H[i][j] for j in ids] for i in ids]
 G=[[quad(Q,ni,nj) for nj in N] for ni in N]
 # A relative-interior maximum of a quadratic needs restricted Hessian
 # negative semidefinite; selecting one of minimal support forces strict negativity.
 for r in range(1,d+1):
  if (-1)**r*det([row[:r] for row in G[:r]]).sign()<=0:return None
 if d:
  v=[-quad(Q,ni,x) for ni in N]
  alpha=solve_affine(G,v)
  assert alpha is not None and not alpha[1]
  a=alpha[0]
  x=[x[j]+sum((N[k][j]*a[k] for k in range(d)),Z) for j in range(len(x))]
 if any(z.sign()<=0 for z in x):return None
 value=quad(Q,x,x)/2
 return value,x,ids,d

if __name__=='__main__':
 reps=sorted(set(representative(m) for m in range(1,1024)))
 good=[]
 for m in reps:
  a=analyze_support(m)
  if a:good.append((m,a))
 assert len(reps)==77 and len(good)==11
 print('total support orbit reps',len(reps),'strict stationary orbit reps',len(good))
 for m,(f,x,ids,d) in sorted(good,key=lambda o:float(o[1][0].a)+float(o[1][0].b)*5**.5,reverse=True):
  print('mask',hex(m),'support',ids,'dim',d,'Q',f,'weights',[str(w) for w in x])
 top=K(F(73,110),F(1,110))
 assert max(f for _,(f,_,_,_) in good)==top
 assert len([v for _,(v,_,_,_) in good if v==top])==1
 assert len({transform(0x175,s,f,w) for s in range(5) for f in (False,True) for w in (False,True)})==10
 aa=K(F(45,110),F(-3,110));bb=K(F(30,110),F(-2,110));cc=K(F(35,110),F(5,110))
 pp=[bb,Z,cc,Z,aa];qq=[bb,aa,Z,cc,Z]
 assert all(v.sign()>0 for v in (aa,bb,cc))
 assert sum(pp,Z)==ONE and sum(qq,Z)==ONE
 assert all(sum((pp[i]+qq[i])*u[i][axis] for i in range(5))==Z for axis in (0,1))
 assert sum(pp[i]*B[i][j]*qq[j] for i in range(5) for j in range(5))==top
 # Strict reduced gradients exclude larger-support flat maximal families.
 val,zz,ids,_=analyze_support(0x175)
 full=[Z]*10
 for i,w in zip(ids,zz):full[i]=w
 grad=[sum((H[i][j]*full[j] for j in range(10)),Z) for i in range(10)]
 dual=solve_affine([[A[j][i] for j in range(4)] for i in ids],[grad[i] for i in ids])
 assert dual is not None and not dual[1]
 lam=dual[0]
 reduced=[grad[i]-sum((A[j][i]*lam[j] for j in range(4)),Z) for i in range(10)]
 assert all(reduced[i]==Z for i in ids)
 assert [reduced[i] for i in (1,3,7,9)]==[K(F(1,11),F(-4,55)),-aa,-aa,K(F(1,11),F(-4,55))]
 assert all(reduced[i].sign()<0 for i in (1,3,7,9))
 print('PASS: exhaustive exact maximum, ten optimizer pairs and strict complementarity')
