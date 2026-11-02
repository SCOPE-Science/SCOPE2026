"""Exact-rational checks for a four-row matrix control-variate model.

Only the Python standard library is required. Run: python verify_cv_frontier.py
"""
from fractions import Fraction as F
from itertools import product

Z=F(0); ONE=F(1)
G=( ((F(1,2),Z),(Z,Z)),
    ((Z,Z),(Z,F(1,2))),
    ((F(1,4),F(1,4)),(F(1,4),F(1,4))),
    ((F(1,4),-F(1,4)),(-F(1,4),F(1,4))) )
I=((ONE,Z),(Z,ONE))

def add(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def sub(A,B):return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))
def scale(x,A):return tuple(tuple(x*A[i][j] for j in range(2)) for i in range(2))
def mat_sum(terms):
 out=((Z,Z),(Z,Z))
 for A in terms:out=add(out,A)
 return out
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]-A[0][1]**2>=0
def frob(A):return sum(A[i][j]**2 for i in range(2) for j in range(2))
def make(eta,K,gamma):
 p=(ONE,ONE,K,ONE)
 Y=mat_sum(scale(p[i],G[i]) for i in range(4))
 B=tuple(tuple(sum(p[i]*G[i][h][k]**2 for i in range(4))/sum(G[i][h][k]**2 for i in range(4)) for k in range(2)) for h in range(2))
 raw=mat_sum(scale(p[i]*F(gamma[i],1)/eta,G[i]) for i in range(4))
 ctrl=mat_sum(scale(F(gamma[i],1)/eta,G[i]) for i in range(4))
 corr=tuple(tuple(raw[h][k]-B[h][k]*(ctrl[h][k]-I[h][k]) for k in range(2)) for h in range(2))
 return Y,B,raw,corr

checks=0
for eta in (F(1,8),F(1,4),F(1,3),F(1,2),F(3,4),F(7,8)):
 boundary=ONE+12*eta/(3-2*eta)
 tests=(ONE,F(9,8),F(3,2),F(2),F(4),F(6),F(100),boundary, (boundary+ONE)/2, boundary+F(1,100))
 for K in tests:
  samples=[]
  lower=ONE+(K-ONE)*(F(1,6)-ONE/(4*eta))
  for bits in product((0,1),repeat=4):
   Y,B,raw,corr=make(eta,K,bits)
   assert Y==(((K+3)/4,(K-1)/4),((K-1)/4,(K+3)/4));checks+=1
   assert B==((((K+5)/6),((K+1)/2)),(((K+1)/2),((K+5)/6)));checks+=1
   assert psd(sub(corr,scale(lower,I))), (eta,K,bits,corr,lower);checks+=1
   if bits==(1,1,0,1):
    assert psd(raw) and raw[0][0]*raw[1][1]-raw[0][1]**2>0;checks+=1
    assert corr[0][0]+corr[0][1] == ONE+(K-ONE)/6;checks+=1
    assert corr[0][0]-corr[0][1] == lower;checks+=1
   weight=eta**sum(bits)*(1-eta)**(4-sum(bits))
   samples.append((weight,raw,corr))
  y=Y
  assert mat_sum(scale(w,raw) for w,raw,corr in samples)==y;checks+=1
  assert mat_sum(scale(w,corr) for w,raw,corr in samples)==y;checks+=1
  rawvar=sum(w*frob(sub(raw,y)) for w,raw,corr in samples)
  corrvar=sum(w*frob(sub(corr,y)) for w,raw,corr in samples)
  assert rawvar==(1-eta)/eta*(K*K+3)/4,(eta,K,rawvar);checks+=1
  assert corrvar==(1-eta)/eta*(K-ONE)**2/6,(eta,K,corrvar);checks+=1
  assert corrvar<rawvar;checks+=1
  assert (lower>0)==(K<boundary);checks+=1
  assert (lower>=0)==(K<=boundary);checks+=1
print('PASS:',checks,'exact-rational analytic identities, PSD bounds, event spectra and variance checks')
