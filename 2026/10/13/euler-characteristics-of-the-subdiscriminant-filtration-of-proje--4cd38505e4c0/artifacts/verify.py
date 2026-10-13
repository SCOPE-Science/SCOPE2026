from functools import lru_cache
from itertools import product
import math

@lru_cache(None)
def S(n,b):
    if n==0 and b==0: return 1
    if n<=0 or b<=0 or b>n: return 0
    return b*S(n-1,b)+S(n-1,b-1)

def q(b):
    if b==1: return 1
    return (-1)**(b-2)*math.factorial(b-2)

def chi_level(n,r):
    return n*(n-1)+sum(S(n,b)*q(b) for b in range(1,r+1))

def chi_layer(n,r):
    if r==1: return n*(n-1)+1
    return S(n,r)*q(r)

formula_checks=0
for n in range(2,31):
    prev=0
    for r in range(1,n+1):
        c=chi_level(n,r)
        e=chi_layer(n,r)
        assert c-prev==e
        prev=c
        formula_checks+=1
    assert prev==n*n

weight_checks=0
for n in range(2,31):
    w=[1<<i for i in range(n)]
    seen={}
    for i in range(n):
        for j in range(n):
            if i==j: continue
            d=w[i]-w[j]
            assert d not in seen, (n,i,j,seen.get(d))
            seen[d]=(i,j)
            weight_checks+=1

# Direct finite-field projective diagonal count: normalize by first nonzero coordinate.
def exact_distinct_projective_count(n,p,b):
    reps=[]
    count=0
    for v in product(range(p), repeat=n):
        if not any(v):
            continue
        k=next(i for i,x in enumerate(v) if x)
        if v[k] != 1:
            continue  # one representative per scalar orbit only if first nonzero is 1
        if len(set(v))==b:
            count+=1
    return count

def falling(p,b):
    z=1
    for j in range(b): z*=p-j
    return z

finite_checks=0
for p in (5,7):
    for n in range(2,6):
        for b in range(1,min(n,p)+1):
            brute=exact_distinct_projective_count(n,p,b)
            if b==1:
                # exactly one coordinate value and nonzero => one projective diagonal point
                predicted=S(n,1)
            else:
                # each equality partition times Conf_b(F_p)/F_p^*
                predicted=S(n,b)*(falling(p,b)//(p-1))
            assert brute==predicted,(p,n,b,brute,predicted)
            finite_checks+=1

assert chi_level(2,1)==3
assert chi_level(3,1)==7
assert chi_level(3,2)==10
assert chi_level(4,2)==20
assert chi_level(5,3)==11
print('VERIFY_OK',formula_checks,weight_checks,finite_checks)
