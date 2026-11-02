"""Exact online-shattering trees for pairwise comparisons of length-three-pattern avoiders.

Uses only Python 3's standard library. Run: python compute_dimensions.py
The output SHATTERING_TREES.json contains concrete complete binary witnesses.
"""
from itertools import permutations, combinations
from functools import lru_cache
from pathlib import Path
import json

PATTERNS = ((1,2,3), (1,3,2))
VALUES = {(1,2,3): (2,3,4,6,7,9), (1,3,2): (2,3,5,6,8,9)}

def avoids(p, q):
    """q avoids pattern p; compare ranks by counting lower members."""
    for a,b,c in combinations(q, 3):
        ranks = (1+(a>b)+(a>c), 1+(b>a)+(b>c), 1+(c>a)+(c>b))
        if ranks == p:
            return False
    return True

def source(n, pattern):
    perms = [p for p in permutations(range(1,n+1)) if avoids(pattern,p)]
    queries = list(combinations(range(1,n+1),2))
    masks = []
    for a,b in queries:
        masks.append(sum(1<<i for i,p in enumerate(perms) if p.index(a)<p.index(b)))
    return perms,queries,masks

def solve(n, pattern):
    perms,queries,masks = source(n,pattern)
    full=(1<<len(perms))-1
    @lru_cache(maxsize=None)
    def can(B,depth):
        if depth == 0:
            return B != 0
        if B.bit_count() < (1<<depth):
            return False
        for m in masks:
            b1=B&m; b0=B^b1
            if min(b0.bit_count(),b1.bit_count()) < (1<<(depth-1)):
                continue
            if can(b0,depth-1) and can(b1,depth-1):
                return True
        return False
    def witness(B,depth):
        if depth==0:
            return ["L", (B & -B).bit_length()-1]
        for (a,b),m in zip(queries,masks):
            b1=B&m; b0=B^b1
            if min(b0.bit_count(),b1.bit_count()) < (1<<(depth-1)):
                continue
            if can(b0,depth-1) and can(b1,depth-1):
                return ["Q",a,b,witness(b0,depth-1),witness(b1,depth-1)]
        raise AssertionError('no shattering tree at requested depth')
    depth = VALUES[pattern][n-3]
    assert can(full,depth) and not can(full,depth+1)
    tree=witness(full,depth)
    return {"pattern":''.join(map(str,pattern)), "n":n, "class_size":len(perms),
            "depth":depth, "upper_depth_test":depth+1,
            "exact_upper_test":not can(full,depth+1), "states_visited":can.cache_info().currsize,
            "tree":tree}

def main():
    records=[solve(n,p) for p in PATTERNS for n in range(3,9)]
    root=Path(__file__).resolve().parent
    (root/'SHATTERING_TREES.json').write_text(json.dumps({"schema_version":1,
        "query_convention":"Q,a,b,left(0:a follows b),right(1:a precedes b); L,index in lexicographic avoiding permutations",
        "records":records}, separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf-8')
    for r in records:
        print('GENERATED',r['pattern'],r['n'],r['class_size'],r['depth'],r['states_visited'])

if __name__=='__main__':main()
