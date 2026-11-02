#!/usr/bin/env python3
"""Independent exhaustive Euler-feasibility matrices vs explicit flow sums (stdlib)."""
from math import comb


def compositions(total, positions):
    if positions == 1:
        yield (total,)
    else:
        for k in range(total + 1):
            for suffix in compositions(total - k, positions - 1):
                yield (k,) + suffix


def euler_feasible(x):
    indeg = [0]*3
    outdeg = [0]*3
    for i in range(3):
        for j in range(3):
            outdeg[i] += x[3*i+j]
            indeg[j] += x[3*i+j]
    divergence = [outdeg[i] - indeg[i] for i in range(3)]
    if sorted(divergence) not in ([0,0,0],[-1,0,1]):
        return False
    active = [i for i in range(3) if indeg[i] + outdeg[i] > 0]
    if not active:
        return True
    reached = {active[0]}
    frontier = [active[0]]
    while frontier:
        v = frontier.pop()
        for u in active:
            if u not in reached and (x[3*v+u] or x[3*u+v]):
                reached.add(u)
                frontier.append(u)
    return len(reached) == len(active)


def direct_flow_count(t):
    """Count by support dimension and oriented integer divergence flows."""
    if t == 0: return 1
    result = 3  # three single-symbol loop profiles
    # exactly two active vertices; total off-diagonal edges positive
    for s in range(1,t+1):
        if s % 2 == 0: result += 3*(t-s+1)   # closed, balanced
        else: result += 6*(t-s+1)             # open, odd, diff=1
        # Open-trail pair flows have odd off-diagonal total.
    # three active vertices; directed cycle flows on pairs 01,12,20
    for d in ((0,0,0), (1,0,-1), (-1,1,0), (0,-1,1),
              (-1,0,1), (1,-1,0), (0,1,-1)):
        # A particular net-flow on 01,12,20 for the specified divergence d
        # is (k, k+d[1], k-d[0]) because divergence=(f01-f20,f12-f01,f20-f12).
        for k in range(-t,t+1):
            f = (k, k+d[1], k-d[0])
            base = sum(abs(v) for v in f)
            if base > t: continue
            for h0 in range((t-base)//2 + 1):
                for h1 in range((t-base-2*h0)//2 + 1):
                    for h2 in range((t-base-2*h0-2*h1)//2 + 1):
                        off = (abs(f[0])+2*h0, abs(f[1])+2*h1,
                               abs(f[2])+2*h2)
                        if sum(off)>t: continue
                        # Support must use all three vertices; exclude the 1/2-vertex cases.
                        incident=[off[0]+off[2],off[0]+off[1],off[1]+off[2]]
                        if not all(incident):continue
                        result += comb(t-sum(off)+2,2)
    return result

if __name__ == '__main__':
    for t in range(0, 15):
        direct = sum(euler_feasible(x) for x in compositions(t,9))
        via = direct_flow_count(t)
        assert direct == via,(t,direct,via)
        print('t=%d n=%d valid_matrices=%d flow_count=%d OK' % (t,t+1,direct,via))
    print('PASS independent matrix census through n=15')
