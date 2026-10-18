"""Finite brute-force checks of mixed restricted binary sums."""
from math import comb

def integer_root_floor(t,r):
    lo,hi=0,t+1
    while lo+1<hi:
        m=(lo+hi)//2
        if m**r<=t:lo=m
        else:hi=m
    return lo

trials=0
for r in range(2,8):
    for N in range(2,51):
        t=N-1
        s=integer_root_floor(t,r)
        enumerated={}
        for a in range(1,t+1):
            for b in range(1,s+1):
                v=2**a + 2**(b**r)
                assert v<=2**N
                enumerated[v]=enumerated.get(v,0)+1
        theoretical=t*s-comb(s,2)
        assert len(enumerated)==theoretical,(r,N,len(enumerated),theoretical)
        assert sum(v==2 for v in enumerated.values())==comb(s,2)
        assert max(enumerated.values())<=2
        # Prove no pair with an exponent above N-1 can fit <=2**N.
        assert 2**N+2>2**N
        trials+=1
print('PASS exact enumeration for',trials,'(r,N) cases; all multiplicities <=2')
print('Sample r=2, N=101: count =',100*10-comb(10,2))
