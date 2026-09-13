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

import sys
cases = [(3,3),(3,4),(4,2),(4,3),(5,2),(6,2),(6,3)]
for (l, k) in cases:
    t0 = time.time()
    R, dimX = witness(l, k)
    p = char_poly(R, dimX)
    s = show_poly(p)
    # predicted S(k): even 41k^2/2, odd (41k^2+1)/2 ; chi=(t-1)(t^2-9k t+S)
    S = (41*k*k)//2 if k % 2 == 0 else (41*k*k+1)//2
    pred = f"(t - 1)*(t**2 - {9*k}*t + {S})"
    print(f"l={l} k={k}: dimX={dimX} |R|={len(R)} (pred |R|={9*k+1}) chi={s[0]} ; pred {pred}  ({time.time()-t0:.1f}s)", flush=True)
