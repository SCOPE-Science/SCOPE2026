"""Independent direct enumeration for fixed-length one-delete/one-insert outputs.

Run: python3 verify_direct.py
"""
from itertools import product


def deletion_set(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}


def output_set(word):
    outcomes = set()
    for shrunk in deletion_set(word):
        for p in range(len(word)):
            for b in "01":
                outcomes.add(shrunk[:p] + b + shrunk[p:])
    return outcomes


def transition(mask, a, w):
    nxt = 0
    if mask & 1:
        if a == w:
            nxt |= 1
        nxt |= 2 | (1 << (2 + w)) | (1 << (4 + a))
    if (mask & 2) and a == w:
        nxt |= 2
    for bit in range(2):
        if (mask & (1 << (2 + bit))) and a == bit:
            nxt |= 2 | (1 << (2 + w))
        if (mask & (1 << (4 + bit))) and w == bit:
            nxt |= 2 | (1 << (4 + a))
    return nxt


def automaton_count(x, z):
    states = {(1, 1): 1}
    for a, b in zip(x, z):
        nxt = {}
        for (s, t), count in states.items():
            for w in (0, 1):
                u = transition(s, int(a), w)
                v = transition(t, int(b), w)
                if u and v:
                    nxt[u, v] = nxt.get((u, v), 0) + count
        states = nxt
    return sum(states.values())


def target_pair(n):
    r, c = divmod(n - 4, 4)
    if c == 0:
        u, v = '01' * r, '01' * r
    elif c == 1:
        u, v = '01' * r + '0', '10' * r
    elif c == 2:
        u, v = '01' * r + '0', '1' + '01' * r
    else:
        u, v = '01' * (r + 1), '0' + '10' * r
    return u + '0110' + v, u + '1001' + v


if __name__ == '__main__':
    checked = 0
    for n in range(2, 9):
        words = [''.join(p) for p in product('01', repeat=n)]
        outputs = {w: output_set(w) for w in words}
        for i, x in enumerate(words):
            for z in words[i:]:
                brute = len(outputs[x] & outputs[z])
                assert brute == automaton_count(x, z), (n, x, z, brute)
                checked += 1
    for n in range(4, 15):
        x, z = target_pair(n)
        assert not (deletion_set(x) & deletion_set(z)), n
        expected = n * n // 4 + 4
        assert len(output_set(x) & output_set(z)) == expected, n
        assert automaton_count(x, z) == expected, n
    print('DIRECT_VERIFY_OK all_pairs_n_le_8=', checked, 'constructed_cases_4_through_14=11')
