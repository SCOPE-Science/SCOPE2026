#!/usr/bin/env python3
"""Exact independent checks for two-burst deletion-ball spectra of binary differential VT codes."""
from collections import Counter, defaultdict
from math import comb

def predicted(n):
    assert n>=4 and n&(n-1)==0
    # G = z(1+z)^(n-2), K=z(1-z)^(n//2)*(1+z)^(n//2-2)
    G=[0]*(n+1); K=[0]*(n+1)
    for j in range(n-1): G[j+1]=comb(n-2,j)
    for j in range(n-1):
        K[j+1]=sum((-1)**t*comb(n//2,t)*comb(n//2-2,j-t)
                   for t in range(max(0,j-(n//2-2)),min(n//2,j)+1))
    sp={i:(2*G[i]+(n-2)*K[i])//n for i in range(1,n)}
    reg={i:(2*G[i]-2*K[i])//n for i in range(1,n)}
    assert all((2*G[i]+(n-2)*K[i])%n==0 and (2*G[i]-2*K[i])%n==0 for i in range(1,n))
    return Counter({k:v for k,v in sp.items() if v}),Counter({k:v for k,v in reg.items() if v})

def exhaustive(n):
    hist=[Counter() for _ in range(2*n)]
    for val in range(1<<n):
        bits=tuple((val>>j)&1 for j in range(n))
        d=[bits[j]^bits[j+1] for j in range(n-1)]+[bits[-1]]
        syndrome=sum((i+1)*bit for i,bit in enumerate(d))%(2*n)
        outputs={bits[:i]+bits[i+2:] for i in range(n-1)}
        number=1+sum(bits[i]!=bits[i+2] for i in range(n-2))
        assert len(outputs)==number, (n,val)
        hist[syndrome][len(outputs)]+=1
    sp,reg=predicted(n)
    for a,h in enumerate(hist):
        assert h==(sp if a%n in (0,n//2) else reg),(n,a,h,sp,reg)
        assert sum(k*v for k,v in h.items())==(1<<(n-2)),(n,a,h)
    return len(hist)

def dp_spectrum(n):
    # For each prefix length i, state (syndrome mod n, last bit, transitions).
    state={(b,b,0):1 for b in (0,1)}
    for i in range(2,n):
        nxt=defaultdict(int)
        for (s,last,t),count in state.items():
            for b in (0,1):
                nxt[((s+i*b)%n,b,t+(last!=b))]+=count
        state=nxt
    hist=[Counter() for _ in range(n)]
    for (s,b,t),count in state.items():
        hist[s][t+1]+=count
    sp,reg=predicted(n)
    for a,h in enumerate(hist):
        assert h==(sp if a in (0,n//2) else reg),(n,a,h,sp,reg)
    return len(state),sum(sum(x.values()) for x in hist)

if __name__=='__main__':
    for n in (4,8,16): print('EXHAUSTIVE',n,exhaustive(n))
    for n in (4,8,16,32,64): print('DP',n,dp_spectrum(n))
    print('N8_SPECIAL',sorted(predicted(8)[0].items()))
    print('N8_REGULAR',sorted(predicted(8)[1].items()))
    print('DVT_BURST_SPECTRA_VERIFY_OK')
