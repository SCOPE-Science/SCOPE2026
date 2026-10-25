"""Complete finite certificate for bounded-distance visibility polynomials.

For k=2,3, every valid set has exact bounding-box dimensions at most 4 by 4.
The code enumerates every anchored set and checks geodesics by a strictly
Manhattan-distance-decreasing search. Thus its finite table applies to every
rectangular grid, with no extrapolation or probabilistic step.
"""
from collections import Counter
from itertools import combinations

MOVES = ((1,0),(-1,0),(0,1),(0,-1))


def md(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def reaches(u,v,blocked):
    pending=[u]
    visited={u}
    while pending:
        p=pending.pop()
        if p==v:
            return True
        for di,dj in MOVES:
            q=(p[0]+di,p[1]+dj)
            if q not in blocked and q not in visited and md(q,v)==md(p,v)-1:
                visited.add(q)
                pending.append(q)
    return False


def valid(S,k):
    for u,v in combinations(S,2):
        if md(u,v)>k or not reaches(u,v,S-{u,v}):
            return False
    return True


def profile(h,w,k):
    cell=[(a,b) for a in range(h) for b in range(w)]
    hist=Counter()
    for bits in range(1,1<<(h*w)):
        S={cell[j] for j in range(h*w) if bits&(1<<j)}
        if min(x for x,y in S)!=0 or max(x for x,y in S)!=h-1:continue
        if min(y for x,y in S)!=0 or max(y for x,y in S)!=w-1:continue
        if valid(S,k):hist[len(S)]+=1
    return dict(sorted(hist.items()))

# Entries are exact anchored-set size histograms; for h>w, transpose symmetry.
TABLE={
 2:{(1,1):{1:1},(1,2):{2:1},(1,3):{2:1},(2,2):{2:2,3:4},
    (2,3):{3:2},(3,3):{4:1}},
 3:{(1,1):{1:1},(1,2):{2:1},(1,3):{2:1},(1,4):{2:1},
    (2,2):{2:2,3:4},(2,3):{2:2,3:10,4:1},
    (2,4):{3:4,4:2},(3,3):{3:8,4:25,5:4},
    (3,4):{4:4,5:4,6:1}}
}


def coefficient_formula(m,n,k):
    coeff=Counter({0:1})
    for h in range(1,5):
        for w in range(1,5):
            weights=TABLE[k].get((min(h,w),max(h,w)),{})
            places=max(m-h+1,0)*max(n-w+1,0)
            for degree,multiplicity in weights.items():
                coeff[degree]+=places*multiplicity
    return dict(sorted((i,v) for i,v in coeff.items() if v))


def verify():
    for k in (2,3):
        for h in range(1,5):
            for w in range(1,5):
                actual=profile(h,w,k)
                expected=TABLE[k].get((min(h,w),max(h,w)),{})
                assert actual==expected,(k,h,w,actual,expected)
        print(f'k={k}: exact anchored histograms of all 16 boxes PASS')
    assert coefficient_formula(3,3,2)=={0:1,1:9,2:26,3:24,4:1}
    assert coefficient_formula(3,3,3)=={0:1,1:9,2:34,3:64,4:29,5:4}
    assert coefficient_formula(4,4,3)=={0:1,1:16,2:90,3:212,4:140,5:32,6:4}
    print('All coefficient formulas and displayed test cases PASS')

if __name__=='__main__':verify()
