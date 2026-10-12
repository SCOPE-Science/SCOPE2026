#!/usr/bin/env python3
import itertools, math
from collections import Counter


def invmod(a,p):
    return pow(a, -1, p)

def normalize(v,p):
    for a in v:
        if a % p:
            z=invmod(a%p,p)
            return tuple((z*x)%p for x in v)
    raise ValueError('zero vector')

def projective_points(p,n):
    d=2*n
    pts={normalize(v,p) for v in itertools.product(range(p), repeat=d) if any(v)}
    return sorted(pts)

def B(x,y,p,n):
    return sum(x[i]*y[n+i]-x[n+i]*y[i] for i in range(n))%p

def quotient(p,n):
    pts=projective_points(p,n)
    N={P:set() for P in pts}
    for i,P in enumerate(pts):
        for Q in pts[i+1:]:
            if B(P,Q,p,n)!=0:
                N[P].add(Q); N[Q].add(P)
    return pts,N

def verify_projective(p,n):
    pts,N=quotient(p,n)
    v=(p**(2*n)-1)//(p-1)
    assert len(pts)==v
    # Every distinct pair is distinguishable by quotient adjacency, allowing
    # one of the two points themselves in the adjacent case.
    for i,P in enumerate(pts):
        for Q in pts[i+1:]:
            if Q in N[P]:
                # landmark from P's fiber gives distances 2 versus 1
                continue
            witnesses=[R for R in pts if ((R in N[P]) != (R in N[Q]))]
            assert witnesses, (p,n,P,Q)
    s=p*(p-1)
    Nfull=v*s
    beta=v*(s-1)
    bases=s**v
    print(f'p={p}, n={n}: projective classes={v}, class_size={s}, vertices={Nfull}, beta=Det={beta}, bases={bases}')
    return pts,N

def heisenberg_vertices(p):
    # H_p = {(a,b,c)} with (a,b)!=(0,0); centre is a=b=0.
    return [(a,b,c) for a in range(p) for b in range(p) for c in range(p) if (a,b)!=(0,0)]

def heis_noncomm(x,y,p):
    a,b,_=x; A,Bb,_=y
    return (a*Bb-A*b)%p != 0

def heis_class(x,p):
    a,b,_=x
    return normalize((a,b),p)

def distances(V,adj):
    # Noncommuting graphs here have diameter two.
    D={}
    for x in V:
        D[x]={x:0}
        for y in V:
            if y==x: continue
            D[x][y]=1 if y in adj[x] else 2
    return D

def brute_p2():
    p=2
    V=heisenberg_vertices(p)
    adj={x:set() for x in V}
    for i,x in enumerate(V):
        for y in V[i+1:]:
            if heis_noncomm(x,y,p):
                adj[x].add(y); adj[y].add(x)
    classes={}
    for x in V: classes.setdefault(heis_class(x,p),[]).append(x)
    assert sorted(map(len,classes.values()))==[2,2,2]
    D=distances(V,adj)
    counts=Counter()
    for mask in range(1<<len(V)):
        S=[V[i] for i in range(len(V)) if mask>>i&1]
        sigs=[tuple(D[x][z] for z in S) for x in V]
        resolving=len(set(sigs))==len(V)
        criterion=all(sum(x in S for x in C)>=len(C)-1 for C in classes.values())
        assert resolving==criterion
        if resolving: counts[len(S)]+=1
    # (2x+x^2)^3 = 8x^3+12x^4+6x^5+x^6
    assert dict(counts)=={3:8,4:12,5:6,6:1}, counts
    print('p=2, n=1 exhaustive resolving polynomial:', dict(sorted(counts.items())))

def verify_heisenberg(p):
    V=heisenberg_vertices(p)
    classes={}
    for x in V: classes.setdefault(heis_class(x,p),[]).append(x)
    assert len(classes)==p+1
    assert all(len(C)==p*(p-1) for C in classes.values())
    # Check exact false-twin neighborhoods in the actual group model.
    neigh={x:frozenset(y for y in V if y!=x and heis_noncomm(x,y,p)) for x in V}
    for C in classes.values():
        assert len({neigh[x] for x in C})==1
    reps=[C[0] for C in classes.values()]
    for i,x in enumerate(reps):
        for y in reps[i+1:]:
            assert neigh[x]!=neigh[y]
    # canonical basis: omit final element from each class
    S=[]; omitted=[]
    for C in classes.values():
        S.extend(C[:-1]); omitted.append(C[-1])
    D=distances(V,{x:set(neigh[x]) for x in V})
    sigs=[tuple(D[x][z] for z in S) for x in V]
    assert len(set(sigs))==len(V)
    expected=(p+1)*(p*(p-1)-1)
    assert len(S)==expected
    print(f'Heisenberg p={p}: actual group twin partition and resolving basis OK')

for p,n in [(2,1),(3,1),(2,2),(3,2),(5,2)]:
    verify_projective(p,n)
for p in [2,3,5]:
    verify_heisenberg(p)
brute_p2()
print('VERIFY_OK')
