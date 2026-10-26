"""Exact rational-series certificate for binary rank-three branched covers.

Python 3 standard library only. The finite polynomial-degree bound converts the
coefficient comparison to a proof of a rational-function identity.
"""
from itertools import product, combinations
from collections import Counter, defaultdict

N = 70
V = range(1, 8)

def action(g, v):
    a, b, c = g
    return (a if v & 1 else 0) ^ (b if v & 2 else 0) ^ (c if v & 4 else 0)

GROUP = [(a,b,c) for a,b,c in product(V,repeat=3)
         if len({action((a,b,c),v) for v in range(8)}) == 8]
assert len(GROUP) == 168

def cycles(g):
    pending=set(V); out=[]
    while pending:
        v=min(pending); orbit=[]; w=v
        while w in pending:
            orbit.append(w); pending.remove(w); w=action(g,w)
        assert w == v
        out.append(tuple(orbit))
    return tuple(out)

types=defaultdict(list)
for g in GROUP:
    types[tuple(sorted(map(len,cycles(g))))].append(g)
assert {k:len(v) for k,v in types.items()} == {
    (1,1,1,1,1,1,1):1, (1,1,1,2,2):21,
    (1,2,4):42, (1,3,3):56, (7,):48}

subspaces={frozenset((0,))}
for d in (1,2,3):
    for basis in combinations(V,d):
        U={0}
        for v in basis: U |= {x^v for x in tuple(U)}
        if len(U)==2**d: subspaces.add(frozenset(U))
assert Counter(map(len,subspaces)) == {1:1,2:7,4:7,8:1}

def mobius(U):
    codim=3-(len(U).bit_length()-1)
    return (-1)**codim * 2**(codim*(codim-1)//2)

def fixed_series(g,U,limit):
    CC=[C for C in cycles(g) if set(C) <= U]
    numerator=Counter()
    xor_sums=[]
    for C in CC:
        x=0
        for v in C:x ^= v
        xor_sums.append(x)
    for mask in range(1<<len(CC)):
        x=d=0
        for j,C in enumerate(CC):
            if mask & (1<<j):
                x ^= xor_sums[j]; d += len(C)
        if x==0: numerator[d]+=1
    den_inv=[1]+[0]*limit
    for C in CC:
        step=2*len(C)
        for k in range(step, limit+1): den_inv[k] += den_inv[k-step]
    result=[0]*(limit+1)
    for d,coef in numerator.items():
        for k in range(d,limit+1): result[k] += coef*den_inv[k-d]
    return result

numerical=[0]*(N+1)
for typ,gs in types.items():
    representative=gs[0]
    f=[0]*(N+1)
    for U in subspaces:
        mu=mobius(U)
        fixed=fixed_series(representative,U,N)
        for k in range(N+1):f[k]+=mu*fixed[k]
    for k in range(N+1): numerical[k]+=len(gs)*f[k]
assert all(n%168==0 for n in numerical)
A=[n//168 for n in numerical]

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):c[i+j]+=x*y
    return c

def factor_power(f,k):
    a=[1]
    for _ in range(k):a=mul(a,f)
    return a

def divide_exact(a,b):
    a=a[:];q=[0]*(len(a)-len(b)+1)
    assert b[-1] in (-1,1)
    for n in range(len(a)-1,len(b)-2,-1):
        x=a[n]//b[-1];q[n-(len(b)-1)]=x
        for j in range(len(b)):a[n-(len(b)-1)+j]-=x*b[j]
    assert all(v==0 for v in a)
    return q

# Candidate numerator t^4 P(t).
P={0:1,2:1,5:-1,7:-1,8:2,9:-1,10:1,11:1,13:1,14:-1,15:-1,16:1}
num=[0]*21
for k,v in P.items():num[k+4]=v
# Positive-factor denominator.
D=[1]
for fac,k in [([1,-1],7),([1,1],4),([1,0,1],2),
              ([1,-1,1],1),([1,1,1],2),([1]*7,1)]:
    D=mul(D,factor_power(fac,k))
assert len(D)-1 == 27 and D[0]==1

# E is a common denominator for all Burnside--Moebius terms, since
# every restricted-cycle denominator divides its full-cycle denominator.
E=[1]
for typ,gs in types.items():
    full=[1]
    for c in cycles(gs[0]):
        fac=[0]*(2*len(c)+1);fac[0]=1;fac[-1]=-1
        full=mul(full,fac)
    assert len(full)-1==14
    E=mul(E,full)
assert len(E)-1==70
Q=divide_exact(E,D)
assert len(num)+len(Q)-2 <=70

compact=[0]*(N+1)
for k in range(N+1):
    compact[k]=(num[k] if k<len(num) else 0)-sum(
        D[j]*compact[k-j] for j in range(1,min(k,len(D)-1)+1))
assert A==compact, [(k,A[k],compact[k]) for k in range(N+1) if A[k]!=compact[k]]
assert A[:13]==[0,0,0,0,1,1,3,4,8,9,17,20,34]

# Independent orbit enumeration for ten smallest admissible branch lengths.
def comps(total,k):
    if k==1:
        yield (total,); return
    for q in range(total+1):
        for rest in comps(total-q,k-1):yield (q,)+rest

def generates(m):
    U={0}
    for v,mv in enumerate(m,1):
        if mv: U|={x^v for x in tuple(U)}
    return len(U)==8

def brute_orbits(r):
    candidates=set()
    for m in comps(r,7):
        xor=0
        for v,mv in enumerate(m,1):
            if mv&1:xor^=v
        if xor==0 and generates(m):candidates.add(m)
    count=0
    while candidates:
        m=next(iter(candidates));orb=set()
        for g in GROUP:
            out=[0]*7
            for v,mv in enumerate(m,1):out[action(g,v)-1]=mv
            orb.add(tuple(out))
        assert orb<=candidates
        candidates-=orb;count+=1
    return count
for r in range(3,13):
    assert A[r]==brute_orbits(r)
print('VERIFY_OK GL3_order=168 conjugacy_types=5 subspaces=16 denominator_degree=70')
print('VERIFY_OK rational_identity_exact=true coefficients_0_to_70=true independent_orbits_r3_to_r12=true')
print('first_coefficients',A[4:21])
