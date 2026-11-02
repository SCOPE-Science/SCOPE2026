from itertools import product
from functools import lru_cache
from time import perf_counter

def rel(x,y):
 if x==y:return 0
 if x & ~y==0:return 1
 if y & ~x==0:return 2
 return 3
@lru_cache(None)
def mask_from_cells(a,b,c,d):
 # x = common+a b; y=common+a c; third z membership split by 4 disjoint regions
 # classify x⊆z, z⊆x etc by counts of included in 4 regions
 sizes=(a,b,c,d)
 mask=0;n=sum(sizes)
 for zz in product(*(range(v+1) for v in sizes)):
  cnt=sum(zz)
  if not (0<cnt<n):continue
  xlen=a+b;ylen=a+c;zlen=cnt
  # intersection x,z = included common and b cells
  ax=zz[0]+zz[1];ay=zz[0]+zz[2]
  def rho(len1,len2,common):
   if len1==len2==common:return 0
   if common==len1:return 1
   if common==len2:return 2
   return 3
  rx=rho(xlen,zlen,ax);ry=rho(ylen,zlen,ay)
  mask |= 1 << (4*rx+ry)
 return mask

def h(n):
 groups=[]
 for i in range(1,n):
  U=set()
  for j in range(1,n):
   for a in range(max(0,i+j-n), min(i,j)+1):
    b=i-a;c=j-a;d=n-i-j+a
    r=0 if i==j==a else 1 if i==a else 2 if j==a else 3
    U.add((r,mask_from_cells(a,b,c,d)))
  groups.append(frozenset(U))
 return frozenset(groups)
def main():
    signatures={}
    for n in range(2,17):
        t=h(n)
        match=[m for m,x in signatures.items() if x==t]
        if n<=8: assert not match,(n,match)
        if n>8: assert 8 in match,(n,match)
        signatures[n]=t
        print('n=%d pointed=%d class=%d' % (n,len(t),min([n]+match)))
    assert len(set(signatures.values())) == 7
    print('EXHAUSTIVE_VENN_SPECTRA: 2..16; seven classes; n>=8 stable in checked range; PASS')

if __name__=='__main__': main()
