from collections import Counter
from math import comb


def book_graph(m):
    n = 2 + 2*m
    adj = [0]*n
    def add(a,b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    x,y=0,1
    add(x,y)
    for i in range(m):
        u=2+2*i; v=u+1
        add(x,u); add(u,v); add(v,y)
    closed=[adj[v] | (1<<v) for v in range(n)]
    return adj, closed


def bits(mask):
    while mask:
        b=mask & -mask
        yield b.bit_length()-1
        mask ^= b


def is_dld(closed, C):
    n=len(closed); full=(1<<n)-1; T=full ^ C
    traces=[]
    for u in bits(T):
        I=closed[u] & C
        if I==0:
            return False
        traces.append(I)
    for i,a in enumerate(traces):
        for j,b in enumerate(traces):
            if i!=j and (a & ~b)==0:
                return False
    return True


def predicted_masks(m):
    x,y=0,1
    U=[2+2*i for i in range(m)]
    V=[3+2*i for i in range(m)]
    out=set()

    # x outside, y and all V inside; U arbitrary.
    for choice in range(1<<m):
        C=(1<<y)
        for v in V: C |= 1<<v
        for i,u in enumerate(U):
            if (choice>>i)&1: C |= 1<<u
        out.add(C)

    # y outside, x and all U inside; V arbitrary.
    for choice in range(1<<m):
        C=(1<<x)
        for u in U: C |= 1<<u
        for i,v in enumerate(V):
            if (choice>>i)&1: C |= 1<<v
        out.add(C)

    # both endpoints outside, all page vertices inside.
    C=0
    for u,v in zip(U,V): C |= (1<<u)|(1<<v)
    out.add(C)

    # both endpoints inside, no page completely omitted: each page is U-only, V-only, or both.
    def rec(i,C):
        if i==m:
            out.add(C); return
        u,v=U[i],V[i]
        rec(i+1,C|(1<<u))
        rec(i+1,C|(1<<v))
        rec(i+1,C|(1<<u)|(1<<v))
    rec(0,(1<<x)|(1<<y))

    # both endpoints inside, exactly one page omitted and every other page full.
    for omit in range(m):
        C=(1<<x)|(1<<y)
        for i,(u,v) in enumerate(zip(U,V)):
            if i!=omit: C |= (1<<u)|(1<<v)
        out.add(C)
    return out


def formula_coeffs(m):
    c=Counter()
    # 2 z^(m+1)(1+z)^m
    for k in range(m+1):
        c[m+1+k] += 2*comb(m,k)
    # (m+1) z^(2m)
    c[2*m] += m+1
    # z^(m+2)(2+z)^m
    for k in range(m+1):
        c[m+2+k] += comb(m,k)*(2**(m-k))
    return c

print('VERIFY_OK')
subsets=0
for m in range(1,9):
    _,closed=book_graph(m); n=len(closed)
    actual=set(); counts=Counter()
    for C in range(1<<n):
        subsets += 1
        if is_dld(closed,C):
            actual.add(C); counts[C.bit_count()] += 1
    expected=predicted_masks(m)
    assert actual==expected, (m,len(actual),len(expected),len(actual^expected))
    assert counts==formula_coeffs(m), (m,counts,formula_coeffs(m))
    gamma=min(counts)
    min_count=counts[gamma]
    assert gamma==m+1
    assert min_count==(4 if m==1 else 2)
    print(f'm={m}: gamma_DLD={gamma}, minimum_codes={min_count}, all_DLD_codes={len(actual)}')
print('vertex_subsets_checked =',subsets)
print('all solid-location-dominating codes matched the structural classification and polynomial')
