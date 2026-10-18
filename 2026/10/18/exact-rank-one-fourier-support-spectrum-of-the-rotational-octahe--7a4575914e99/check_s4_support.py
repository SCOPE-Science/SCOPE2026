"""Exact independent checks for the octahedral rank-one matrix-coefficient support spectrum.

Run with Python >=3.8 and no third-party packages. Arithmetic is in Z[omega],
where omega^2+omega+1=0, with exact integer pairs.
"""
from itertools import permutations, product

I = (1, 0)
ZERO = (0, 0)
OMEGA = (0, 1)
OMEGA2 = (-1, -1)

def z(n):
    return (n, 0)

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)

def signed(x,sgn):
    return x if sgn==1 else neg(x)

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

# Group elements are matrices with exactly one signed entry per row,
# and determinant +1; all 24 obtained once.
GROUP = []
for p in permutations(range(3)):
    for e,f in product((1,-1),repeat=2):
        s1=parity(p)*e*f
        sig=(s1,s1*e,s1*f)
        GROUP.append((p,sig))
assert len(GROUP)==24 and len(set(GROUP))==24

def coefficient(u,v,g):
    p,s=g
    out=ZERO
    for i in range(3):
        out=add(out,signed(mul(u[i],v[p[i]]),s[i]))
    return out

# Exact Schur orthogonality on the entire matrix coefficient block.
matrices=[]
for p,s in GROUP:
    m=[[0]*3 for _ in range(3)]
    for i in range(3): m[i][p[i]]=s[i]
    matrices.append(m)
for i,j,k,l in product(range(3),repeat=4):
    got=sum(m[i][j]*m[k][l] for m in matrices)
    assert got==(8 if i==k and j==l else 0), (i,j,k,l,got)

# The nine support sizes, listed via exact nonzero u and v vectors.
witnesses = {
    24: ((z(1),z(1),z(1)), (z(1),z(1),z(1))),
    23: ((z(1),z(2),z(3)), (z(1),z(2),z(4))),
    22: ((z(1),z(1),z(2)), (z(1),z(2),z(3))),
    21: ((I,OMEGA,OMEGA2), (I,OMEGA,OMEGA2)),
    20: ((z(1),z(1),z(2)), (z(1),z(1),z(3))),
    18: ((z(1),z(1),z(1)), (z(1),z(1),z(2))),
    16: ((z(1),ZERO,ZERO), (z(1),z(1),ZERO)),
    12: ((z(1),z(1),ZERO), (z(1),z(1),z(1))),
    8: ((z(1),ZERO,ZERO), (z(1),ZERO,ZERO)),
}
for expected,(u,v) in sorted(witnesses.items()):
    assert any(x!=ZERO for x in u) and any(x!=ZERO for x in v)
    size=sum(coefficient(u,v,g)!=ZERO for g in GROUP)
    assert size==expected,(expected,size)
    print('verified rank-one S4 coefficient support:',size)

# The full-support five-zero obstruction is an alternating identity.
# Q_p(a,b) is the product of the four relative-sign coefficient values
# for permutation p; the identity is polynomial, checked exactly below.
def Q(a,b,p):
    xs=[mul(a[i],b[p[i]]) for i in range(3)]
    # a and b are squared coordinates, hence Q = sum x_i^2 - 2 sum x_i x_j.
    ans=ZERO
    for i in range(3): ans=add(ans,mul(xs[i],xs[i]))
    for i in range(3):
        for j in range(i+1,3):
            ans=add(ans,neg(add(mul(xs[i],xs[j]),mul(xs[i],xs[j]))))
    return ans
for a in [(I,OMEGA,OMEGA2),(z(2),z(-4),z(9))]:
    for b in [(z(1),z(5),z(8)),(I,OMEGA2,OMEGA)]:
        alternating=ZERO
        for p in permutations(range(3)):
            q=Q(a,b,p)
            alternating=add(alternating,signed(q,parity(p)))
        assert alternating==ZERO
print('all exact group, Fourier, witness, and parity tests passed')

# A deterministic finite stress test (not part of the infinite-field proof).
alphabet=(ZERO,z(1),z(-1),OMEGA,OMEGA2)
nonzero_vectors=[u for u in product(alphabet, repeat=3) if any(x!=ZERO for x in u)]
allowed={8,12,16,18,20,21,22,23,24}
observed=set()
for u in nonzero_vectors:
    for v in nonzero_vectors:
        size=sum(coefficient(u,v,g)!=ZERO for g in GROUP)
        assert size in allowed,(u,v,size)
        observed.add(size)
print('finite-alphabet stress pairs:',len(nonzero_vectors)**2,'observed sizes:',sorted(observed))
