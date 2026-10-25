#!/usr/bin/env python3
"""Exact finite-state and symbolic-induction checks for Rudin--Shapiro progression correlations.

Only Python's standard library is required. No numerical approximations enter the certificate.
"""
from collections import deque, defaultdict
from fractions import Fraction

START = ((0, 0, 0), (0, 0, 0, 0))

def branch(state, digit, source_bit):
    carry, previous = state
    x = tuple((source_bit + j*digit + carry[j-1]) % 2 if j else source_bit for j in range(4))
    newcarry = tuple((source_bit + j*digit + carry[j-1]) // 2 for j in range(1, 4))
    sign = 1 if sum(a*b for a,b in zip(previous,x)) % 2 == 0 else -1
    return (newcarry, x), sign


def T(vector, digit):
    out = defaultdict(int)
    for state, weight in vector.items():
        for bit in range(2):
            dst, sign = branch(state, digit, bit)
            out[dst] += sign * weight
    return {s: w for s, w in out.items() if w}


def add(x, y, ax=1, ay=1):
    keys = set(x) | set(y)
    return {k: v for k in keys if (v := ax*x.get(k,0) + ay*y.get(k,0)) != 0}


def scale(x, a):
    return {k:a*v for k,v in x.items() if a*v}


def path(bits):
    d={START:1}
    for b in bits:
        d=T(d,b)
    return d


def norm(v):
    return sum(abs(a) for a in v.values())


def verify_affine_norm(a, b, slope, intercept, tmin=7):
    # Certify a stable sign for each affine coefficient on the full half-line t >= tmin.
    totalslope=totalintercept=0
    for s in set(a)|set(b):
        u=a.get(s,0);v=b.get(s,0)
        atmin=u*tmin+v
        if u>0:
            assert atmin>=0, (s,u,v)
            sign=1
        elif u<0:
            assert atmin<=0, (s,u,v)
            sign=-1
        else:
            sign=1 if v>=0 else -1
        totalslope += sign*u
        totalintercept += sign*v
    assert (totalslope,totalintercept)==(slope,intercept),((totalslope,totalintercept),(slope,intercept))


def verify():
    # Complete finite carry/output automaton, not a bounded-length enumeration.
    reached={START}
    pending=deque([START])
    while pending:
        s=pending.popleft()
        for digit in range(2):
            for bit in range(2):
                dst,_=branch(s,digit,bit)
                if dst not in reached:
                    reached.add(dst);pending.append(dst)
    assert len(reached)==30, len(reached)
    for s in reached:
        for digit in (0,1):
            for bit in (0,1):
                assert branch(s,digit,bit)[0] in reached
    # After h is exhausted, h-digits are all zero. Verify that the 3-step
    # terminal average is an EXACT fixed point of the zero-digit operator.
    f0={s:1 for s in reached}
    def dual(f,digit):
        return {s:sum(sign*f[dst] for bit in (0,1)
                      for dst,sign in [branch(s,digit,bit)]) for s in reached}
    f3=dual(dual(dual(f0,0),0),0)
    assert dual(f3,0)==scale_full(f3,2,reached)
    def corr(h):
        bits=[(h>>j)&1 for j in range(h.bit_length())]
        d=path(bits)
        return Fraction(sum(w*f3[s] for s,w in d.items()),8*(2**len(bits)))
    assert corr(1)==Fraction(-1,2)
    small={h:corr(h) for h in range(3,18,2)}
    assert all(abs(x)<Fraction(1,2) for x in small.values())
    # Every possible five-bit prefix of an odd positive spacing.
    tv5={h: norm(path([(h>>j)&1 for j in range(5)])) for h in range(1,32,2)}
    assert {h for h,x in tv5.items() if x>16}=={1,31}
    assert {h for h,x in tv5.items() if x==16}=={15,17}
    for h in (15,17):
        base=path([(h>>j)&1 for j in range(5)])
        assert all(norm(T(base,b))==24 for b in (0,1))
    # All exceptional branches have an exact two-parity affine form.
    # Each branch starts at five bits and extends by its own repeated digit.
    for mode in (0,1):
        def exceptional(k):
            return path([1]+[mode]*(k-1))
        d5,d6,d7,d8=(exceptional(k) for k in (5,6,7,8))
        rawodd=add(d5,d7,1,-1)
        raweven=add(d6,d8,1,-1)
        assert all(w%24==0 for w in rawodd.values())
        assert all(w%48==0 for w in raweven.values())
        B={s:w//24 for s,w in rawodd.items() if w}
        assert B=={s:w//48 for s,w in raweven.items() if w}
        assert len(B)==2 and set(B.values())=={1}
        vodd=add(d5,B,1,7)
        veven=add(d6,B,1,15)
        assert T(B,mode)==scale(B,2)
        assert T(vodd,mode)==add(veven,B,1,-1)
        assert T(veven,mode)==add(vodd,B,1,-1)
        for parityv in (vodd,veven):
            negative_B=scale(B,-1)
            verify_affine_norm(negative_B,parityv,2,6)
            opposite=1-mode
            opposite_a=T(negative_B,opposite)
            opposite_b=T(parityv,opposite)
            verify_affine_norm(opposite_a,opposite_b,4,4)
            for nextbit in (0,1):
                verify_affine_norm(T(opposite_a,nextbit),T(opposite_b,nextbit),8,0)
        # Extra zero-padding is required when a word ends on the all-one branch.
        for k in range(5,16):
            d=exceptional(k)
            assert norm(d)==2**(k-1)+4
            if mode==1:
                assert norm(T(T(d,0),0))<2**(k+1)
            else:
                assert norm(T(T(d,1),0))<2**(k+1)
    # Independent exact checks of the output sign function on dyadic cylinders.
    def rs(n):
        return -1 if (n & (n>>1)).bit_count()%2 else 1
    for h in (1,2,3,5,7,9,11,13,15,17,31,33,63,65):
        n=1<<16
        z=sum(rs(i)*rs(i+h)*rs(i+2*h)*rs(i+3*h) for i in range(n))
        assert abs(Fraction(z,n)-corr(h))<=Fraction(32*h+16,n)
        if h%2==0:
            assert corr(h)==corr(h//2)
    print('VERIFY_OK: 30 reachable transducer states; three-step stationary tail;')
    print('16 exhaustive five-bit prefixes; two symbolic affine branches,')
    print('two parity phases and both outgoing bits; strict equality classification;')
    print('independent 14-lag binary prefix comparisons.')
    print('small odd correlations:',small)


def scale_full(v,m,states):
    return {s:m*v.get(s,0) for s in states}

if __name__=='__main__':
    verify()
