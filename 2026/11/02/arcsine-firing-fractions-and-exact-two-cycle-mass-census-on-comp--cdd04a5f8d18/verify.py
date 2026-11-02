"""Exact checks for synchronous chip-firing two-cycles on complete bipartite graphs."""
import itertools
import math
from collections import Counter
from fractions import Fraction


def advance(chips, a, b):
    fire_l = [int(x >= b) for x in chips[:a]]
    fire_r = [int(x >= a) for x in chips[a:]]
    left_received, right_received = sum(fire_r), sum(fire_l)
    return tuple(x - b * fire_l[i] + left_received for i, x in enumerate(chips[:a])) + tuple(
        x - a * fire_r[j] + right_received for j, x in enumerate(chips[a:]))


def brute(a, b):
    counts = Counter()
    states = 0
    for x in itertools.product(range(2*b), repeat=a):
        for y in itertools.product(range(2*a), repeat=b):
            c = x + y
            d = advance(c, a, b)
            if d != c and advance(d, a, b) == c:
                counts[sum(c)] += 1
                states += 1
    assert all(v % 2 == 0 for v in counts.values())
    return Counter({m: v // 2 for m, v in counts.items()}), states // 2


def convolution(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def weighted_formula(a, b):
    total = [0] * (4*a*b-a-b+1)
    def addterm(scale, base, widths_and_counts):
        p = [1]
        for width, count in widths_and_counts:
            for _ in range(count):
                p = convolution(p, [1]*width)
        for k, c in enumerate(p):
            total[base+k] += scale*c
    # Count doubled-phase polynomial and divide by two at the end.
    addterm(2, a*b, ((b,a),(a,b)))
    for i in range(1,a):
        for j in range(1,b):
            addterm(math.comb(a,i)*math.comb(b,j),
                    i*b+j*a+2*(a-i)*(b-j),
                    ((b-j,i),(j,a-i),(a-i,j),(i,b-j)))
    assert all(k % 2 == 0 for k in total), (a,b,total)
    return Counter({k: v//2 for k,v in enumerate(total) if v})


def spectral_formula(n):
    result = Fraction(0,1)
    falling = 1
    for k in range(n+1):
        if k:
            falling *= n-k+1
        result += Fraction(falling*falling,n**(2*k))
    val = result * n**(2*n) / 2
    assert val.denominator == 1
    return val.numerator


checked = 0
for a,b in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)):
    f = weighted_formula(a,b)
    brute_f, _ = brute(a,b)
    assert f == brute_f, (a,b,f,brute_f)
    checked += (2*b)**a * (2*a)**b

for a in range(1,5):
    for b in range(1,5):
        f=weighted_formula(a,b)
        assert sum(f.values()) == b**a * a**b + sum(
            math.comb(a,i)*math.comb(b,j)*(b-j)**i*j**(a-i)*(a-i)**j*i**(b-j)
            for i in range(1,a) for j in range(1,b))//2
        top=4*a*b-a-b
        assert all(f.get(k,0)==f.get(top-k,0) for k in range(top+1))

for n in range(1,11):
    f=weighted_formula(n,n) if n<=4 else None
    s=spectral_formula(n)
    if f is not None: assert sum(f.values())==s,(n,s,sum(f.values()))

# Exact finite weighted phase-count marginal, verifying that its total equals 2N.
for n in range(1,15):
    phase=0
    for i in range(n+1):
        for j in range(n+1):
            if i==n and j==0 or i==0 and j==n:
                phase+=n**(2*n)
            elif 0<i<n and 0<j<n:
                phase+=math.comb(n,i)*math.comb(n,j)*(n-j)**i*j**(n-i)*(n-i)**j*i**(n-j)
    assert phase==2*spectral_formula(n), n

print('BIPARTITE_TWO_CYCLE_EXACT_OK')
print('independently enumerated confined configurations',checked)
print('balanced counts for n=1,...,10:',[spectral_formula(n) for n in range(1,11)])
print('checked polynomial reflection and spectral totals for all a,b<=4')
print('verified phase marginal total identity through n=14')
