#!/usr/bin/env python3
"""Exact prime-by-prime check of five consecutive trace discriminant sign words."""

def primes_below(stop):
    sieve = bytearray(b'\x01') * stop
    sieve[:2] = b'\x00\x00'
    for a in range(2, int((stop - 1)**0.5) + 1):
        if sieve[a]:
            sieve[a*a:stop:a] = b'\x00' * ((stop-1-a*a)//a+1)
    return [p for p in range(3,stop,2) if sieve[p]]

FULL = (1 << 32) - 1
EXCEPTIONS = (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
              61,67,71,73,79,83,89,97,101,103,109,113,127,131,
              139,149,157,163,173,179,181,223,227,233)

def masks_by_squares(p):
    sq = bytearray(p)
    for a in range(1,(p+1)//2):
        sq[(a*a)%p] = 1
    mask = 0
    for t in range(p):
        bits = 0
        for j in range(5):
            y = ((t+j)*(t+j)-4)%p
            if y == 0:
                break
            if sq[y]:
                bits |= (1<<j)
        else:
            mask |= 1<<bits
            if mask == FULL:
                return FULL
    return mask

def masks_by_euler(p):
    mask=0
    for t in range(p):
        bits=0
        for j in range(5):
            y=((t+j)**2-4)%p
            if y==0:
                break
            symbol = pow(y,(p-1)//2,p)
            assert symbol in (1,p-1)
            if symbol==1:
                bits|=(1<<j)
        else:
            mask|=1<<bits
    return mask


def main():
    primes=primes_below(14000)
    actual=[]
    for p in primes:
        mask=masks_by_squares(p)
        if mask!=FULL:
            actual.append(p)
        if p<1600:
            assert masks_by_euler(p)==mask, p
    assert tuple(actual)==EXCEPTIONS, (actual,EXCEPTIONS)
    assert [i for i in range(32) if not (masks_by_euler(233)>>i)&1]==[0]
    assert masks_by_euler(229)==FULL
    ordinary = sum(2*mask.bit_count()-1 for mask in range(1,32))
    collisions = [mask for mask in range(1,32) if (mask & 17)==17]
    adjusted = ordinary - 2*len(collisions)
    assert (ordinary,len(collisions),adjusted)==(129,8,113)
    roots = {2-j for j in range(5)} | {-2-j for j in range(5)}
    assert len(roots)==9
    assert 14000 - 113*119 - 152 > 0  # sqrt(14000) < 119.
    print('VERIFY_OK')
    print('odd_primes_below_14000',len(primes))
    print('exception_count',len(actual))
    print('last_exception',max(actual))
    print('missing_at_233', [i for i in range(32) if not (masks_by_euler(233)>>i)&1])
    print('quadratic_character_bound_at_14000_positive',True)
    print('weil_coefficient_before_after_collision',ordinary,adjusted)
    print('exact_crosscheck_odd_primes_below_1600',len([p for p in primes if p<1600]))

if __name__=='__main__':
    main()
