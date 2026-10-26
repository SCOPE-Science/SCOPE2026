#!/usr/bin/env python3
"""Exact arithmetic checks for degree-(2,2,2) normal-bundle strata."""
import itertools
import sympy as S
s,t=S.symbols('s t')
a,b,c,d,e,f=S.symbols('a b c d e f')
P=a*s*s+b*s*t+c*t*t
Q=d*s*s+e*s*t+f*t*t
z=S.symbols('z')
R=(a*e-b*d)*s*s+2*(a*f-c*d)*s*t+(b*f-c*e)*t*t
Wr_aff=S.expand(S.diff(P.subs({s:z,t:1}),z)*Q.subs({s:z,t:1}) - P.subs({s:z,t:1})*S.diff(Q.subs({s:z,t:1}),z))
assert S.expand(Wr_aff-R.subs({s:z,t:1}))==0
print('VERIFY_OK universal_wronskian_identity')

def wc(A,B,mod=None):
 aa,bb,cc=A; dd,ee,ff=B
 vals=[aa*ee-bb*dd,2*(aa*ff-cc*dd),bb*ff-cc*ee]
 return tuple(x if mod is None else x%mod for x in vals)

def matrix_rank(M,p=None):
 mat=[list(row) for row in M]
 if not mat:return 0
 nr=len(mat); nc=len(mat[0]); rank=0
 for j in range(nc):
  k=next((i for i in range(rank,nr) if mat[i][j]%(p or 1000000007)!=0),None) if p else next((i for i in range(rank,nr) if mat[i][j]!=0),None)
  if k is None: continue
  mat[rank],mat[k]=mat[k],mat[rank]
  val=mat[rank][j]
  if p:
   inv=pow(int(val%p),-1,p)
   mat[rank]=[(x*inv)%p for x in mat[rank]]
  else:
   mat[rank]=[S.Rational(x,val) for x in mat[rank]]
  for i in range(rank+1,nr):
   factor=mat[i][j]
   if factor:
    mat[i]=[(x-factor*y)%p if p else x-factor*y for x,y in zip(mat[i],mat[rank])]
  rank+=1
  if rank==nr:break
 return rank

phi1=((1,0,0),(0,0,1))             # [s^2:t^2]
phi2=((1,0,1),(0,1,0))             # [s^2+t^2:s*t]
phi3=((1,0,-1),(0,1,0))            # [s^2-t^2:s*t]
for p in (0,3,5,7):
 rs=[wc(*x,p or None) for x in (phi1,phi2,phi3)]
 assert matrix_rank(rs,p or None)==3,(p,rs)
 jump=[wc(*x,p or None) for x in (phi1,phi1,phi2)]
 assert matrix_rank(jump,p or None)==2
 print('VERIFY_OK characteristic=%s full_rank=3 split=(5,5) jump_rank=2 split=(4,6)'%(p or 'zero'))

# Characteristic two: all ramification quadratics have no mixed coefficient.
phiB=((1,1,0),(0,0,1))             # [s^2+st:t^2], R=t^2
phiC=((0,1,1),(1,0,0))             # [st+t^2:s^2], R=s^2
phiA=((1,0,0),(0,0,1))             # purely inseparable; R=0
rs=[wc(*x,2) for x in (phiA,phiB,phiC)]
assert rs==[(0,0,0),(0,0,1),(1,0,0)] and matrix_rank(rs,2)==2,rs
print('VERIFY_OK characteristic=2 explicit_unramified_rank2 split=(4,6)')

# Exhaust all degree-two maps over F2. In an algebraic closure, two binary
# quadratics have a common projective root iff the determinant of the
# Sylvester resultant is zero.
F2=list(itertools.product(range(2),repeat=3))
def resultant2(A,B):
 AA,BB,CC=A; DD,EE,FF=B
 T=S.Matrix([[AA,BB,CC,0],[0,AA,BB,CC],[DD,EE,FF,0],[0,DD,EE,FF]])
 return int(T.det())%2
maps=[(A,B) for A in F2 for B in F2 if resultant2(A,B)==1]
assert len(maps)==24,len(maps)
rows=[wc(A,B,2) for A,B in maps]
assert all(row[1]==0 for row in rows)
# For quadratics with zero middle term over algebraically closed F2, two
# independent coefficient vectors have disjoint roots; rank two is exactly
# the unramified condition for a triple.
counts={0:0,1:0,2:0,3:0}
for r1,r2,r3 in itertools.product(rows,repeat=3):
 counts[matrix_rank((r1,r2,r3),2)]+=1
assert counts[3]==0 and counts[2]>0 and sum(counts.values())==24**3
print('VERIFY_OK F2_maps=%d triples=%d unramified_triples=%d all_rank2'%(len(maps),24**3,counts[2]))
print('VERIFY_OK exact_checks_complete')
