#!/usr/bin/env python3
"""Standalone exact finite-state certificate for five-point arithmetic factors.

For each input bit of the fixed difference, this verifier computes the full
nondeterministic carry machine over all possible starting-position bits.
Every reachable determinized state is checked; finite-prefix computations
serve only as independent regression tests.
"""
from collections import deque, Counter

LENGTH = 5
B = LENGTH
FULL_MASK = (1 << 16)-1


def encode(carries, prev, rel):
    c = sum(v * B**j for j, v in enumerate(carries))
    return (c * 32 + prev) * 16 + rel


def decode(code):
    rel = code & 15
    code >>= 4
    prev = code & 31
    code >>= 5
    return tuple(code // B**j % B for j in range(4)), prev, rel


def transition(code, d_bit, n_bit):
    carries, prev, rel = decode(code)
    bits = n_bit
    new_carries = []
    for j in range(1, LENGTH):
        total = n_bit + j * d_bit + carries[j-1]
        bits |= (total & 1) << j
        new_carries.append(total // 2)
    base_pair = (prev & 1) & n_bit
    flip = 0
    for j in range(1, LENGTH):
        pair = ((prev >> j) & 1) & ((bits >> j) & 1)
        flip |= (pair ^ base_pair) << (j-1)
    return encode(tuple(new_carries), bits, rel ^ flip)


def build():
    initial = encode((0, 0, 0, 0), 0, 0)
    nodes = [initial]
    idx = {initial: 0}
    q = deque([initial])
    edges = []
    while q:
        code = q.popleft()
        nxt = [transition(code, d, n) for d in (0, 1) for n in (0, 1)]
        edges.append(tuple(nxt))
        for t in nxt:
            if t not in idx:
                idx[t] = len(nodes)
                nodes.append(t)
                q.append(t)
    assert len(nodes) == len(edges) == 864

    # Terminal outcomes when difference has no further nonzero digits.
    # Allow arbitrary finitely many higher bits of the starting position.
    # A terminal state with zero carries has already computed all output bits
    # (any further leading zeros leave the overlap parity unchanged).
    out = [(1 << decode(code)[2]) if not any(decode(code)[0]) else 0
           for code in nodes]
    rounds = 0
    while True:
        changed = False
        for k, e in enumerate(edges):
            val = out[k] | out[idx[e[0]]] | out[idx[e[1]]]
            if val != out[k]:
                out[k] = val
                changed = True
        rounds += 1
        if not changed:
            break
        assert rounds <= len(nodes) * 16  # finite least-fixed-point closure
    assert all(0 < m <= FULL_MASK for m in out)

    def subset_step(subset, bit):
        result = set()
        for i in subset:
            e = edges[i]
            result.add(idx[e[2*bit]])
            result.add(idx[e[2*bit+1]])
        return frozenset(result)

    start = frozenset({0})
    det = [start]
    positions = {start: 0}
    work = deque([start])
    det_edges = []
    while work:
        ss = work.popleft()
        t0, t1 = subset_step(ss, 0), subset_step(ss, 1)
        det_edges.append((t0, t1))
        for tt in (t0, t1):
            if tt not in positions:
                positions[tt] = len(det)
                det.append(tt)
                work.append(tt)
    assert len(det) == len(det_edges) == 1302

    def output(ss):
        mask = 0
        for i in ss:
            mask |= out[i]
        return mask

    # Inductively check *every* reachable determinized state and its two
    # transitions against the exact three-class popcount invariant.
    tclass = {start: 0}
    todo = deque([start])
    count = Counter()
    while todo:
        ss = todo.popleft()
        t = tclass[ss]
        target = (0x0001, 0xff96, 0xffff)[t]
        actual = output(ss)
        assert actual == target, (t, hex(actual), hex(target))
        count[t] += 1
        for bit, nxt in enumerate(det_edges[positions[ss]]):
            cls = min(2, t+bit)
            if nxt in tclass:
                assert tclass[nxt] == cls  # no inconsistent class for same subset
            else:
                tclass[nxt] = cls
                todo.append(nxt)
    assert len(tclass) == 1302
    assert (count[0], count[1], count[2]) == (2, 13, 1287)

    # Explicit exceptional relative pattern labels, q_i=r(n+id) xor r(n).
    missing_rel = tuple(k for k in range(16) if not (0xff96 >> k) & 1)
    assert missing_rel == (0, 3, 5, 6)
    missing_abs = sorted(tuple((a,) + tuple(a ^ ((sig >> j) & 1)
                           for j in range(4)))
                         for sig in missing_rel for a in (0, 1))
    missing_words = {''.join(map(str, bits)) for bits in missing_abs}
    assert missing_words == {
        '00000', '11111', '00110', '11001',
        '01010', '10101', '01100', '10011'
    }

    # Exhaustive direct check for a substantial independent sample of fixed
    # differences; not used to prove the infinite theorem.
    max_d = 128
    sample_n = 131072
    bits = bytearray(sample_n + max_d*4)
    for n in range(1, len(bits)):
        bits[n] = bits[n >> 1] ^ ((n & 1) & ((n >> 1) & 1))
    witnesses = 0
    for d in range(1, max_d+1):
        found = set()
        for n in range(sample_n):
            pat = (bits[n] << 4) | (bits[n+d] << 3) | (bits[n+2*d] << 2) | (bits[n+3*d] << 1) | bits[n+4*d]
            found.add(pat)
            if len(found) == 32:
                break
        assert len(found) == (24 if not (d & (d-1)) else 32), (d, len(found))
        if not (d & (d-1)):
            assert {format(p, '05b') for p in range(32) if p not in found} == missing_words
        witnesses += len(found)

    print('VERIFY_OK nfa_states=864 dfa_states=1302 classes=2,13,1287 '
          'relative_masks=0x0001,0xff96,0xffff '
          'missing=00000,11111,00110,11001,01010,10101,01100,10011 '
          f'direct_d=1..128 direct_patterns={witnesses}')


if __name__ == '__main__':
    build()
