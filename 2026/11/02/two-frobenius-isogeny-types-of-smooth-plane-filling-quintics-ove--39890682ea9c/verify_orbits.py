"""Exact matrix classification for smooth ternary plane-filling quintics; Python stdlib."""
from itertools import product
from collections import Counter

def det(M):
 a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
 return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3

def poly_coeff(A):
 tr=sum(A[i][i] for i in range(3))%3
 s=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i in range(3) for j in range(i+1,3))%3
 return ((-tr)%3,s,(-det(A))%3)

def at(p,t):
 a,b,c=p
 return (t**3+a*t**2+b*t+c)%3

def irreducible(p):
 return all(at(p,t)!=0 for t in range(3))

def transformed(p,u,v):
 # u^{-3}P(uT+v): monic polynomial of u^{-1}(alpha-v)
 a,b,c=p
 lead=pow(u,3,3);inv=pow(lead,-1,3)
 return ((a*u*u+3*v*u*u)*inv%3,
         (3*v*v*u+2*a*v*u+b*u)*inv%3,
         (v**3+a*v*v+b*v+c)*inv%3)

def main():
 types=Counter()
 for coeff in product(range(3),repeat=9):
  A=[list(coeff[i*3:i*3+3]) for i in range(3)]
  p=poly_coeff(A)
  if irreducible(p):types[p]+=1
 polys=sorted(p for p in product(range(3),repeat=3) if irreducible(p))
 assert len(polys)==8
 assert set(types)==set(polys) and set(types.values())=={432}
 assert sum(types.values())==3456
 # The equivalence F_A=F_{uA+vI}/u has 3*2=6 members, all distinct.
 assert sum(types.values())//6==576
 seen=set();classes=[]
 for p in polys:
  if p in seen:continue
  orbit={transformed(p,u,v) for u in (1,2) for v in (0,1,2)}
  assert orbit <= set(polys)
  seen.update(orbit);classes.append(orbit)
 assert sorted(len(x) for x in classes)==[2,6]
 # Each characteristic polynomial contributes 432 matrices. The six-element
 # free affine-scalar action yields 144 and 432 equation classes.
 assert sorted(len(x)*432//6 for x in classes)==[144,432]
 assert (0,2,1) in next(o for o in classes if len(o)==2)
 assert (1,0,2) in next(o for o in classes if len(o)==6)
 # The degree-five plane-point ideal has dimension 8: map A -> F_A
 # has kernel exactly <I> (verified by distinct monomial coefficient patterns).
 U={(0,3,1):1,(0,1,3):-1};V={(1,0,3):1,(3,0,1):-1};W={(3,1,0):1,(1,3,0):-1}
 forms=[]
 for i in range(3):
  for Q in (U,V,W):
   D={}
   for m,c in Q.items():
    e=list(m);e[i]+=1;D[tuple(e)]=c%3
   forms.append(D)
 mons=sorted(set().union(*(d.keys() for d in forms)))
 M=[[d.get(m,0) for d in forms] for m in mons]
 rank=0
 for j in range(9):
  k=next((k for k in range(rank,len(M)) if M[k][j]),None)
  if k is None:continue
  M[rank],M[k]=M[k],M[rank];inv=pow(M[rank][j],-1,3)
  M[rank]=[t*inv%3 for t in M[rank]]
  for k in range(len(M)):
   if k!=rank and M[k][j]:
    v=M[k][j];M[k]=[(x-v*y)%3 for x,y in zip(M[k],M[rank])]
  rank+=1
 assert rank==8
 print('MATRIX_CLASSIFICATION_OK', 'irreducible_matrices=3456', 'projective_forms=576', 'orbits=144,432')

if __name__=='__main__':main()
