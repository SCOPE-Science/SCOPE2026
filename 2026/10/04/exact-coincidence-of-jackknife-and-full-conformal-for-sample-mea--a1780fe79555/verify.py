from fractions import Fraction as F
from math import floor

def ceil_frac(x):
    return -((-x.numerator)//x.denominator)

def q_indices(n,a):
    j=(a*(n+1)).numerator//(a*(n+1)).denominator
    k=ceil_frac((1-a)*(n+1))
    return j,k

def endpoints(ys,a):
    ys=list(map(F,ys)); n=len(ys); mu=sum(ys,F(0))/n
    c=F(n+1,n-1)
    lows=[]; ups=[]
    for y in ys:
        d=y-mu
        lo=mu+min(d,-c*d)
        up=mu+max(d,-c*d)
        lows.append(lo); ups.append(up)
        # direct LOO check
        muminus=(sum(ys)-y)/(n-1)
        r=abs(y-muminus)
        assert muminus-r==lo and muminus+r==up
    j,k=q_indices(n,a)
    lo=None if j==0 else sorted(lows)[j-1]
    up=None if k==n+1 else sorted(ups)[k-1]
    return lo,up,lows,ups,j,k

def conf_member(ys,a,y):
    ys=list(map(F,ys)); y=F(y); n=len(ys)
    _,k=q_indices(n,a)
    if k==n+1: return True
    mu=(sum(ys)+y)/(n+1)
    rt=abs(y-mu)
    rr=sorted(abs(z-mu) for z in ys)
    return rt<=rr[k-1]

def jp_member(ys,a,y):
    lo,up,*_=endpoints(ys,a)
    y=F(y)
    return (lo is None or y>=lo) and (up is None or y<=up)

def check_sample(ys,a):
    lo,up,lows,ups,j,k=endpoints(ys,a)
    pts=sorted(set(lows+ups))
    tests=[]
    if pts:
        tests += [pts[0]-7, pts[-1]+7]
        tests += pts
        tests += [(x+y)/2 for x,y in zip(pts,pts[1:])]
    for y in tests:
        assert conf_member(ys,a,y)==jp_member(ys,a,y),(ys,a,y,lo,up,j,k)
    assert n_minus_k_plus_1(len(ys),k)==j
    if j:
        assert k==len(ys)-j+1
        assert up==sorted(ups)[len(ys)-j]

def n_minus_k_plus_1(n,k): return n-k+1

samples=[
    ([0,1,4,10],F(1,5)),
    ([0,1,4,10],F(2,5)),
    ([-7,-2,3,11,19],F(1,10)),
    ([-7,-2,3,11,19],F(1,3)),
    ([F(-5,2),F(1,3),F(7,4),F(9,2),F(13,2),F(12)],F(2,7)),
]
for ys,a in samples: check_sample(ys,a)

# Edge quantile case: alpha < 1/(n+1) gives the whole real line for both methods.
ys=[0,2,7,11]
a=F(1,10)
lo,up,*_=endpoints(ys,a)
assert lo is None and up is None
for y in [-100,0,100]: assert conf_member(ys,a,y) and jp_member(ys,a,y)

# Exact rank-coverage check on one generic exchangeable orbit with distinct augmented residuals.
vals=list(map(F,[0,1,4,10,23]))
a=F(2,5); n=4
j,k=q_indices(n,a)
mu=sum(vals,F(0))/5
assert len({abs(v-mu) for v in vals})==5
covered=0
for t in range(5):
    test=vals[t]; train=vals[:t]+vals[t+1:]
    covered += int(jp_member(train,a,test))
assert covered==k==3
assert F(covered,5)==F(k,n+1)

# Symbolic factorization check on a grid of exact rationals.
for n in range(2,9):
    c=F(n+1,n-1)
    for d in map(F,[-5,-2,-1,1,3,7]):
        for x in map(F,[-11,-4,-1,0,2,5,13]):
            lhs=((n+1)*d-x)**2-(n*x)**2
            rhs=(n+1)*(n-1)*(d-x)*(x+c*d)
            assert lhs==rhs

print('VERIFY_OK')
