"""Witness chi for general k: H={x2-x3=0} restriction in cShi(B3,k), plus lifts to l=4,5,6."""
from fractions import Fraction
from shiarr import char_poly, show_poly, build_cone
from restrict_flat import restrict_to_flat
import time

def witness(l, k):
    N = build_cone(l, k)
    d = l + 1
    def find(nm):
        return next(t for t, (w, n) in enumerate(N) if w == nm)
    if l == 3:
        sel = [find('x2-x3=0z')]
    else:
        sel = [find('x2-x3=0z')] + [find(f'x{i}=0z') for i in range(4, l + 1)]
    R, dimX = restrict_to_flat(N, sel, d)
    return R, dimX

for (l, k) in [(3, 1), (3, 2), (4, 1), (5, 1), (6, 1)]:
    t0 = time.time()
    R, dimX = witness(l, k)
    p = char_poly(R, dimX)
    s = show_poly(p)
    print(f"l={l} k={k}: dimX={dimX} |R|={len(R)} chi={s[0]} = {s[1]}  ({time.time()-t0:.1f}s)", flush=True)
