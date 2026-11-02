#!/usr/bin/env python3
"""Independent adversarial three-move game solver for finite 2-regular graph test cases."""
from functools import lru_cache
from itertools import combinations

REPS=[(3,),(4,),(5,),(3,3),(6,),(7,),(3,4),(4,4),(3,5),(4,5),(3,3,3),(3,4,5)]

def adjacency(parts):
    n=sum(parts); A=[[0]*n for _ in range(n)];off=0
    for m in parts:
        for i in range(m):
            x=off+i;y=off+(i+1)%m
            A[x][y]=A[y][x]=1
        off+=m
    return A

def game(A,B,rounds=3):
    m=len(A);n=len(B)
    @lru_cache(None)
    def win(xs,ys):
        for i in range(len(xs)):
            for j in range(i):
                if (xs[i]==xs[j])!=(ys[i]==ys[j]):return False
                if A[xs[i]][xs[j]] != B[ys[i]][ys[j]]: return False
        if len(xs)==rounds:return True
        for x in range(m):
            if not any(win(xs+(x,),ys+(y,)) for y in range(n)):return False
        for y in range(n):
            if not any(win(xs+(x,),ys+(y,)) for x in range(m)):return False
        return True
    return win((),())

def main():
    As=[adjacency(x) for x in REPS]
    for i,j in combinations(range(len(REPS)),2):
        assert not game(As[i],As[j]),(REPS[i],REPS[j])
    pairs=[((7,),(8,)), ((7,),(5,5)),((3,4),(3,3,4)),((3,5),(3,6)),((4,4),(4,4,4)),((3,3,3),(3,3,3,3)), ((3,4,5),(3,4,6)),((5,5),(7,)),((4,5),(4,6)),((6,7),(7,))]
    for a,b in pairs:
        assert game(adjacency(a),adjacency(b)),(a,b)
    print('INDEPENDENT_THREE_ROUND_GAME_OK','distinct_representatives',len(REPS),'pairwise_inequivalences',66,'extra_equivalences',len(pairs))

if __name__=='__main__':main()
