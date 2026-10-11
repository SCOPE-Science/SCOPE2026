"""Standalone exact checks for the eight-mode cubic Fourier-aperture theorem.

Run: python3 checker.py. No nonstandard dependencies.
The continuum bound follows from the proof, not these finite checks.
"""
from collections import defaultdict
from itertools import product

CUBE = list(product((0, 1), repeat=3))
ZERO = (0, 0, 0, 0)
UNIT = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

def add(a, b):
    c = defaultdict(int, a)
    for k, v in b.items():
        c[k] += v
    return {k:v for k,v in c.items() if v}

def mon(e, scale=1):
    return {tuple(e):scale}

def mul(a,b):
    d = defaultdict(int)
    for k,x in a.items():
        for l,y in b.items():
            d[tuple(k[i]+l[i] for i in range(4))] += x*y
    return {k:v for k,v in d.items() if v}

def star(a):
    return {tuple(-x for x in k):v for k,v in a.items()}

def scal(a, x):
    return {k:v*x for k,v in a.items() if v*x}

def total(items):
    ans = {}
    for i in items: ans = add(ans,i)
    return ans

COEFF = {
    (0,0,0):mon(ZERO),
    (1,0,0):mon(ZERO),
    (0,1,0):mon(ZERO),
    (0,0,1):mon(ZERO),
    (1,1,0):mon(UNIT[0]),
    (1,0,1):mon(UNIT[1]),
    (0,1,1):mon(UNIT[2]),
    (1,1,1):mon(UNIT[3]),
}

# Direct convolution coefficient expansion, independent of the theorem formula.
conv = defaultdict(dict)
for x in CUBE:
    for y in CUBE:
        s = tuple(x[j]+y[j] for j in range(3))
        conv[s] = add(conv[s], mul(COEFF[x],COEFF[y]))
lhs = total([mul(v,star(v)) for v in conv.values()])
A,B,C,D = [mon(u) for u in UNIT]
p = total([mon(ZERO),A,B,C])
e2 = total([A,B,C,mul(A,B),mul(A,C),mul(B,C)])
rhs = total([mon(ZERO,104),scal(mul(p,star(p)),4),
             scal(mul(D,star(e2)),4),scal(mul(star(D),e2),4)])
assert lhs == rhs,(lhs,rhs)

# Independent exact Gaussian-integer evaluation on the 3-dimensional cube.
# In all evaluations, the root of unity lies in {1,-1,i,-i}.
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cadd(a,b):return (a[0]+b[0],a[1]+b[1])
def norm2(a):return a[0]*a[0]+a[1]*a[1]
roots = [(1,0),(0,1),(-1,0),(0,-1)]
def phase(j):return roots[j%4]

def moment_by_convolution(a,b,c,d):
    coeff={(0,0,0):phase(0),(1,0,0):phase(0),
           (0,1,0):phase(0),(0,0,1):phase(0),
           (1,1,0):phase(a),(1,0,1):phase(b),
           (0,1,1):phase(c),(1,1,1):phase(d)}
    out={}
    for x in CUBE:
        for y in CUBE:
            k=tuple(x[j]+y[j] for j in range(3))
            out[k]=cadd(out.get(k,(0,0)),cmul(coeff[x],coeff[y]))
    return sum(norm2(v) for v in out.values())

# q-ary phases: one common phase and three coordinate modulations are free.
# Only the four residual parameters need exhaustive checking.
checks = 1
for q in (2,4):
    minima=[]; maxima=[]
    for a,b,c,d in product(range(0,4,4//q),repeat=4):
        m=moment_by_convolution(a,b,c,d)
        checks+=1
        if m==88:minima.append((a,b,c,d))
        if m==216:maxima.append((a,b,c,d))
        assert 88<=m<=216
    expected=[(0,2,2,0),(2,0,2,0),(2,2,0,0)]
    assert sorted(minima)==sorted(expected), (q,minima)
    assert maxima==[(0,0,0,0)]
    print('q=',q,'normalized configurations',q**4,
          'minimizers',len(minima),'maximizers',len(maxima),
          'full minimizers',len(minima)*q**4)

# Verify orthogonality sampling on every finite torus of side length >=3
# by the exact combinatorial condition on convolution exponents.
for n in (3,4,5,7):
    for k in conv:
        assert all(0<=v<=2 for v in k)
    # k in {0,1,2}^3 are pairwise distinct modulo n if n>=3.
    assert len({tuple(i%n for i in k) for k in conv})==len(conv)
    checks+=1

print('CHECK_PASS; independent exact symbolic moment identity and',checks,
      'normalized-pattern/frequency-separation checks')
