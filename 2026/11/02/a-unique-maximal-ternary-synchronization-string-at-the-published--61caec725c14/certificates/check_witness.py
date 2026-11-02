#!/usr/bin/env python3
"""Direct exact LCS verification for an explicit ternary epsilon-synchronization word."""
from pathlib import Path
from fractions import Fraction

s = Path(__file__).with_name('witness.txt').read_text().strip()
assert len(s) == 123
assert sorted(set(s)) == ['0', '1', '2']
assert [s.count(str(a)) for a in range(3)] == [41, 41, 41]
assert all(int(s[i]) + int(s[-1-i]) == 2 for i in range(len(s)))

def lcs(x, y):
    dp = [0]*(len(y)+1)
    for a in x:
        old = 0
        for j,b in enumerate(y,1):
            curr = dp[j]
            dp[j] = old+1 if a==b else max(dp[j], dp[j-1])
            old = curr
    return dp[-1]

peak = Fraction(0,1)
peaks = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)+1):
            ell = lcs(s[i:j], s[j:k])
            assert 26*ell < 12*(k-i), (i,j,k,ell)
            val = Fraction(2*ell,k-i)
            if val > peak:
                peak = val
                peaks = [(i,j,k,ell)]
            elif val==peak:
                peaks.append((i,j,k,ell))
assert peak == Fraction(58,63), peak
print('WITNESS_OK length=123 counts=41,41,41 reversal_complement=yes peak=58/63')
print('peak_triples=',len(peaks), 'first=',peaks[0])
