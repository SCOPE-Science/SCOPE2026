"""Exact finite-group census for genus-two epimorphisms and SU(2)-classes.

Only the Python standard library is required.  Binary octahedral units are
represented in exact Z[sqrt(2)] quaternion coordinates.  Binary icosahedral
is represented by the abstract group SL(2,F5), whose faithful binary
icosahedral realisation in SU(2) is classical.
"""

import itertools, collections
from fractions import Fraction

def build_sl25():
  arr=[(a,b,c,d) for a,b,c,d in itertools.product(range(5),repeat=4) if (a*d-b*c)%5==1]
  idx={x:i for i,x in enumerate(arr)}
  def m(x,y):
    a,b,c,d=x; e,f,g,h=y
    return ((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
  mult=[[idx[m(x,y)] for y in arr] for x in arr]
  return arr,mult,idx[(1,0,0,1)],idx[(4,0,0,4)]

def build_bin_oct():
  E=[]
  # coordinates are (a+b sqrt2)/2, represented by 4 pairs.
  for i in range(4):
    for s in [-1,1]:
      v=[(0,0)]*4;v[i]=(2*s,0);E.append(tuple(v))
  for signs in itertools.product([-1,1],repeat=4):
    E.append(tuple((s,0) for s in signs))
  for i,j in itertools.combinations(range(4),2):
    for si,sj in itertools.product([-1,1], repeat=2):
      v=[(0,0)]*4;v[i]=(0,si);v[j]=(0,sj);E.append(tuple(v))
  assert len(E)==48 and len(set(E))==48
  idx={v:i for i,v in enumerate(E)}
  def mul(x,y):
    def qm(q,r):
      a,b=q;c,d=r
      return (a*c+2*b*d,a*d+b*c)
    def plus(*vs):
      sums=tuple(map(sum,zip(*vs)))
      assert all(t%2==0 for t in sums)
      return tuple(t//2 for t in sums)
    def neg(q):return -q[0],-q[1]
    w,x1,y1,z1=x; t,u,v,z2=y
    return (plus(qm(w,t),neg(qm(x1,u)),neg(qm(y1,v)),neg(qm(z1,z2))),
            plus(qm(w,u),qm(x1,t),qm(y1,z2),neg(qm(z1,v))),
            plus(qm(w,v),neg(qm(x1,z2)),qm(y1,t),qm(z1,u)),
            plus(qm(w,z2),qm(x1,v),neg(qm(y1,u)),qm(z1,t)))
  mult=[[idx[mul(x,y)] for y in E] for x in E]
  return E,mult,idx[((2,0),(0,0),(0,0),(0,0))],idx[((-2,0),(0,0),(0,0),(0,0))]

def enumerate_subgroups(M,one):
 n=len(M)
 def closure(gens):
   gens=tuple(gens)
   obs={one}; stack=[one]
   while stack:
     h=stack.pop()
     for g in gens:
       k=M[h][g]
       if k not in obs:obs.add(k);stack.append(k)
   return obs
 stack=[(frozenset([one]),())]; allsub={stack[0][0]:()}
 for H,gens in stack:
   for g in range(n):
     if g in H:continue
     K=frozenset(closure(gens+(g,)))
     if K not in allsub:
       allsub[K]=gens+(g,);stack.append((K,gens+(g,)))
 assert frozenset(range(n)) in allsub
 return sorted(allsub, key=lambda s:(len(s),tuple(sorted(s))))

def census(M,one,minus):
 n=len(M)
 assert all(M[one][i]==i and M[i][one]==i for i in range(n))
 inv=[next(j for j in range(n) if M[i][j]==one and M[j][i]==one) for i in range(n)]
 assert all(M[minus][i]==M[i][minus] and M[minus][minus]==one for i in range(n))
 S=enumerate_subgroups(M,one)
 hcount={}; epi={}; cc=[]
 for H in S:
   counter=collections.Counter()
   for a in H:
    for b in H:
     c=M[M[M[a][b]][inv[a]]][inv[b]]
     assert c in H
     counter[c]+=1
   num=sum(counter[z]*counter[inv[z]] for z in H)
   hcount[H]=num
   epi[H]=num-sum(v for K,v in epi.items() if K < H)
 assert all(v>=0 for v in epi.values())
 target=frozenset(range(n))
 s=epi[target]
 print('group_order',n,'genus2_hom',hcount[target],'genus2_epi',s,'bundle_classes',s//(n//2))
 print('subgroup orders',dict(sorted(collections.Counter(map(len,S)).items())))
 mobius={}
 for H in reversed(S):
   mobius[H]=1 if H==target else -sum(m for K,m in mobius.items() if H < K)
 assert sum(mobius[H]*hcount[H] for H in S)==s
 contrib=collections.Counter()
 for H in S: contrib[len(H)]+=mobius[H]*hcount[H]
 print('subgroup_mobius_contributions',dict(sorted(contrib.items())))
 return S,hcount,epi


if __name__=='__main__':
 for builder,expected,dimensions in [
   (build_bin_oct,(48,35,335616,207360,8640),(1,1,2,2,2,3,3,4)),
   (build_sl25,(120,76,3309120,2764800,46080),(1,2,2,3,3,4,4,5,6))]:
   els,M,one,minus=builder()
   n=len(els)
   center={j for j in range(n) if all(M[j][i]==M[i][j] for i in range(n))}
   assert center=={one,minus}
   assert sum(d*d for d in dimensions)==n
   S,h,e=census(M,one,minus)
   G=frozenset(range(n))
   assert (n,len(S),h[G],e[G],e[G]//(n//2))==expected
   frobenius=n**3*sum((Fraction(1,d*d) for d in dimensions),Fraction(0))
   assert frobenius==h[G]
   print('frobenius_hom_confirmed',frobenius)
 print('VERIFY_OK two_exact_finite_group_models_subgroup_mobius_frobenius_genus2_bundle_counts')
