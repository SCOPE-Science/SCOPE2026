"""Exact-rational independent deviation checks for a four-vertex network-formation result.

Run: python3 verify.py
Standard-library only. Finite checks supplement, but do not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import combinations


def solve(a, b):
    n = len(b)
    m = [[Q(a[i][j]) for j in range(n)] + [Q(b[i])] for i in range(n)]
    for i in range(n):
        j = next(k for k in range(i, n) if m[k][i] != 0)
        m[i], m[j] = m[j], m[i]
        t = m[i][i]
        m[i] = [v / t for v in m[i]]
        for k in range(n):
            if k != i:
                t = m[k][i]
                if t:
                    m[k] = [v - t * w for v, w in zip(m[k], m[i])]
    return [m[i][-1] for i in range(n)]


def centrality(profile, delta):
    n = len(profile)
    a = [[int((j in profile[i]) or (i in profile[j])) if i != j else 0
          for j in range(n)] for i in range(n)]
    M = [[int(i == j) - delta * a[i][j] for j in range(n)] for i in range(n)]
    return [x-1 for x in solve(M, [1]*n)]


def actions(i, n):
    others = [j for j in range(n) if j != i]
    for mask in range(1 << (n - 1)):
        yield frozenset(others[k] for k in range(n - 1) if (mask >> k) & 1)


def utility(profile, i, costs, delta):
    return centrality(profile, delta)[i] - costs[i] * len(profile[i])


def check_ne(profile, costs, delta, strict):
    n = len(profile)
    comparisons = 0
    for i in range(n):
        current = utility(profile, i, costs, delta)
        for action in actions(i, n):
            if action == profile[i]:
                continue
            other = list(profile)
            other[i] = action
            rival = utility(other, i, costs, delta)
            comparisons += 1
            assert (current > rival if strict else current >= rival), (delta, i, action, costs, current, rival)
    return comparisons


def main():
    profile = [frozenset([1]), frozenset([2]), frozenset([0]), frozenset()]
    dvalues = [Q(1,1000), Q(1,100), Q(1,20), Q(1,10), Q(1,4), Q(3,10), Q(33,100)]
    comparisons = 0
    for d in dvalues:
        # B: K3 vertex. L: P3 leaf. P: K3 vertex with one pendant.
        B = 2*d/(1-2*d)
        L = d*(1+2*d)/(1-2*d*d)
        P = d*(3+2*d-d*d)/(1-d-3*d*d+d*d*d)
        U = d/((1-2*d)*(1-2*d*d))
        G = d*(1-d)**2/((1-2*d)*(1-d-3*d*d+d*d*d))
        C = d/(1-3*d)
        assert B-L == U and P-B == G and G < U and C > U
        assert centrality(profile,d) == [B,B,B,Q(0)]
        drop = [frozenset(), frozenset([2]), frozenset([0]), frozenset()]
        add = [frozenset([1,3]), frozenset([2]), frozenset([0]), frozenset()]
        assert centrality(drop,d)[0] == L
        assert centrality(add,d)[0] == P
        isolated_all = [frozenset([1]),frozenset([2]),frozenset([0]),frozenset([0,1,2])]
        assert centrality(isolated_all,d)[3] == 3*C
        strict_cost = [(G+U)/2]*3 + [C+d**3]
        weak_cost = [U]*3 + [C]
        comparisons += check_ne(profile, strict_cost, d, True)
        comparisons += check_ne(profile, weak_cost, d, False)
        assert C/U == (1-2*d)*(1-2*d*d)/(1-3*d)
        # Check all eight sponsorship orientations of K3.
        edges = [(0,1),(0,2),(1,2)]
        best_ratio = None
        for mask in range(8):
            s=[set() for _ in range(4)]
            for j,(u,v) in enumerate(edges):
                payer = v if (mask >> j)&1 else u
                recipient = u if payer==v else v
                s[payer].add(recipient)
            p=[frozenset(x) for x in s]
            bounds = []
            feasible = True
            for i in range(4):
                old=centrality(p,d)[i]
                m=len(p[i])
                low=Q(0); high=None
                for T in actions(i,4):
                    a=list(p); a[i]=T
                    gain=centrality(a,d)[i]-old
                    count=len(T)-m
                    if count>0:low=max(low,gain/count)
                    elif count<0:
                        cap=gain/count
                        high=cap if high is None else min(high,cap)
                    elif gain>0:feasible=False
                if high is not None and low>high:feasible=False
                bounds.append((low,high))
            if feasible:
                # For every supporting cost vector the isolate costs at least C,
                # and some sponsor's costs at most U.
                assert bounds[3][0] >= C
                assert any(hi is not None and hi <= U for lo,hi in bounds[:3])
        # Three-vertex structural obstruction: owner would gain by joining an isolate.
        b2=d/(1-d)
        center=(1+2*d)/(1-2*d*d)-1
        assert center-2*b2 == 2*d**3/((1-d)*(1-2*d*d)) > 0
    print('VERIFIED exact rational identities, 4-agent strict/weak Nash profiles,')
    print('orientation cost bounds, and 3-agent obstruction;')
    print(f'{len(dvalues)} attenuation settings; {comparisons} unilateral comparisons')

if __name__=='__main__': main()
