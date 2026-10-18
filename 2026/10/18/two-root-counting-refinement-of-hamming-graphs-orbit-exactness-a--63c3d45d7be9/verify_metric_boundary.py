"""Independent arithmetic verification of the exact metric-pair obstruction."""
from collections import defaultdict

def profiles(q,d,t):
 for a in range(t+1):
  for b in range(t-a+1):
   c=t-a-b
   if c and q==2: continue
   for f in range(d-t+1): yield (a,b,c,f)

def main():
 cases=0;ambiguous=0
 for q in range(2,9):
  for d in range(1,28):
   for t in range(1,d+1):
    pair=defaultdict(set)
    for a,b,c,f in profiles(q,d,t):pair[(b+c+f,a+c+f)].add((a,b,c,f))
    collision=any(len(v)>1 for v in pair.values())
    assert collision==(q>=3 and 2<=t<d)
    if collision:
     # Two explicit type witnesses having distances (2,t) and different f.
     assert (t-2,0,2,0) in profiles(q,d,t)
     assert (t-1,1,0,1) in profiles(q,d,t)
     p1=(t-2,0,2,0);p2=(t-1,1,0,1)
     assert (p1[1]+p1[2]+p1[3],p1[0]+p1[2]+p1[3])==(2,t)
     assert (p2[1]+p2[2]+p2[3],p2[0]+p2[2]+p2[3])==(2,t)
     ambiguous+=1
    cases+=1
 print('METRIC_OK cases=%s nontrivial_collision_cases=%s'%(cases,ambiguous))
if __name__=='__main__':main()
