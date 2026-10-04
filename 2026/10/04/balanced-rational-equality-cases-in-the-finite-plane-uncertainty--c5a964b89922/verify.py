from itertools import product


def partitions(n, hi=None):
    if hi is None or hi > n:
        hi = n
    if n == 0:
        yield []
        return
    for first in range(min(hi, n), 0, -1):
        for rest in partitions(n-first, first):
            yield [first] + rest

# Exact multiplicity-lemma checks for several small primes.
for p in (3, 5, 7, 11):
    pats = [q for q in partitions(p) if len(q) >= 2]
    target = (p-1)*(p-1) + 1
    eq = []
    for r in pats:
        for s in pats:
            L = max(len(r), len(s))
            rr = r + [0]*(L-len(r))
            ss = s + [0]*(L-len(s))
            dot = sum(a*b for a,b in zip(rr,ss))
            assert dot <= target, (p,r,s,dot,target)
            if dot == target:
                eq.append((r,s))
    assert eq == [([p-1,1],[p-1,1])], (p,eq)

# Exact arithmetic in Q(zeta_3), represented as A + B*zeta, zeta^2=-1-zeta.
def zpow(e):
    e %= 3
    return [(1,0),(0,1),(-1,-1)][e]

def add(u,v):
    return (u[0]+v[0], u[1]+v[1])

def scale(c,u):
    return (c*u[0], c*u[1])

pts = [(x,y) for x in range(3) for y in range(3)]

def fourier_support(f):
    out = []
    for a,b in pts:
        z=(0,0)
        for val,(x,y) in zip(f,pts):
            if val:
                z = add(z, scale(val, zpow(-(a*x+b*y))))
        if z != (0,0):
            out.append((a,b))
    return frozenset(out)

# Affine lines, normalized normal vectors (1,t) and (0,1).
normals = [(1,t) for t in range(3)] + [(0,1)]
lines=[]
for normal in normals:
    a,b=normal
    for c in range(3):
        mask=tuple(1 if (a*x+b*y-c)%3==0 else 0 for x,y in pts)
        lines.append((normal,c,mask))
assert len(lines)==12 and len({m for _,_,m in lines})==12

expected=set()
for i,(ni,ci,mi) in enumerate(lines):
    for j,(nj,cj,mj) in enumerate(lines):
        if j<=i or ni==nj:
            continue
        d=tuple(a-b for a,b in zip(mi,mj))
        expected.add(d)
        expected.add(tuple(-x for x in d))
assert len(expected)==108

found=set()
for f in product((-1,0,1), repeat=9):
    if all(v==0 for v in f):
        continue
    if sum(v!=0 for v in f)!=4:
        continue
    if len(fourier_support(f))==4:
        found.add(f)
assert found==expected, (len(found),len(expected), len(found-expected), len(expected-found))

print('VERIFY_OK')
