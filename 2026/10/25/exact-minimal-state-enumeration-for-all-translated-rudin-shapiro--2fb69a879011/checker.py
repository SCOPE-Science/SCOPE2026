#!/usr/bin/env python3
"""Independent exact finite-state checks for shifted Rudin-Shapiro automata."""
from collections import deque

def rs(n):
    return (n & (n >> 1)).bit_count() & 1

def symbolic_states(c):
    start = (c, 0, 0)
    seen = {start}
    queue = deque([start])
    while queue:
        q, s, t = queue.popleft()
        for bit in (0, 1):
            z = q + bit
            v = z & 1
            qq = z >> 1
            next_state = (qq, v, t ^ (s & bit) ^ (v & (qq & 1)))
            if next_state not in seen:
                seen.add(next_state)
                queue.append(next_state)
    return seen

def interval_formula_states(c):
    b = c.bit_length()
    states = {(c, 0, 0)}
    for e in range(1, b + 4):
        m = 1 << e
        h = m >> 1
        q_min = c // m
        for q in (q_min, q_min + 1):
            for s in (0, 1):
                lo = max(c, q*m + s*h)
                hi = min(c + m - 1, q*m + (s+1)*h - 1)
                if lo > hi:
                    continue
                if hi - lo + 1 >= 5:
                    choices = (0, 1)
                else:
                    choices = set(rs(a-q*m) for a in range(lo, hi+1))
                for parity in choices:
                    states.add((q, s, parity ^ (s & (q & 1))))
    return states

def independent_dfa(c):
    length = c.bit_length()
    start = (0, 0, 0, 0)
    states = [start]
    ids = {start: 0}
    edges = []
    outputs = []
    for p, carry, prev, par in states:
        remainder = (c >> p) + carry
        outputs.append(par ^ rs(remainder) ^ (prev & (remainder & 1)))
        nxts = []
        for x in (0, 1):
            tot = x + carry + ((c >> p) & 1 if p < length else 0)
            d = tot & 1
            nxt = (min(p+1, length), tot >> 1, d, par ^ (prev & d))
            if nxt not in ids:
                ids[nxt] = len(states)
                states.append(nxt)
            nxts.append(ids[nxt])
        edges.append(nxts)
    colors = outputs[:]
    while True:
        signatures = [(colors[i], colors[edges[i][0]], colors[edges[i][1]]) for i in range(len(states))]
        renumber = {sig: j for j, sig in enumerate(sorted(set(signatures)))}
        updated = [renumber[x] for x in signatures]
        if len(set(updated)) == len(set(colors)):
            return len(set(updated)), len(states)
        colors = updated

def main():
    test = 2048
    for c in range(test):
        a = symbolic_states(c)
        b = interval_formula_states(c)
        dfa_min, dfa_raw = independent_dfa(c)
        assert a == b, ('interval', c, a ^ b)
        assert len(a) == dfa_min, ('dfa', c, len(a), dfa_min)
        if c < 250:
            for n in range(60):
                p = 0
                state = (c, 0, 0)
                digits = max(1, n.bit_length())
                for j in range(digits):
                    v = (n >> j) & 1
                    q, s, t = state
                    z = q + v
                    dd = z & 1
                    qq = z >> 1
                    state = (qq, dd, t ^ (s & v) ^ (dd & (qq & 1)))
                q,s,t = state
                assert rs(q)^t == rs(n+c), ('output',c,n)
    for m in range(3, 20):
        c = 1 << m
        assert len(symbolic_states(c)) == 4*m + 2
        assert len(interval_formula_states(c)) == 4*m + 2
    print('PASS: 2048 shifts, symbolic and interval states identical; independent DFA minimizations agree.')
    print('PASS: 15000 direct output tests and 17 exact dyadic identities (m=3..19).')
    print('state counts:', [(c,len(symbolic_states(c))) for c in (0,1,2,3,4,5,7,8,13,16,29,32,53,64,101,128,197,256)])

if __name__=='__main__':main()
