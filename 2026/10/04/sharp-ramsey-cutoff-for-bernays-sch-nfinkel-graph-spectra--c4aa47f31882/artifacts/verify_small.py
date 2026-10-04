from itertools import combinations

def homogeneous_subset_exists(n,l,mask):
    edges=list(combinations(range(n),2))
    idx={e:i for i,e in enumerate(edges)}
    for S in combinations(range(n),l):
        vals=[(mask>>idx[(min(a,b),max(a,b))])&1 for a,b in combinations(S,2)]
        if all(v==vals[0] for v in vals):
            return True
    return False

for mask in range(1<<15):
    if not homogeneous_subset_exists(6,3,mask):
        raise SystemExit("counterexample on 6")

edges=list(combinations(range(5),2))
idx={e:i for i,e in enumerate(edges)}
cycle={(0,1),(1,2),(2,3),(3,4),(0,4)}
mask=0
for e in cycle:
    mask |= 1<<idx[tuple(sorted(e))]
if homogeneous_subset_exists(5,3,mask):
    raise SystemExit("C5 is not Ramsey-critical")
print("VERIFY_OK R33=6 exhaustive_32768 C5_critical")
