#!/usr/bin/env python3
"""Reproduce the six finite brick certificates and deterministic tilings.

Usage: python3 verify.py
No third-party dependencies or external resources.
"""
from itertools import combinations

# A digit occurring exactly three times identifies one shortest path;
# a dot is an uncovered vertex. Entries encode cells, not graph edges.
BRICKS = {
    (3, 3): ('122', '311', '233'),
    (3, 4): ('1234', '1234', '2143'),
    (3, 5): ('12332', '45453', '51214'),
    (4, 4): ('1234', '5451', '.521', '3423'),
    (4, 5): ('12334', '25241', '1.6.6', '56543'),
    (5, 5): ('1.123', '45234', '65671', '77826', '84538'),
}


def adjacent(a, b):
    return a[0] != b[0] and a[1] != b[1]


def check_path(triple):
    if len(triple) != 3 or len(set(triple)) != 3:
        return False
    return sum(adjacent(a,b) for a,b in combinations(triple,2)) == 2


def brick(a,b):
    if (a,b) in BRICKS:
        rows = BRICKS[a,b]
    elif (b,a) in BRICKS:
        source=BRICKS[b,a]
        rows = tuple(''.join(source[j][i] for j in range(b)) for i in range(a))
    else:
        raise ValueError((a,b))
    assert len(rows)==a and all(len(x)==b for x in rows)
    groups={}
    for i,row in enumerate(rows):
        for j,s in enumerate(row):
            if s != '.': groups.setdefault(s,[]).append((i,j))
    assert len(groups)==(a*b)//3
    assert all(check_path(p) for p in groups.values())
    assert len(set(pt for p in groups.values() for pt in p))==3*len(groups)
    return tuple(tuple(p) for p in groups.values())


def parts(k):
    if k < 3: raise ValueError(k)
    if k%3 == 0: return [3]*(k//3)
    if k%3 == 1: return [4]+[3]*((k-4)//3)
    return [5]+[3]*((k-5)//3)


def packing(m,n):
    p=[]
    offset_i=0
    for a in parts(m):
        offset_j=0
        for b in parts(n):
            for triple in brick(a,b):
                p.append(tuple((i+offset_i,j+offset_j) for i,j in triple))
            offset_j+=b
        assert offset_j==n
        offset_i+=a
    assert offset_i==m
    return p


def enumerate_all_induced_paths(m,n):
    triples=[]
    for ids in combinations(range(m*n),3):
        p=tuple(divmod(q,n) for q in ids)
        if check_path(p): triples.append(ids)
    return triples


def find_disjoint_triples_independently(m,n):
    size=m*n; target=size//3
    triples=enumerate_all_induced_paths(m,n)
    by_vertex=[[] for _ in range(size)]
    for pp in triples:
        bitset=sum(1<<q for q in pp)
        for q in pp: by_vertex[q].append(bitset)
    full=(1<<size)-1
    failed=set()
    def go(remaining, count):
        if count==target: return ()
        if remaining.bit_count()<3*(target-count): return None
        if (remaining,count) in failed: return None
        v=(remaining & -remaining).bit_length()-1
        for mask in by_vertex[v]:
            if remaining & mask == mask:
                z=go(remaining ^ mask,count+1)
                if z is not None: return (mask,)+z
        if remaining.bit_count()>3*(target-count):
            z=go(remaining ^ (1<<v),count)
            if z is not None:return z
        failed.add((remaining,count))
        return None
    answer=go(full,0)
    assert answer is not None, (m,n)
    return len(triples),len(failed)


def main():
    for a,b in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)]:
        paths=brick(a,b)
        print('BRICK_OK',a,b,'paths',len(paths),'uncovered',a*b-3*len(paths))
    counter=0
    for m in range(3,51):
        for n in range(3,51):
            p=packing(m,n)
            assert len(p)==m*n//3
            used=set()
            for path in p:
                assert check_path(path)
                for i,j in path:
                    assert 0<=i<m and 0<=j<n and (i,j) not in used
                    used.add((i,j))
            assert len(used)==3*(m*n//3)
            counter+=1
    print('TILING_OK',counter,'rectangles, sizes 3..50 x 3..50')
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5)]:
        num,dead=find_disjoint_triples_independently(m,n)
        print('INDEPENDENT_PATH_SEARCH_OK',m,n,'available_triples',num,'unsuccessful_states',dead)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
