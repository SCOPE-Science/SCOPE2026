from itertools import combinations
W=[''.join('1' if i in c else '0' for i in range(4)) for c in combinations(range(4),2)]
P=['00','01','10','11']
N=0
for u in W:
 if u[0]!='0':continue
 for v in W:
  w=[u,v]; s='0'
  for _ in range(3):s=''.join(w[int(c)] for c in s)
  if u!=v:
   for d in (1,2,3):assert {s[i]+s[i+d] for i in range(len(s)-d)}==set(P),(u,v,d)
   for r in range(4):
    S=set()
    for t in range(4):
     for a in P:
      S.add(w[int(a[0])][t]+w[int(a[1])][(t+r)%4])
    assert S==set(P),(u,v,r)
  t='0'
  for _ in range(7):t=''.join(w[int(c)] for c in t)
  for n in range(1,65):
   q,r=divmod(n,4)
   if u!=v and q>=1:
    C={2*q+w[z][:r].count('1') for z in (0,1)}
    for h in (1,2,3):
     j=h+r;delta=int(j>4);j-=4*delta
     C.update(2*(q-1+delta)+w[a][h:].count('1')+w[b][:j].count('1') for a in (0,1) for b in (0,1))
    exp=max(C)-min(C)+1
   elif u==v:
    exp=len({sum(int((u*2)[(i+j)%4]) for j in range(n)) for i in range(4)})
   else:
    C={ (w[a]+w[b])[t0:t0+n].count('1') for a in (0,1) for b in (0,1) for t0 in range(4)}
    exp=len(C)
   got=set()
   z=t[:n].count('1');got.add(z)
   for i in range(n,len(t)):
    z+=int(t[i])-int(t[i-n]);got.add(z)
   assert len(got)==exp,(u,v,n,exp,len(got))
   N+=1
print('VERIFY_OK morphisms=18 theorem_pair_base_checks=45 theorem_pair_lift_checks=60 factor_length_checks=',N)
