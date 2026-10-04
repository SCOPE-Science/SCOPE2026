from itertools import combinations

def has_mono_triangle(n, mask):
    edges=list(combinations(range(n),2))
    idx={e:i for i,e in enumerate(edges)}
    for a,b,c in combinations(range(n),3):
        vals=[]
        for u,v in [(a,b),(a,c),(b,c)]:
            e=(min(u,v),max(u,v))
            vals.append((mask>>idx[e])&1)
        if vals[0]==vals[1]==vals[2]:
            return True
    return False

# Every red/blue coloring of K6 has a monochromatic triangle.
for mask in range(1 << 15):
    if not has_mono_triangle(6, mask):
        raise SystemExit('counterexample to R_2(3)<=6')

# A 5-cycle coloring of K5 has no monochromatic triangle.
edges=list(combinations(range(5),2))
idx={e:i for i,e in enumerate(edges)}
red={(0,1),(1,2),(2,3),(3,4),(0,4)}
mask=0
for e in red:
    mask |= 1 << idx[tuple(sorted(e))]
if has_mono_triangle(5, mask):
    raise SystemExit('C5 coloring is not critical')

# Calibration of the hypergraph endpoint for k=0,1.
# N(k)=k+(R_{2^k}(3)-1)*2^{binom(k,2)}.
assert 0 + (3-1)*1 == 2
assert 1 + (6-1)*1 == 6
print('VERIFY_OK R2_triangle=6 exhaustive_32768 C5_critical endpoints_k0_1=2_6')
