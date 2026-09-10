"""Step 1-2: genericity + lingering-path enumeration for (g,r,d)=(6,1,5), l=12,m=1.
Stdlib only. Prints auditable results and writes point/table files."""
from fractions import Fraction
from itertools import product

g, r, d = 6, 1, 5
ell, m = 12, 1
N = ell + m  # 13

# Step 1: genericity: no l_i/m_i == a/b with a,b>=1, a+b<=2g-2=10
S = [(a,b) for a in range(1, 2*g-1) for b in range(1, 2*g-1) if a+b <= 2*g-2]
target = Fraction(ell, m)
hits = [(a,b) for (a,b) in S if Fraction(a,b) == target]
print(f"g={g} 2g-2={2*g-2} top={ell} bottom={m} total={N}")
print(f"candidate ratios a/b (a+b<={2*g-2}): {len(S)} pairs; max={max(Fraction(a,b) for a,b in S)}")
print(f"hits of 12/1: {hits} -> GENERIC={len(hits)==0}")

# Step 2: lingering paths in Z^1. p0=(d0,), steps in {-1,+1,0}; rank>=1 iff all p_i>=1.
rho = g - (r+1)*(g-d+r)
print(f"rho={rho}")
def valid_paths():
    out = []
    for d0 in range(0, d+1):
        for steps in product([-1,0,1], repeat=g):
            p = d0
            ok = True
            for s in steps:
                p = p + s
                if p < 1:  # leaves open Weyl chamber C={y>0}
                    ok = False; break
            if not ok: continue
            # degree check: #down steps a must equal g-d+d0
            a = steps.count(-1)
            if a != g-d+d0: continue
            out.append((d0, steps))
    return out

paths = valid_paths()
print(f"total valid (rank>=1) v0-reduced paths: {len(paths)}")
from collections import Counter
c = Counter()
for d0, steps in paths:
    b = steps.count(1); z = steps.count(0)
    c[(d0, b, z)] += 1
print("(d0,#up,#linger): count")
for k in sorted(c): print(" ", k, c[k])
# components: exactly rho=2 lingers
comp = [(d0,s) for d0,s in paths if s.count(0)==2]
print(f"paths with exactly 2 lingers (components): {len(comp)}")
# positions of lingers
pos = Counter()
for d0,s in comp:
    L = tuple(i+1 for i,v in enumerate(s) if v==0)
    pos[L]+=1
print(f"distinct linger-position pairs: {len(pos)}")
# Show pairs involving loop 3
print("linger pairs containing loop 3:")
for L in sorted(pos):
    if 3 in L: print(" ", L, "count(paths)=", pos[L])
# Exhibit named circle T: two paths sharing free loop 3 + fixed other steps.
# Take linger pair {3,5}: paths with lingers at loops 3 and 5.
cand = [(d0,s) for d0,s in comp if {i+1 for i,v in enumerate(s) if v==0}=={3,5}]
print(f"paths lingering exactly at {{3,5}}: {len(cand)}")
for d0,s in cand: print("  d0=",d0,"steps=",s)
