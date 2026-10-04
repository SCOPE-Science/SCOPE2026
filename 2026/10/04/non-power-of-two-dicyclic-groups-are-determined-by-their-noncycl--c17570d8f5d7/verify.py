#!/usr/bin/env python3

def mul(x,y,n):
    i,e=x; j,f=y
    return ((i + (-j if e else j) + (n if e and f else 0))%(2*n), (e+f)%2)

def generated(x,y,n):
    S={(0,0),x,y}
    changed=True
    while changed:
        changed=False
        old=list(S)
        for a in old:
            for b in old:
                c=mul(a,b,n)
                if c not in S:
                    S.add(c); changed=True
    return S

def cyclic(H,n):
    for g in H:
        S={(0,0)}
        z=(0,0)
        for _ in range(4*n):
            z=mul(z,g,n); S.add(z)
        if S==H:
            return True
    return False

def pair_cyclic(x,y,n):
    return cyclic(generated(x,y,n),n)

tests=[3,5,6,7,9,10,11,12,13,14,15]
for n in tests:
    assert n & (n-1)
    G=[(i,e) for i in range(2*n) for e in (0,1)]
    cyc={x for x in G if all(pair_cyclic(x,y,n) for y in G)}
    assert cyc=={(0,0),(n,0)}, (n,cyc)

    A={(i,0) for i in range(2*n) if i not in (0,n)}
    parts=[A]+[{(i,1),((i+n)%(2*n),1)} for i in range(n)]
    assert sum(len(P) for P in parts)==4*n-2
    assert set().union(*parts)==set(G)-cyc

    for r,P in enumerate(parts):
        for x in P:
            for y in P:
                if x!=y:
                    assert pair_cyclic(x,y,n)
            for s,Q in enumerate(parts):
                if r!=s:
                    for y in Q:
                        assert not pair_cyclic(x,y,n)

    candidates=[c for c in range(1,5) if (c+2)%c==0]
    assert candidates==[1,2]
    assert (4*n-1)%(2*n-1)!=0
    assert 4*n==(4*n-2)+2

    print(f"n={n} order={4*n} cyclicizer=2 parts={[len(P) for P in parts]} reconstruction_c=2")

print("VERIFY_OK")
