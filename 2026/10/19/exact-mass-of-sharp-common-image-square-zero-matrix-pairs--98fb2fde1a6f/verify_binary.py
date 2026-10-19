from itertools import product

def mul(a,b):
 c=[]
 for ai in a:
  t=0
  for j in range(4):
   if (ai>>j)&1:t^=b[j]
  c.append(t)
 return tuple(c)

def rank(rows):
 v=list(rows);r=0
 for j in range(4):
  z=next((k for k in range(r,4) if (v[k]>>j)&1),None)
  if z is None:continue
  v[z],v[r]=v[r],v[z]
  for k in range(4):
   if k!=r and ((v[k]>>j)&1):v[k]^=v[r]
  r+=1
 return r

def im_1(a):
 for j in range(4):
  t=sum((((a[i]>>j)&1)<<i) for i in range(4))
  if t:return t
 return 0

if __name__=='__main__':
 mats=[tuple((x>>(4*i))&15 for i in range(4)) for x in range(1<<16)]
 z=[x for x in mats if mul(x,x)==(0,0,0,0) and rank(x)==2]
 print('squarezero_rank2',len(z))
 c=0
 for a in z:
  for b in z:
   ab=mul(a,b);ba=mul(b,a)
   if rank(ab)==rank(ba)==1 and im_1(ab)==im_1(ba):c+=1
 print('extremal_pairs',c)
 print('expected',2520)
 assert c==2520
