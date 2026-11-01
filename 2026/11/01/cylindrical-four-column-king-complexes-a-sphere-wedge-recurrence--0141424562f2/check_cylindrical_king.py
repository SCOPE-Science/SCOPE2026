#!/usr/bin/env python3
"""Reproducible finite checks for cylindrical four-column king graphs.

Only Python standard-library modules are used. Infinite statements in the
accompanying proof follow from locally verified graph-neighborhood identities.
"""
from collections import defaultdict
from functools import lru_cache

FULL = 15
# (prefix of row masks, kind, u, v, [(new_prefix, change in full-row count)])
# Vertex indices are 4*row+column; rows and columns begin at zero.
RULES = [
    ((), 'closed', 0, 4, [((15, 14), -2), ((4, 4, 4), -3)]),
    ((15, 14), 'open', 0, 2, [((11, 14), 0)]),
    ((4, 4, 4), 'open', 2, 10, [((4, 4, 0), 0)]),
    ((11, 14), 'open', 0, 6, [((11, 10), 0)]),
    ((4, 4, 0), 'closed', 2, 6, [((4, 0, 0), 0), ((), 0)]),
    ((11, 10), 'closed', 1, 0, [((10, 10), 0), ((), 0)]),
    ((4, 0, 0), 'cone', None, None, []),
    ((10, 10), 'open', 1, 8, [((10, 10, 14), -1)]),
    ((10, 10, 14), 'open', 1, 9, [((10, 10, 12), 0)]),
    ((10, 10, 12), 'open', 1, 10, [((10, 10, 8), 0)]),
    ((10, 10, 8), 'open', 3, 11, [((10, 10, 0), 0)]),
    ((10, 10, 0), 'closed', 1, 5, [((10, 8, 0), 0), ((8, 8, 0), 0)]),
    ((10, 8, 0), 'cone', None, None, []),
    ((8, 8, 0), 'closed', 3, 7, [((8, 0, 0), 0), ((), 0)]),
    ((8, 0, 0), 'cone', None, None, []),
]

def adjacent(i, j):
    if i == j: return False
    r, c = divmod(i, 4)
    s, d = divmod(j, 4)
    return abs(r-s) <= 1 and (d-c) % 4 in (0, 1, 3)

def adjacency(number_rows):
    return [sum(1 << j for j in range(4*number_rows) if adjacent(i,j))
            for i in range(4*number_rows)]

def to_mask(word):
    return sum(x << (4*i) for i, x in enumerate(word))

def canonical(mask, number_rows):
    rows = [(mask >> (4*i)) & 15 for i in range(number_rows)]
    while rows and rows[0] == 0: rows.pop(0)
    while rows and rows[-1] == 0: rows.pop()
    count = 0
    while rows and rows[-1] == FULL:
        rows.pop()
        count += 1
    return tuple(rows), count

def check_rules():
    count = 0
    for prefix, kind, u, v, expected in RULES:
        for m in range(2, 9):
            # The bare-full-row rule needs at least three rows.
            if not prefix and m < 3: continue
            word = prefix + (FULL,)*m
            n = len(word)
            M = to_mask(word)
            A = adjacency(n)
            vertices = [k for k in range(4*n) if M & (1 << k)]
            N = {k: A[k] & M for k in vertices}
            if kind == 'cone':
                assert any(N[k] == 0 for k in vertices), (prefix,m)
                count += 1
                continue
            assert u in N and v in N and u != v
            if kind == 'open':
                assert N[u] & ~N[v] == 0, (prefix, m, u, v)
                masks = [M ^ (1 << v)]
            elif kind == 'closed':
                assert (N[u] | (1 << u)) & ~(N[v] | (1 << v)) == 0
                masks = [M ^ (1 << v), M & ~(N[v] | (1 << v))]
            else:
                raise AssertionError(kind)
            actual = [(p, k-m) for p,k in (canonical(Y,n) for Y in masks)]
            assert actual == expected, (prefix,m,kind,actual,expected)
            count += 1
    return count


def add(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))
def shift(a):
    return (0,) + a if a else ()


