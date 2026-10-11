"""Exact, dependency-free exhaustive certificate for normalized weak tiling in
all five abelian groups of order 16. Python >=3.9. No floating point/LP.
"""
from itertools import combinations, product
from math import gcd
from functools import reduce

GROUP_TYPES=((16,), (8,2), (4,4), (4,2,2), (2,2,2,2))
ALL=(1<<16)-1

def group_table(factors):
    points=list(product(*(range(n) for n in factors)))
    assert len(points)==16 and points[0]==tuple(0 for _ in factors)
    index={p:i for i,p in enumerate(points)}
    addition=[[index[tuple((x+y)%n for x,y,n in zip(a,b,factors))]
               for b in points] for a in points]
    opposite=[index[tuple((-x)%n for x,n in zip(a,factors))] for a in points]
    return addition,opposite

def inconsistent_over_q(matrix):
    """Exact integer row reduction: test M*c=ones for any rational c."""
    if not matrix:
        return False
    width=len(matrix[0])-1
    rows=[list(map(int,row)) for row in matrix]
    assert all(len(row)==width+1 for row in rows)
    lead=0
    for col in range(width):
        pivot=next((i for i in range(lead,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[lead],rows[pivot]=rows[pivot],rows[lead]
        top=rows[lead]
        for i in range(lead+1,len(rows)):
            entry=rows[i][col]
            if entry==0:continue
            mult=top[col]
            rows[i]=[0 if j<=col else mult*rows[i][j]-entry*top[j]
                     for j in range(width+1)]
            divisor=reduce(gcd,(abs(v) for v in rows[i]),0)
            if divisor>1:rows[i]=[v//divisor for v in rows[i]]
        lead+=1
        if lead==len(rows):break
    return any(all(v==0 for v in row[:width]) and row[-1]!=0
               for row in rows)

def check(factors):
    add,neg=group_table(factors)
    counts={}
    for size in range(1,17):
        total=0; cover=0; tilings=0; exact_obstructions=0
        for rest in combinations(range(1,16),size-1):
            A=(0,)+rest
            total+=1
            amask=sum(1<<a for a in A)
            diffset={add[a][neg[b]] for a in A for b in A}
            shifts=[t for t in range(1,16) if t not in diffset]
            blocks={t:sum(1<<add[a][t] for a in A) for t in shifts}
            reach=amask
            for b in blocks.values():reach|=b
            if reach!=ALL:
                continue  # no candidate translates can cover G\A
            cover+=1
            # Try an actual tiling containing shift 0; use exact bitsets.
            tiled=False
            if 16%size==0:
                for B in combinations(shifts,16//size-1):
                    union=amask
                    for t in B:union|=blocks[t]
                    if union==ALL:
                        tiled=True
                        break
            if tiled:
                tilings+=1
                continue
            # With h(0)=1 and h>=0, support h\{0} avoids A-A.
            # On G\A the convolution equation is M c = ones.
            # Show impossibility over Q (thus over R for rational data).
            rows=[[int(bool(blocks[t]&(1<<x))) for t in shifts]+[1]
                  for x in range(16) if x not in A]
            assert inconsistent_over_q(rows), (factors,A,shifts)
            exact_obstructions+=1
        counts[size]=(total,cover,tilings,exact_obstructions)
    assert sum(v[0] for v in counts.values())==2**15
    return counts

def main():
    total=0
    for group in GROUP_TYPES:
        counts=check(group)
        total+=sum(v[0] for v in counts.values())
        print(group,[(n,*vals) for n,vals in counts.items() if vals[2] or vals[3]])
    assert total==5*(2**15)
    print('VERIFIED: every normalized weak tile in every abelian group of order 16 tiles.')
    print('NORMALIZED_SUBSETS_CHECKED=',total)
if __name__=='__main__':main()
