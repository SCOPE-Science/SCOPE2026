#!/usr/bin/env python3
"""Reproducible exact finite-field checks for 600-cell harmonic sampling.
Uses standard library only. Numerical field specialization is supplementary to the
representation-theoretic proof; a rank match in a finite field is not by itself a
characteristic-zero proof.
"""
from itertools import product, permutations

DIM=(1,2,3,4,5,6,4,2,3)
LABEL=('1','2','3','4','5','6','4b','2b','3b')
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
ADJ=[[0]*9 for _ in range(9)]
for a,b in EDGES: ADJ[a][b]=ADJ[b][a]=1
assert all(sum(ADJ[i][j]*DIM[j] for j in range(9))==2*DIM[i] for i in range(9))
V=[[1]+[0]*8,[0,1]+[0]*7]
for n in range(2,121):
 r=[sum(ADJ[i][j]*V[-1][j] for j in range(9))-V[-2][i] for i in range(9)]
 assert min(r)>=0 and sum(a*b for a,b in zip(DIM,r))==n+1,(n,r)
 V.append(r)
RANK=[sum(DIM[i]**2 for i in range(9) if V[n][i]) for n in range(121)]
assert RANK[6]==25 and RANK[13]==60 and RANK[15]==52
assert RANK[27]==56 and RANK[29]==60 and RANK[58]==59 and RANK[59]==60 and RANK[60]==60
assert all(RANK[n]==60 for n in range(60,121))
assert all(RANK[n]==60 for n in range(29,121,2))
assert any(RANK[n]!=60 for n in range(0,60,2)) and RANK[58]==59
PARITY=[0,1,0,1,0,1,0,1,0]
for n in range(61):
 assert all(V[n+60][i]-V[n][i] == (DIM[i] if PARITY[i]==n%2 else 0) for i in range(9))

# Exact finite-field realization, with a square root of 5 mod 101.
P=101
root5=next(x for x in range(P) if (x*x-5)%P==0)
phi=((1+root5)*pow(2,-1,P))%P
invphi=((root5-1)*pow(2,-1,P))%P
H=pow(2,-1,P)
base=[0,H,(phi*H)%P,(invphi*H)%P]
pts=[]
for i in range(4):
 for sign in (1,-1):
  a=[0]*4;a[i]=sign%P;pts.append(tuple(a))
for ss in product((1,-1),repeat=4): pts.append(tuple((H*s)%P for s in ss))
def even(t):return sum(t[i]>t[j] for i in range(4) for j in range(i+1,4))%2==0
for perm in permutations(range(4)):
 if not even(perm):continue
 a=[base[i] for i in perm]
 loc=[j for j in range(4) if a[j]]
 for ss in product((1,-1),repeat=3):
  z=a.copy()
  for j,s in zip(loc,ss):z[j]=(z[j]*s)%P
  pts.append(tuple(z))
assert len(pts)==len(set(pts))==120
assert all(sum(x*x for x in p)%P==1 for p in pts)
T=[[sum(a*b for a,b in zip(x,y))%P for y in pts] for x in pts]
angles={1%P,(-1)%P,0,H,(-H)%P,phi*H%P,(-phi*H)%P,invphi*H%P,(-invphi*H)%P}
assert len(angles)==9 and set(T[0])==angles
# 1,1,30,20,20,12,12,12,12 is the 600-cell distance distribution.
assert sorted([T[0].count(t) for t in angles])==[1,1,12,12,12,12,20,20,30]

def rank_mod(a):
 a=[row[:] for row in a]
 rank=0;N=len(a);M=len(a[0])
 for j in range(M):
  piv=next((i for i in range(rank,N) if a[i][j]),None)
  if piv is None:continue
  a[rank],a[piv]=a[piv],a[rank]
  rr=a[rank];inv=pow(rr[j],-1,P)
  for k in range(j,M):rr[k]=rr[k]*inv%P
  for i in range(rank+1,N):
   cc=a[i][j]
   if cc:
    row=a[i]
    for k in range(j,M):row[k]=(row[k]-cc*rr[k])%P
  rank+=1
  if rank==N:break
 return rank

u0=[[1]*120 for _ in range(120)]
u1=[[(2*t)%P for t in row] for row in T]
checks=[]
for n in range(61):
 if n==0:M=u0
 elif n==1:M=u1
 else:
  m=[[(2*T[i][j]*u1[i][j]-u0[i][j])%P for j in range(120)] for i in range(120)]
  u0,u1=u1,m;M=m
 r=rank_mod(M)
 checks.append(r)
 assert r==RANK[n],(n,r,RANK[n])
print('EXACT_FINITE_FIELD_GRAM_RANKS_PASS: all n=0..60, p=101, sqrt5=',root5)
print('MCKAY_MULTIPLICITIES_PASS: n=0..120; periodic shift n=0..60')
print('RANKS_0_59:',','.join(map(str,checks[:60])))
print('FULL_ODD_FROM_29_AND_FULL_BOTH_FROM_60_PASS')
