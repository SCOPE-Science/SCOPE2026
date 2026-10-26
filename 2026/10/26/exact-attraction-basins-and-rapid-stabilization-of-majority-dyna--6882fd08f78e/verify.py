from collections import Counter
from math import comb

def step(x,m):
 n=2*m+1
 old_h=x&1
 new_h=old_h
 opp=sum(((x>>(i+1))&1) != old_h for i in range(2*m))
 if opp>m:new_h=1-old_h
 y=new_h
 for j in range(m):
  aa=(x>>(2*j+1))&1
  bb=(x>>(2*j+2))&1
  na=old_h if bb==old_h else aa
  nb=old_h if aa==old_h else bb
  y |= na <<(2*j+1)
  y |= nb <<(2*j+2)
 return y

def expected(m):
 g=Counter()
 for b in range(m+1):
  c=comb(m,b)*3**(m-b)
  if 2*b<m:
   g[2*m-2*b+1]+=c
   g[2*b]+=c
  elif 2*b>m:
   g[2*m-2*b]+=c
   g[2*b+1]+=c
  else:
   g[m]+=c
   g[m+1]+=c
 return g

def fixed_total(m):
 return 2*sum(comb(m,j) for j in range(m//2+1))

def basin(m,j):
 return 3**(m-j)+3**j if 2*j<m else 3**j

def two_round_formula(m):
 return 2*sum(comb(m,b)*sum(comb(m-b,a)*2**(m-b-a) for a in range(b)) for b in range(1,(m-1)//2+1))

def run(m):
 hist=Counter(); basins=Counter(); tt=Counter()
 for x in range(1<<(2*m+1)):
  y=step(x,m)
  z=step(y,m)
  assert step(z,m)==z,(m,x,y,z)
  hist[z.bit_count()]+=1
  basins[z]+=1
  tt[0 if x==y else 1 if y==z else 2]+=1
 assert hist==expected(m),(m,hist,expected(m))
 fixed=[k for k in range(1<<(2*m+1)) if step(k,m)==k]
 assert len(fixed)==fixed_total(m)
 for x in fixed:
  h=x&1
  j=sum(1 for i in range(m) if ((x>>(2*i+1))&1)!=h)
  assert basins[x]==basin(m,j),(m,x,j,basins[x],basin(m,j))
 assert hist[0]+hist[2*m+1]==2*(3**m+1)
 assert tt[2]==two_round_formula(m)
 return {'m':m,'profiles':1<<(2*m+1),'fixed_points':len(fixed),'time_hist':dict(tt),'distribution':dict(sorted(hist.items()))}
if __name__=='__main__':
 for m in range(1,9):print(run(m))
