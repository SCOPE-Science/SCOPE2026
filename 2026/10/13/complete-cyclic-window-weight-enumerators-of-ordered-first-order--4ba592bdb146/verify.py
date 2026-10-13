from collections import Counter

def predicted(m,b):
    N=1<<m
    out=Counter({0:1,N:1})
    for t in range(m):
        B=1<<t; q=m-t-1; H=1<<q
        if q==0: dist={0:1}
        else: dist={j:(1 if j in (0,H//2) else 2) for j in range(H//2+1)}
        for j,mul in dist.items():
            zeros=(H-2*j)*max(B-b+1,0)+j*max(2*B-b+1,0)
            out[N-zeros]+=2*mul
    return out

def actual(m,b):
    N=1<<m; out=Counter()
    for a in range(1<<m):
        for c in range(2):
            v=[(j&a).bit_count()%2 ^ c for j in range(N)]
            out[sum(any(v[(i+k)%N] for k in range(b)) for i in range(N))]+=1
    return out
for m in range(1,9):
    for b in range(1,(1<<m)+1):
        a=actual(m,b); p=predicted(m,b)
        if a!=p:
            print('WRONG',m,b,a,p); raise SystemExit(1)
    print('PASS m',m)
print('VERIFY_OK all b for m 1..8')
for m in range(1,9):
    N=1<<m
    for b in range(1,N+1):
        p=predicted(m,b)
        assert sum(p.values())==2**(m+1)
        assert min(w for w,count in p.items() if w>0 and count)>0
        assert min(w for w,count in p.items() if w>0 and count)==min(N,N//2+b-1)
    pair=predicted(m,2)
    wanted=Counter({0:1,N:3})
    for w in range(N//2+1,N):wanted[w]+=4
    assert pair==wanted, (m,pair,wanted)
print('CONSISTENCY_OK cardinality/minimum-distance/pair-spectrum m=1..8')
