#!/usr/bin/env python3
"""Reproducible exact checker for geodesic packings of rook graphs."""
from itertools import combinations
from functools import lru_cache

# Zero-based (row, column) coordinates of mutually disjoint three-cell L shapes.
BRICKS = {
    (2, 2): [((0,1),(1,0),(1,1))],
    (2, 3): [((0,0),(1,0),(1,1)), ((0,1),(0,2),(1,2))],
    (3, 3): [((0,0),(1,0),(1,1)), ((0,1),(0,2),(2,1)), ((1,2),(2,0),(2,2))],
    (2, 4): [((0,2),(1,0),(1,2)), ((0,3),(1,1),(1,3))],
    (3, 4): [((0,0),(1,0),(1,1)), ((0,1),(2,0),(2,1)), ((0,2),(1,2),(1,3)), ((0,3),(2,2),(2,3))],
    (4, 4): [((0,1),(1,0),(1,1)), ((0,2),(1,2),(1,3)), ((0,3),(2,0),(2,3)), ((2,1),(3,0),(3,1)), ((2,2),(3,2),(3,3))],
}

def row_parts(m, width):
    if width==3:
        # Every m>=2 is 2a+3b.
        if m % 2==0:return [2]*(m//2)
        return [3]+[2]*((m-3)//2)
    q, r=divmod(m,3)
    if r==0:return [3]*q
    if r==1:return [3]*(q-1)+[4]
    return [3]*q+[2]

def col_parts(n):
    q,r=divmod(n,3)
    if r==0:return [3]*q
    if r==2:return [3]*q+[2]
    return [3]*(q-1)+[4]

def build(m,n):
    assert m>=2 and n>=2
    pack=[]; c=0
    for w in col_parts(n):
        r=0
        for h in row_parts(m,w):
            triples = BRICKS[(w,h)] if (h,w) not in BRICKS else BRICKS[(h,w)]
            transpose=(h,w) not in BRICKS
            for L in triples:
                if transpose: pack.append(tuple((r+col,c+row) for row,col in L))
                else: pack.append(tuple((r+row,c+col) for row,col in L))
            r+=h
        assert r==m
        c+=w
    assert c==n
    return pack

def is_L(cells):
    if len(set(cells))!=3:return False
    # Check pairwise distances in Cartesian product of complete graphs.
    adj=sum(int(x[0]==y[0] or x[1]==y[1]) for x,y in combinations(cells,2))
    return adj==2

def check_pack(m,n,pack):
    used=set()
    for L in pack:
        assert is_L(L), ('not an induced geodesic',m,n,L)
        for row,col in L:
            assert 0<=row<m and 0<=col<n, ('out of bounds',m,n,L)
            assert (row,col) not in used, ('collision',m,n,row,col)
            used.add((row,col))
    assert len(pack)==(m*n)//3, ('not optimal',m,n,len(pack),(m*n)//3)

@lru_cache(None)
def all_geodesics(m,n):
    cells=tuple((i,j) for i in range(m) for j in range(n))
    ans=[]
    for s in combinations(cells,3):
        if is_L(s):
            ans.append(sum(1<<(i*n+j) for i,j in s))
    return tuple(ans)

def exact_gpack(m,n):
    shapes=all_geodesics(m,n)
    by_first=[[] for _ in range(m*n)]
    for shape in shapes:
        for k in range(m*n):
            if (shape>>k)&1:by_first[k].append(shape)
    @lru_cache(None)
    def dp(mask):
        if not mask:return 0
        first=(mask&-mask).bit_length()-1
        best=dp(mask^(1<<first))
        for tri in by_first[first]:
            if mask&tri==tri:best=max(best,1+dp(mask^tri))
        return best
    return dp((1<<(m*n))-1),dp.cache_info().currsize

if __name__=='__main__':
    all_bricks=0
    for (m,n),packing in sorted(BRICKS.items()):
        check_pack(m,n,packing)
        exact,states=exact_gpack(m,n)
        assert len(packing)==exact
        all_bricks+=1
        print('BRICK',m,n,'optimal',exact,'exact_DP_states',states)
    constructed=0
    for m in range(2,61):
        for n in range(2,61):
            check_pack(m,n,build(m,n));constructed+=1
    print('CONSTRUCTED',constructed,'board sizes, all sharp and valid')
    brute=0
    for m in range(2,5):
        for n in range(m,9):
            if m*n>21:continue
            exact,states=exact_gpack(m,n)
            assert exact == (m*n)//3,(m,n,exact)
            brute+=1
            print('BRUTE',m,n,'max',exact,'states',states)
    print('ALL_CHECKS_PASSED','brick_templates',all_bricks,'constructed',constructed,'brute_cases',brute)
