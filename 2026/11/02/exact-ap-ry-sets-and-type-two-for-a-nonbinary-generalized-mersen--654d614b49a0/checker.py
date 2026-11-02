"""Independent finite checks for the generalized-Mersenne four-generator family.
Run: python3 checker.py (standard library only). Infinite claims are proved in RESULT.md.
"""
from math import gcd
from heapq import heappush, heappop


def residue_minima(a, generators):
    best = [None] * a
    best[0] = 0
    queue = [(0, 0)]
    while queue:
        x, r = heappop(queue)
        if x != best[r]:
            continue
        for generator in generators:
            nr = (r + generator) % a
            nx = x + generator
            if best[nr] is None or nx < best[nr]:
                best[nr] = nx
                heappush(queue, (nx, nr))
    return best


def greedy_weight(h, m_value):
    b = h*h - h + 1
    c = h**3 - h + 1
    quot, residue = divmod(m_value, c)
    short, units = divmod(residue, b)
    return h**3*quot + h*h*short + h*units


def independent_weight_dp(h, upper):
    b = h*h - h + 1
    c = h**3 - h + 1
    scores = [0] + [10**20] * upper
    for v in range(1, upper + 1):
        scores[v] = h + scores[v-1]
        if v >= b:
            scores[v] = min(scores[v], h*h + scores[v-b])
        if v >= c:
            scores[v] = min(scores[v], h**3 + scores[v-c])
    return scores


def predicted(h, m, d):
    b = h*h - h + 1
    c = h**3 - h + 1
    a = m*c
    t = (h-1)**2
    wmax = (m-1)*h**3 + 2*h*h*(h-1)
    special = h*h*(h-1)*(2*h**3+h*h-3*h+2)//2
    genus = c*h**3*m*(m-1)//2 +m*special + (d-1)*(a-1)//2
    frobenius = a*(wmax-1)+d*(a-1)
    return a, [a,h*a+d,h*h*a+b*d,h**3*a+c*d], genus, frobenius, [frobenius - d*t, frobenius]


def run():
    dynamic_checks = 0
    residue_checks = 0
    family_checks = 0
    for h in range(2, 11):
        b = h*h-h+1
        c = h**3-h+1
        if h <= 8:
            dp = independent_weight_dp(h, 5*c)
            for value, optimum in enumerate(dp):
                assert greedy_weight(h, value) == optimum, (h, value)
                dynamic_checks += 1
        for m in range(1, 7):
            for d in (1, 2, 3, 5, 7, 11):
                a, generators, genus, F, pf = predicted(h,m,d)
                if gcd(a,d) != 1:
                    continue
                W = residue_minima(a, generators)
                assert all(z is not None for z in W)
                for r in range(a):
                    expected = a*greedy_weight(h,r) + d*r
                    assert W[(d*r)%a] == expected, (h,m,d,r)
                    residue_checks += 1
                measured_genus = (sum(W) - a*(a-1)//2)//a
                assert measured_genus == genus, (h,m,d,measured_genus,genus)
                assert max(W) - a == F, (h,m,d)
                observed_pf = sorted(z-a for z in W if all(z+g-a>=W[(z+g)%a] for g in generators))
                assert observed_pf == pf, (h,m,d, observed_pf, pf)
                family_checks += 1
    print('weighted_change_dp_checks', dynamic_checks)
    print('independent_apery_residue_checks', residue_checks)
    print('complete_family_invariant_checks', family_checks)
    print('PASS (finite tests; unrestricted result has a separate proof)')


if __name__ == '__main__':
    run()
