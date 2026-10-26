from collections import defaultdict
from fractions import Fraction

def conv(a,b):
    z=defaultdict(int)
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            z[(i+k,j+l)]+=v*w
    return dict(z)

def hc(n):
    return {(a-c,b-c):1 for a in range(n+1) for b in range(n-a+1) for c in [n-a-b]}

def weyl():
    p={(0,0):1}
    for e in [(1,-1),(-1,1),(2,1),(-2,-1),(1,2),(-1,-2)]:
       p=conv(p,{(0,0):1,e:-1})
    return p
W=weyl()

def integrate(n,p,q):
    h=hc(n); hb={(-a,-b):v for (a,b),v in h.items()}
    a={(0,0):1}
    for f in [h]*p+[hb]*q:a=conv(a,f)
    return Fraction(sum(v*a.get((-i,-j),0) for (i,j),v in W.items()),6)

for n in range(1,11):
    ms=(integrate(n,1,1),integrate(n,2,2),integrate(n,3,1),integrate(n,4,0))
    target=(1,n+1,int(n%3==0),int(n%3==0))
    assert tuple(ms)==target,(n,ms,target)
    print(n,target)
