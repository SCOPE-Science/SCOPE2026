#!/usr/bin/env python3
"""Independent prefix-window and repeated-tortoise verifier.
Enumerates from a proved covering prefix of the paperfolding word.
"""
from pathlib import Path
import csv


def f(n):
    # The independent recurrence: f(2r)=f(r), f(4r+1)=0, f(4r+3)=1.
    if n%2==0:return f(n//2)
    if n%4==1:return 0
    return 1


def factors(n):
    h=n.bit_length();p=1<<(h+1)
    stream=bytes(f(i) for i in range(1,5*p+n))
    return {stream[i:i+n] for i in range(5*p)}


def tortoise_once(w):
    j=w.find(b'\x01')
    return w if j<0 else w[:j]+w[j+1:]+b'\x01'


def tortoise_power(w,k):
    for i in range(k):w=tortoise_once(w)
    return w


def collision(words,k):
    seen={}
    for w in sorted(words):
        image=tortoise_power(w,k)
        if image in seen and seen[image]!=w:
            return seen[image],w
        seen[image]=w
    return None


def main():
    with open('threshold_table.csv',newline='',encoding='utf-8') as file:
        rows=list(csv.DictReader(file))
    assert len(rows)==31
    for row in rows:
        k=int(row['k']); t=int(row['threshold'])
        for n,expect_collision in ((t-1,True),(t,False)):
            S=factors(n)
            assert len(S)==int(row['factors_previous' if expect_collision else 'factors_at_threshold'])
            c=collision(S,k)
            assert (c is not None)==expect_collision, (k,n)
            if expect_collision:
                a=bytes(int(x) for x in row['collision_predecessor_first'])
                b=bytes(int(x) for x in row['collision_predecessor_second'])
                assert a in S and b in S and a!=b
                assert tortoise_power(a,k)==tortoise_power(b,k)
            else:
                assert min(w.count(1) for w in S)==int(row['minimum_ones_at_threshold'])
    print('PREFIX_OK independent recursion, original tortoise iteration, all 62 decisive finite levels')
if __name__=='__main__':main()