def homotopy_polynomial(n):
    """Exact finite wedge decomposition via open/closed folding (augmented degree)."""
    A = adjacency(n)
    calls = {'open':0,'closed':0,'cone':0}
    @lru_cache(maxsize=None)
    def rec(M):
        if M == 0: return (1,) # formal S^{-1}
        vertices = [i for i in range(4*n) if M & (1<<i)]
        N = {i:A[i]&M for i in vertices}
        if any(N[i] == 0 for i in vertices):
            calls['cone'] += 1
            return ()
        for u in vertices:
            for v in vertices:
                if u != v and N[u] & ~N[v] == 0:
                    calls['open'] += 1
                    return rec(M ^ (1 << v))
        for u in vertices:
            for v in vertices:
                if u != v and (N[u]|(1<<u))&~(N[v]|(1<<v)) == 0:
                    calls['closed'] += 1
                    return add(rec(M^(1<<v)),shift(rec(M&~(N[v]|(1<<v)))))
        raise AssertionError('No homotopy-preserving graph move at '+str(M))
    p=rec((1<<(4*n))-1)
    assert calls['open']+calls['closed']+calls['cone'] > 0
    return p, calls


def independent_faces(n, fixed=False):
    if fixed:
        # Orbit graph of the antipodal two-column-pair involution:
        # a clique on each pair of adjacent P_n row fibres.
        length=2*n
        A=[sum(1<<j for j in range(length)
               if i!=j and abs(i//2-j//2)<=1) for i in range(length)]
    else:
        length=4*n
        A=adjacency(n)
    faces=[0]
    for v in range(length):
        faces += [s|(1<<v) for s in faces if s&A[v]==0]
    return faces

def reduced_betti_mod2(n, fixed=False):
    faces=independent_faces(n, fixed)
    by=defaultdict(list)
    for s in faces:
        by[s.bit_count()-1].append(s)
    ranks={-1:1}
    for d in range(0,max(by)+1):
        below={s:i for i,s in enumerate(by[d-1])}
        pivots={}
        for face in by[d]:
            boundary=0
            rem=face
            while rem:
                low=rem&-rem; rem ^= low
                boundary ^= 1<<below[face ^ low]
            while boundary:
                p=boundary.bit_length()-1
                if p not in pivots:
                    pivots[p]=boundary;break
                boundary ^= pivots[p]
        ranks[d]=len(pivots)
    out={}
    for d in range(0,max(by)+1):
        value=len(by[d])-ranks[d]-ranks.get(d+1,0)
        if value: out[d+1]=value
    return tuple(out.get(i,0) for i in range(max(out,default=-1)+1)),len(faces)


def verify():
    count=check_rules()
    print('Template-neighborhood cases checked:',count)
    # The first five base values are finite, exact homotopy computations.
    bases={1:(0,1), 2:(0,1,2), 3:(0,0,3),
           4:(0,0,1,4), 5:(0,0,0,5,4)}
    poly={0:(1,)}
    for n in range(1,14):
        if n<=5:
            direct,steps=homotopy_polynomial(n)
            assert direct == bases[n], (n,direct,bases[n])
            poly[n]=direct
            print('Base',n, 'reduced Betti by degree',[(i-1,a) for i,a in enumerate(direct) if a])
        else:
            poly[n]=add(shift(poly[n-2]),shift(shift(add(poly[n-3],poly[n-3]))))
        if n <= 9:
            direct,faces=reduced_betti_mod2(n)
            assert direct == poly[n],(n,direct,poly[n])
            fixed_direct,fixed_faces=reduced_betti_mod2(n, fixed=True)
            assert sum(fixed_direct)==sum(poly[n]),(n,fixed_direct,poly[n])
            print('Direct F2 boundary',n,'cylinder_faces',faces,'fixed_faces',fixed_faces,'passed')
        if n in range(6,12):
            actual,steps=homotopy_polynomial(n)
            assert actual==poly[n],(n,actual,poly[n])
            print('Exact finite homotopy graph reductions',n,'passed')
    # Published P_n strong P_2 recurrence: B1=1, B2=3, B3=3.
    fixed={1:1,2:3,3:3}
    for n in range(4,14): fixed[n]=fixed[n-2]+2*fixed[n-3]
    for n in range(1,14):
        assert sum(poly[n]) == fixed[n],(n,poly[n],fixed[n])
    print('Smith equality of total Betti ranks: n=1,...,13 PASSED')
    print('All independent checks passed.')

if __name__=='__main__': verify()
