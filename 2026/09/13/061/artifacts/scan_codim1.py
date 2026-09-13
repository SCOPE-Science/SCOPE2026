"""Test char poly machinery; then scan corank-1 restrictions of cShi(B3,1)."""
from shiarr import *
import time

# sanity: braid A2 (normals e1-e2,e1-e3,e2-e3 in C^3): chi=(t-1)(t-2)(t-3)? No: essential rank 2 -> t(t-1)(t-2)
v=[(1,-1,0),(1,0,-1),(0,1,-1)]
p=char_poly(v,3)
print("A2:",p, show_poly(p))
# B2 full: normals e1,e2,e1-e2,e1+e2: chi=(t-2)^2? check
v2=[(1,0),(0,1),(1,-1),(1,1)]
print("B2:",char_poly(v2,2), show_poly(char_poly(v2,2)))

# cone Shi B3,1: codim-1 restrictions = restrict to one hyperplane
l,k=3,1
N=build_cone(l,k)
d=l+1
print("n:",len(N))
seen={}
for i,(name,n) in enumerate(N):
    t0=time.time()
    R=restrict_to_hyperplane(N,i,d)
    p=char_poly(R,d-1)
    s=show_poly(p)
    seen.setdefault((tuple(p),s[1]),[]).append(name)
    print(f"X={name}: |R|={len(R)} chi={s[0]} = {s[1]}  ({time.time()-t0:.1f}s)")
print()
for key,names in seen.items():
    print(key[1]," <- ",names)
