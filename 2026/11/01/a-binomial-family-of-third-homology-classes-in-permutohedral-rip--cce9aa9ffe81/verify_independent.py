"""Independent cross-check using discordant-pair distance, direct clique recursion and ROW elimination.
No external packages; exact F_2 arithmetic.
"""
from itertools import permutations, combinations

def all_faces(n):
    words=list(permutations(range(n)))
    pos=[tuple(w.index(i) for i in range(n)) for w in words]
    neigh=[set() for _ in words]
    for i in range(len(words)):
        a=pos[i]
        for j in range(i+1,len(words)):
            b=pos[j]
            discord=0
            for x in range(n):
                for y in range(x+1,n):
                    if (a[x]<a[y])!=(b[x]<b[y]):
                        discord+=1
                        if discord>2: break
                if discord>2:break
            if discord<=2:
                neigh[i].add(j)
                neigh[j].add(i)
    by_dim=[[] for _ in range(n)]
    def extend(prefix, viable):
        if prefix:
            by_dim[len(prefix)-1].append(prefix)
        for index,v in enumerate(viable):
            more=[w for w in viable[index+1:] if w in neigh[v]]
            extend(prefix+(v,),more)
    extend((),list(range(len(words))))
    return [v for v in by_dim if v]

def row_rank(target,domain):
    faces={s:i for i,s in enumerate(target)}
    rows=[0]*len(target)
    for j,c in enumerate(domain):
        mask=1<<j
        for k in range(len(c)):
            rows[faces[c[:k]+c[k+1:]]]^=mask
    pivots={}
    for row in rows:
        while row:
            pivot=row.bit_length()-1
            if pivot in pivots:row ^= pivots[pivot]
            else:
                pivots[pivot]=row
                break
    return len(pivots)

for n in (5,6):
    faces=all_faces(n)
    sizes=tuple(map(len,faces))
    r3=row_rank(faces[2],faces[3]); r4=row_rank(faces[3],faces[4])
    b3=len(faces[3])-r3-r4
    print(f'n={n} f={sizes} row_rank_d3={r3} row_rank_d4={r4} betti3={b3}',flush=True)
    assert (r3,r4,b3)==({5:(570,120,0),6:(8370,3600,90)}[n])
print('INDEPENDENT_CHECK_OK')
