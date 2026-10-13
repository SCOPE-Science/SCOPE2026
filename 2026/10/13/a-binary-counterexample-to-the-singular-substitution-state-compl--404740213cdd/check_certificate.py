"""Verify a complete minimal-quotient certificate for finite subsequence ideals.

No third-party packages are needed. Run from this directory using:
    python check_certificate.py
"""
import json
from collections import Counter, deque
from pathlib import Path


def embedded(x, y):
    pos = 0
    for symbol in y:
        if pos < len(x) and symbol == x[pos]:
            pos += 1
    return pos == len(x)


def normalize(candidates):
    s = set(candidates)
    return tuple(sorted(w for w in s if all(w == z or not embedded(w, z) for z in s)))


def after(symbol, words):
    # Left quotients of principal subsequence ideals: greedy earliest symbol.
    return normalize(w[w.index(symbol)+1:] for w in words if symbol in w)


def verify_case(record):
    alphabet = 'ab'
    states = [tuple(x) for x in record['states']]
    edges = record['transitions']
    n = record['state_count']
    assert len(states) == len(edges) == n
    assert len(set(states)) == n
    assert states[0] == normalize(record['generators'])
    assert all(x == normalize(x) for x in states)
    idx = {s: i for i, s in enumerate(states)}
    assert tuple() in idx and states[idx[tuple()]] == tuple()

    for i, state in enumerate(states):
        assert len(edges[i]) == len(alphabet)
        for j, symbol in enumerate(alphabet):
            target = after(symbol, state)
            assert target in idx and idx[target] == edges[i][j], (record['name'], i, symbol)

    reached = {0}
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in edges[i]:
            if j not in reached:
                reached.add(j)
                queue.append(j)
    assert len(reached) == n  # Complete reachable quotient automaton.

    # In every state the words listed form the UNIQUE maximal antichain
    # of the residual finite downward-closed language. Distinct lists
    # are thus pairwise Myhill-Nerode inequivalent, not just graph nodes.
    return n, dict(sorted(Counter(map(len, states)).items()))


def main():
    cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf8'))
    assert cert['alphabet'] == 'ab'
    case_names = [c['name'] for c in cert['cases']]
    assert case_names == ['L','K','singular_substitution']
    counts = [verify_case(c)[0] for c in cert['cases']]
    assert counts == [15,8,127], counts
    assert 127 > 15*8
    a,b,z = cert['cases']
    assert a['generators'] == ['aaaaaaa','baaaaaba']
    assert b['generators'] == ['aababa']
    assert z['generators'] == ['aababa'*7,'b'+'aababa'*5+'b'+'aababa']
    print('VERIFY_OK complete_reachable_quotients L=15 K=8 substitution=127 product=120 excess=7')


if __name__ == '__main__':
    main()
