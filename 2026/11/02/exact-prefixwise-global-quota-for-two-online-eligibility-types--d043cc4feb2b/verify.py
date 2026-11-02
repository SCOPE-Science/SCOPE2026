from math import gcd
cases=0
checks=0
for s in range(1,31):
 for t in range(s,31):
  for k in range(min(s,t)+1):
   pairs=[(p,(t*(s-p))//s+1) for p in range(1,k+1)]
   assert len({q for p,q in pairs})==len(pairs)
   assert all(s*t < p*t+q*s < s*t+s+t for p,q in pairs)
   for p,q in pairs:
    for r in range(s):
     for u in range(t):
      L=int(r>=p)+int(u>=q)
      P=r*t+u*s;den=s*t
      assert P//den<=L<=(P+den-1)//den,(s,t,p,q,r,u,L,P,den)
      checks+=1
   cases+=1
print('VERIFY_OK cases=',cases,'residue_checks=',checks)
