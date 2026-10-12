from fractions import Fraction as F
from collections import defaultdict

def norm(xs):
 d=defaultdict(F)
 for x,p in xs:d[F(x)]+=F(p)
 d={k:v for k,v in d.items() if v}
 assert sum(d.values())==1
 return d

def avg(d):return sum(x*p for x,p in d.items())
def call(d,t):return sum(max(x-t,0)*p for x,p in d.items())
def put(d,t):return sum(max(t-x,0)*p for x,p in d.items())
def mix(d,e,h):
 z=defaultdict(F)
 for x,p in d.items():z[x]+=(1-h)*p
 for x,p in e.items():z[x]+=h*p
 return norm(z.items())
def cpress(d,m,delta):return norm([(m+(1-delta)*(x-m),p) for x,p in d.items()])
def upper(m):return norm([(m/2,1-m/(2-m)),(F(1),m/(2-m))])
def lower(m):return norm([(F(0),(1-m)/(1+m)),((1+m)/2,2*m/(1+m))])

for m in [F(1,100),F(1,7),F(1,2),F(3,4),F(99,100)]:
 h=F(1,10);d=F(1,10); H=cpress(norm([(m,1)]),m,d)
 U=mix(H,upper(m),h); L=mix(H,lower(m),h)
 assert avg(U)==avg(L)==m
 tl=min(U)/2
 th=(max(L)+1)/2
 assert call(U,tl)<call(L,tl)
 assert call(U,th)>call(L,th)
 assert put(U,tl)==0 and put(L,tl)>0
 assert call(L,th)==0 and call(U,th)>0

m=F(1,2)
H=norm([(m,1)])
U=mix(H,upper(m),F(1,10))
L=mix(H,lower(m),F(1,10))
low=call(U,F(1,8))-call(L,F(1,8))
high=call(U,F(7,8))-call(L,F(7,8))
assert low==-F(1,240),(low,high)
assert high==F(1,240),(low,high)

# Distinct ordered initial pair, modified at exact equal mean:
B=norm([(F(0),F(1,2)),(F(1),F(1,2))]);Dir=H
E=mix(Dir,B,F(1,100))
G=cpress(B,m,F(1,100))
assert avg(E)==avg(G)==m
assert call(E,m)<call(G,m)
assert call(E,F(399,400))>call(G,F(399,400))
print('VERIFY_OK mean=1/2 low_gap=-1/240 high_gap=1/240 smooth_margin_positive=true')
