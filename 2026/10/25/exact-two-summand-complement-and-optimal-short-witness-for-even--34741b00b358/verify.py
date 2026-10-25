#!/usr/bin/env python3
"""Exact finite certificate for the Zeckendorf-even two-summand theorem."""
from itertools import chain

TRANSLATION = str.maketrans('01','10')
def flip(s):
    return s.translate(TRANSLATION)

def words(limit=18):
    w={1:'0',2:'01'}
    for k in range(3,limit+1):
        w[k]=w[k-1]+flip(w[k-2])
    return w

def parity_greedy(n):
    if n==0: return 0
    fib=[1,2]
    while fib[-1] <= n:
        fib.append(fib[-1]+fib[-2])
    bits=0
    for f in fib[::-1]:
        if n>=f:
            n-=f
            bits ^=1
    assert n==0
    return bits

def main():
    w=words(20)
    assert len(w[13])==377
    for k in range(3,21):
        assert len(w[k])==len(w[k-1])+len(w[k-2])
        assert w[k].startswith(w[k-1])
    for n in range(10000):
        assert int(w[20][n])==parity_greedy(n),n
    L=21
    F=set(w[13][i:i+L] for i in range(len(w[13])-L+1))
    assert len(F)==132
    assert F==set(w[14][i:i+L] for i in range(len(w[14])-L+1))
    assert {flip(t) for t in F}==F
    prefix=w[13][:L-1]
    for k in range(13,17):
        assert w[k][:L-1]==prefix
        boundary=w[k][-20:]+flip(prefix)
        assert all(boundary[i:i+L] in F for i in range(L-1))
        assert w[k+2][-20:]==flip(w[k][-20:])
        assert w[k+4][-20:]==w[k][-20:]
    S=(0,4,6,7,9,10)
    assert all(parity_greedy(a)==0 for a in S)
    assert all(any(t[20-a]=='0' for a in S) for t in F)
    # The preceding finite factor certificate inductively covers every
    # length-21 factor of the infinite word, rather than just a tested prefix.
    exceptions=[]
    for n in range(20):
        if not any(parity_greedy(a)==0 and parity_greedy(n-a)==0 for a in range(n+1)):
            exceptions.append(n)
    assert exceptions==[1,2,3,5]
    for n in range(6,20):
        assert any(a<=n and parity_greedy(n-a)==0 for a in S)
    assert all(not (a<=34 and parity_greedy(34-a)==0) for a in S if a<10)
    assert parity_greedy(34-10)==0
    # Additional independent sample, not needed for the infinite theorem.
    for n in range(20,10000):
        assert any(n>=a and parity_greedy(n-a)==0 for a in S)
    print('PASS: 132 complement-stable length-21 factors, 4 boundary classes, '+
          'all 132 witnesses, exact finite exceptions, optimal witness 10; '+
          '10,000 independent greedy parity checks')
if __name__=='__main__':
    main()
