#!/usr/bin/env python3
"""Reproducible finite checks for the base-3/2 parity-word repetition theorem.

These checks supplement, rather than replace, the universal block argument.
"""

def sequence(size):
    x = bytearray(size)
    for n in range(size):
        if n % 3 == 0:
            x[n] = x[2*(n//3)] if n else 0
        elif n % 3 == 1:
            x[n] = 1-x[2*(n//3)]
        else:
            x[n] = x[2*(n//3)]
    return x

def parity_digits(n):
    parity=0
    while n:
        d=n % 3
        parity ^= d & 1
        n=2*(n-d)//3
    return parity

def run():
    size=50000
    x=sequence(size)
    for n in range(5000):
        assert x[n]==parity_digits(n), (n,x[n],parity_digits(n))
    assert ''.join(str(a) for a in x[12:21])=='101010101'
    longest_alternating=0
    r=1
    for i in range(size):
        if i and x[i]!=x[i-1]:
            r+=1
        else:
            r=1
        longest_alternating=max(longest_alternating,r)
    assert longest_alternating == 9, longest_alternating
    triples=[]
    tested=0
    for p in range(1,121):
        if p%3==0:
            continue
        # In the length-3p factor at start s, every index j in
        # [s,s+2p) must satisfy x[j]==x[j+p].
        r=0
        for j in range(size-p):
            if x[j] == x[j+p]:
                r+=1
            else:
                r=0
            if r>=2*p:
                s=j-2*p+1
                triples.append((s,p,bytes(x[s:s+3*p])))
                assert p==2 and bytes(x[s:s+3*p]) in (b'\x00\x01\x00\x01\x00\x01',b'\x01\x00\x01\x00\x01\x00')
        tested+=1
    assert triples and {v[2] for v in triples} == {b'\x00\x01\x00\x01\x00\x01', b'\x01\x00\x01\x00\x01\x00'}
    print('PASS: 5000 digit-parity values, 50000-symbol alternation bound,', tested, 'coprime-to-three periods,', len(triples), 'cubic occurrences. All such cubes have period two.')

if __name__=='__main__':
    run()
