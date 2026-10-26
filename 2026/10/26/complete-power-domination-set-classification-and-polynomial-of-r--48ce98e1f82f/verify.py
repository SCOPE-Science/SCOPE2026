"""Standalone verification for power-domination classification of rook graphs.
Uses original closed-neighborhood and unique-neighbor forcing definition independently
of the proposed support criterion; exact polynomial uses independent inclusion-exclusion.
"""
from math import comb
from collections import Counter


def poly_add(A,B,s=1):
 n=max(len(A),len(B));return [ (A[i] if i<len(A) else 0)+s*(B[i] if i<len(B) else 0) for i in range(n)]

def poly_pow(base,n):
 out=[1]
 for _ in range(n):
  C=[0]*(len(out)+len(base)-1)
  for i,a in enumerate(out):
   for j,b in enumerate(base): C[i+j]+=a*b
  out=C
 return out

def E(r,c):
 # polynomial for all subsets of r*c matrix meeting every row and column
 # convention E(0,0)=1, E(0,c)=E(r,0)=0 for other cases
 if r==0 or c==0:return [1] if r==c==0 else [0]
 out=[0]*(r*c+1)
 for a in range(r+1):
  for b in range(c+1):
   s=(-1)**(r-a+c-b)*comb(r,a)*comb(c,b)
   for k in range(a*b+1):out[k]+=s*comb(a*b,k)
 return out

def theoretical_poly(p,q):
 out=[comb(p*q,k) for k in range(p*q+1)]
 for r in range(p-1):
  for c in range(q-1):
   v=E(r,c)
   mult=comb(p,r)*comb(q,c)
   for k,a in enumerate(v):out[k]-=mult*a
 return out

def direct_poly(p,q):
 n=p*q;neighbors=[]
 for i in range(p):
  for j in range(q):
   mask=0
   for ii in range(p):
    for jj in range(q):
     if (i==ii or j==jj) and (i,j)!=(ii,jj):mask|=1<<(ii*q+jj)
   neighbors.append(mask)
 rowmask=[sum(1<<(i*q+j) for j in range(q)) for i in range(p)]
 colmask=[sum(1<<(i*q+j) for i in range(p)) for j in range(q)]
 allmask=(1<<n)-1
 coeff=Counter(); checks=0; bad=0;wrong=[]
 for S in range(1<<n):
  observed=S
  for v in range(n):
   if (S>>v)&1:observed|=neighbors[v]
  while observed!=allmask:
   nextobs=observed
   for v in range(n):
    if (observed>>v)&1:
     unseen=neighbors[v]&~observed
     if unseen and (unseen&(unseen-1))==0: nextobs|=unseen
   if nextobs==observed:break
   observed=nextobs
  actual=observed==allmask
  active_rows=sum(bool(S&R) for R in rowmask)
  active_cols=sum(bool(S&C) for C in colmask)
  predicted=(active_rows>=p-1 or active_cols>=q-1)
  if actual!=predicted:wrong.append((p,q,S,actual,predicted))
  if actual:coeff[S.bit_count()]+=1
  else:bad+=1
  checks+=1
 return [coeff[i] for i in range(n+1)],checks,bad,wrong

def main():
 total=0
 boards=[(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]
 for p,q in boards:
  expected=theoretical_poly(p,q)
  got,checks,bad,wrong=direct_poly(p,q)
  assert not wrong,(p,q,wrong[:5])
  assert expected==got,(p,q,expected,got)
  minimum=next(k for k,a in enumerate(got) if a)
  claimed_min=p-1
  claimed_mult = p*q**(p-1) if p<q else 2*p*p**(p-1)-p*p*__import__('math').factorial(p-1)
  assert minimum==claimed_min,(p,q,minimum,claimed_min)
  assert got[minimum]==claimed_mult,(p,q,got[minimum],claimed_mult)
  assert not any(expected[i] for i in range(p-1))
  print(f'{p}x{q}: subsets={checks}, non_power_dom={bad}, degree={minimum}, minima={got[minimum]}, validated=YES')
  total+=checks
 print(f'TOTAL {total} subsets; direct propagation, support condition, inclusion-exclusion and minima agree')
 for p in range(2,9):
  for q in range(p,12):
   poly=theoretical_poly(p,q)
   assert poly[p-1]==(p*q**(p-1) if p<q else 2*p*p**(p-1)-p*p*__import__('math').factorial(p-1))
   assert sum(poly)==2**(p*q)-sum(comb(p,r)*comb(q,c)*sum(E(r,c)) for r in range(p-1) for c in range(q-1))
 print('symbolic-integer checks for 2<=p<=8,p<=q<=11: PASS')

if __name__=='__main__':main()
