#!/usr/bin/env python3
"""Independent exact transfer and brute checks for 1-limited domination of Mobius ladders."""
from itertools import product


def flip(s):
    return ((s & 1) << 1) | ((s & 2) >> 1)


def allowed(left, mid, right):
    for row in (0, 1):
        inside = (mid >> row) & 1
        neighbors = (((left >> row) & 1) + ((right >> row) & 1)
                     + ((mid >> (1 - row)) & 1))
        if (inside and neighbors < 2) or (not inside and neighbors < 1):
            return False
    return True


def transfer(n):
    assert n >= 3
    optimum = 2*n+1
    howmany = 0
    for a,b in product(range(4), repeat=2):
        dp={(a,b):(a.bit_count()+b.bit_count(),1)}
        for _ in range(2,n):
            new={}
            for (prev,cur),(cost,num) in dp.items():
                for nxt in range(4):
                    if not allowed(prev,cur,nxt):
                        continue
                    key=(cur,nxt)
                    candidate=cost+nxt.bit_count()
                    old=new.get(key)
                    if old is None or candidate < old[0]:
                        new[key]=(candidate,num)
                    elif candidate == old[0]:
                        new[key]=(candidate,old[1]+num)
            dp=new
        for (prev,cur),(cost,num) in dp.items():
            if not allowed(prev,cur,flip(a)) or not allowed(flip(cur),a,b):
                continue
            if cost < optimum:
                optimum,howmany = cost,num
            elif cost == optimum:
                howmany+=num
    return optimum,howmany


def brute(n):
    N=2*n
    adj=[((i-1)%N,(i+1)%N,(i+n)%N) for i in range(N)]
    best=N+1
    num=0
    for mask in range(1<<N):
        count=mask.bit_count()
        if count>best:
            continue
        good=True
        for i in range(N):
            countD=sum(bool(mask & (1<<j)) for j in adj[i])
            if mask & (1<<i):
                if countD<2:good=False;break
            elif countD<1:
                good=False;break
        if good:
            if count<best:best,num=count,1
            else:num+=1
    return best,num


def main():
    # Brute is independent of the two-rung transfer implementation.
    for n in range(3,9):
        assert brute(n)==transfer(n),(n,brute(n),transfer(n))
    for n in range(3,201):
        gamma,count=transfer(n)
        assert gamma == n+(0 if n%4==0 else 1),(n,gamma)
        if n%4==0:
            assert count==4,(n,count)
    print('VERIFY_OK exhaustive_n=3..8 transfer_n=3..200')
    print('samples',[(n,transfer(n)) for n in range(3,13)])


if __name__ == '__main__':
    main()
