"""Exact finite-field verification for the line-free cubic threefold example.

The field F_4 is represented by bits, with a=2 and a^2=a+1=3.
No external packages are used. All enumerations are exhaustive.
"""
from itertools import combinations, product
from collections import Counter

Q = 4
N = 5
MONOMIALS = (
    (0,0,0), (1,1,1), (2,2,2),
    (0,0,1), (1,1,2), (2,2,0), (0,1,2),
    (0,3,3), (0,0,3), (1,4,4), (1,1,4), (3,3,4),
)

def mul(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # reduction modulo z^2+z+1
    return ans

def inv(a):
    assert a
    return next(b for b in range(1,4) if mul(a,b) == 1)

def F(v):
    out = 0
    for i,j,k in MONOMIALS:
        out ^= mul(mul(v[i],v[j]),v[k])
    return out

def coeff(u, v):
    """Coefficients of F(s*u+t*v) in s^(3-k)*t^k for k=0..3."""
    c = [0,0,0,0]
    for mon in MONOMIALS:
        for mask in range(8):
            z=1
            for j,i in enumerate(mon):
                z=mul(z, v[i] if mask & (1<<j) else u[i])
            c[mask.bit_count()] ^= z
    return tuple(c)

def rref_2spaces():
    for i,j in combinations(range(N),2):
        free1 = [k for k in range(i+1,N) if k != j]
        free2 = list(range(j+1,N))
        for vals in product(range(Q), repeat=len(free1)+len(free2)):
            u=[0]*N;v=[0]*N
            u[i]=1;v[j]=1
            for k,z in zip(free1,vals[:len(free1)]):u[k]=z
            for k,z in zip(free2,vals[len(free1):]):v[k]=z
            yield tuple(u),tuple(v)

def rank(rows):
    A=[list(row) for row in rows]
    k=0
    for j in range(N):
        t=next((t for t in range(k,len(A)) if A[t][j]),None)
        if t is None:continue
        A[k],A[t]=A[t],A[k]
        y=inv(A[k][j]);A[k]=[mul(y,z) for z in A[k]]
        for t in range(len(A)):
            if t != k and A[t][j]:
                y=A[t][j]
                A[t]=[a^mul(y,b) for a,b in zip(A[t],A[k])]
        k+=1
        if k == len(A):break
    return k

def norm(v):
    a=next(x for x in v if x)
    return tuple(mul(inv(a),b) for b in v)

def line_points(u,v):
    return frozenset([norm(v)] +
        [norm(tuple(u[i]^mul(t,v[i]) for i in range(N))) for t in range(Q)])

def main():
    assert [[mul(a,b) for b in range(4)] for a in range(4)] == [
        [0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]
    ]
    candidates=list(rref_2spaces())
    assert len(candidates) == 5797
    accepted=[(u,v) for u,v in candidates if coeff(u,v) == (0,0,0,0)]
    expected=(
       ((1,0,0,2,0),(0,1,0,0,2)),
       ((1,0,0,2,0),(0,1,1,0,2)),
       ((1,0,0,3,0),(0,1,0,0,3)),
       ((1,0,0,3,0),(0,1,1,0,3)),
       ((1,0,1,2,0),(0,1,1,0,2)),
       ((1,0,1,3,0),(0,1,1,0,3)),
       ((1,1,0,0,2),(0,0,1,2,2)),
       ((1,1,0,0,3),(0,0,1,3,3)),
    )
    assert tuple(accepted) == expected, (len(accepted),accepted)
    # A different containment check: degree-3 polynomials cannot vanish at
    # all five F_4-rational points of P^1 unless identically zero.
    for uv in candidates:
        assert (coeff(*uv)==(0,0,0,0)) == all(F(p)==0 for p in line_points(*uv))
    edges=set()
    for i,j in combinations(range(len(accepted)),2):
        if rank(accepted[i]+accepted[j]) == 3:
            edges.add((i,j))
    assert edges == {(0,1),(0,4),(1,4),(2,3),(2,5),(3,5)}
    # Each K3 really is a triangle of distinct pairwise intersections.
    pts=[line_points(*uv) for uv in accepted]
    for a,b,c in [(0,1,4),(2,3,5)]:
        cuts=[pts[i]&pts[j] for i,j in ((a,b),(a,c),(b,c))]
        assert all(len(s)==1 for s in cuts)
        assert len(set.union(*[set(z) for z in cuts])) == 3
        assert rank(accepted[a]+accepted[b]+accepted[c]) == 3
    # Frobenius x -> x^2 permutes the eight lines in four two-cycles.
    lookup={p:i for i,p in enumerate(pts)}
    frob=[]
    for pset in pts:
        img=frozenset(norm(tuple(mul(t,t) for t in p)) for p in pset)
        frob.append(lookup[img])
    assert frob == [2,3,0,1,5,4,7,6]
    # Explicit pair of conjugate planes and their split cubic sections.
    for a in [2,3]:
        for s,t,z in product(range(4),repeat=3):
            pt=(s,t,z,mul(a,s),mul(a,t))
            # F restricted to the plane is z(z+t)(z+s+t).
            assert F(pt) == mul(mul(z,z^t),z^s^t)
    # The two planes meet only at [0:0:1:0:0], which lies outside X.
    assert F((0,0,1,0,0)) == 1
    # Independent second enumeration via all projective point pairs, not RREF.
    allpoints={norm(v) for v in product(range(4),repeat=5) if any(v)}
    assert len(allpoints) == 341
    basepoints=[p for p in allpoints if all(z in (0,1) for z in p)]
    assert len(basepoints) == 31
    assert sum(F(p)==0 for p in basepoints)==9
    assert sum(F(p)==0 for p in allpoints)==81
    on_x=sorted(p for p in allpoints if F(p)==0)
    discovered=set()
    for u,v in combinations(on_x,2):
        line=line_points(u,v)
        if all(F(p)==0 for p in line):discovered.add(line)
    assert discovered==set(pts) and len(discovered)==8
    # Any F_2-line contained in X has at least two F_2-rational points.
    # Test every pair among the nine F_2-rational points, using coefficients
    # rather than just testing its three rational points.
    f2pts=sorted(p for p in basepoints if F(p)==0)
    assert len(f2pts)==9
    for u,v in combinations(f2pts,2):
        assert coeff(u,v) != (0,0,0,0)
    print('VERIFY_OK', 'Grassmann=5797', 'F4_lines=8',
          'graph=2K3+2K1', 'Frobenius=2^4', 'F2_lines=0',
          'points=(9,81)', 'split_planes=2')

if __name__ == '__main__':
    main()
