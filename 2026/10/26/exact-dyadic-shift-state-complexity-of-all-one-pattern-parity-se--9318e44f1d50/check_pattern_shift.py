"""Independent finite DFAO minimization checks for all-one-pattern parity shifts."""
from collections import deque


def direct_value(m, n):
    bits = bin(n)[2:]
    block = '1' * m
    return sum(bits[i:i+m] == block for i in range(len(bits) - m + 1)) & 1


def transition(m, state, digit):
    carry, suffix, parity = state
    val = carry + digit
    out_digit = val & 1
    carry = val >> 1
    if out_digit:
        parity ^= int(suffix == m - 1)
        suffix = min(suffix + 1, m - 1)
    else:
        suffix = 0
    return (carry, suffix, parity)


def terminal(m, state):
    carry, suffix, parity = state
    while carry:
        out_digit = carry & 1
        carry >>= 1
        if out_digit:
            parity ^= int(suffix == m - 1)
            suffix = min(suffix + 1, m - 1)
        else:
            suffix = 0
    return parity


def build(m, c):
    states = [(c, 0, 0)]
    indices = {states[0]: 0}
    graph = []
    for state in states:
        row = []
        for digit in (0, 1):
            nxt = transition(m, state, digit)
            if nxt not in indices:
                indices[nxt] = len(states)
                states.append(nxt)
            row.append(indices[nxt])
        graph.append(tuple(row))
    output = [terminal(m, s) for s in states]
    return states, graph, output


def minimize(graph, output):
    # Partition refinement, independent of arithmetic state signatures.
    partition = output[:]
    while True:
        keys = [(output[i], partition[v[0]], partition[v[1]])
                for i, v in enumerate(graph)]
        key_ids = {key: i for i, key in enumerate(sorted(set(keys)))}
        new_partition = [key_ids[k] for k in keys]
        if new_partition == partition:
            return len(set(partition))
        partition = new_partition


def prediction(m, r):
    def reachable_count(k):
        return k + 1 if k < m else m + 1 + min(m - 1, k - m)
    return 2*m + sum(reachable_count(k) for k in range(r+1)) + (r == m)


def run():
    tested = 0
    inputs = 0
    for m in range(2, 12):
        for r in range(19):
            states, graph, output = build(m, 1 << r)
            minimal = minimize(graph, output)
            expected = prediction(m, r)
            assert len(states) == minimal == expected, (m, r, len(states), minimal, expected)
            tested += 1
            for n in range(1024):
                bits = bin(n)[2:][::-1] if n else ''
                at = 0
                for bit in bits:
                    at = graph[at][int(bit)]
                assert output[at] == direct_value(m, n + (1 << r)), (m, r, n)
                inputs += 1
    # Further arbitrary-shift samples check universal residual separation.
    additional = 0
    for m in (2, 3, 4, 5, 7):
        for c in range(81):
            states, graph, output = build(m, c)
            assert minimize(graph, output) == len(states), (m, c)
            additional += 1
    print('PASS: power-of-two formula and no-state-merging for', tested, 'parameter pairs')
    print('PASS: direct outputs for', inputs, 'inputs')
    print('PASS: arbitrary-shift no-merging for', additional, 'additional parameter pairs')
    print('EXAMPLE: m=3, shift powers r=0..10: ', [prediction(3,r) for r in range(11)])
    print('EXAMPLE: m=4, shift powers r=0..10: ', [prediction(4,r) for r in range(11)])

if __name__ == '__main__':
    run()
