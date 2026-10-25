"""Independent exact-rational checks for endpoint projections on Steiner-design incidence graphs.

Requires Python 3 and SymPy (tested with 1.13+). No network access needed.
"""
from itertools import combinations, product
from sympy import Matrix, Rational, Symbol, factor, zeros


def affine_plane(q):
    assert q in (2, 3, 5, 7)  # prime field cases used here
    points = list(product(range(q), repeat=2))
    blocks = []
    for slope in range(q):
        for intercept in range(q):
            blocks.append(frozenset((x, (slope*x+intercept) % q) for x in range(q)))
    for abscissa in range(q):
        blocks.append(frozenset((abscissa, y) for y in range(q)))
    return points, blocks


def projective_plane(q):
    assert q in (2, 3)
    candidates = [a for a in product(range(q), repeat=3) if any(a)]
    def normalize(a):
        leading = next(x for x in a if x)
        inv = pow(leading, -1, q)
        return tuple(x * inv % q for x in a)
    points = sorted({normalize(x) for x in candidates})
    lines = sorted({normalize(x) for x in candidates})
    blocks = [frozenset(p for p in points if sum(p[i]*l[i] for i in range(3))%q==0) for l in lines]
    return points, blocks


def cyclic_sts13():
    v = 13
    points = list(range(v))
    seeds = [(0,1,4),(0,2,7)]
    blocks = [frozenset((x+t)%v for x in seed) for seed in seeds for t in range(v)]
    return points, blocks


def all_pairs(v):
    pts=list(range(v))
    return pts,[frozenset(block) for block in combinations(pts,2)]


def check(name, points, blocks):
    v = len(points)
    k = len(blocks[0])
    assert 2 <= k < v and len(set(blocks)) == len(blocks)
    assert all(len(b) == k for b in blocks)
    assert set().union(*blocks) == set(points)
    assert all(sum(a in B and b in B for B in blocks) == 1 for a,b in combinations(points,2))
    r = (v-1)//(k-1)
    assert r*(k-1)==v-1
    assert all(sum(p in B for B in blocks)==r for p in points)
    assert len(blocks)*k==v*r
    idx = {p:i for i,p in enumerate(points)}
    edges = [(idx[p],v+j) for j,B in enumerate(blocks) for p in points if p in B]
    nv = v+len(blocks)
    L=zeros(nv)
    for i,j in edges:
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    # Ground the final block vertex, then use an independent exact inverse.
    H=L[:nv-1,:nv-1].inv()
    incidence = zeros(nv-1,len(edges))
    for c,(i,j) in enumerate(edges):
        if i<nv-1:incidence[i,c]+=1
        if j<nv-1:incidence[j,c]-=1
    Q=incidence.T*H*incidence
    qgoal=Rational(5)-Rational(4,k)-Rational(4*(k-1),v)
    pgoal=Rational(6)-Rational(6,k)-Rational(6*(k-1),v)
    diag=Rational(1,k)+Rational(k-1,v)
    assert Q == Q.T
    assert Q*Q == Q
    for j in range(len(edges)):
        assert Q[j,j]==diag
        assert sum(abs(Q[i,j]) for i in range(len(edges)))==qgoal
        assert sum(abs(int(i==j)-Q[i,j]) for i in range(len(edges)))==pgoal
    print(f'{name}: v={v} k={k} blocks={len(blocks)} edges={len(edges)} '
          f'cut={qgoal} cycle={pgoal} all_columns=PASS')
    return len(edges)


def symbolic_check():
    v,k=Symbol('v'),Symbol('k')
    rminus=(v-k)/(k-1)
    R=(k-1)/v+1/k
    six_current_types = [
        R,
        rminus*(k-1)**2/(v*k),
        (k-1)*(v-k)/(v*k),
        (k-1)*rminus*(k-1)/(v*k),
        rminus*(k-1)*(k-1)/(v*k),
        (k-1)*rminus*(k-1)/(v*k),
    ]
    C=sum(six_current_types)
    assert factor(C-(5-4/k-4*(k-1)/v))==0
    assert factor((1+C-2*R)-(6-6/k-6*(k-1)/v))==0
    assert factor((1+C-2*R)-C-(1-2/k-2*(k-1)/v))==0
    print('symbolic_current_counts=PASS symbolic_norms=PASS dominance=PASS')


def main():
    symbolic_check()
    examples=[('complete-pair-design',all_pairs(5)),
              ('Fano projective plane',projective_plane(2)),
              ('affine plane 3',affine_plane(3)),
              ('cyclic triple system 13',cyclic_sts13()),
              ('projective plane 3',projective_plane(3)),
              ('affine plane 5',affine_plane(5))]
    total=sum(check(name,*data) for name,data in examples)
    print(f'STEINER_INCIDENCE_HODGE_EXACT_OK designs={len(examples)} full_columns={total}')

if __name__=='__main__':
    main()
