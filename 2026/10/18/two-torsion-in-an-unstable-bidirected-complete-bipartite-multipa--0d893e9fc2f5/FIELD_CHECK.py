#!/usr/bin/env python3
"""Independent face enumerator and mod-p boundary-rank corroboration."""
from itertools import combinations

def allowed(edges):
    out, inc = {}, {}
    for a,b in edges:
        if a in out or b in inc: return False
        out[a] = b; inc[b] = a
    for start in out:
        seen=set();x=start
        while x in out:
            if x in seen: return False
            seen.add(x); x=out[x]
    return True

def rank(columns,p):
    pivots={}
    for orig in columns:
        column=orig.copy()
        while column:
            j=max(column)
            if j not in pivots:
                unit=pow(column[j],-1,p)
                pivots[j]={t:unit*v%p for t,v in column.items() if unit*v%p}
                break
            scalar=column[j]
            for t,v in pivots[j].items():
                z=(column.get(t,0)-scalar*v)%p
                if z:column[t]=z
                else:column.pop(t,None)
    return len(pivots)

arcs=[(a,2+b) for a in (0,1) for b in range(4)]
arcs += [(2+b,a) for a in (0,1) for b in range(4)]
faces={k:[s for s in combinations(range(16),k)
          if allowed([arcs[j] for j in s])] for k in range(1,5)}
assert [len(faces[k]) for k in range(1,5)]==[16,80,144,72]
idx={k:{s:i for i,s in enumerate(faces[k])} for k in faces}
for p in (2,3,5,7,11):
    ranks={1:1}
    for k in (2,3,4):
        columns=[]
        for face in faces[k]:
            columns.append({idx[k-1][face[:i]+face[i+1:]]:(-1)**i%p
                            for i in range(k)})
        ranks[k]=rank(columns,p)
    betti=(len(faces[2])-ranks[2]-ranks[3],
           len(faces[3])-ranks[3]-ranks[4],
           len(faces[4])-ranks[4])
    expected=(0,8,1) if p==2 else (0,7,0)
    assert betti == expected,(p,betti)
    print('char',p,'boundary ranks', [ranks[k] for k in (2,3,4)],
          'Betti H1,H2,H3', betti)
print('independent finite-field checks passed')
