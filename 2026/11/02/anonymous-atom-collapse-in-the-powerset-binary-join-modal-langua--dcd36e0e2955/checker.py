#!/usr/bin/env python3
"""Checks binary-join modal equivalence for finite powerset models."""

def verify(n,k):
    assert 0<=k<=n
    N=1<<n; mask=(1<<k)-1
    q=lambda s: (s&mask) | ((1<<k) if (s & ~mask) else 0)
    classes={s: (int(s==0), *(int(s==1<<i) for i in range(k))) for s in range(N)}
    # Modal refinement of full unordered binary join relation with ordered left/right witnesses
    while True:
        kinds=sorted(set(classes.values()))
        lab={t:i for i,t in enumerate(kinds)}
        old={s:lab[classes[s]] for s in range(N)}
        fresh={}
        for s in range(N):
            witnesses=set()
            for u in range(N):
                if (u | s)!=s: continue
                for v in range(N):
                    if (v|s)!=s or (u|v)!=s: continue
                    witnesses.add((old[u],old[v]))
            fresh[s]=(old[s],tuple(sorted(witnesses)))
        if all(fresh[s]==fresh[t] for s in range(N) for t in range(N) if old[s]==old[t]):
            break
        classes=fresh
    for s in range(N):
        for t in range(N):
            assert (old[s]==old[t])==(q(s)==q(t)),(n,k,s,t)
    # Check explicit back-and-forth for quotient ternary relation
    possible=1<<(k+(n>k))
    for s in range(N):
        for a in range(possible):
            for b in range(possible):
                if (a|b)!=q(s): continue
                assert any((u|v)==s and q(u)==a and q(v)==b
                           for u in range(N) for v in range(N)),(n,k,s,a,b)
    return len(set(old.values()))

if __name__=='__main__':
    for n in range(1,6):
        for k in range(n+1):
            actual=verify(n,k)
            expected=1<<(k+(n>k))
            assert actual==expected,(n,k,actual,expected)
            print(f'n={n} k={k} classes={actual}: OK')
    print('ALL_CHECKS_OK')
