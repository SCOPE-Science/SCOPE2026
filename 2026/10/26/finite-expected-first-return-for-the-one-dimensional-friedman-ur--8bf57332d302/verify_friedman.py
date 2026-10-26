from fractions import Fraction
from math import comb
# Distribution on positive positions conditional on no return to 0.
dist={1:Fraction(1)}
A=Fraction(1); u=Fraction(1)
for n in range(1,81):
    xmom=sum(Fraction(x)*p for x,p in dist.items())
    assert n*xmom == A, (n,A,xmom)
    assert sum(dist.values())==u
    nxt={}
    for x,v in dist.items():
        pup=Fraction(n+2-x,2*(n+1))
        assert 0<=pup<=Fraction(1,2)
        for y,q in [(x+1,pup),(x-1,1-pup)]:
            if y>0:nxt[y]=nxt.get(y,Fraction(0))+v*q
    A=A+u; u=sum(nxt.values());dist=nxt
print('80 exact-rational killed-chain/martingale/monotonicity checks passed')
print('P(T>80)=',float(u),'A_81=',float(A))
