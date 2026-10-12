#!/usr/bin/env python3
"""Exact arithmetic verification for the 12 tangent lines of the Edge quartic.

Uses only the Python standard library. All projective finite-field
calculations are exact, with i^2 = -1 where the quadratic ring is a field.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd
from functools import reduce

# Gaussian integer arithmetic: (a,b) means a+b*i, i*i=-1.
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,k): return (k*a[0],k*a[1])
def powg(a,n):
    r=(1,0)
    for _ in range(n): r=mul(r,a)
    return r

def det3(rows):
    a,b,c=rows[0]; d,e,f=rows[1]; g,h,j=rows[2]
    return add(sub(mul(a,sub(mul(e,j),mul(f,h))),
                   mul(b,sub(mul(d,j),mul(f,g)))),
               mul(c,sub(mul(d,h),mul(e,g))))

def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))

O=(0,0); E=(1,0); NEG=(-1,0); I=(0,1); MINUSI=(0,-1); TWOI=(0,2); MINTWOI=(0,-2)
POINTS=[(I,E,NEG),(MINUSI,E,NEG),(NEG,I,E),(NEG,MINUSI,E),
        (E,NEG,I),(E,NEG,MINUSI),(MINUSI,E,E),(I,E,E),
        (E,MINUSI,E),(E,I,E),(E,E,MINUSI),(E,E,I)]
LINES=[(TWOI,E,NEG),(MINTWOI,E,NEG),(NEG,TWOI,E),(NEG,MINTWOI,E),
       (E,NEG,TWOI),(E,NEG,MINTWOI),(MINTWOI,E,E),(TWOI,E,E),
       (E,MINTWOI,E),(E,TWOI,E),(E,E,MINTWOI),(E,E,TWOI)]

# Tangency identities over Z[i], not only modulo selected primes.
def quartic(P):
    q=[mul(v,v) for v in P]
    return add(add(mul(q[0],q[0]),mul(q[1],q[1])),
               add(mul(q[2],q[2]),scale(add(add(mul(q[0],q[1]),mul(q[0],q[2])),mul(q[1],q[2])),3)))
def gradient(P):
    q=[mul(v,v) for v in P]
    return tuple(add(scale(powg(P[k],3),4),scale(mul(P[k],add(q[(k+1)%3],q[(k+2)%3])),6)) for k in range(3))
for p,line in zip(POINTS,LINES):
    assert quartic(p)==O
    assert gradient(p)==tuple(scale(v,4) for v in line)

D=Counter()
for i,j,k in combinations(range(12),3):
    a,b=det3([LINES[i],LINES[j],LINES[k]])
    assert (a,b)!=(0,0)
    D[a*a+b*b]+=1
assert D=={4:8,20:48,36:24,40:24,64:12,80:48,100:48,200:8},D
assert sum(D.values())==220
assert {p for p in (2,3,5,7,11,13,17,19,23,29) if any(n%p==0 for n in D)}=={2,3,5}

# Fields of the form F_p(i) with p=3 mod 4; i*i=-1 is irreducible.
def geometry_quadratic(p):
    assert p%4==3
    def red(a): return (a[0]%p,a[1]%p)
    def plus(a,b): return red(add(a,b))
    def times(a,b): return red(mul(a,b))
    def minus(a,b): return red(sub(a,b))
    def inv(a):
        n=(a[0]*a[0]+a[1]*a[1])%p
        assert n!=0
        return red(scale((a[0],-a[1]),pow(n,-1,p)))
    def norm(a):
        c=next(t for t in a if t!=(0,0))
        u=inv(c)
        return tuple(times(t,u) for t in a)
    def wedge(a,b):
        return (minus(times(a[1],b[2]),times(a[2],b[1])),
                minus(times(a[2],b[0]),times(a[0],b[2])),
                minus(times(a[0],b[1]),times(a[1],b[0])))
    LL=[norm(tuple(red(t) for t in line)) for line in LINES]
    assert len(set(LL))==12
    pts={norm(wedge(a,b)) for a,b in combinations(LL,2)}
    def dot(a,b):
        t=(0,0)
        for x,y in zip(a,b): t=plus(t,times(x,y))
        return t
    dist=Counter(sum(dot(L,P)==(0,0) for L in LL) for P in pts)
    nrat=sum(all(c[1]==0 for c in P) for P in pts)
    nratlines=sum(all(c[1]==0 for c in L) for L in LL)
    return len(pts),dist,nrat,nratlines
assert geometry_quadratic(3)==(36,Counter({2:30,4:6}),6,0)
for p in (7,11,19):
    assert geometry_quadratic(p)==(66,Counter({2:66}),6,0)

# In split characteristics use an embedding i -> root of -1.
def geometry_prime(p):
    assert p%4==1
    i=next(a for a in range(p) if a*a%p==p-1)
    def norm(V):
        d=next(v for v in V if v%p)
        return tuple(v*pow(d,-1,p)%p for v in V)
    LL=[norm(tuple((a+i*b)%p for a,b in line)) for line in LINES]
    assert len(set(LL))==12
    def wedge(A,B):
        return ((A[1]*B[2]-A[2]*B[1])%p,
                (A[2]*B[0]-A[0]*B[2])%p,
                (A[0]*B[1]-A[1]*B[0])%p)
    pts={norm(wedge(a,b)) for a,b in combinations(LL,2)}
    count=Counter(sum(sum(l[j]*q[j] for j in range(3))%p==0 for l in LL) for q in pts)
    return len(pts),count
for p in (13,17,29):
    assert geometry_prime(p)==(66,Counter({2:66}))

# In characteristic 5, evaluate either embedding i=2 or i=-2.
def reduction_five(i):
    def norm(V):
        d=next(v for v in V if v%5)
        return tuple(v*pow(d,-1,5)%5 for v in V)
    groups=defaultdict(list)
    for k,line in enumerate(LINES):
        groups[norm(tuple((a+i*b)%5 for a,b in line))].append(k+1)
    assert sorted(map(len,groups.values()))==[3,3,3,3]
    expected={((1,4,1),(1,6,10)),((1,1,4),(2,3,12)),
              ((1,4,4),(4,5,8)),((1,1,1),(7,9,11))}
    if i==2: assert {(line,tuple(inds)) for line,inds in groups.items()}==expected
    ll=list(groups)
    def wedge(A,B):
        return ((A[1]*B[2]-A[2]*B[1])%5,
                (A[2]*B[0]-A[0]*B[2])%5,
                (A[0]*B[1]-A[1]*B[0])%5)
    assert len({norm(wedge(a,b)) for a,b in combinations(ll,2)})==6
    # C3 modulo 5 equals product of the four reduced lines.
    terms={(0,0,0):1}
    for line in ll:
        new=defaultdict(int)
        for (a,b,c),v in terms.items():
            for d,co in enumerate(line):
                ex=[a,b,c];ex[d]+=1
                new[tuple(ex)]=(new[tuple(ex)]+v*co)%5
        terms=dict(new)
    f={(4,0,0):1,(0,4,0):1,(0,0,4):1,
       (2,2,0):3,(2,0,2):3,(0,2,2):3}
    assert {e:v for e,v in terms.items() if v%5}==f
reduction_five(2)
reduction_five(3)
print('VERIFY_OK: 12 tangent gradients, 220 determinant norms, all-prime support, F9 six quadruples, F5 four-line factorization, Frobenius spectra')
