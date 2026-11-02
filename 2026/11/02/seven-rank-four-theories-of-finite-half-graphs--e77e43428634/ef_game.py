#!/usr/bin/env python3
"""Independent four-move Ehrenfeucht–Fraisse adversarial game checker.

Checks critical finite boundary using minimax with memoization. Repeated
Spoiler choices are harmless because corresponding selected vertices are
already paired by a partial isomorphism, so they can be skipped safely.
Run: python3 ef_game.py
"""
from functools import lru_cache

def half_graph(n):
    return tuple(tuple((x<n and y>=n and x<=y-n) or
                       (y<n and x>=n and y<=x-n)
                       for y in range(2*n)) for x in range(2*n))

def duplicator_wins(a,b,rounds=4):
    grids=(half_graph(a),half_graph(b))
    dimensions=(2*a,2*b)
    @lru_cache(None)
    def winning(A,B):
        if len(A)==rounds:
            return True
        for side in (0,1):
            src = A if side==0 else B
            dst = B if side==0 else A
            for x in range(dimensions[side]):
                if x in src:
                    continue
                successful_reply=False
                for y in range(dimensions[1-side]):
                    if y in dst:
                        continue
                    if all(grids[side][x][src[j]]==grids[1-side][y][dst[j]]
                           for j in range(len(src))):
                        nxt = (A+(x,),B+(y,)) if side==0 else (A+(y,),B+(x,))
                        if winning(*nxt):
                            successful_reply=True
                            break
                if not successful_reply:
                    return False
        return True
    answer=winning((),())
    print(f'EF{rounds} H{a} H{b}: {answer}; states={winning.cache_info().currsize}')
    return answer

def main():
    assert not duplicator_wins(4,5)
    assert not duplicator_wins(5,6)
    assert not duplicator_wins(6,7)
    assert duplicator_wins(7,8)
    print('INDEPENDENT_EF_BOUNDARY_CHECKS_PASS')
if __name__=='__main__':
    main()
