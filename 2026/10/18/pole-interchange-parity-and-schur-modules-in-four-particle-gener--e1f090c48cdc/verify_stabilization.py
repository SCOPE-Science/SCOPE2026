import sys
sys.path.insert(0,'/mnt/data')
from verify import monomials, rows, add, rank_sparse
from itertools import combinations,permutations
from math import comb

def parity(p):
 return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

for k in (3,4,5,6):
 from itertools import combinations_with_replacement
 mon3=monomials(k,1); idx3={t:i for i,t in enumerate(mon3)}
 mon4=monomials(k,2); idx4={t:i for i,t in enumerate(mon4)}
 src3=rows(k,3); src4=rows(k,4)
 ncols=[]
 for tri in combinations(range(1,k),3):
  generator={}
  for z in permutations(range(3)):
   i,j,c=(tri[z[0]],tri[z[1]],tri[z[2]])
   sign=parity(z)
   for e,s in ((c,1),(0,-1)):
    ex=tuple(int(v==e) for v in range(k))
    col=(i-1)*(k-1)*len(mon3)+(j-1)*len(mon3)+idx3[ex]
    generator[col]=generator.get(col,0)+sign*s
  dz={}
  for z in permutations(range(3)):
   i,j,c=(tri[z[0]],tri[z[1]],tri[z[2]])
   sign=parity(z)
   for e,s in ((c,1),(0,-1)):
    ex=tuple(int(v==e) for v in range(k))
    dz=add(dz,src3[(i,j,ex)],sign*s)
  assert not dz,(k,tri,dz)
  for e in range(k):
   v4={}
   for col,coeff in generator.items():
    a=col//((k-1)*len(mon3))+1
    b=(col//len(mon3))%(k-1)+1
    t=mon3[col%len(mon3)]
    t4=tuple(t[q]+int(q==e) for q in range(k))
    col4=(a-1)*(k-1)*len(mon4)+(b-1)*len(mon4)+idx4[t4]
    v4[col4]=v4.get(col4,0)+coeff
   ncols.append({c:x for c,x in v4.items() if x})
 m=k-1
 wanted=(comb(m,3) if m>=3 else 0)+(m*(m+1)*(m-1)*(m-2)//8 if m>=3 else 0)
 r=rank_sparse(ncols)
 print('k',k,'stabilized_image_rank',r,'pole_plus',wanted)
 assert r==wanted
print('STABILIZATION_VERIFY_OK')
