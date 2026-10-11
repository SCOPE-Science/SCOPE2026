#!/usr/bin/env python3
"""Reproduce finite tests for dihedral Euler traces of strong cycle complexes.

Enumeration by vertex-filtration orders is independent of the 3-state formula.
No third-party packages are used.
"""
from itertools import permutations, product
from math import gcd


def face_ok(s):
    n = len(s)
    if any(s[i] and s[(i+1)%n] and s[i] != s[(i+1)%n] for i in range(n)):
        return False
    colors = set(s) - {0}
    if len(colors) == 1 and not any(s[i] == s[(i+1)%n] == 0 for i in range(n)):
        return False
    return True


def words_to_masks(n):
    out = set()
    for word in product((0, 1, 2), repeat=n):
        if face_ok(word):
            out.add(sum(1 << (2*i + c-1) for i,c in enumerate(word) if c))
    return out


def filtration_masks(n):
    out = set()
    for order in permutations(range(n)):
        rank = [0]*n
        for j,x in enumerate(order): rank[x] = j
        mask = 0
        for i in range(n):
            older = [j for j in ((i-1)%n,(i+1)%n) if rank[j] < rank[i]]
            if len(older) == 1:
                # right edge -> slot 0; left edge -> slot 1
                mask |= 1 << (2*i + (older[0] == (i-1)%n))
        sub=mask
        while True:
            out.add(sub)
            if not sub: break
            sub=(sub-1)&mask
    return out


def perm(n,k,flip):
    return tuple(2*((k-i)%n if flip else (i+k)%n) + ((1-c) if flip else c)
                 for i in range(n) for c in (0,1))


def trace(faces,n,k,flip):
    p=perm(n,k,flip); total=0
    for mask in faces:
        inds=[i for i in range(2*n) if (mask>>i)&1]
        if any(not ((mask>>p[i])&1) for i in inds): continue
        unseen=set(inds); cyc=0
        while unseen:
            x=next(iter(unseen));cyc+=1
            while x in unseen:
                unseen.remove(x);x=p[x]
        total+=(-1)**cyc
    return -total


def L(d): return -1+6*(d%3==0)-4*(d%4==0)

def Z(k): return (1,-1,-1,1)[k%4]

def refl(n,k):
    if n%2: return -Z((n-3)//2)
    return -Z(n//2-1 if k%2==0 else n//2-2)

def C(n): return -1+2*(n%3==0)-(n%4==0)

def B(n):
    if n%2: return -Z((n-3)//2)
    return (-Z(n//2-1)-Z(n//2-2))//2


def main():
    face_checks=0;action_checks=0
    for n in range(3,9):
        filt=filtration_masks(n); words=words_to_masks(n)
        assert filt==words, (n,len(filt),len(words))
        face_checks+=len(filt)
        for k in range(n):
            for flip in (False,True):
                actual=trace(filt,n,k,flip)
                expected=refl(n,k) if flip else L(gcd(n,k))
                assert actual==expected,(n,k,flip,actual,expected)
                action_checks+=1
        assert sum(trace(filt,n,k,False) for k in range(n)) == n*C(n)
        assert sum(trace(filt,n,k,False)+trace(filt,n,k,True) for k in range(n)) == n*(C(n)+B(n))
    for n in range(3,301):
        assert sum(L(gcd(n,k)) for k in range(n))==n*C(n),n
        refsum=sum(refl(n,k) for k in range(n))
        assert refsum==n*B(n),(n,refsum)
        assert (C(n)+B(n))%2==0,n
    print('VERIFY_OK independent_filtration_faces=%d signed_action_checks=%d arithmetic_sizes=298' % (face_checks,action_checks))


if __name__=='__main__': main()
