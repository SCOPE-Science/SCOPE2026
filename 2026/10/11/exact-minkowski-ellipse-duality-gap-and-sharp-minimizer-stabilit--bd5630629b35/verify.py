from fractions import Fraction as Q
from itertools import product
from random import Random
rng=Random(230087)
checks=0

def l1(x): return sum(abs(t) for t in x)
def li(x): return max(abs(t) for t in x)
def chord(x,y,norm):
    return (norm([a+b for a,b in zip(x,y)])+norm([a-b for a,b in zip(x,y)]))/2
for n in range(2,7):
    axis=[]
    for i in range(n):
        for sign in (-1,1):
            v=[Q(0)]*n; v[i]=Q(sign); axis.append(v)
    corners=[tuple(Q(s) for s in eps) for eps in product((-1,1),repeat=n)]
    U=list(product((-Q(1,n),Q(1,n)),repeat=n))
    E=axis
    for k in range(130):
        raw=[Q(rng.randrange(-12,13)) for _ in range(n)]
        if not any(raw):raw[0]=Q(1)
        x=[v/l1(raw) for v in raw]
        z=[v/li(raw) for v in raw]
        m=min(abs(v) for v in x)
        f1=max(chord(x,y,l1) for y in axis)
        assert f1==2-m
        a=sorted((abs(v) for v in z),reverse=True)
        fi=max(chord(z,y,li) for y in corners)
        assert fi==1+(a[0]+a[1])/2
        d1=min(l1([v-u for v,u in zip(x,p)]) for p in U)
        deficit=Q(1,n)-m
        assert 2*deficit<=d1<=2*(n-1)*deficit
        di=min(li([v-u for v,u in zip(z,p)]) for p in E)
        assert di==a[1]==2*(fi-Q(3,2))
        checks+=1
    for d in [Q(0),Q(1,4*n),Q(1,2*n),Q(1,n)]:
        m=Q(1,n)-d
        low=[m]+[(1-m)/(n-1)]*(n-1)
        high=[1-(n-1)*m]+[m]*(n-1)
        assert l1(low)==l1(high)==1
        assert min(low)==min(high)==m
        distlow=sum(abs(v-Q(1,n)) for v in low)
        disthigh=sum(abs(v-Q(1,n)) for v in high)
        assert distlow==2*d and disthigh==2*(n-1)*d
        checks+=1
    assert (2-Q(1,n))-Q(3,2)==Q(1,2)-Q(1,n)
    assert chord([Q(1)]+[Q(0)]*(n-1), [Q(0),Q(1)]+[Q(0)]*(n-2),l1)==2
    assert chord([Q(1),Q(1)]+[Q(0)]*(n-2), [Q(1),-Q(1)]+[Q(0)]*(n-2),li)==2
print(f'VERIFY_OK dimensions=2..6 exact_rational_profiles={checks} sharp_stability=both_families duality_gap=half_minus_inverse_dimension')
