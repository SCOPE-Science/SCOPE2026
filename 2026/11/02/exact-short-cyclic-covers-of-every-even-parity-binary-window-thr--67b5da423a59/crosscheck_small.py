#!/usr/bin/env python3
"""Independent exhaustive check of optimal circular lengths at n=2,3,4."""

def brute_minimum(n):
    target = sum(1<<w for w in range(1<<n) if w.bit_count()%2==0)
    for length in range(1<<(n-1), (1<<n)+1):
        for bits in range(1<<length):
            seen = 0
            for i in range(length):
                word = 0
                for j in range(n):
                    word = (word<<1) | ((bits>>((i+j)%length))&1)
                if word.bit_count()%2==0:
                    seen |= 1<<word
                if (seen & target)==target:
                    return length
    assert False

if __name__=='__main__':
    for n,expect in [(2,4),(3,7),(4,16)]:
        actual=brute_minimum(n)
        assert actual==expect, (n,actual)
        print(n,actual)
    print('CROSSCHECK_OK')
