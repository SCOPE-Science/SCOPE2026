"""Exact rational checks for the tetrahedral two-orbit illumination theorem.

Run with Python 3: python verify.py
The general proof is algebraic; these finite checks test its geometric
reduction, uniform witnesses, boundary transitions, and sample profiles.
"""
from fractions import Fraction as Q
from itertools import product

V = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

def norm_from_index(i, l, lam):
    # n is the unit-support (not Euclidean-unit) outward facet normal.
    a = [None] * 4
    a[i] = Q(1)
    a[l] = Q(2)/lam - 1
    for j in range(4):
        if a[j] is None:
            a[j] = -1/lam
    assert sum(a) == 0
    return tuple(sum(a[j]*V[j][k] for j in range(4))/4 for k in range(3))

def facets(lam):
    vertices = [tuple(Q(x) for x in v) for v in V] + [tuple(-lam*x for x in v) for v in V]
    triples = []
    for i in range(4):
        for l in range(4):
            if l == i:
                continue
            n = norm_from_index(i,l,lam)
            equal = tuple(j for j,point in enumerate(vertices) if dot(n,point) == 1)
            assert len(equal) == 3
            assert (i in equal) and (4 + i not in equal)
            assert all(dot(n,point) <= 1 for point in vertices)
            assert all(dot(n,point) < 1 for j,point in enumerate(vertices) if j not in equal)
            triples.append((i,l,equal,n))
    assert len(triples) == 12
    assert len({t[2] for t in triples}) == 12
    assert all(sum(j in t[2] for t in triples) >= 3 for j in range(8))
    return triples

def incidence(t,s):
    """Return illuminated vertices +0..+3,-0..-3 using proven facets."""
    assert len(t)==4 and sum(t)==0
    plus = {i for i in range(4) if all(t[i]+s*t[l] < 0 for l in range(4) if l!=i)}
    minus = {i for i in range(4) if all(t[p]+s*t[l] < 0
             for p in range(4) for l in range(4) if p!=i and l!=i and p!=l)}
    return plus, minus

def constructed(s,i):
    delta = min(s, (1-s)**2/s)/2
    assert 0<delta<s
    A = 2-s+delta
    C = s-delta
    t = [Q(0)]*4
    t[i], t[(i+1)%4], t[(i+2)%4], t[(i+3)%4] = A,C,Q(-1),Q(-1)
    assert sum(t)==0
    return t

def test(lam):
    assert Q(1)<lam<Q(3)
    f=facets(lam)
    s=(3-lam)/(lam+1)
    all_positive=set(); all_negative=set()
    for i in range(4):
        t=constructed(s,i)
        plus,minus=incidence(t,s)
        assert minus == {i}, (lam,i,minus)
        assert plus == {(i+2)%4,(i+3)%4}, (lam,i,plus)
        all_positive.update(plus);all_negative.update(minus)
        u=tuple(sum(t[j]*V[j][k] for j in range(4))/4 for k in range(3))
        assert tuple(dot(u,V[j]) for j in range(4))==tuple(t)
        for k in range(8):
            active = [n for _,_,tri,n in f if k in tri]
            from_planes = all(dot(u,n)<0 for n in active)
            from_rule = k in plus if k<4 else (k-4) in minus
            assert from_planes==from_rule
    assert all_positive==all_negative==set(range(4))
    # A sufficiently large symmetric integer sample tests all combinatorial types.
    max_seen=0
    for a,b,c in product(range(-5,6),repeat=3):
        t=[Q(a),Q(b),Q(c),Q(-a-b-c)]
        if not any(t):continue
        plus,minus=incidence(t,s)
        assert len(minus)<=1
        assert len(plus)+len(minus) <= (3 if s>=Q(1,3) else 4)
        max_seen=max(max_seen,len(plus)+len(minus))
    assert max_seen >= 2
    if s < Q(1,3):
        plus,minus=incidence([Q(3),Q(-1),Q(-1),Q(-1)],s)
        assert len(plus)==3 and minus=={0}
    return max_seen

if __name__=='__main__':
    laminas=[Q(1001,1000),Q(11,10),Q(6,5),Q(4,3),Q(3,2),Q(5,3),Q(2),Q(5,2),Q(299,100)]
    maxima=[test(lam) for lam in laminas]
    # The four sign patterns of each tetrahedral orbit form all eight cube corners.
    assert sorted(V+tuple(tuple(-a for a in x) for x in V)) == sorted(product((-1,1),repeat=3))
    # At lambda=3 the four positive generators lie in facets of the negative simplex.
    for lam in (Q(3),Q(4),Q(10)):
        wi=(1-Q(3)/lam)/4
        wo=(1+Q(1)/lam)/4
        assert wi>=0 and wo>0 and wi+3*wo==1
        for i in range(4):
            combo=[wi if j==i else wo for j in range(4)]
            assert all(sum(combo[j]*(-lam)*V[j][k] for j in range(4))==V[i][k] for k in range(3))
    print('EXACT_OK rational_lambdas=',len(laminas),'facet_planes=',len(laminas)*12,
          'four_direction_covers=',len(laminas),'integer_profiles=',len(laminas)*(11**3-1),
          'sample_maxima=',maxima,'cube_corners=8','simplex_endpoints=3')
