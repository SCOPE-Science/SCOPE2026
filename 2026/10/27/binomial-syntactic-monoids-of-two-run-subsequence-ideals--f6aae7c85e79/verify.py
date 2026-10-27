"""Independent finite checks for two-run subsequence-ideal transition monoids.
Run with Python 3: python verify.py
"""
from collections import deque
from itertools import combinations_with_replacement, product
from math import comb


def actions(r, s):
    size = r+s+1
    return (
        tuple(i+1 if i<r else i for i in range(size)),
        tuple(i+1 if r<=i<r+s else i for i in range(size))
    )


def apply(current, action):
    return tuple(action[i] for i in current)


def closure(r, s):
    generators = actions(r, s)
    identity = tuple(range(r+s+1))
    result = {identity}
    todo = deque([identity])
    while todo:
        t = todo.popleft()
        for action in generators:
            u = apply(t, action)
            if u not in result:
                result.add(u)
                todo.append(u)
    return result


def normal_forms(r,s):
    n = r+s+1
    result = set()
    for c in range(r+1):
        for t in combinations_with_replacement(range(s+1), r-c+1):
            f = [None]*n
            for i in range(c):
                f[i] = i+r-c
            for i in range(c,r+1):
                f[i] = r+t[i-c]
            for i in range(r+1,n):
                f[i] = min(i+t[-1], r+s)
            result.add(tuple(f))
    return result


def enumerate_words(r,s):
    n = r+s+1
    a,b=actions(r,s)
    result=set()
    for length in range(r+s+1):
        for word in product([a,b],repeat=length):
            t=tuple(range(n))
            for act in word:
                t=apply(t,act)
            result.add(t)
    return result


def greedy_recognizes(bits,r,s):
    i=0
    for bit in bits:
        if i<r and bit==0: i+=1
        elif r<=i<r+s and bit==1: i+=1
    return i==r+s


def subsequence_recognizes(bits,r,s):
    pattern=(0,)*r+(1,)*s
    for pos in __import__('itertools').combinations(range(len(bits)),len(pattern)):
        if tuple(bits[i] for i in pos)==pattern:
            return True
    return False


def main():
    checks=0
    for r in range(1,7):
        for s in range(1,7):
            cl=closure(r,s)
            nf=normal_forms(r,s)
            target=comb(r+s+2,r+1)-1
            assert len(cl)==target, ('size',r,s,len(cl),target)
            assert cl==nf, ('normal',r,s,len(cl),len(nf))
            identity=tuple(range(r+s+1))
            assert identity in cl
            assert all(apply(identity,g)!=identity for g in actions(r,s))
            if r<=4 and s<=4:
                assert cl==enumerate_words(r,s), ('words',r,s)
            checks+=1
    words=0
    for r in range(1,4):
        for s in range(1,4):
            for length in range(0,9):
                for bits in product((0,1),repeat=length):
                    assert greedy_recognizes(bits,r,s)==subsequence_recognizes(bits,r,s)
                    words+=1
    print('VERIFY_OK monoid_pairs=',checks,'word_membership_cases=',words)
    print('samples:',[(r,s,len(closure(r,s))) for r,s in [(1,1),(2,2),(3,3),(4,4),(6,6)]])

if __name__=='__main__':main()
