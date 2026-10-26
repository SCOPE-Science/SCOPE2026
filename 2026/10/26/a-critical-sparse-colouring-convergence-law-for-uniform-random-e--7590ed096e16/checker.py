"""Exact finite identities for independently marked uniform set partitions.
No external dependencies; python3 checker.py.
"""
from math import comb, factorial

MAX_N = 7
P_NUM, P_DEN = 2, 5

def falling(x, m):
    t = 1
    for j in range(m):
        t *= x-j
    return t

def partitions(n):
    if n == 0:
        yield ()
        return
    rg = [0]*n
    def go(i, top):
        if i == n:
            blocks = [[] for _ in range(top+1)]
            for x, v in enumerate(rg):
                blocks[v].append(x)
            yield tuple(tuple(b) for b in blocks)
            return
        for t in range(top+2):
            rg[i] = t
            yield from go(i+1, max(t,top))
    yield from go(1,0)

bell=[1]
stirling=[[1]]
for n in range(1, MAX_N+1):
    bell.append(sum(comb(n-1,k)*bell[k] for k in range(n)))
    row=[0]*(n+1)
    for j in range(1,n+1):
        row[j]= (stirling[n-1][j-1] if j-1<len(stirling[n-1]) else 0) +j*(stirling[n-1][j] if j<len(stirling[n-1]) else 0)
    stirling.append(row)

checked=0; samples=0
for n in range(MAX_N+1):
    observed_total={m:0 for m in range(1,4)}
    profiles={(j,u):0 for j in range(1,4) for u in (1,2)}
    for blocks in partitions(n):
        for mask in range(1<<n):
            k=mask.bit_count()
            w=P_NUM**k*(P_DEN-P_NUM)**(n-k)
            sizes=[len(b) for b in blocks if all(mask & (1<<v) for v in b)]
            t=len(sizes)
            for m in observed_total:
                observed_total[m]+=w*falling(t,m)
            for j,u in profiles:
                profiles[(j,u)]+=w*falling(sizes.count(j),u)
            samples+=1
    for m,obs in observed_total.items():
        exp = factorial(m)*sum(comb(n,s)*bell[n-s]*stirling[s][m]*P_NUM**s*P_DEN**(n-s) for s in range(m,n+1))
        assert obs==exp, ('total factorial moments',n,m,obs,exp)
        checked+=1
    for (j,u),obs in profiles.items():
        s=j*u
        exp = (falling(n,s)*bell[n-s]*P_NUM**s*P_DEN**(n-s)//(factorial(j)**u)) if s<=n else 0
        assert obs==exp, ('size-resolved factorial moments',n,j,u,obs,exp)
        checked+=1
print('SPARSE_EQUIVALENCE_MOMENTS_OK', samples, checked)
