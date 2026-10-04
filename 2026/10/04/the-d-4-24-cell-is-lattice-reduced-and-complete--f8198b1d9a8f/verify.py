from fractions import Fraction as F
from itertools import combinations, product

# Exact rational linear algebra for 4x4 systems.
def det(M):
    n=len(M)
    if n==1: return M[0][0]
    s=F(0)
    for j in range(n):
        minor=[row[:j]+row[j+1:] for row in M[1:]]
        s += (F(-1) if j%2 else F(1))*M[0][j]*det(minor)
    return s

def solve(A,b):
    D=det(A)
    if D==0: return None
    x=[]
    for j in range(4):
        Aj=[row[:] for row in A]
        for i in range(4): Aj[i][j]=b[i]
        x.append(det(Aj)/D)
    return tuple(x)

def dot(a,b): return sum(x*y for x,y in zip(a,b))

# D4 roots: all signed e_i+/-e_j, including both global signs.
roots=[]
for i,j in combinations(range(4),2):
    for si,sj in product((-1,1),repeat=2):
        v=[F(0)]*4; v[i]=F(si); v[j]=F(sj); roots.append(tuple(v))
roots=sorted(set(roots))
assert len(roots)==24

# P = {x : r.x <= 1 for all D4 roots r}. Enumerate every 4-active-hyperplane intersection.
verts=set()
for inds in combinations(range(24),4):
    A=[list(roots[k]) for k in inds]
    x=solve(A,[F(1)]*4)
    if x is None: continue
    if all(dot(r,x)<=1 for r in roots): verts.add(x)

M=set()
for i in range(4):
    for s in (-1,1):
        v=[F(0)]*4; v[i]=F(s); M.add(tuple(v))
for signs in product((-1,1),repeat=4):
    M.add(tuple(F(s,2) for s in signs))
assert len(M)==24
assert verts==M

# C = P^o is the root polytope conv(roots). Q=C/2 has H-description m.x <= 1/2 for m in M.
# Enumerate vertices of Q from that H-description and recover exactly half-roots.
Mlist=sorted(M)
qverts=set()
for inds in combinations(range(24),4):
    A=[list(Mlist[k]) for k in inds]
    x=solve(A,[F(1,2)]*4)
    if x is None: continue
    if all(dot(m,x)<=F(1,2) for m in Mlist): qverts.add(x)
halfroots={tuple(t/F(2) for t in r) for r in roots}
assert qverts==halfroots

# Check the two infinite-support inequalities over a large exact box as a consistency replay.
# Analytic proof in RESULT.md covers all lattice vectors.
def in_D4(z): return all(x.denominator==1 for x in z) and sum(int(x) for x in z)%2==0

def in_D4star(z):
    # all integral, or all half-integral with fractional part 1/2
    ints=all(x.denominator==1 for x in z)
    halves=all(x.denominator==2 and abs(x.numerator)%2==1 for x in z)
    return ints or halves

def hP(z):
    return max(max(abs(x) for x in z), sum(abs(x) for x in z)/2)

def hQ(z):
    a=sorted((abs(x) for x in z), reverse=True)
    return (a[0]+a[1])/2

vals=[F(k) for k in range(-4,5)]
for z in product(vals,repeat=4):
    if z==(F(0),)*4 or not in_D4(z): continue
    assert hP(z) <= dot(z,z)/2

halfvals=[F(k,2) for k in range(-7,8)]
for z in product(halfvals,repeat=4):
    if z==(F(0),)*4 or not in_D4star(z): continue
    assert hQ(z) <= dot(z,z)/2

# Width certificate for C with respect to D4*: dual directions are D4.
# For a root r, h_C(r)=2 uniquely at r; hence width is 4 and every C-vertex is selected.
for r in roots:
    vals=[dot(r,s) for s in roots]
    assert max(vals)==2 and vals.count(F(2))==1

print('VERIFY_OK D4 24-cell reduced-complete identity')
