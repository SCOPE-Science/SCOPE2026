"""Finite exact checks for paired-composition maximum-gap theorem."""
from itertools import combinations
from math import comb, factorial

def compositions(n,k):
    for cuts in combinations(range(1,n),k-1):
        pieces=(0,)+cuts+(n,)
        yield tuple(pieces[i+1]-pieces[i] for i in range(k))

def small_count_by_dp(n,k,u):
    d={(0,0):1}
    for step in range(k):
        nxt={}
        for (x,y),v in d.items():
            for a in range(1,n-x+1):
                for b in range(1,min(n-y,u-a-1)+1):
                    key=(x+a,y+b)
                    nxt[key]=nxt.get(key,0)+v
        d=nxt
    return d.get((n,n),0)

def verify():
    tests=0
    for n in range(2,9):
        total=0
        brute={u:0 for u in range(2,2*n+2)}
        exact={u:0 for u in brute}
        for k in range(1,n+1):
            C=list(compositions(n,k))
            total+=len(C)**2
            for a in C:
                for b in C:
                    m=max(x+y for x,y in zip(a,b))
                    for u in brute:
                        brute[u]+=int(m<u)
            for u in exact:
                exact[u]+=small_count_by_dp(n,k,u)
        assert total==comb(2*n-2,n-1),(n,'path-count')
        for u in brute:
            assert brute[u]==exact[u],(n,u,brute[u],exact[u])
            tests+=1
    print('VERIFICATION_OK',tests,'threshold coefficient checks, path counts n=2..8')
if __name__=='__main__': verify()
