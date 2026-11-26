"""Exact finite tests for the elastic-demand bottleneck Braess example."""
from fractions import Fraction as F


def inspect(B, x, y, z):
    u, v, r = x+y, x+z, x+y+z
    assert min(x,y,z) >= 0 and r <= 3
    costs = (max(u,v), max(1,u), max(1,v), B)
    flows = (x,y,z,3-r)
    nash = all(not flow or cost == min(costs) for flow,cost in zip(flows,costs))
    cc = sum(flow*cost for flow,cost in zip(flows,costs))
    return nash, cc


assert inspect(F(6,5), 0, F(6,5), F(6,5)) == (True, F(18,5))
assert inspect(F(7,4), 0, F(3,2), F(3,2)) == (True, F(9,2))
for B, den, opt in [(F(9,8), 16, (F(9,16),0,0)), (F(6,5),20,(0,1,1)),
                    (F(3,2), 20, (0,1,1)), (F(7,4),20,(0,1,1))]:
    best, worst, minimizers = None, None, []
    for i in range(3*den+1):
        for j in range(3*den-i+1):
            for h in range(3*den-i-j+1):
                x,y,z = F(i,den), F(j,den), F(h,den)
                r = x+y+z
                nash, cc = inspect(B,x,y,z)
                same_load = y == z
                predicted = same_load and ((r<3 and x+y==B) or (r==3 and x+y<=B))
                assert nash == predicted
                if best is None or cc < best:
                    best, minimizers = cc, []
                if cc == best:
                    minimizers.append((x,y,z))
                if nash and (worst is None or cc > worst):
                    worst = cc
    assert best == min(3*B-B*B/4, B+2) and minimizers == [opt]
    assert worst == 3*B
    if B == F(6,5):
        assert worst/best == F(9,8)
    print(f'grid B={B}: optimum {best}; worst Nash cost {worst}; ratio {worst/best}')
