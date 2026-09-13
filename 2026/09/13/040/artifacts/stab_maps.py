# Stabilization maps on the surviving twisted classes:
# H4: 1-dim for k>=3 (C-type orbit sum); H6: 2-dim for k>=4 (need explicit invariant basis + transition).
# For H4, compute stab map Phi: A4_k x W_k -> A4_{k+1} x W_{k+1} restricted to invariants:
# A-part: inclusion of positions 0..k-1 into 0..k (add point at infinity? puncture stab adds a point far away; on cohomology it forgets? For configuration stabilization, map on Kriz models: ?).
# Simpler robust test: dimensions already stabilize (H4: k=2: 0, k>=3: 1; H5: k=3: ?; H6: k=3: ? vs k>=4).
# If dimensions jump at the boundary k=2i+2 vs 2i+3, that gives sharpness witness directly (single pair where map is not iso because dimensions differ), without needing explicit matrix.
# Compute: H4(k=2..6), H5(k=3..6, quotiented), H6(k=3..6, quotiented).
import itertools
from collections import defaultdict
import sympy as sp

# --- H4 dims already: 0,1,1,1 for k=2,3,4,5 (check_smallk). Confirm k=6 too (identify_maps said rank 1).
# --- H5 quotiented for k=3: need compute_H5(3). The relation-rank code handles k=3 (NC5=2*3*3*1=18).
exec(open('output/artifacts/h5_quotient.py').read().split("for k in [4,5,6]:")[0])
print("### H5 quotiented k=3")
res3=compute_H5(3)
print(res3)
print("### H5 quotiented k=4")
res4=compute_H5(4)
print(res4)
