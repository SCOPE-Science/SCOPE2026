#!/usr/bin/env python3
"""Separate two-coordinate matrix check of scheduling residue criterion."""
from itertools import product

def apply_A(p):return p[0]^p[1],p[1]
def apply_B(p):return p[0],p[0]^p[1]

def mat(word):
    images=[(1,0),(0,1)]
    for char in word:
        images=[(apply_A if char==0 else apply_B)(p) for p in images]
    return images

def order(images):
    def apply(p):
        return ((p[0]&images[0][0])^(p[1]&images[1][0]),(p[0]&images[0][1])^(p[1]&images[1][1]))
    for k in [1,2,3]:
        works=True
        for q in [(1,0),(0,1)]:
            x=q
            for _ in range(k):x=apply(x)
            if x!=q:works=False
        if works:return k
    raise AssertionError(images)

def main():
    z=0
    for n in range(2,15):
        for w in product((0,1),repeat=n):
            if not (0 in w and 1 in w):continue
            p=order(mat(w))
            if n&1: exp=2
            else:
                r=sum(w[::2]); b=sum(w)
                exp=1 if (b-2*r)%3==0 else 3
            assert p==exp,(w,p,exp)
            z+=1
    print('ASYNC_BIPARTITE_QUOTIENT_OK','binary_schedule_words=',z,'lengths=2..14')
if __name__=='__main__': main()
