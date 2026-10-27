import itertools,math
from fractions import Fraction as F
for n in range(2,7):
  N=2*n
  for b in range(1,N):
    good=0; badstates=[]
    for reds in itertools.combinations(range(N),b):
      red=set(reds); k=len(red&set(range(n))); h=b-k
      stablepred=(b!=n or k in (n//2,(n+1)//2))
      bad=False
      def v(u,RR):
        opposite = (range(n,N) if u<n else range(n))
        same=sum((w in RR)==(u in RR) for w in opposite)
        # prefer balanced within open neighbors, payoff 1 - 2*abs(frac-1/2)
        return -abs(2*same-n)
      for a in red:
        for c in range(N):
          if c in red: continue
          new=(red-{a})|{c}
          if v(c,new)>v(a,red) and v(a,new)>v(c,red):bad=True; break
        if bad:break
      if not bad:good+=1
      if (not bad)!=stablepred:badstates.append((reds,k,h))
    expected=(math.comb(N,b) if b!=n else sum(math.comb(n,k)**2 for k in set((n//2,(n+1)//2))))
    print('n',n,'b',b,'count',good,'formula',expected,'exceptions',badstates[:2]); assert not badstates and good==expected
