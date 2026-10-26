from itertools import combinations, product

def projective(n,q):
    return sum(q**j for j in range(n+1)) if n>=0 else 0

def gaussian(n,k,q):
    if k<0 or k>n: return 0
    num=den=1
    for j in range(k): num*=q**(n-j)-1;den*=q**(k-j)-1
    assert num%den==0
    return num//den

def strata(d,r,q):
    assert d>=1 and 1<=r<=3 and q>=2
    semisimple=gaussian(2*d,3,q)
    h=q**(3*d)-(q+1)*q**d+q
    assert h%(q-1)==0
    rank2=q**(2*d-2)*(h//(q-1))
    rank1=(q+1)*q**(2*d-2)*projective(d-1,q)*projective(2*d-2,q)
    uniserial=r*q**(3*d-1)*projective(d-1,q)
    return semisimple,rank2,rank1,uniserial

for q in (2,3,5,7):
 for r in (1,2,3):
  assert sum(strata(1,r,q))==1+q+(r+1)*q*q
for q in (2,3,5):
 for d in range(1,8):
  for r in (1,2,3):
   assert all(v>=0 for v in strata(d,r,q))
assert strata(2,3,2)==(15,216,252,288)

# Completely independent length-three-submodule enumeration for rank one in char. 2.
# R=F_2[[x,y]]/(xy(x+y)) mod m^4; basis x,y,x^2,xy,y^2,x^3,x^2y,y^3.
xb={0:2,1:3,2:5,3:6,4:6};yb={0:3,1:4,2:6,3:6,4:7}
def mul(v,mp):
 out=0
 while v:
  j=(v&-v).bit_length()-1;v&=v-1
  if j in mp:out^=1<<mp[j]
 return out
def contains(v,rows,pivs):
 for rr,p in zip(rows,pivs):
  if v>>p&1:v^=rr
 return v==0
count=0
for pivs in combinations(range(8),5):
 nonpivs=[[j for j in range(p+1,8) if j not in pivs] for p in pivs]
 for choices in product(*[range(1<<len(x)) for x in nonpivs]):
  rows=[]
  for p,indices,c in zip(pivs,nonpivs,choices):
   v=1<<p
   for j,i in enumerate(indices):
    if c>>j&1:v|=1<<i
   rows.append(v)
  if all(contains(mul(v,xb),rows,pivs) and contains(mul(v,yb),rows,pivs) for v in rows):count+=1
assert count==19
print('VERIFY_OK',strata(2,3,2),'rank-one count',count)
