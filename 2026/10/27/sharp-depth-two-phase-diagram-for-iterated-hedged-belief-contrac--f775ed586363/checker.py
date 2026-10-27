"""Exhaustive finite tests of exact depth-two hedged-contraction lifetimes.

Execute with Python 3.9+ as `python checker.py`. All arithmetic and sets are exact.
"""
from itertools import product

MODES = ('DB', 'BB', 'DD', 'BD')

def lifetime(n, rows, truth, mode):
    rows=list(rows)
    full=(1<<n)-1
    steps=0
    while True:
        clean=[(r & truth)==r for r in rows]
        live=[bool(r & truth) for r in rows]
        if mode=='DB':
            active=[any((r>>j)&1 and clean[j] for j in range(n)) for r in rows]
        elif mode=='BB':
            active=[all(not ((r>>j)&1) or clean[j] for j in range(n)) for r in rows]
        elif mode=='DD':
            active=[any((r>>j)&1 and live[j] for j in range(n)) for r in rows]
        elif mode=='BD':
            active=[all(not ((r>>j)&1) or live[j] for j in range(n)) for r in rows]
        else: raise ValueError(mode)
        bad=sum((1<<j) for j,x in enumerate(active) if not x)
        new=[r|bad if x else r for r,x in zip(rows,active)]
        if new==rows:
            return steps
        steps+=1
        assert steps<=n*n, 'monotonicity check'
        rows=new

def predicted(n):
    if n==1:return {'DB':0,'BB':0,'DD':0,'BD':0}
    if n==2:return {'DB':1,'BB':1,'DD':1,'BD':1}
    return {'DB':1,'BB':2,'DD':n-1,'BD':n}

def run():
    total=0
    for n in range(1,5):
        maxima={m:0 for m in MODES}
        for rows in product(range(1<<n),repeat=n):
            for truth in range(1<<n):
                for mode in MODES:
                    h=lifetime(n, rows, truth, mode)
                    maxima[mode]=max(maxima[mode],h)
                    total+=1
        assert maxima==predicted(n),(n,maxima,predicted(n))
        print('EXACT',n,maxima,flush=True)
    for n in range(3,36):
        path=[(1<<(i+1)) if i<n-1 else 0 for i in range(n)]
        cycle=[1<<((i+1)%n) for i in range(n)]
        assert lifetime(n,path,1,'BD')==n
        assert lifetime(n,cycle,1,'DD')==n-1
        # Clone the third vertex in the three-world witness into n-2 twins.
        # World 0 sees no world; world 1 sees 0; each twin sees 1.
        rows=[0,1]+[2]*(n-2)
        assert lifetime(n,rows,2,'BB')==2
        # Clone the first vertex in the two-world witness.
        rows=[0]*(n-1)+[(1<<(n-1))]
        assert lifetime(n,rows,1<<(n-1),'DB')==1
    print('ALL_CHECKS_OK',total,flush=True)

if __name__=='__main__':run()
