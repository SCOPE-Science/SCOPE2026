#!/usr/bin/env python3
"""Independent exact-rational checks for stationary Markov jury increments.

Standard library only.  Checks examples, an independent count-DP, and the
complement bijection at several rational transition parameter pairs.
Finite tests supplement, and do not replace, the all-size path argument.
"""
from fractions import Fraction as Q
from itertools import product


def path_probability(bits, s, t):
    p0, p1 = t / (s+t), s / (s+t)
    v = p1 if bits[0] else p0
    for x, y in zip(bits, bits[1:]):
        v *= ((1-s) if not x else t) if y == 0 else (s if not x else (1-t))
    return v


def enumerated_majority(n, s, t):
    return sum((path_probability(w,s,t) for w in product((0,1),repeat=n)
                if sum(w)>n//2), Q(0))


def dynamic_majority(n, s, t):
    # State = (most recent bit, number of ones); independent from path enumeration.
    d = {(0,0): t/(s+t), (1,1): s/(s+t)}
    for _ in range(1,n):
        nd = {}
        for (last,ones),w in d.items():
            for bit in (0,1):
                prob = ((1-s) if bit == 0 else s) if last==0 else (t if bit==0 else (1-t))
                key = (bit,ones+bit)
                nd[key] = nd.get(key,Q(0)) + w*prob
        d=nd
    return sum((v for (_,k),v in d.items() if 2*k>n),Q(0))


def verify():
    count=0
    samples=[(Q(9,10),Q(3,5)),(Q(1,5),Q(1,10)),
             (Q(1,4),Q(11,20)),(Q(17,20),Q(19,20)),
             (Q(1,2),Q(1,2)),(Q(9,10),Q(99,100)),
             (Q(3,4),Q(1,4)),(Q(1,100),Q(99,100))]
    for s,t in samples:
        p = s/(s+t)
        assert p>Q(1,2) if s>t else (p<Q(1,2) if s<t else p==Q(1,2));count+=1
        for m in range(5):
            n=2*m+1
            jn=enumerated_majority(n,s,t)
            assert jn==dynamic_majority(n,s,t);count+=1
            jnext=enumerated_majority(n+2,s,t)
            assert jnext==dynamic_majority(n+2,s,t);count+=1
            if m<4:
                gain=Q(0);loss=Q(0)
                for word in product((0,1),repeat=n+2):
                    interior=sum(word[1:-1])
                    if word[0]==1 and word[-1]==1 and interior==m:
                        gain += path_probability(word,s,t)
                        flipped=tuple(1-bit for bit in word)
                        assert sum(flipped[1:-1])==m+1;count+=1
                        assert path_probability(word,s,t)*t==path_probability(flipped,s,t)*s;count+=1
                    if word[0]==0 and word[-1]==0 and interior==m+1:
                        loss += path_probability(word,s,t)
                assert gain>0 and loss>0;count+=1
                assert gain*t==loss*s;count+=1
                assert jnext-jn==gain-loss;count+=1
                assert jnext-jn==(s-t)/s*gain;count+=1
                assert (jnext>jn if s>t else jnext<jn if s<t else jnext==jn);count+=1
        if s==t:
            for m in range(5):
                assert enumerated_majority(2*m+1,s,t)==Q(1,2);count+=1
    s,t=Q(9,10),Q(3,5)
    exact=[Q(3,5),Q(177,250),Q(9687,12500),Q(102621,125000),Q(5342487,6250000)]
    for m,value in enumerate(exact):
        actual=enumerated_majority(2*m+1,s,t)
        assert actual==value,(m,actual,value)
        count+=1
    assert 1-s-t==Q(-1,2);count+=1
    print(f'PASS: {count} exact rational assertions on 8 independent parameter pairs.')
    print('Example probabilities for n=1,3,5,7,9:', ', '.join(str(x) for x in exact))


if __name__=='__main__':
    verify()
