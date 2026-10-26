#!/usr/bin/env python3
"""Finite exact checks for three-symbol cyclic-substitution abelian complexities.

Checks are computational illustrations of an independently stated infinite proof.
"""

def morph(word, t):
    return b''.join(bytes([a]) * t + bytes([(a + 1) % 3]) for a in word)


def image(a, t, m):
    z = bytes([a])
    for _ in range(m):
        z = morph(z, t)
    return z


def direct_minmax(t, m):
    blocks = [image(a, t, m) for a in range(3)]
    N = len(blocks[0]); low = N; high = 0
    for left in blocks:
        for right in blocks:
            joined = left + right
            count = sum(v == 0 for v in joined[:N])
            low = min(low, count); high = max(high, count)
            for i in range(N):
                count -= joined[i] == 0
                count += joined[i + N] == 0
                low = min(low, count); high = max(high, count)
    return low, high


tests = 0
for t in (3, 4, 5, 6, 7, 15):
    witness = image(0, t, 4)
    pairs = {tuple(witness[i:i+2]) for i in range(len(witness)-1)}
    assert pairs == {(a,b) for a in range(3) for b in range(3)}
    P = 2
    for m in range(5):
        N = tuple(image(0,t,m).count(a) for a in range(3))
        assert sum(N) == (t+1)**m
        if m > 0:
            Nprev = tuple(image(0,t,m-1).count(a) for a in range(3))
            assert N == tuple(t*Nprev[a] + Nprev[(a-1)%3] for a in range(3))
            P += t*(max(Nprev)-min(Nprev))
        lower, upper = direct_minmax(t,m)
        assert upper-lower+1 == P, (t,m,P,lower,upper)
        tests += 1
        print(f't={t:2d} m={m} counts={N} lower={lower} upper={upper} P={P}')
print(f'PASS: {tests} exact factor-extremum checks, with all nine ordered pairs verified for each t')
