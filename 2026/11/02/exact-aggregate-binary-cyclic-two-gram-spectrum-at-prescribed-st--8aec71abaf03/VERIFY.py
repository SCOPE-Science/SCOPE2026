#!/usr/bin/env python3
"""Direct finite checks for aggregate cyclic binary 2-gram profiles."""
from itertools import product


def profile(word):
    n = len(word)
    assert n >= 2
    a = sum(word[i] == '0' and word[(i+1) % n] == '0' for i in range(n))
    b = sum(word[i] == '1' and word[(i+1) % n] == '1' for i in range(n))
    t = sum(word[i] == '0' and word[(i+1) % n] == '1' for i in range(n))
    z = sum(word[i] == '1' and word[(i+1) % n] == '0' for i in range(n))
    assert t == z and a+b+2*t == n
    return a,t


def direct(n):
    return {profile(''.join(bits)) for bits in product('01',repeat=n)}


def interval_witness(lengths, target_a, target_t):
    """Construct one word per strand from exact transition/run decomposition."""
    n = len(lengths)
    N = sum(lengths)
    if target_t == 0:
        for tags in product('01',repeat=n):
            words=[symbol*L for symbol,L in zip(tags,lengths)]
            if sum(profile(w)[0] for w in words)==target_a:
                return words
        return None

    caps=[L//2 for L in lengths]
    for transitions in product(*(range(c+1) for c in caps)):
        if sum(transitions)!=target_t:continue
        active=[i for i,t in enumerate(transitions) if t]
        if not active:continue
        inactive=[i for i in range(n) if not transitions[i]]
        for bits in product((0,1),repeat=len(inactive)):
            base=sum(lengths[j] for j,bit in zip(inactive,bits) if bit==0)
            total=sum(lengths[i]-2*transitions[i] for i in active)
            if not base<=target_a<=base+total:continue
            remaining=target_a-base
            words=['']*n
            for j,bit in zip(inactive,bits):words[j]=('0' if bit==0 else '1')*lengths[j]
            for i in active:
                t=transitions[i]
                a=min(remaining,lengths[i]-2*t)
                remaining-=a
                b=lengths[i]-2*t-a
                words[i]='0'*(a+1)+'1'*(b+1)+'01'*(t-1)
            assert remaining==0
            assert all(len(w)==L for w,L in zip(words,lengths))
            assert sum(profile(w)[0] for w in words)==target_a
            assert sum(profile(w)[1] for w in words)==target_t
            return words
    return None


def predicted(lengths):
    N=sum(lengths)
    S=sum(L//2 for L in lengths)
    return {(A,T) for T in range(S+1) for A in range(N-2*T+1)
            if interval_witness(lengths,A,T) is not None}


def closed_two(n1,n2):
    N=n1+n2
    S=n1//2+n2//2
    out={(0,0),(n1,0),(n2,0),(N,0)}
    out|={(a,1) for a in range(N-1) if n1!=n2 or a!=n1-1}
    out|={(a,t) for t in range(2,S+1) for a in range(N-2*t+1)}
    assert len(out)==S*(N-S)+4-2*(n1==n2)
    return out


def direct_sum(lengths):
    out={(0,0)}
    for L in lengths:
        out={(a+c,b+d) for a,b in out for c,d in direct(L)}
    return out


def verify():
    checked=0
    for n1 in range(2,10):
        for n2 in range(2,10):
            a=direct_sum((n1,n2))
            b=closed_two(n1,n2)
            c=predicted((n1,n2))
            assert a==b==c,(n1,n2,a^b,a^c)
            checked+=1
    triples=0
    for lengths in product(range(2,6),repeat=3):
        actual=direct_sum(lengths)
        expected=predicted(lengths)
        assert actual==expected,(lengths,actual^expected)
        S=sum(L//2 for L in lengths)
        N=sum(lengths)
        for T in range(3,S+1):
            assert all((A,T) in expected for A in range(N-2*T+1))
        triples+=1
    quadruples=0
    for lengths in product(range(2,5),repeat=4):
        assert direct_sum(lengths)==predicted(lengths),lengths
        quadruples+=1
    for k in range(2,13):
        lengths=(2,)*k
        N=2*k
        assert interval_witness(lengths,1,k-1) is None
        assert interval_witness(lengths,0,k-1) is not None
        assert interval_witness(lengths,2,k-1) is not None
    print('VERIFY_OK two_length_pairs=%d triple_length_tuples=%d quadruple_length_tuples=%d sharpness_k=2..12' % (checked,triples,quadruples))

if __name__=='__main__':verify()
