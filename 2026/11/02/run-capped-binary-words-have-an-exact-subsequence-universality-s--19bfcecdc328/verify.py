#!/usr/bin/env python3
"""Independent finite checks for exact run-capped binary universality spectra.
Run with Python 3 standard library: python3 verify.py
"""
from collections import Counter
from itertools import product


def arches(word):
    seen = set()
    k = 0
    for c in word:
        seen.add(c)
        if len(seen) == 2:
            k += 1
            seen.clear()
    return k


def contains_subsequence(pattern, host):
    j = 0
    for c in host:
        if j < len(pattern) and pattern[j] == c:
            j += 1
    return j == len(pattern)


def literal_index(host):
    k = 0
    while all(contains_subsequence(p, host) for p in product('01', repeat=k+1)):
        k += 1
    return k


def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def formula_row(h,k):
    # Coefficients of [u^k] F_h(z,u) with the length z^{2k} removed.
    if k == 0:
        return [1]+[2]*h
    P = [1]*h
    Pprev = [1]*(h-1)
    T = [a+(Pprev[i] if i<len(Pprev) else 0) for i,a in enumerate(P)]
    powT = [1]
    for _ in range(k-1):powT=mul(powT,T)
    B=[1]+T   # coefficients of 1+zT (degree h)
    out=mul(mul(P,powT),B)
    return [2*v for v in out]


def automaton_distribution(h,N):
    # Fully labeled transfer, independent of the compact formula.
    state={(None,None,0,0):1}
    out=[Counter({0:1})]
    for n in range(1,N+1):
        nxt=Counter()
        for (seen,last,run,k), multiplicity in state.items():
            for symbol in (0,1):
                run2=run+1 if symbol==last else 1
                if run2>h:continue
                if seen is None:
                    nextseen=symbol; delta=0
                elif seen==2:
                    nextseen=symbol; delta=0
                elif seen!=symbol:
                    nextseen=2; delta=1
                else:
                    nextseen=seen; delta=0
                nxt[(nextseen,symbol,run2,k+delta)] += multiplicity
        state=nxt
        count=Counter()
        for (_,_,_,k),multiplicity in state.items():count[k]+=multiplicity
        out.append(count)
    return out


def main():
    exhaustive=0
    literal=0
    max_n=16
    for h in range(1,6):
        transfer=automaton_distribution(h,max_n)
        for n in range(max_n+1):
            enumerated=Counter()
            for bits in product('01', repeat=n):
                word=''.join(bits)
                if '0'*(h+1) in word or '1'*(h+1) in word:continue
                k=arches(word)
                enumerated[k]+=1
                exhaustive+=1
                if n<=9:
                    assert literal_index(word)==k,(h,n,word,k)
                    literal+=1
            predicted=Counter()
            for k in range(n//2+1):
                row=formula_row(h,k)
                idx=n-2*k if k else n
                if 0<=idx<len(row) and row[idx]:predicted[k]=row[idx]
            assert enumerated==predicted,(h,n,enumerated,predicted)
            assert transfer[n]==predicted,(h,n,transfer[n],predicted)
        for k in range(1,10):
            row=formula_row(h,k)
            assert len(row)==k*(h-1)+h+1,(h,k,len(row))
            assert row[-1]==2,(h,k,'maximum length')
            assert row[0]==(2 if h==1 else 2**k),(h,k,'minimum length')
            for a,b in [('0','1'),('1','0')]:
                witness=a*h+(b+a*h)*k
                assert len(witness)==(h+1)*k+h
                assert arches(witness)==k
                assert a*(h+1) not in witness and b*(h+1) not in witness
    print(f'VERIFY_OK caps=1..5 lengths=0..{max_n} exhaustive_host_checks={exhaustive} literal_subsequence_checks={literal} boundary_k=1..9')

if __name__=='__main__':main()
