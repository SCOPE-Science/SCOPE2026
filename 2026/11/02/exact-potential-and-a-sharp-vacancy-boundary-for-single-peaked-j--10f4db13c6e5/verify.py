"""Exact finite checks for the complete-multipartite one-vacancy potential and a two-vacancy improvement cycle. Stdlib only."""
from fractions import Fraction as Q
from itertools import product


def enumerate_exact(sizes, totals):
    color_count = len(totals)
    parts = [i for i, s in enumerate(sizes) for _ in range(s)]
    n = len(parts)
    assert len(sizes) >= 2 and all(s > 0 for s in sizes)
    assert sum(totals) == n-1
    def u(i, c, f):
        return Q(1+3*i+c, 7)*f-Q((i+2)*(c+1), 5)*f*f
    def potential(st):
        ans = Q(0)
        for i, s in enumerate(sizes):
            for c in range(color_count):
                hmax = sum(st[j] == c for j in range(n) if parts[j] == i)
                for h in range(1, hmax+1):
                    ans += u(i, c, min(Q(1), Q(totals[c]-h+1, n-s)))
        return ans
    def pay(st, j):
        i = parts[j]
        color = st[j]
        assert color >= 0
        neighbors = [st[k] for k in range(n) if parts[k] != i and st[k] >= 0]
        return u(i, color, Q(1+neighbors.count(color), 1+len(neighbors)))
    nprofiles = transitions = strict = 0
    for st in product(range(-1,color_count), repeat=n):
        if st.count(-1) != 1 or any(st.count(c) != totals[c] for c in range(color_count)):
            continue
        nprofiles += 1
        e = st.index(-1)
        for j, c in enumerate(st):
            if c < 0:
                continue
            nxt = list(st)
            nxt[e], nxt[j] = c, -1
            nxt = tuple(nxt)
            gain = pay(nxt, e)-pay(st, j)
            assert gain == potential(nxt)-potential(st), (sizes, st, j, e)
            transitions += 1
            strict += gain > 0
    return nprofiles, transitions, strict


def peak(f):
    return 1-abs(2*f-1)


def check_cycle():
    parts = (0, 0, 0, 1, 1, 1)
    states = [
        (0,-1,0,1,0,-1),
        (0,1,0,-1,0,-1),
        (-1,1,0,-1,0,0),
        (-1,-1,0,1,0,0),
        (0,-1,0,1,0,-1),
    ]
    jumps = [(3,1,1),(0,5,0),(1,3,1),(5,0,0)]
    expected = [(Q(2,3),Q(1)),(Q(0),Q(2,3)),(Q(2,3),Q(1)),(Q(0),Q(2,3))]
    def payoff(st, j):
        assert st[j] != -1
        outside = [st[k] for k in range(6) if parts[k] != parts[j] and st[k] != -1]
        return peak(Q(1+outside.count(st[j]),1+len(outside)))
    for i, (origin,target,color) in enumerate(jumps):
        before, after = states[i], states[i+1]
        assert before.count(-1)==after.count(-1)==2
        assert before[origin]==color and before[target]==-1
        test=list(before)
        test[origin], test[target]=-1,color
        assert tuple(test)==after
        score=(payoff(before,origin),payoff(after,target))
        assert score == expected[i] and score[1]>score[0],(i,score)
    print('TWO_VACANCY_FOUR_STEP_IMPROVING_CYCLE_OK')


def main():
    cases = [((2,2),(2,1)),((2,3),(2,2)),((2,2,2),(3,2)),((1,2,3),(2,3)),((2,2,2),(2,2,1)),((1,1,2,2),(2,1,2))]
    checked = 0
    for sizes, totals in cases:
        p,t,s = enumerate_exact(sizes, totals)
        print('EXACT_POTENTIAL_CASE', sizes, 'totals', totals, 'profiles', p, 'transitions', t, 'improving', s)
        checked += t
    assert checked == 2556
    print('EXACT_POTENTIAL_TRANSITIONS_OK',checked)
    check_cycle()

if __name__ == '__main__':
    main()
