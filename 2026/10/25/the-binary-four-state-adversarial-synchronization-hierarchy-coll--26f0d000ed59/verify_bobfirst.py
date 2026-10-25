#!/usr/bin/env python3
"""Independent classification by Bob-first alternating quantifiers on pair configurations."""
from itertools import combinations, product

def classify(n):
    pairs=list(combinations(range(n),2)); pos={p:i for i,p in enumerate(pairs)}; m=len(pairs)
    functions=list(product(range(n),repeat=n))
    image={f:tuple(m if f[i]==f[j] else pos[tuple(sorted((f[i],f[j])))] for i,j in pairs) for f in functions}
    histogram=[0]*(m+1)
    example={}
    for a in functions:
        ta=image[a]
        for b in functions:
            tb=image[b]; trans=(ta,tb)
            # Reachability lists of Bob replies of length strictly less than k.
            reachable=[[set([p]) for p in range(m+1)]]
            for k in range(2,m+1):
                old=reachable[-1]
                reachable.append([old[p]|(old[ta[p]] if p<m else {m})|(old[tb[p]] if p<m else {m}) for p in range(m+1)])
            # Independent unrestricted-reply closure, not a bounded-length proxy.
            for p in range(m+1):
                closure={p}
                while True:
                    grown=closure|{trans[a][q] for q in closure if q<m for a in range(2)}
                    if grown==closure:break
                    closure=grown
                assert (reachable[m-1][p]-{m})==(closure-{m})
            winners=[]
            for k in range(1,m+1):
                W={m}
                while True:
                    # Bob moves first, any legal word; Alice may answer a or b.
                    nxt={p for p in range(m) if all(q==m or ta[q] in W or tb[q] in W for q in reachable[k-1][p])}
                    nxt |= W
                    if nxt==W:break
                    W=nxt
                winners.append(len(W)==m+1)
            level=sum(winners)
            histogram[level]+=1
            example.setdefault(level,(a,b))
    print(f'n={n} classes by maximum k (with infinity={m}): {histogram}')
    print('examples:',example)
    a_counts=[sum(histogram[t] for t in range(k,m+1)) for k in range(1,m+1)]
    print('A_k counts',a_counts, 'A_omega',a_counts[-1], '(verified against full reply closure)')
    return a_counts
if __name__=='__main__':
    assert classify(3)==[549,381,381]
    assert classify(4)==[51520,25360,22384,22384,22384,22384]
    print('INDEPENDENT_CHECK_OK')
