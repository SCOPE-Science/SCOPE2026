"""Exact finite-window check of the initial palindromic deficit plateau.

The finite-block covering argument makes each calculation exact for the
specified finite parameter; it is not the proof of the universal theorem.
"""
def morph(s):
    return ''.join('01' if a == '0' else '10' for a in s)

def block(a, depth=5):
    for _ in range(depth):
        a = morph(a)
    return a

pairs = [block(a) + block(b) for a in '01' for b in '01']

def transform(s, M):
    return ''.join('a' if a == '0' else 'a' * M + 'b' for a in s)


def factors(M, n):
    # Each transformed 32-symbol Thue--Morse block is much longer than n;
    # every length-n factor is in the image of two consecutive length-32
    # aligned blocks, with every adjacent pair of block types represented.
    return set().union(*(set(w[i:i+n] for i in range(len(w)-n+1))
                         for w in (transform(x, M) for x in pairs)))

for M in range(1, 36):
    N = 2*M + 3
    cache = {}
    for n in range(N, 3*M+6):
        F = factors(M, n)
        cache[n] = (len(F), sum(x == x[::-1] for x in F))
    assert cache[N][0] == 3*M+6
    assert cache[N+1][0] == 3*M+10
    for t in range(1, M+2):
        n = N+t
        assert cache[n][0] == 3*M+7+3*t, (M,n,cache[n])
        assert cache[n][1] == (2 if (M+t)%2 else 1), (M,n,cache[n])
    assert cache[3*M+5][1] == 0
    for n in range(N, 3*M+5):
        delta = cache[n+1][0] - cache[n][0]
        gap = delta+2-cache[n][1]-cache[n+1][1]
        assert gap == 2, (M,n,gap)
print('PASS: exact transformed-block factor enumeration, M=1..35, all n=2M+3..3M+5.')
print('PASS: factor formula, palindrome counts, and constant gap on the stated plateau.')
