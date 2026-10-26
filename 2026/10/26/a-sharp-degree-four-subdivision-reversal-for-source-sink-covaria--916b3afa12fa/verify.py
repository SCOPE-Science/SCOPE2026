"""Independent finite enumeration for randomly oriented finite simple graphs."""
from itertools import combinations
from fractions import Fraction
from time import monotonic

def basic_formula(n,edges):
    deg=[0]*n
    for u,v in edges:
        assert 0<=u<v<n
        deg[u]+=1;deg[v]+=1
    a=[Fraction(1,2**d) if d else Fraction(0) for d in deg]
    return 2*sum((a[u]*a[v] for u,v in edges),Fraction(0))-sum((a[v]*a[v] for v in range(n)),Fraction(0))

def exact_exhaustive(n,edges):
    m=len(edges)
    incident=[0]*n;srcmask=[0]*n
    for j,(u,v) in enumerate(edges):
        b=1<<j
        incident[u]|=b;incident[v]|=b
        srcmask[u]|=b
    sums=[0,0,0]
    for orient in range(1<<m):
        S=T=0
        for v in range(n):
            inc=orient & incident[v]
            S+=int(inc==srcmask[v])
            T+=int(inc==(incident[v]^srcmask[v]))
        sums[0]+=S;sums[1]+=T;sums[2]+=S*T
    N=1<<m
    return Fraction(sums[2]*N-sums[0]*sums[1],N*N)

def subdivide(n,edges,i=None):
    new=[];j=n
    for k,(u,v) in enumerate(edges):
        if i is None or k==i:
            new.extend((tuple(sorted((u,j))), tuple(sorted((v,j)))))
            j+=1
        else:
            new.append((u,v))
    return j,sorted(new)

def degree_pair(n,edges,i):
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    u,v=edges[i]
    a=Fraction(1,2**deg[u]);b=Fraction(1,2**deg[v])
    return (deg[u],deg[v]),(a+b)/2-2*a*b-Fraction(1,16)

def K(n):return list(combinations(range(n),2))

def cycle(n):return sorted(tuple(sorted((i,(i+1)%n))) for i in range(n))

def star(d):return [(0,i) for i in range(1,d+1)]

tests=0
for n in range(2,5):
    poss=K(n)
    for mask in range(1<<len(poss)):
        ee=[e for j,e in enumerate(poss) if mask>>j&1]
        if any(all(v not in e for e in ee) for v in range(n)):
            continue
        exact=exact_exhaustive(n,ee)
        assert exact==basic_formula(n,ee),(n,ee,exact,basic_formula(n,ee))
        tests+=1
        for i in range(len(ee)):
            newn,newe=subdivide(n,ee,i)
            df=basic_formula(newn,newe)-basic_formula(n,ee)
            (d,e),expected=degree_pair(n,ee,i)
            assert df==expected,(ee,i,df,expected)
            expected_sign = -1 if ((d==1 and e==1) or (d>=4 and e>=4)) else 1
            assert (df>0)-(df<0)==expected_sign,(d,e,df)
            assert exact_exhaustive(newn,newe)==basic_formula(newn,newe)
            tests+=3
for name,n,ee in [('path5',5,cycle(5)[:-1]),('star5',6,star(5)),('K4',4,K(4)),('K5',5,K(5)),('cycle5',5,cycle(5))]:
    ex=exact_exhaustive(n,ee)
    assert ex==basic_formula(n,ee),(name,ex,basic_formula(n,ee));tests+=1
    for i in range(len(ee)):
        nn,ff=subdivide(n,ee,i)
        assert basic_formula(nn,ff)-basic_formula(n,ee)==degree_pair(n,ee,i)[1]
        tests+=1
for r in range(2,6):
    n=r+1;ee=K(n)
    actual=basic_formula(n,ee)
    assert actual==Fraction(n*(r-1),4**r)
    nn,ff=subdivide(n,ee)
    actual2=basic_formula(nn,ff)
    assert actual2==n*(Fraction(r,2**(r+1))-Fraction(1,4**r)-Fraction(r,32))
    assert (actual2>0)==(r<=3)
    tests+=3
# Most demanding independent enumeration: 2^20 orientations of the 1-subdivision of K5.
n,ee=subdivide(5,K(5))
start=monotonic()
assert exact_exhaustive(n,ee)==Fraction(-5,256)
print('subdivided K5 exact enumeration:',1<<len(ee),'orientations, seconds',round(monotonic()-start,2))
tests+=1
print('PASS',tests,'independent assertions')
