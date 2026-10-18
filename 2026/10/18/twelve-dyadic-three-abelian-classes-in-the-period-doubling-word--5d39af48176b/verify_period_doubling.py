"""Exact independent finite checks for period-doubling three-abelian dyadic theorem.

The infinite conclusion relies on the mathematical induction, not the tests.
"""
from collections import Counter


def morphic(depth):
    s = "0"
    for _ in range(depth):
        s = ''.join('01' if ch == '0' else '00' for ch in s)
    return s


def by_valuation(length):
    return ''.join(str(((i + 1) & -(i + 1)).bit_length() - 1 & 1) for i in range(length))


def factors_signatures(s, n):
    counts = Counter(s[i:i+3] for i in range(n-2))
    ones = s[:n].count('1')
    total = len(s)-n+1
    signatures = set()
    reduced = set()
    alphabet = ('000','001','010','011','100','101','110','111')
    for i in range(total):
        sig = (ones, s[i:i+2], s[i+n-2:i+n])
        reduced.add(sig)
        full = (s[i:i+2], s[i+n-2:i+n], tuple(counts.get(t,0) for t in alphabet))
        signatures.add(full)
        # Gap classification is a prediction, distinct from the signature enumeration.
        boundary00 = (s[i:i+2] == '00') + (s[i+n-2:i+n] == '00')
        assert counts.get('101',0) == 2*ones - 1 - n//2 + boundary00, (n,i,sig,counts)
        if i+1<total:
            old = s[i:i+3]
            new = s[i+n-2:i+n+1]
            counts[old] -= 1
            counts[new] += 1
            ones += (s[i+n]=='1')-(s[i]=='1')
    return reduced, signatures


def test():
    p = morphic(18)
    assert p == by_valuation(len(p))
    # Base induction data: each weight has all three letter endpoints (00),(01),(10).
    # The class endpoint pairs are six ordered length-two blocks, not seven.
    pairs = {('01','01'),('01','00'),('00','01'),('10','10'),('10','00'),('00','10')}
    scanned = 0
    for n in [8,16,32,64,128,256,512,1024,2048,4096]:
        red, full = factors_signatures(p[:min(len(p), max(4096,8*n))], n)
        weight_set = {n//3,(n+2)//3}
        if n == 8:
            ends = {(k, pre[0],suf[-1]) for k,pre,suf in red}
            assert ends == {(k,a,b) for k in weight_set for a,b in (('0','0'),('0','1'),('1','0'))}, ends
        if n>=16:
            expected = {(k,a,b) for k in weight_set for a,b in pairs}
            assert red == expected, (n, len(red),red-expected,expected-red)
            assert len(full)==12, (n,len(full))
        assert len(full)==len(red), (n,len(full),len(red))
        scanned += 1
    for n in range(4,129,2):
        red, full = factors_signatures(p[:5000],n)
        assert len(red)==len(full), (n, len(red), len(full))
    print('VERIFY_OK independent_generation=262144 dyadic_scales=%d other_even_lengths=63' % scanned)


if __name__ == '__main__':
    test()
