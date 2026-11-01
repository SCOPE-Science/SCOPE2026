#!/usr/bin/env python3
"""Finite numerical corroboration of the irrational-rotation ordinal coding theorem.

All universal assertions follow from the mathematical proof, not these tests.
Run: python3 CHECK.py
"""
import math


def check_alpha(alpha):
    assert 0.0 < alpha < 0.5
    a = (1 - 2*alpha)/(1 - alpha)
    b = alpha/(1 - alpha)
    h = -(1 - 2*alpha)*math.log(a) - alpha*math.log(b)
    hb = -(1-alpha)*math.log(1-alpha)-alpha*math.log(alpha)
    K = max(abs(math.log(alpha)),abs(math.log(1-alpha))) + 3*abs(math.log(a)) + 2*abs(math.log(b))
    previous = 0.0
    for n in (1, 2, 3, 5, 8, 12, 20, 30, 40, 60):
        cuts = sorted((-j*alpha) % 1.0 for j in range(n+1))
        p = {}
        for j, left in enumerate(cuts):
            right = cuts[j+1] if j+1 < len(cuts) else cuts[0]+1
            x = (left+right)/2 % 1
            word = ''.join('D' if (x+t*alpha) % 1 >= 1-alpha else 'U' for t in range(n))
            p[word] = p.get(word, 0.0) + right-left
        assert len(p) == n+1, (alpha, n, len(p))
        assert abs(sum(p.values()) - 1) < 1e-11
        q = {}
        for word in p:
            k = word.count('D')
            first = int(word[0] == 'D')
            last = int(word[-1] == 'D')
            uu = n-1-2*k+first+last
            ud = k-first
            assert uu >= 0 and ud >= 0 and 'DD' not in word
            assert abs(k - n*alpha) < 1.00000000001
            q[word] = (alpha if first else 1-alpha)*(a**uu)*(b**ud)
            assert math.exp(-K-1e-10) * math.exp(-n*h) <= q[word]
            assert q[word] <= math.exp(K+1e-10)*math.exp(-n*h)
        overlap = sum(min(p[w],q[w]) for w in p)
        assert overlap > 0
        assert overlap <= 1+1e-10
        entropy = -sum(z*math.log(z) for z in p.values())
        relative_entropy = sum(p[w]*math.log(p[w]/q[w]) for w in p)
        predicted = hb+(n-1)*h-entropy
        assert abs(relative_entropy-predicted) < 1e-9
        if n <= 2:
            assert abs(overlap-1) < 1e-9, (n,overlap)
        if n>=40:
            assert 1-overlap > .9999
        if n==60:
            assert -math.log(overlap)/n > 0.70*h
        if n==2:
            assert abs(p.get('UD',0)-alpha) < 1e-9
            assert abs(p.get('DU',0)-alpha) < 1e-9
            assert abs(p.get('UU',0)-(1-2*alpha)) < 1e-9
        previous = overlap
    assert h > 0
    assert abs((-b) - (a-1)) < 1e-14
    print('alpha={:.12g}  Markov entropy={:.12g}  last overlap={:.6g}  checks=PASS'.format(alpha,h,previous))


if __name__ == '__main__':
    check_alpha((math.sqrt(5)-1)/4)
    check_alpha(math.sqrt(2)-1)
    check_alpha((math.sqrt(3)-1)/2)
    print('VERIFICATION_OK')
