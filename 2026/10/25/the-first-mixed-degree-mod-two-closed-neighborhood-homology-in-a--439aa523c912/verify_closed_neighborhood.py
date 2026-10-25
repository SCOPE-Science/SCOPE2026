"""Exact, independent GF(2) homology checks for the closed-neighborhood complex
of categorical products K_3 x K_n. Python standard library only.
"""
from itertools import combinations
from collections import defaultdict

EXPECTED = {
    2: ([6, 12, 6], [0, 5, 6], {1: 1}),
    3: ([9, 36, 78, 45, 9], [0, 8, 28, 36, 9], {2: 14}),
    4: ([12, 66, 216, 366, 252, 84, 12], [0, 11, 55, 161, 180, 72, 12], {3: 25}),
    5: ([15, 105, 450, 1155, 1650, 1230, 540, 135, 15],
        [0, 14, 91, 359, 796, 810, 420, 120, 15], {4: 44}),
    6: ([18, 153, 810, 2700, 5598, 7026, 5580, 2925, 990, 198, 18],
        [0, 17, 136, 674, 2026, 3525, 3465, 2115, 810, 180, 18],
        {4: 47, 5: 36})
}

def tuple_complex(n):
    faces = defaultdict(set)
    for i in range(3):
        for j in range(n):
            ball = sorted({i*n+j} | {
                a*n+b for a in range(3) for b in range(n)
                if a != i and b != j})
            for s in range(1, len(ball)+1):
                faces[s-1].update(combinations(ball, s))
    return faces

def rank_as_sets(columns):
    pivots = {}
    for col in columns:
        v = frozenset(col)
        while v:
            lead = max(v)
            if lead not in pivots:
                pivots[lead] = v
                break
            v = v.symmetric_difference(pivots[lead])
    return len(pivots)

def compute_tuples(n):
    faces = tuple_complex(n)
    ranks = {}
    for k in sorted(faces):
        if k == 0: continue
        prev = {face: ix for ix, face in enumerate(sorted(faces[k-1]))}
        columns = []
        for sigma in sorted(faces[k]):
            columns.append(frozenset(prev[sigma[:i]+sigma[i+1:]]
                                     for i in range(len(sigma))))
        ranks[k] = rank_as_sets(columns)
    fvec = [len(faces[k]) for k in sorted(faces)]
    rvec = [ranks.get(k, 0) for k in sorted(faces)]
    betti = {k:len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)
             for k in sorted(faces)}
    return fvec, rvec, betti

def masks_complex(n):
    faces = defaultdict(set)
    for i in range(3):
        for j in range(n):
            mask = sum(1 << (a*n+b) for a in range(3) for b in range(n)
                       if (a==i and b==j) or (a!=i and b!=j))
            subset = mask
            while subset:
                faces[subset.bit_count()-1].add(subset)
                subset = (subset-1)&mask
    return faces

def rank_bits(columns):
    pivots = {}
    for col in columns:
        while col:
            lead = col.bit_length()-1
            if lead not in pivots:
                pivots[lead] = col
                break
            col ^= pivots[lead]
    return len(pivots)

def compute_masks(n):
    faces=masks_complex(n)
    ranks={}
    for k in sorted(faces):
        if k == 0: continue
        prev={face:ix for ix,face in enumerate(sorted(faces[k-1]))}
        cols=[]
        for face in sorted(faces[k]):
            col=0; remaining=face
            while remaining:
                bit=remaining & -remaining
                remaining-=bit
                col ^= 1<<prev[face ^ bit]
            cols.append(col)
        ranks[k]=rank_bits(cols)
    fvec=[len(faces[k]) for k in sorted(faces)]
    rvec=[ranks.get(k,0) for k in sorted(faces)]
    betti={k:len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)
           for k in sorted(faces)}
    return fvec,rvec,betti

if __name__=='__main__':
    for n in range(2,7):
        tuple_output=compute_tuples(n)
        mask_output=compute_masks(n)
        f,r,b=tuple_output
        reduced={k:v for k,v in b.items() if k>0 and v}
        assert b[0]==1, (n,b)
        assert (f,r,reduced)==EXPECTED[n], (n, f, r, reduced)
        assert tuple_output==mask_output, n
        assert sum((-1)**k*count for k,count in enumerate(f)) == \
            sum((-1)**k*count for k,count in b.items()), n
        print('n',n, 'faces',f, 'boundary ranks',r, 'reduced positive Betti',reduced)
    print('All complete finite GF(2) checks passed by both implementations.')
