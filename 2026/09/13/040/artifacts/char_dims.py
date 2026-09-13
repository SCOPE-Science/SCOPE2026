import itertools
from math import factorial, comb
from collections import Counter
from functools import lru_cache
import sympy as sp

def partitions_of_n(n, max_part=None):
    if n==0:
        yield []
        return
    if max_part is None: max_part=n
    for f in range(min(max_part,n),0,-1):
        for rest in partitions_of_n(n-f, f):
            yield [f]+rest

def class_size(n, part):
    # part: list of cycle lengths summing to n
    c=Counter(part)
    denom=1
    for l,m in c.items():
        denom*= (l**m)*factorial(m)
    return factorial(n)//denom

def fix_of_part(part, n):
    # number of 1-cycles (need to include 1s). partitions as given include 1s explicitly if we generate that way.
    return sum(1 for x in part if x==1)

def chi_V(part, n):
    # standard rep: fix-1
    return fix_of_part(part,n)-1

def chi_V_sq(part, n, power=2):
    # chi_V(g^power): need cycle structure of g^power. Compute fix(g^power) = sum_{d|power} d * (# cycles of length d with ...)? Actually fix(g^p) = sum_{d|p} d * m_d where m_d = number of d-cycles? No: a d-cycle raised to p splits into gcd(d,p) cycles each of length d/gcd; it contributes fixed points iff d|p? Then each such cycle gives d fixed points. So fix(g^p)= sum_{d|p} d*m_d.
    from math import gcd
    c=Counter(part)
    # need m_1 includes? part includes 1s; total n covered.
    s=0
    for d,m in c.items():
        if power % d == 0 and d <= power:
            # condition d | power
            if power % d==0:
                # g^power on d-cycle: if d|power then identity -> d fixed points
                s+= d*m
    # also need divisors? Actually if d|p then yes. That's it.
    return s-1

def chi_W(part,n):
    a=chi_V(part,n)
    b=chi_V_sq(part,n,2)
    return (a*a - b)//2

def chi_perm_Qk(part,n):
    return fix_of_part(part,n)

def chi_H2(part,n):
    return 2*chi_perm_Qk(part,n)

def dim_inv_H2W(n):
    # (1/n!) sum_C |C| chi_H2 * chi_W (since self-dual, inner product)
    tot=0
    for part in partitions_of_n(n):
        # partitions_of_n yields decreasing; need to add 1s? Our generator includes 1s already (since parts can be 1). Yes.
        cs=class_size(n,part)
        tot+= cs*chi_H2(part,n)*chi_W(part,n)
    return tot//factorial(n)

for n in range(2,13):
    print(f"n={n} chiW(id)={(n-1)*(n-2)//2} dim_inv_H2W={dim_inv_H2W(n)}")

# Also compute dim inv(V tensor W) = <V, W>? and <1,W>?
def dim_inv_W(n):
    tot=0
    for part in partitions_of_n(n):
        tot+= class_size(n,part)*chi_W(part,n)
    return tot//factorial(n)
def dim_inv_VW(n):
    tot=0
    for part in partitions_of_n(n):
        tot+= class_size(n,part)*chi_V(part,n)*chi_W(part,n)
    return tot//factorial(n)

print("---")
for n in range(2,13):
    print(f"n={n} invW={dim_inv_W(n)} invVW={dim_inv_VW(n)} H2W={2*dim_inv_W(n)+2*dim_inv_VW(n)}")
