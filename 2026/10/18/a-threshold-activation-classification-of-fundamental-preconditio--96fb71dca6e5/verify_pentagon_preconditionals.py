#!/usr/bin/env python3
"""Independent exhaustive checks for preconditionals on long pentagon lattices.

No dependencies outside Python's standard library. Run:
  python3 verify_pentagon_preconditionals.py
The classification is proved mathematically in RESULT.md; this is a finite check.
"""
from itertools import product
from math import factorial
from collections import Counter


def lattice(m):
    """0, c_1,...,c_m, u, top, indexed 0..m+2."""
    n=m+3; u=m+1; top=m+2
    def le(x,y):
        return x==0 or x==y or y==top or (1<=x<=m and 1<=y<=m and x<=y)
    meet=[]
    for a in range(n):
        row=[]
        for b in range(n):
            lower=[x for x in range(n) if le(x,a) and le(x,b)]
            maxima=[x for x in lower if all(le(y,x) for y in lower)]
            assert len(maxima)==1
            row.append(maxima[0])
        meet.append(row)
    return n,u,top,le,meet


def holds_axioms(m,tab):
    n,u,top,le,meet=lattice(m)
    if any(not le(tab[top][b],b) for b in range(n)):return False # P1
    if any(not le(meet[a][b],tab[a][b]) for a in range(n) for b in range(n)):return False # P2
    if any(not le(tab[a][b],tab[a][meet[a][b]]) for a in range(n) for b in range(n)):return False # P3
    if any(not le(tab[a][meet[b][c]],tab[a][b]) for a in range(n) for b in range(n) for c in range(n)):return False # P4
    if any(not le(tab[a][tab[meet[a][b]][c]],tab[meet[a][b]][c]) for a in range(n) for b in range(n) for c in range(n)):return False # P5
    if any(tab[a][a]!=top for a in range(n)):return False
    if any(meet[a][tab[a][0]]!=0 for a in range(n)):return False
    if any(not le(a,tab[tab[a][0]][0]) for a in range(n)):return False
    return True


def predicted(m):
    return factorial(m)+sum((m-j+1)**j*factorial(m-j) for j in range(1,m+1))


def canonical_tables(m):
    n,u,top,le,meet=lattice(m)
    for j in range(m+1):
        # An atom c_s may first be fixed in the row indexed i>=max(s+1,j+1).
        choices=[list(range(max(s+1,j+1),m+1))+[m+1] for s in range(1,m)]
        for activations in product(*choices):
            threshold={s:t for s,t in zip(range(1,m),activations)}
            tab=[[top for _ in range(n)] for _ in range(n)]
            tab[top]=list(range(n))
            for a in range(1,m+1):
                for b in range(n):
                    w=meet[a][b]
                    if w==0:
                        tab[a][b]=u if 1<=a<=j else 0
                    elif w==a:
                        tab[a][b]=top
                    elif 1<=a<=j:
                        tab[a][b]=top
                    else:
                        # The least element >=w among the fixed points of this row and top.
                        opts=[s for s in range(w,a) if threshold[s]<=a]
                        tab[a][b]=min(opts) if opts else top
            for b in range(n):
                tab[u][b]=top if meet[u][b]==u else (j if j else 0)
            assert holds_axioms(m,tab), (m,j,threshold)
            yield j, tuple(tuple(r) for r in tab)


def exhaustive_tables(m):
    n,u,top,le,meet=lattice(m)
    # Every P3/P4 row depends monotonically on a meet, reducing the complete
    # (n^(n*n))-size table universe without excluding any preconditional.
    rowchoices=[]
    for a in range(n):
        lower=[b for b in range(n) if le(b,a)]
        candidates=[]
        for vals in product(range(n),repeat=len(lower)):
            v=dict(zip(lower,vals))
            if v[a]!=top or (a==top and any(v[b]!=b for b in lower)):continue
            if any(not le(b,v[b]) for b in lower):continue
            if any(le(b,c) and not le(v[b],v[c]) for b in lower for c in lower):continue
            if meet[a][v[0]]!=0:continue
            candidates.append(tuple(v[meet[a][b]] for b in range(n)))
        rowchoices.append(candidates)
    accepted=[]
    for rows in product(*rowchoices):
        # Early exact condition: DNI. Other P axioms checked independently.
        neg=[rows[a][0] for a in range(n)]
        if not all(le(a,neg[neg[a]]) for a in range(n)):continue
        if holds_axioms(m,rows):
            accepted.append(tuple(tuple(x) for x in rows))
    return accepted


def main():
    for m in range(1,6):
        can=list(canonical_tables(m))
        tuples=[x for _,x in can]
        assert len(tuples)==predicted(m)==len(set(tuples))
        counts=Counter(j for j,_ in can)
        assert counts[0]==factorial(m)
        for j in range(1,m+1):
            assert counts[j]==(m-j+1)**j*factorial(m-j)
        if m<=4:
            exhaustive=set(exhaustive_tables(m))
            assert exhaustive==set(tuples), (m, len(exhaustive), len(set(tuples)))
        print('m=%d F=%d by_negation=%s exhaustive=%s' % (m,len(tuples),dict(sorted(counts.items())),m<=4))
    print('LONG_PENTAGON_PRECONDITIONAL_VERIFY_OK')

if __name__=='__main__':
    main()
