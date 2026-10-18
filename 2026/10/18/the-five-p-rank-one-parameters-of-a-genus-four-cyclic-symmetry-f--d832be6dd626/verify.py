#!/usr/bin/env python3
"""Exact characteristic-seven polynomial and finite-field checks for the stated curve family."""
from math import factorial
P = 7

def trim(f):
    g = [int(c) % P for c in f]
    while g and g[-1] == 0: g.pop()
    return g

def add(f,g):
    out = [0]*max(len(f),len(g))
    for i,x in enumerate(f): out[i]=(out[i]+x)%P
    for i,x in enumerate(g): out[i]=(out[i]+x)%P
    return trim(out)

def scale(f,c): return trim([c*x for x in f])

def mul(f,g):
    if not f or not g: return []
    out=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g): out[i+j]=(out[i+j]+x*y)%P
    return trim(out)

def power(f,n):
    out=[1]
    while n:
        if n&1:out=mul(out,f)
        f=mul(f,f); n//=2
    return out

def rem(f,g):
    f=trim(f);g=trim(g)
    if not g:raise ZeroDivisionError
    inv=pow(g[-1],P-2,P)
    while len(f)>=len(g):
        s=(f[-1]*inv)%P; shift=len(f)-len(g)
        for j,y in enumerate(g):f[shift+j]=(f[shift+j]-s*y)%P
        f=trim(f)
    return f

def gcd(f,g):
    while g:f,g=g,rem(f,g)
    return scale(f,pow(f[-1],P-2,P)) if f else []

def evaluate(f,a):
    y=0
    for x in reversed(f):y=(y*a+x)%P
    return y

def expected_poly(*terms):
    return {tuple(k):v%P for k,v in terms if v%P}

# Coefficients c_d of f(x)^3 where f=x^10+x^7+a x^4+b x,
# each c_d is a sparse bivariate polynomial in a,b.
coeff={}
for i in range(4):
 for j in range(4-i):
  for k in range(4-i-j):
   ell=3-i-j-k
   d=10*i+7*j+4*k+ell
   n=factorial(3)//(factorial(i)*factorial(j)*factorial(k)*factorial(ell))
   h=coeff.setdefault(d,{})
   h[(k,ell)]=(h.get((k,ell),0)+n)%P
coeff={d:{mon:v for mon,v in q.items() if v} for d,q in coeff.items()}

known=[
 [ {(1,2):3}, {}, {}, {(0,3):1} ],
 [ {}, {(3,0):1,(1,1):6,(0,2):3}, {}, {} ],
 [ {}, {}, {(2,0):3,(1,0):3,(0,1):6}, {} ],
 [ {(0,0):3}, {}, {}, {(1,0):3,(0,0):3} ],
]
for i in range(4):
 for j in range(4):
  c=coeff.get(7*(i+1)-(j+1),{})
  assert c==known[i][j],('Cartier entry',i,j,c,known[i][j])

A=[0,1]             # a
one=[1]
Ap1=add(A,one)
B=scale(mul(A,Ap1),3) # b=3a(a+1) on V=0
U=add(add(power(A,3),scale(mul(A,B),-1)),scale(power(B,2),3))
V=add(add(scale(power(A,2),3),scale(A,3)),scale(B,-1))
assert not V
assert U == scale(mul(power(A,2),power(add(A,[-5]),2)),6)
Delta=add(add(add(add(power(A,2),scale(power(A,3),-4)),scale(B,-4)),scale(power(B,2),-27)),scale(mul(A,B),18))
assert Delta == scale(mul(A,power(add(A,[2]),3)),2)
W=add(scale(mul(A,power(B,2)),3),scale(power(Ap1,7),3))
Q=[-1,0,3,1]       # a^3+3a^2-1
expectedW=scale(mul(mul(mul(add(A,[-3]),add(A,[-2])),power(Ap1,2)),Q),3)
assert W == expectedW,(W,expectedW)
assert gcd(Q, [0,1])==[1]
assert gcd(Q,Ap1)==[1]
assert gcd(Q,Delta)==[1]
assert gcd(W,Delta)==[1]
assert gcd(W,B)==Ap1
assert all(evaluate(Q,z)!=0 for z in range(7)) # Q irreducible over F7
assert all(evaluate(Q,z)!=0 for z in (0,5,6))
assert rem(Q,[0,1]) # independent sanity

# Exhaust all rational parameter pairs and compare ranks for p-rank via
# powers of Cartier matrix M.  For elements of F7, Frobenius fixes entries.
def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]
def rank(M):
 T=[list(map(lambda x:x%P,row)) for row in M]
 m=len(T);n=len(T[0]);r=0
 for c in range(n):
  k=next((i for i in range(r,m) if T[i][c]),None)
  if k is None:continue
  T[r],T[k]=T[k],T[r]
  z=pow(T[r][c],P-2,P);T[r]=[(v*z)%P for v in T[r]]
  for i in range(m):
   if i!=r and T[i][c]:
    z=T[i][c]
    T[i]=[(T[i][j]-z*T[r][j])%P for j in range(n)]
  r+=1
  if r==m:break
 return r

classes={}
for a in range(P):
 for b in range(P):
  d=(a*a-4*a**3-4*b-27*b*b+18*a*b)%P
  if b*d==0:continue
  u=(a**3-a*b+3*b*b)%P
  v=(3*a*a+3*a-b)%P
  w=(3*a*b*b+3*pow(a+1,7,7))%P
  M=[[3*a*b*b,0,0,b**3],[0,u,0,0],[0,0,v,0],[3,0,0,3*a+3]]
  M=[[z%P for z in row] for row in M]
  N=[row[:] for row in M]
  for _ in range(3):N=matmul(N,M)
  aa=4-rank(M)
  pr=rank(N)
  predicted=(4,0) if u and v else (3,1) if v else ((1,2) if w==0 else (2,2))
  assert (pr,aa)==predicted,(a,b,pr,aa,predicted)
  classes[predicted]=classes.get(predicted,0)+1
assert (1,2) in classes and (2,2) in classes and (3,1) in classes and (4,0) in classes
print('PASS: all 16 Cartier entries, rank/p-rank strata, discriminant substitution,')
print('      W factorization and coprimality, and F7 rational checks.')
print('F7 smooth parameter counts by (p-rank,a-number):',sorted(classes.items()))
print('Geometric p-rank-one locus: 2 rational points plus 3 roots of irreducible Q; total 5.')
