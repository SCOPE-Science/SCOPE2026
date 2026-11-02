from fractions import Fraction
from itertools import product
from collections import Counter

def span(t):
 s={0}
 for a in t:
  s|={x^a for x in list(s)}
 return frozenset(s)

states={frozenset([0])};change=True
while change:
 nxt={span(tuple(s)+(v,)) for s in states for v in range(1,16)}
 change=bool(nxt-states)
 states|=nxt
assert len(states)==67
win=((1,2,4,8,15),(3,5,7,10,11),(6,9,12,13,14))
trips=list(product(*win)); assert len(trips)==125
memo={frozenset(range(16)):Fraction(0)}
for s in sorted(states,key=len,reverse=True):
 if len(s)==16:continue
 transitions=Counter(span(tuple(s)+t) for t in trips)
 self_count=transitions.pop(s,0)
 assert self_count<125
 assert all(len(x)>len(s) for x in transitions)
 memo[s]=(Fraction(125)+sum(c*memo[x] for x,c in transitions.items()))/(125-self_count)
print('states',len(states),'direct_markov_E',memo[frozenset([0])],float(memo[frozenset([0])]))
assert memo[frozenset([0])]==Fraction(7491,3596)
