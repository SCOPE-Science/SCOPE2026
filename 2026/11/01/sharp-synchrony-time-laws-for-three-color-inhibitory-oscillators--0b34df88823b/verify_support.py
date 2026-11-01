"""Exact 49-mask certificate for the three-state inhibitory oscillator on K_m join I_n."""
from collections import Counter
from itertools import product

# The mask uses bit 1<<c to indicate that color c is present.
# Masks 1..7 are all nonempty supports. Equal colors in one graph part
# have identical futures, so one representative per occupied color is exact.
EXPECTED_ROWS = (
    ('0','2','2','3','6','6','6'),
    ('2','0','5','1','5','1','5'),
    ('2','2','2','2','2','2','2'),
    ('3','1','5','0','3','4','*'),
    ('3','2','2','3','3','6','6'),
    ('2','1','5','1','5','1','5'),
    ('2','2','2','2','2','2','2'),
)

def step(x,m):
    """Vertex-level rule, not a transition lookup table."""
    y = []
    for i,c in enumerate(x):
        sees = any(x[j]==1 and (i<m or j<m) and j!=i
                   for j in range(len(x)))
        y.append(c if c==2 and sees else (c+1)%3)
    return tuple(y)

def classify(a,b):
    left=tuple(c for c in range(3) if a&(1<<c))
    right=tuple(c for c in range(3) if b&(1<<c))
    x=left+right
    for t in range(7):
        if len(set(x))==1:
            return str(t)
        x=step(x,len(left))
    # Any genuinely nonsynchronizing configuration has to be periodic
    # with period 3 already at time 0. The test below is independent
    # from the asserted unique exceptional mask pair.
    x=left+right
    x1=step(x,len(left))
    x2=step(x1,len(left))
    x3=step(x2,len(left))
    if x3!=x or len(set(x))==1:
        raise AssertionError(('unexpected recurrent class',a,b,x,x3))
    return '*'

poly=Counter()
for a,b in product(range(1,8), repeat=2):
    tag=classify(a,b)
    assert tag==EXPECTED_ROWS[a-1][b-1],(a,b,tag)
    # A monomial u^p v^q U^r V^s represents the exact number of
    # labeled colorings realizing the two support masks.
    dims = [0,0,0,0]
    for mask,offset in ((a,0),(b,2)):
        size=mask.bit_count()
        if size>1: dims[offset+size-2]=1
    poly[(tag,tuple(dims))]+=1

# Grouping the 49 masks gives the following formal polynomial identities.
U=(0,0,1,0);V=(0,0,0,1);u=(1,0,0,0);v=(0,1,0,0)
def sum_exp(*vec):return tuple(sum(p[i] for p in vec) for i in range(4))
def terms(d):return Counter({(tag,ex):coef for tag,coeff in d.items() for ex,coef in coeff.items()})
expected=terms({
 '0':{(0,0,0,0):3},
 '1':{(0,0,1,0):1,(1,0,1,0):1,(0,0,0,0):2,u:2},
 '2':{sum_exp(u,U):4,sum_exp(v,U):3,U:1,sum_exp(u,V):1,sum_exp(v,V):1,u:5,v:3,(0,0,0,0):2},
 '3':{(0,0,1,0):1,(1,0,1,0):1,(0,0,0,0):2,u:2},
 '4':{U:1},
 '5':{sum_exp(u,U):2,U:3,sum_exp(u,V):1,V:1},
 '6':{sum_exp(u,U):1,U:2,sum_exp(u,V):1,V:1},
 '*':{V:1},
})
assert poly==expected,(poly-expected,expected-poly)
# Besides the sole nonsynchronous mask, each other support synchronizes
# in at most six steps, so all eventual periodic orbits are length three.
assert classify(4,7)=='*'
assert sum(1 for a,b in product(range(1,8),repeat=2) if classify(a,b)=='*')==1

for m in range(1,7):
 for n in range(1,7):
    small=2**m-2
    large=3**m-3*2**m+3
    left=2**n-2
    right=3**n-3*2**n+3
    counts=Counter()
    for (tag,(p,q,r,s)),coef in poly.items():
       counts[tag]+=coef*small**p*large**q*left**r*right**s
    assert sum(counts.values())==3**(m+n),(m,n,counts)
    assert counts['*']==right
    assert counts['2']==3**n*(small+large)+2**n*(small+1)
    assert counts['1']==counts['3']==2**n*(small+1)
    assert counts['4']==2**n-2
    assert counts['5']==small*(3**n-2**n-1)+3**n-3
    assert counts['6']==small*(3**n-2**(n+1)+1)+3**n-2**n-1
    assert counts['0']==3
print('MASK_CERTIFICATE_OK: all 49 support pairs; exact formal polynomial identities; dimensions 1..6')
for row in EXPECTED_ROWS:print(' '.join(row))
