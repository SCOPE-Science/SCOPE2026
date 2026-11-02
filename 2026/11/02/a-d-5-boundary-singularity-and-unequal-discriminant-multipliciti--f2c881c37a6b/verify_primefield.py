#!/usr/bin/env python3
"""Independent exhaustive direct polynomial/Cartier computation over GF(5)."""
p=5

def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,t in enumerate(x):
  for j,s in enumerate(y):z[i+j]=(z[i+j]+t*s)%p
 return z

def eval_(coeff,x):
 r=0
 for t in reversed(coeff):r=(r*x+t)%p
 return r

def poly_deriv(coeff):return [(i*coeff[i])%p for i in range(1,len(coeff))]

def smooth(coeff):
 # A quartic over F5 may have roots repeated only over extensions; Euclidean gcd.
 def trim(q):
  while q and q[-1]==0:q.pop()
  return q
 def rem(q,t):
  q=trim(q[:]);t=trim(t[:]); inv=pow(t[-1],-1,p)
  while len(q)>=len(t):
   scale=q[-1]*inv%p;off=len(q)-len(t)
   for i in range(len(t)):q[off+i]=(q[off+i]-scale*t[i])%p
   trim(q)
  return q
 q=coeff[:];t=poly_deriv(coeff)
 while t:q,t=t,rem(q,t)
 return len(q)==1

def stable_rank(H):
 # Left multiplication with 5-Frobenius twist; over GF5 twist is identity.
 def prod(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%5 for j in range(3)] for i in range(3)]
 def rank(A):
  A=[r[:] for r in A];k=0
  for col in range(3):
   pivot=next((r for r in range(k,3) if A[r][col]),None)
   if pivot is None:continue
   A[k],A[pivot]=A[pivot],A[k]
   iv=pow(A[k][col],-1,5);A[k]=[t*iv%5 for t in A[k]]
   for r in range(3):
    if r!=k:
     s=A[r][col];A[r]=[(A[r][j]-s*A[k][j])%5 for j in range(3)]
   k+=1
  return k
 Q=prod(prod(H,H),H)
 return rank(Q),3-rank(H)

out={}
for a in range(5):
 for b in range(5):
  for c in range(5):
   f=[c,b,a,0,1]
   if not smooth(f):
    out['singular']=out.get('singular',0)+1;continue
   fp=mul(mul(f,f),f)
   # Basis u=dx/y^2, v=x dx/y^2, w=dx/y
   # Directly extract x^4 and x^9 coefficients of f^3.
   H=[[0,0,fp[4]],[0,0,fp[9]],[1,0,0]]
   rr,aa=stable_rank(H)
   expect=0 if (a*a*c+a*b*b+c*c)%5==0 else 2
   assert (rr,aa)==(expect,1),(a,b,c,rr,aa)
   assert not (rr==0 and b==0)
   out[(rr,aa)]=out.get((rr,aa),0)+1
print('GF5_EXHAUSTIVE_DIRECT_CARTIER_OK',out)
