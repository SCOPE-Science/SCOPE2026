from itertools import product
from math import factorial

def surjections(n,m):
    for q in product(range(m), repeat=n):
        if len(set(q)) == m:
            yield tuple(sum(1<<y for y in set(q[i] for i in range(n) if A&(1<<i))) for A in range(1,1<<n))

def classify(n,m):
    src=list(range(1,1<<n)); tar=list(range(1,1<<m)); ns=len(src); nt=len(tar)
    # All encoded target values for each source state.
    neighbor_s=[sum(1<<j for j,B in enumerate(src) if A&B) for A in src]
    neighbor_t=[sum(1<<j for j,D in enumerate(tar) if C&D) for C in tar]
    expected=set(surjections(n,m))
    count=0; total=0
    for mapping in product(range(nt),repeat=ns):
        total+=1
        # Precompute source fibers as masks.
        fibers=[0]*nt
        for i,k in enumerate(mapping): fibers[k] |= 1<<i
        ok=True
        for i,k in enumerate(mapping):
            accessible=neighbor_s[i]
            for j,h in enumerate(mapping):
                if accessible & (1<<j) and not (neighbor_t[k] & (1<<h)):
                    ok=False; break
            if not ok:break
            for h in range(nt):
                if neighbor_t[k]&(1<<h) and not (accessible & fibers[h]):
                    ok=False; break
            if not ok:break
        if ok:
            count+=1
            observed=tuple(tar[j] for j in mapping)
            assert observed in expected, (n,m,observed)
    assert count==len(expected), (n,m,count,len(expected))
    return (n,m,total,count,len(expected))

if __name__=='__main__':
    import time
    for n,m in ((1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(3,3)):
        st=time.monotonic();r=classify(n,m);print(r,'secs=',round(time.monotonic()-st,3),flush=True)
