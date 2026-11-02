"""Independent exact-arithmetic checks for a three-agent epidemic best-response law.
Requires only Python 3.9+ standard library. Finite checks supplement the proof.
"""
from collections import defaultdict
from fractions import Fraction as Q

def transition(state, choice, tau):
    actions, infected = state
    actions = list(actions)
    if infected & (1 << choice):
        actions[choice] = Q(1)
    else:
        neighbor = [j for j in range(3) if j != choice]
        viral = sum((actions[j] for j in neighbor if infected & (1 << j)), Q(0))
        total = sum((actions[j] for j in neighbor), Q(0))
        actions[choice] = min(Q(1), tau * total / viral) if viral else Q(1)
    future = infected
    for i in range(3):
        if infected & (1 << i):
            continue
        neighbor = [j for j in range(3) if j != i]
        viral = sum((actions[j] for j in neighbor if infected & (1 << j)), Q(0))
        total = sum((actions[j] for j in neighbor), Q(0))
        if actions[i] * viral > tau * total:
            future |= 1 << i
    return (tuple(actions), future)

def certified_absorbing_count(state, tau):
    actions, infected = state
    if infected == 7:
        return 3
    if infected.bit_count() == 2:
        remaining = next(i for i in range(3) if not infected & (1 << i))
        # Its exposure is one, and it remains forever below the threshold.
        return 2 if actions[remaining] <= tau else None
    if infected == 1 and actions[0] == Q(1):
        # Each susceptible's next best response is tau*(1+other action).
        if actions[1] <= tau * (1 + actions[2]) and actions[2] <= tau * (1 + actions[1]):
            return 1
    return None

def exact_finite_tree(a, tau, horizon=27):
    frontier = {((a, a, a), 1): Q(1)}
    absorbed = [Q(0)] * 4
    evaluated = 0
    for _ in range(horizon):
        next_states = defaultdict(Q)
        for state, mass in frontier.items():
            evaluated += 1
            k = certified_absorbing_count(state, tau)
            if k is not None:
                absorbed[k] += mass
            else:
                for j in range(3):
                    next_states[transition(state, j, tau)] += mass / 3
        frontier = next_states
    for state, mass in list(frontier.items()):
        k = certified_absorbing_count(state, tau)
        if k is not None:
            absorbed[k] += mass
            del frontier[state]
    unresolved = sum(frontier.values(), Q(0))
    assert sum(absorbed, Q(0)) + unresolved == 1
    return absorbed, unresolved, evaluated

def predicted(a, tau):
    assert 0 < a < 1 and a/2 < tau < min(a, Q(1, 2))
    stage0 = int(tau + 2*tau*tau >= a)
    stage1 = int(tau*(1+a) >= a)
    stage2 = int(2*tau*tau + a*tau >= a)
    assert stage0 >= stage1 >= stage2, (a, tau, stage0,stage1,stage2)
    p1 = Q(stage1, 3)
    p2 = Q(stage0, 9) + Q(stage2, 18)
    return [Q(0), p1, p2, 1-p1-p2], (stage0,stage1,stage2)

def test():
    examples = [
        (Q(3,5), Q(1,3)),
        (Q(3,5), Q(9,25)),
        (Q(3,5), Q(2,5)),
        (Q(3,5), Q(9,20)),
        # Three exact algebraic boundary instances, including equality.
        (Q(18,25), Q(2,5)),
        (Q(2,3), Q(2,5)),
        (Q(8,15), Q(2,5)),
        # Last phase is absent for small initial action.
        (Q(1,4), Q(1,5)),
    ]
    # Deterministic rational parameter grid, including nontrivial fractions.
    for den in range(3,12):
        for num in range(1,den):
            a = Q(num,den)
            for k in range(1,10):
                tau = Q(k,20)
                if a/2 < tau < min(a, Q(1,2)):
                    examples.append((a,tau))
    examples = list(dict.fromkeys(examples))
    checks=0; count=0; max_tail=Q(0)
    for a,tau in examples:
        target,stage = predicted(a,tau)
        got, tail, evaluated = exact_finite_tree(a,tau,24)
        for k in (1,2,3):
            # Exact probability enclosures: unclassified finite-time mass
            # can contribute at most its total weight to any class.
            assert got[k] <= target[k] <= got[k]+tail, (a,tau,k,target,got,tail)
            checks += 1
        assert tail < Q(1,10000), (a,tau,tail)
        max_tail=max(max_tail,tail)
        count += 1
    print(f'PASS: {count} distinct rational parameter pairs, {checks} exact probability enclosures')
    print(f'PASS: all three jump boundaries included; worst unresolved weight at 24 steps = {float(max_tail):.10f}')
    for a,tau in examples[:8]:
        target,_=predicted(a,tau)
        print(f'  (a,tau)=({a},{tau}) -> (P1,P2,P3)=({target[1]},{target[2]},{target[3]})')
if __name__ == '__main__':
    test()
