from itertools import product, combinations
from collections import Counter
from math import comb

MAX_ORDER = 10

def graph(seq):
    n=len(seq)
    adj=[set() for _ in range(n)]
    for j,c in enumerate(seq):
        if c=='1':
            for i in range(j):
                adj[i].add(j); adj[j].add(i)
    return adj

def is_identifying(adj, mask):
    n=len(adj)
    traces=[]
    for v in range(n):
        tr=tuple(sorted(u for u in (adj[v] | {v}) if (mask>>u)&1))
        if not tr:
            return False
        traces.append(tr)
    return len(set(traces))==n

def blocks(seq):
    a=[]; b=[]; cur=seq[0]; cnt=0
    runs=[]
    for c in seq:
        if c==cur:
            cnt+=1
        else:
            runs.append((cur,cnt)); cur=c; cnt=1
    runs.append((cur,cnt))
    for c,m in runs:
        (a if c=='0' else b).append(m)
    return a,b

def theorem(seq):
    a,b=blocks(seq); n=len(seq); k=len(a)
    if a[0]<2 or any(q!=1 for q in b):
        return None
    eligible=[]
    for i,ai in enumerate(a,1):
        if (i==1 and ai>=3) or (i>=2 and ai>=2):
            eligible.append(i)
    out=Counter()
    for q in range(k+1):
        out[n-k+q]+=comb(k,q)
    for t in range(1,len(eligible)+1):
        for R in combinations(eligible,t):
            mult=1
            for i in R:
                mult*=a[i-1]
            dp=Counter({0:1})
            L=R[0]-1
            dp=Counter({q:comb(L,q) for q in range(L+1)})
            intervals=[R[j+1]-R[j] for j in range(t-1)] + [k-R[-1]+1]
            for L in intervals:
                nd=Counter()
                for d,c in dp.items():
                    for q in range(1,L+1):
                        nd[d+q]+=c*comb(L,q)
                dp=nd
            base=n-k-t
            for d,c in dp.items():
                out[base+d]+=mult*c
    return out

def brute(seq):
    adj=graph(seq); n=len(seq); out=Counter()
    for mask in range(1<<n):
        if is_identifying(adj,mask):
            out[mask.bit_count()]+=1
    return out

def main():
    seq_count=0; subset_checks=0
    for n in range(2,MAX_ORDER+1):
        for mid in product('01', repeat=n-2):
            seq='0'+''.join(mid)+'1'
            seq_count+=1; subset_checks += 1<<n
            actual=brute(seq); predicted=theorem(seq)
            if predicted is None:
                assert not actual, (seq,actual)
            else:
                assert actual==predicted, (seq,actual,predicted)
    print(f'VERIFY_OK sequences={seq_count} subset_checks={subset_checks} max_order={MAX_ORDER}')

if __name__=='__main__':
    main()
