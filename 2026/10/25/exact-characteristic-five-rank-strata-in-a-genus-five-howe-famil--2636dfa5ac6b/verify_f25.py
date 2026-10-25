#!/usr/bin/env python3
"""Independent exhaustive arithmetic of the 25-element quadratic field; stdlib only."""
from itertools import product, combinations
# F_25 = F_5[u]/(u^2-2), with 2 a nonsquare modulo 5.
class F:
    def __init__(self, x=0, y=0): self.x=x%5; self.y=y%5
    def __add__(self,o):
        if isinstance(o,int):o=F(o)
        return F(self.x+o.x,self.y+o.y)
    __radd__=__add__
    def __neg__(self):return F(-self.x,-self.y)
    def __sub__(self,o): return self+(-o if isinstance(o,F) else -F(o))
    def __mul__(self,o):
        if isinstance(o,int):o=F(o)
        return F(self.x*o.x+2*self.y*o.y,self.x*o.y+self.y*o.x)
    __rmul__=__mul__
    def __eq__(self,o):
        if isinstance(o,int):o=F(o)
        return self.x==o.x and self.y==o.y
    def __hash__(self):return hash((self.x,self.y))
    def __repr__(self):return f'({self.x}+{self.y}u)'
    def __pow__(self,n):
        assert n>=0
        v=F(1); w=self
        while n:
            if n&1:v=v*w
            w=w*w;n//=2
        return v
points=[F(a,b) for a,b in product(range(5),repeat=2)]
rank_counts={3:0,4:0,5:0}
pair_counts={pair:0 for pair in combinations(range(5),2)}
for a,b in product(points,repeat=2):
    if a==b or a*a==4 or b*b==4:continue
    h2=2*(a+b)
    h4=a*a-a*b+b*b-1
    h8=a*a*b*b+2*(a*a+b*b)-2*a*b+1
    factors=[a*a+2,b*b+2,h4+h2,h4-h2,h8]
    zeros=tuple(i for i,v in enumerate(factors) if v==0)
    assert len(zeros)<=2,(a,b)
    rank_counts[5-len(zeros)]+=1
    if len(zeros)==2:pair_counts[zeros]+=1
assert rank_counts=={3:20,4:180,5:306},rank_counts
assert set(pair_counts.values())=={2},pair_counts
u=F(0,1)
def rank(a,b):
    h2=2*(a+b);h4=a*a-a*b+b*b-1
    h8=a*a*b*b+2*(a*a+b*b)-2*a*b+1
    return sum(c!=0 for c in (a*a+2,b*b+2,h4+h2,h4-h2,h8))
assert rank(2*u,3*u)==3
assert rank(F(0),u)==4
assert rank(F(0),F(1))==5
print('F25_VERIFY_OK: 506 valid parameters, rank spectrum',rank_counts,'two for every pair')
