#!/usr/bin/env python3
"""Independent executable verification of finite Baum-Sweet prefix statements.

Proof of the infinite formula is supplied in RESULT.md; this executable
checks finite prefixes and digit-automaton counts rather than certifying infinity.
"""

def digit_value(n):
    if n == 0:
        return 1
    s = format(n, 'b')
    return int(all(len(run) % 2 == 0 for run in s.split('1')))

NEXT = {'A':'AB', 'B':'CB', 'C':'BD', 'D':'DD'}
CODING = {'A':'1','B':'1','C':'0','D':'0'}

def via_morphism(k):
    state = 'A'
    for _ in range(k):
        state = ''.join(NEXT[s] for s in state)
    return ''.join(CODING[s] for s in state)

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def main():
    limit = 65536
    bits = ''.join(str(digit_value(i)) for i in range(limit))
    cnt = 0
    arch = 0
    seen = set()
    exception = {4**j + 1 for j in range(2,10)}
    for i, ch in enumerate(bits):
        cnt += (ch == '1')
        seen.add(ch)
        if len(seen) == 2:
            arch += 1
            seen.clear()
        N = i+1
        if N >= 6:
            assert arch == cnt - 2 - int(N in exception), (N, arch,cnt)
    for k in range(2,17):
        W = via_morphism(k)
        assert W == bits[:1<<k], k
        assert W.count('1') == fib(k+2), k
    for n in range(limit-1):
        if bits[n:n+2] == '11':
            assert n in {4**j-1 for j in range(9)}, n
        if n in {4**j-1 for j in range(9)}:
            assert bits[n:n+2] == '11', n
    # independent exhaustive check for small prefixes: every length-r
    # binary target occurs, but at least one length-(r+1) target is missing.
    for N in range(6,33):
        w = bits[:N]
        count=w.count('1')
        target=count-2-int(N in exception)
        if target <= 12:
            def occurs(t):
                it=iter(w)
                return all(c in it for c in t)
            import itertools
            assert all(occurs(''.join(t)) for t in itertools.product('01',repeat=target)),N
            assert any(not occurs(''.join(t)) for t in itertools.product('01',repeat=target+1)),N
    print('PASS: 65,536 prefix indices; 15 morphic iterates; 11-pair positions; independent small-subsequence enumeration.')

if __name__ == '__main__':
    main()
