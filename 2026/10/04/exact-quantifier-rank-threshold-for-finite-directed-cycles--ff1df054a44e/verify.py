from functools import lru_cache
from itertools import product

def arc(n,u,v):
    return (u+1)%n==v

def dup_wins(n,m,q):
    @lru_cache(maxsize=None)
    def win(flat,r):
        pairs=list(zip(flat[::2],flat[1::2]))
        for (x,y),(x2,y2) in product(pairs,pairs):
            if (x==x2)!=(y==y2):
                return False
            if arc(n,x,x2)!=arc(m,y,y2):
                return False
        if r==0:
            return True
        for side,N,M in ((0,n,m),(1,m,n)):
            for x in range(N):
                ok=False
                for y in range(M):
                    ps=pairs+([(x,y)] if side==0 else [(y,x)])
                    nf=tuple(z for p in ps for z in p)
                    if win(nf,r-1):
                        ok=True
                        break
                if not ok:
                    return False
        return True
    return win((),q)

def g(q):
    if q==1: return 1
    if q==2: return 4
    return 2**(q-1)+3

cases=0
for q in range(1,5):
    for n in range(3,13):
        for m in range(n,13):
            got=dup_wins(n,m,q)
            want=(n==m or (n>=g(q) and m>=g(q)))
            cases+=1
            if got!=want:
                raise SystemExit(f"FAIL q={q} n={n} m={m} got={got} want={want}")
print(f"VERIFY_OK cases={cases}")
