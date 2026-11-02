#!/usr/bin/env python3
"""Independent arithmetic-sequence cross-check of finite fiber partitions."""

def rudin_bit(x):
    flips=0
    while x >= 3:
        flips ^= int((x & 3) == 3)
        x >>= 1
    return str(flips)

def first_one_to_end(s):
    ix=s.find('1')
    if ix < 0:return s
    return s[:ix] + s[ix+1:] + '1'

def fibers(factors, power):
    groups={}
    for s in factors:
        image=s
        for _ in range(power):
            image=first_one_to_end(image)
        groups.setdefault(image,set()).add(s)
    return frozenset(frozenset(g) for g in groups.values())

def check():
    raw=''.join(rudin_bit(x) for x in range(1<<15))
    for n in [13,14,17,18,20,25,32,48,63,64,65,96,128]:
        ff={raw[i:i+n] for i in range(len(raw)-n+1)}
        a=fibers(ff,1)
        b=fibers(ff,2)
        c=fibers(ff,3)
        assert (a==b) == (n>=14), ('second', n)
        assert (a==c) == (n>=18), ('third', n)
        assert len(ff)==8*n-8
    print('ARITHMETIC_STABILITY_OK')
if __name__ == '__main__':check()
