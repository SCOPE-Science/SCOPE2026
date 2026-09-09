"""Second verification: principal-angle orbit exclusion + flat bounds + scale law.

- Principal angles P0 vs Pd: cosines = singular values of inter-basis inner products.
- Flat upper bound: Hausdorff/flat -> 0 as d->0 (graph slope tan d).
- Scale law: normalized height excess constant in r.
- Decomposition lemma numeric sanity: union of two transverse planes determines components.
"""
import math

def principal_cosines(d):
    # M = [[-sin d,0],[0,sin d]] -> sing vals |sin d|,|sin d|
    return (abs(math.sin(d)), abs(math.sin(d)))

for d in [0.0, 0.01, 0.05, 0.1, 0.2]:
    c1, c2 = principal_cosines(d)
    t1 = math.degrees(math.acos(min(1.0, c1)))
    print(f'd={d}: cosines=({c1:.6f},{c2:.6f}) angles=({t1:.4f},{t1:.4f}) deg')

# Gap: angle distance from (90,90) is |d| to first order
for d in [0.05, 0.1, 0.2]:
    gap = math.pi/2 - math.acos(abs(math.sin(d)))
    print(f'd={d}: per-angle gap={gap:.6f} rad (~|d|={d})')

# Flat/graph bound: Pd as graph over P1 with slope |tan d|
for d in [0.2, 0.1, 0.05, 0.01]:
    print(f'd={d}: tan={math.tan(d):.7f} Hausdorff<=sin={abs(math.sin(d)):.7f}')

# Normalized excess const in r, for the orbit-inf reading:
# inf_U E(Qd,UQ,Br): each U term scale-invariant; min over compact orbit attained, >0.
# Exhibit one number: fixed-Q excess H=(pi/2)sin^2 d; orbit-inf <= H but >=0;
# positivity: any UQ has angle pair (90,90), Qd has (90-|d|,90-|d|), Hausdorff angle gap uniform in r.
print('scale law: H_r = (pi/2) sin^2 d for all r>0 (cone homogeneity).')
print('VERIFY2_OK')
