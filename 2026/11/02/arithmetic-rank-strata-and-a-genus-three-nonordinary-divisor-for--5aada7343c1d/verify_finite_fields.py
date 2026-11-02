"""Independent finite-field Cartier-rank replay, for F5 and F25.

No symbolic packages required. Polynomial squarefreeness is checked by
Euclidean gcd (not by the resultant polynomial).
Run: python verify_finite_fields.py
"""
import itertools
p=5
class FF:
 def __init__(self,ext):self.ext=ext;self.size=25 if ext else 5
 def add(self,x,y):
  if not self.ext:return (x+y)%5
  return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
 def neg(self,x):return self.mul(4,x)
 def mul(self,x,y):
  if not self.ext:return x*y%5
  a,b=x%5,x//5;c,d=y%5,y//5
  return (a*c+3*b*d)%5+5*((a*d+b*c)%5)
 def pow(self,x,n):
  v=1
  while n:
   if n%2:v=self.mul(v,x)
   x=self.mul(x,x);n//=2
  return v
 def inv(self,x):return self.pow(x,self.size-2)
 def sub(self,x,y):return self.add(x,self.neg(y))
 def rank(self,A):
  M=[x[:] for x in A];j=0
  for c in range(len(M[0])):
   k=next((r for r in range(j,len(M)) if M[r][c]),None)
   if k is None:continue
   M[j],M[k]=M[k],M[j];v=self.inv(M[j][c]);M[j]=[self.mul(v,z) for z in M[j]]
   for r in range(len(M)):
    if r!=j and M[r][c]:
     f=M[r][c];M[r]=[self.sub(u,self.mul(f,z)) for u,z in zip(M[r],M[j])]
   j+=1
  return j
 def matrix_mul(self,A,B):
  return [[sum_field([self.mul(x,y) for x,y in zip(row,col)],self) for col in zip(*B)] for row in A]
def sum_field(xs,K):
 s=0
 for x in xs:s=K.add(s,x)
 return s
def coeff_poly_power(K,terms,n):
 x={0:1}
 for k in range(n):
  y={}
  for deg1,c1 in x.items():
   for deg2,c2 in terms.items():
    deg=deg1+deg2;y[deg]=K.add(y.get(deg,0),K.mul(c1,c2))
  x=y
 return x
def matrix(K,a,b):
 f={0:1,1:b,3:a,7:1};f3=coeff_poly_power(K,f,3)
 M=[[0]*6 for _ in range(6)]
 # input group 1 (j=1), output 2 (j=2): f^3
 for i in range(1,3):
  for k in range(1,5):
   M[k+1][i-1]=f3.get(5*k-i,0)
 # input group 2 (j=2), output 1 (j=1): f
 for i in range(1,5):
  for k in range(1,3):
   M[k-1][i+1]=f.get(5*k-i,0)
 return M
def stable(K,M):
 P=[row[:] for row in M]
 for n in range(2,18):
  Mtw=[[K.pow(x,5**(n-1)) for x in row] for row in M]
  P=K.matrix_mul(Mtw,P)
 return K.rank(P)
def predicted(K,a,b):
 powr=K.pow; add=K.add;mul=K.mul
 H=K.sub(K.sub(powr(a,5),mul(2,mul(powr(a,2),powr(b,2)))),b)
 D=sum_field([mul(2,powr(a,7)),K.neg(mul(powr(a,6),powr(b,3))),K.neg(mul(powr(a,3),powr(b,5))),mul(powr(a,2),b),K.neg(mul(2,mul(a,powr(b,4)))),powr(b,7),K.neg(2)],K)
 if D==0:return None
 if a==0:rp=0
 elif H:rp=4
 elif b==mul(2,powr(a,47)):rp=0
 else:rp=2
 return (rp,4 if (a==0 and b==0) else 2)
def trim(u):
 while len(u)>1 and not u[-1]:u.pop()
 return u
def polynomial_mod(K,u,v):
 u=trim(u[:]);v=trim(v[:]);assert v[-1]
 while len(u)>=len(v) and u!=[0]:
  c=K.mul(u[-1],K.inv(v[-1]));d=len(u)-len(v)
  for i in range(len(v)):u[i+d]=K.sub(u[i+d],K.mul(c,v[i]))
  trim(u)
 return u
def is_squarefree(K,a,b):
 # x^7 + a*x^3 + b*x + 1 and derivative 2*x^6 + 3*a*x^2 + b.
 f=[1,b,0,a,0,0,0,1]
 g=[b,0,K.mul(3,a),0,0,0,2]
 while g!=[0]:f,g=g,polynomial_mod(K,f,g)
 return len(f)==1
for ext in (False,True):
 K=FF(ext);cnt={};matched=0
 for a,b in itertools.product(range(K.size),repeat=2):
  pr=predicted(K,a,b)
  assert (pr is not None)==is_squarefree(K,a,b), (ext,a,b,"squarefree disagreement")
  if pr is None: continue
  M=matrix(K,a,b); sr=stable(K,M); anum=6-K.rank(M)
  if (sr,anum)!=pr:print('ERROR',ext,a,b,(sr,anum),pr);raise SystemExit(1)
  cnt[pr]=cnt.get(pr,0)+1;matched+=1
 print('F',K.size,'smooth',matched,'strata',sorted(cnt.items()))
print('FINITE_FIELDS_GENUS6_OK')
