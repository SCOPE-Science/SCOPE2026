#!/usr/bin/env python3
"""Independent finite enumeration and transfer verification of a rank-refined idempotent-pair formula."""
from itertools import product
from collections import Counter, defaultdict

def idem(n):
    yield (0,)*n
    for mask in range(1, 1<<n):
        fixed={i+1 for i in range(n) if (mask >> i)&1}
        previous=0
        choice=[]
        for i in range(1,n+1):
            if i in fixed:
                previous=i
                choice.append((i,))
            elif previous:
                choice.append((0,previous))
            else:
                choice.append((0,))
        yield from product(*choice)

def compose(a,b):
    return tuple(b[t-1] if t else 0 for t in a)

def coeff_div(num,den,N):
    assert den[0]==1
    c=[]
    for n in range(N+1):
        c.append((num[n] if n<len(num) else 0)-sum(den[j]*c[n-j] for j in range(1,min(len(den)-1,n)+1)))
    return c

def multiply(A,B,N):
    return [sum(A[j]*B[i-j] for j in range(i+1) if j<len(A) and i-j<len(B)) for i in range(N+1)]

def rank_poly(N):
    q=[1,-7,8]
    dz=[1,-10,27,-18]  # (1-z)(1-3z)(1-6z)
    dh=[1,-13,54,-72]  # (1-3z)(1-4z)(1-6z)
    Z=coeff_div(q,dz,N)
    H=coeff_div(q,dh,N)
    p=Z
    by_n=[Counter() for _ in range(N+1)]
    for k in range(N+1):
        for n in range(k,N+1):
            by_n[n][k]=p[n-k]
        p=multiply(p,H,N)
    return by_n

# Twelve transfer states, without assuming the rational form.
S=[('N','N',0,0),('N','E',0,0),('E','N',0,0),('E','E',0,0),
 ('C','C',1,1),('C','E',1,0),('C','E',1,1),('E','C',0,1),('E','C',1,1),
 ('E','E',0,0),('E','E',0,1),('E','E',1,0)]

def transfer(state):
    A,B,u,v=state
    out=Counter()
    # Neither map acquires a new fixed point at this coordinate.
    nonfixed=1+int(A!='N' and u==0)+int(B!='N' and v==0)+int(A!='N' and B!='N' and u==v)
    out[(state,0)]+=nonfixed
    # Only the first or only the second becomes fixed.
    out[(('E',B,0,v),0)]+=1
    if B=='C':out[(('E',B,1,v),0)]+=1
    out[((A,'E',u,0),0)]+=1
    if A=='C':out[((A,'E',u,1),0)]+=1
    # Both become fixed: the product gains a fixed point.
    out[(('C','C',1,1),1)]+=1
    assert all(x[0] in S for x in out)
    return out

def transfer_counts(N):
    cur={(('N','N',0,0),0):1}
    totals=[]
    for i in range(N+1):
        out=Counter()
        for (state,k),c in cur.items():out[k]+=c
        totals.append(out)
        nxt=defaultdict(int)
        for (state,k),c in cur.items():
            for (new,inc),w in transfer(state).items():nxt[(new,k+inc)]+=c*w
        cur=nxt
    return totals

def exhaustive(n):
    maps=list(idem(n))
    counts=Counter()
    for a in maps:
        for b in maps:
            ab=compose(a,b)
            if ab==compose(b,a):
                assert compose(ab,ab)==ab
                rank=sum(x==i+1 for i,x in enumerate(ab))
                counts[rank]+=1
    assert len(maps)==(3**n+1)//2
    return counts

if __name__=='__main__':
    nmax=16
    expected=rank_poly(nmax)
    assert transfer_counts(nmax)==expected
    for n in range(0,8):
        direct=exhaustive(n)
        assert direct==expected[n],(n,direct,expected[n])
        print(n,sum(direct.values()), dict(sorted(direct.items())))
    print('VERIFY_OK')
