#!/usr/bin/env python3
"""Direct finite-state enumeration independent of the linear-rank implementation."""
from collections import Counter
def main():
    for d in (2,3):
        n=1<<d
        s=n+1
        adj=[sum(1<<(v^(1<<j)) for j in range(d)) | (1<<n)
             for v in range(n)] + [(1<<n)-1]
        def step(z):
            u,v=z
            new=0
            for i,mask in enumerate(adj):
                if (u&mask).bit_count()&1:
                    new|=1<<i
            return (new^v,u)
        counts=Counter()
        divisors=(1,2,4,8) if d%2==0 else (1,2,3,6)
        for key in range(1<<(2*s)):
            state=(key & ((1<<s)-1),key>>s)
            current=state
            orbit_length=None
            for t in range(1,max(divisors)+1):
                current=step(current)
                if current==state:
                    orbit_length=t
                    break
            assert orbit_length in divisors,(d,key,orbit_length)
            counts[orbit_length]+=1
        if d%2:
            want={
                1:2, 2:4-2, 3:(1<<(n+1))-2,
                6:(1<<(2*s))-(1<<(n+1))-4+2
            }
        else:
            want={
                1:1<<(n//2+1),
                2:(1<<(n+2))-(1<<(n//2+1)),
                4:(1<<(2*n))-(1<<(n+2)),
                8:(1<<(2*s))-(1<<(2*n))
            }
        assert dict(counts)==want,(d,counts,want)
        print("d=%d states=%d primitive_counts=%s"%(d,1<<(2*s),dict(sorted(counts.items()))))
    print("PASS: direct independent updates on all 263168 states")
if __name__=="__main__":
    main()
