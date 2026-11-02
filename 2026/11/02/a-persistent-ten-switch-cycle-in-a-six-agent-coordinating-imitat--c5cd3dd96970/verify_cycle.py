"""Exact integer certificate for a six-agent mixed imitation/BR periodic orbit."""

N = 6
ADJ = (
    (1, 2, 4, 5), (0, 3, 4), (0, 3, 4),
    (1, 2, 5), (0, 1, 2), (0, 3),
)
ROLE = ('BR', 'I', 'BR', 'I', 'I', 'I')
# Each payoff row is (R, S, T, P), for (A,A), (A,B), (B,A), (B,B).
PAYOFF = (
    (2, 0, -1, 5),
    (12, -1, 0, 13),
    (3, -4, -7, 2),
    (1, -6, -7, 5),
    (4, -4, -6, 9),
    (10, -4, -2, 5),
)
STATES = (43, 42, 58, 56, 60, 52, 53, 37, 39, 35, 43)
SWITCHES = (0, 4, 1, 2, 3, 0, 4, 1, 2, 3)

def bit(state, i):
    return (state >> i) & 1

def utility(state, i, action=None):
    if action is None:
        action = bit(state, i)
    r, s, t, p = PAYOFF[i]
    return sum((r if bit(state, j) else s) if action else
               (t if bit(state, j) else p) for j in ADJ[i])

def update(state, i):
    current = bit(state, i)
    if ROLE[i] == 'BR':
        a = utility(state, i, 1)
        b = utility(state, i, 0)
        return state if a == b else ((state | (1 << i)) if a > b else
                                     (state & ~(1 << i)))
    earnings = [(utility(state, j), j) for j in ADJ[i]]
    max_pay = max(v for v, _ in earnings)
    winners = [j for v, j in earnings if v == max_pay]
    target_strategies = {bit(state, j) for j in winners}
    return state if len(target_strategies) != 1 else (
        (state | (1 << i)) if 1 in target_strategies else
        (state & ~(1 << i)))

def verify():
    for i in range(N):
        assert set(ADJ[i]) <= set(range(N)) - {i}
        assert len(ADJ[i]) == len(set(ADJ[i]))
        for j in ADJ[i]:
            assert i in ADJ[j]
        r, s, t, p = PAYOFF[i]
        assert min(r, p) > max(s, t), ('non-coordination', i)

    assert STATES[0] == STATES[-1]
    assert len(STATES) == len(SWITCHES) + 1
    assert set(SWITCHES) == {0, 1, 2, 3, 4}
    for k, (start, finish, agent) in enumerate(zip(STATES, STATES[1:], SWITCHES)):
        assert start != finish and start ^ finish == 1 << agent, ('bad change', k)
        assert update(start, agent) == finish, ('bad update', k)
        if ROLE[agent] == 'BR':
            assert utility(start, agent, bit(finish, agent)) > utility(start, agent), k
        else:
            neighbors = ADJ[agent]
            vals = [utility(start, j) for j in neighbors]
            assert vals.count(max(vals)) == 1, ('imitator tie', k)
    # Agent 5's activation is idle at state 43, so inserting it once per
    # 10-switch cycle makes an 11-step schedule visiting all six agents.
    assert update(STATES[0], 5) == STATES[0]
    period = (5,) + SWITCHES
    assert set(period) == set(range(N))
    s0 = STATES[0]
    for _ in range(3):
        for a in period:
            s0 = update(s0, a)
        assert s0 == STATES[0]
    print('PASS: strict 10-switch orbit, fair 11-activation periodic schedule; exact integers')

if __name__ == '__main__':
    verify()
