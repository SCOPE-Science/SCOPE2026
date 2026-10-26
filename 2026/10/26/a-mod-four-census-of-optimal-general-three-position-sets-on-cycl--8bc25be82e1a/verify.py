"""Independent finite checks for maximum general 3-position sets on cycles.

Run: python verify.py
The finite tests are supplementary to the unrestricted gap proof.
"""
from itertools import combinations
from math import comb


def prediction(n):
    if n % 4 == 0:
        return 6
    if n % 4 == 2:
        return 2
    if n % 4 == 1:
        return n * (n + 3) // 4
    return n * (n + 1) // 4


def geodesic_condition(n, selected):
    # Independently uses graph distances, not the four-window rule.
    def dist(a, b):
        t = abs(a - b)
        return min(t, n - t)
    for u, v, w in combinations(selected, 3):
        if (dist(u, v) + dist(v, w) == dist(u, w) <= 3 or
            dist(u, w) + dist(w, v) == dist(u, v) <= 3 or
            dist(v, u) + dist(u, w) == dist(v, w) <= 3):
            return False
    return True


def window_condition(n, mask):
    for i in range(n):
        if sum((mask >> ((i+j)%n)) & 1 for j in range(4)) > 2:
            return False
    return True


def rotate(mask, n, r):
    return ((mask << r) | (mask >> (n-r))) & ((1 << n)-1)


def transfer_optimum_count(n):
    # Independently counts all cyclic binary words via the 8-state
    # closed-walk transfer graph, weighted by their number of ones.
    total=0
    target=n//2
    for initial in range(8):
        states={(initial,0):1}
        for _ in range(n):
            next_states={}
            for (state,weight),multiplicity in states.items():
                for bit in (0,1):
                    if state.bit_count()+bit>2 or weight+bit>target:
                        continue
                    newstate=((state<<1)&7)|bit
                    key=(newstate,weight+bit)
                    next_states[key]=next_states.get(key,0)+multiplicity
            states=next_states
        total += states.get((initial,target),0)
    return total


def main():
    total = 0
    distance_cases = 0
    for n in range(6, 24):
        k=n//2
        valid=[]
        for ss in combinations(range(n), k):
            total += 1
            mask=sum(1 << p for p in ss)
            via_windows=window_condition(n, mask)
            if n <= 15:
                via_distances=geodesic_condition(n, ss)
                distance_cases += 1
                assert via_distances == via_windows, (n,ss)
            if via_windows:
                valid.append(mask)
        assert len(valid) == prediction(n), (n,len(valid),prediction(n))
        assert any(window_condition(n, sum(1 << p for p in ss))
                   for ss in [range(0,n-1,2)]) if n%2 else True
        if n <= 18:
            orbits={min(rotate(x,n,r) for r in range(n)) for x in valid}
            expected = (1 if n%4==2 else 2) if n%2==0 else (n+3)//4
            assert len(orbits)==expected, (n,len(orbits),expected)
    for n in range(6,121):
        assert transfer_optimum_count(n) == prediction(n), n
    print(f'VERIFICATION_OK orders=6..23 candidate_subsets={total} direct_distance_cases={distance_cases} orbit_orders=6..18 transfer_orders=6..120')

if __name__=='__main__':
    main()
