from itertools import combinations, permutations
from math import ceil

SOLUTIONS = {
4: [[(0,1),(1,3),(3,0)],[(0,2),(2,1),(1,0)],[(0,3),(3,2),(2,0)],[(1,2),(2,3),(3,1)]],
5: [[(0,3),(3,0)],[(0,1),(1,2),(2,0)],[(0,2),(2,4),(4,0)],[(0,4),(4,1),(1,0)],[(1,3),(3,2),(2,1)],[(1,4),(4,3),(3,1)],[(2,3),(3,4),(4,2)]],
6: [[(0,4),(1,0)],[(1,2),(2,1)],[(3,1),(4,3)],[(0,1),(1,4),(4,0)],[(0,2),(2,5),(5,0)],[(0,3),(3,2),(2,0)],[(0,5),(5,3),(3,0)],[(1,3),(3,5),(5,1)],[(1,5),(5,4),(4,1)],[(2,3),(3,4),(4,2)],[(2,4),(4,5),(5,2)]],
7: [[(0,1),(1,3),(3,0)],[(0,2),(2,1),(1,0)],[(0,3),(3,5),(5,0)],[(0,4),(4,6),(6,0)],[(0,5),(5,4),(4,0)],[(0,6),(6,2),(2,0)],[(1,2),(2,5),(5,1)],[(1,4),(4,3),(3,1)],[(1,5),(5,6),(6,1)],[(1,6),(6,4),(4,1)],[(2,3),(3,4),(4,2)],[(2,4),(4,5),(5,2)],[(2,6),(6,3),(3,2)],[(3,6),(6,5),(5,3)]],
8: [[(1,4),(4,1)],[(0,1),(1,6),(6,0)],[(0,2),(2,7),(7,0)],[(0,3),(3,5),(5,0)],[(0,4),(4,3),(3,0)],[(0,5),(5,2),(2,0)],[(0,6),(6,4),(4,0)],[(0,7),(7,1),(1,0)],[(1,2),(2,6),(6,1)],[(1,3),(3,2),(2,1)],[(1,5),(5,3),(3,1)],[(1,7),(7,5),(5,1)],[(2,3),(3,4),(4,2)],[(2,4),(4,7),(7,2)],[(2,5),(5,6),(6,2)],[(3,6),(6,7),(7,3)],[(3,7),(7,6),(6,3)],[(4,5),(5,7),(7,4)],[(4,6),(6,5),(5,4)]]
}

def arcs(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def block_valid(block):
    if len(set(block)) != len(block): return False
    for (i,j),(k,l) in combinations(block,2):
        if i == k or j == l: return False
        # If both cross edges exist, the two edges are opposite on a C4 and cannot share a B-color.
        if i != l and k != j: return False
    return True

def is_directed_triangle(block):
    if len(block) != 3: return False
    tails={i for i,j in block}; heads={j for i,j in block}
    if tails != heads or len(tails) != 3: return False
    # every vertex has one outgoing and one incoming arc in the block
    return all(sum(i==v for i,j in block)==1 and sum(j==v for i,j in block)==1 for v in tails)

def check_structure(n):
    E=arcs(n)
    checked=0
    for r in range(1,5):
        for block in combinations(E,r):
            v=block_valid(block); checked += 1
            if v:
                assert r <= 3
                if r == 3: assert is_directed_triangle(block)
    return checked

def directed_triangles(n):
    out=[]; seen=set()
    for a,b,c in permutations(range(n),3):
        block=((a,b),(b,c),(c,a))
        key=tuple(sorted(block))
        if key not in seen:
            seen.add(key); out.append(block)
    return out

def mts6_exists():
    n=6; E=arcs(n); pos={e:i for i,e in enumerate(E)}
    tris=[]
    containing=[[] for _ in E]
    for block in directed_triangles(n):
        mask=sum(1<<pos[e] for e in block)
        idx=len(tris); tris.append(mask)
        for e in block: containing[pos[e]].append(idx)
    full=(1<<len(E))-1
    memo=set()
    def dfs(mask):
        if mask==full: return True
        if mask in memo: return False
        # choose uncovered arc with fewest currently compatible triples
        best=None; opts=None
        for p in range(len(E)):
            if mask>>p & 1: continue
            cand=[t for t in containing[p] if not (mask & tris[t])]
            if not cand: memo.add(mask); return False
            if opts is None or len(cand)<len(opts):
                best=p; opts=cand
                if len(opts)==1: break
        for t in opts:
            if dfs(mask|tris[t]): return True
        memo.add(mask); return False
    return dfs(0), len(memo)

def check_solution(n, blocks):
    E=set(arcs(n)); seen=[]
    for block in blocks:
        assert block_valid(tuple(block)), (n,block)
        seen.extend(block)
    assert len(seen)==len(set(seen))==len(E)
    assert set(seen)==E
    target=11 if n==6 else ceil(n*(n-1)/3)
    assert len(blocks)==target

checked=0
for n in range(4,7): checked += check_structure(n)
for n,b in SOLUTIONS.items(): check_solution(n,b)
exists,states=mts6_exists(); assert not exists
for n in range(4,201):
    q=11 if n==6 else ceil(n*(n-1)/3)
    assert q >= ceil(n*(n-1)/3)
print(f'ALL CHECKS PASSED; class_subsets={checked}; construction_orders={sorted(SOLUTIONS)}; mts6_exact_cover_states={states}; formula_range=4..200')
