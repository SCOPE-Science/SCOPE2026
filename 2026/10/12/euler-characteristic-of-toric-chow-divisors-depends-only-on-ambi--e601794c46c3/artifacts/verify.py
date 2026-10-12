from itertools import combinations
from math import comb

# Exhaustive abstract fixed-point census.
checked = 0
subsets_checked = 0
for N in range(2, 17):
    for d in range(1, N-1):
        q = N-d-1
        for v in range(1, N+1):
            vertices = set(range(v))
            direct = 0
            for S in combinations(range(N), q):
                subsets_checked += 1
                if vertices.intersection(S):
                    direct += 1
            closed = comb(N, q) - (comb(N-v, q) if N-v >= q else 0)
            assert direct == closed, (N,d,v,direct,closed)
            checked += 1

# Elementary 2D convex-hull routine for explicit support examples.
def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p) <= 0:
            lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

# Degree-e Veronese surfaces: all lattice points in a triangle, v=3.
family_checks=0
for e in range(2,8):
    A=[(i,j) for i in range(e+1) for j in range(e+1-i)]
    N=len(A); d=2; v=len(hull(A)); q=N-d-1
    assert v==3
    direct=sum(1 for S in combinations(range(N),q) if set(S)&set(range(v)))
    assert direct==comb(N,d+1)-1
    family_checks+=1

# Rectangle grids: four hull vertices regardless of interior lattice points.
for a in range(1,5):
    for b in range(1,5):
        A=[(i,j) for i in range(a+1) for j in range(b+1)]
        assert len(hull(A))==4
        family_checks+=1

# Rational-normal-curve support is one-dimensional: endpoints are the two vertices.
for e in range(2,15):
    N=e+1; d=1; v=2; q=N-d-1
    direct=sum(1 for S in combinations(range(N),q) if set(S)&{0,N-1})
    assert direct==comb(N,2)-1
    family_checks+=1

assert checked > 1000
assert subsets_checked > 100000
assert family_checks > 30
print('VERIFY_OK', checked, subsets_checked, family_checks)
