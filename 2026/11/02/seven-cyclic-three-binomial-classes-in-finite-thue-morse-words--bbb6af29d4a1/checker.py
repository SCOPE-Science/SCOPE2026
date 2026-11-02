"""Self-contained exact checks of finite Thue--Morse rotation binomial spectra.
Run: python3 checker.py
The unrestricted theorem rests on the accompanying mathematical proof.
"""
from collections import Counter


def thue(k):
    w = '0'
    for _ in range(k):
        w = ''.join('01' if c == '0' else '10' for c in w)
    return w


def profile(w, length=3):
    counts = {'': 1}
    for i in range(1, length+1):
        for a in range(1 << i):
            counts[format(a, '0%db' % i)] = 0
    for c in w:
        for i in range(length, 0, -1):
            for a in range(1 << (i-1)):
                t = format(a, '0%db' % (i-1)) if i>1 else ''
                counts[t+c] += counts[t]
    return tuple(counts[format(j,'0%db' % i)] for i in range(1,length+1) for j in range(1 << i))


def test():
    for k in range(0, 10):
        w = thue(k)
        n = len(w)
        profiles = Counter(profile(w[i:]+w[:i]) for i in range(n))
        expected = {0: [1], 1: [1,1], 2: [1]*4}.get(k)
        if expected is None:
            m = n//2
            expected = [m//2]+[m//4]*6
        assert sorted(profiles.values()) == sorted(expected), (k,profiles)
        if k >= 3:
            # Two scattered counts alone separate every full 3-binomial class.
            ab = {}
            for i in range(n):
                rot = w[i:]+w[:i]
                p=profile(rot)
                # p indexes: length-one 0,1; length-two 00,01,10,11;
                # length-three 000,001,...
                pair = (p[3],p[7])
                if pair in ab: assert ab[pair]==p
                else: ab[pair]=p
            assert len(ab)==7
        print(k,n,len(profiles),sorted(profiles.values()))
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__': test()
