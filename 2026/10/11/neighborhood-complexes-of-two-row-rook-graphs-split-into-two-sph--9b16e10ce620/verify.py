#!/usr/bin/env python3
from itertools import combinations

def graph(n):
    A = list(range(n))
    B = list(range(n,2*n))
    adj = {v:set() for v in A+B}
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(j)
                adj[j].add(i)
                adj[n+i].add(n+j)
                adj[n+j].add(n+i)
        adj[i].add(n+i)
        adj[n+i].add(i)
    return adj

def facets_from_graph(n):
    adj = graph(n)
    return sorted({tuple(sorted(adj[v])) for v in adj})

def expected_facets(n):
    A = set(range(n))
    B = set(range(n,2*n))
    fs = []
    for i in range(n):
        fs.append(tuple(sorted((A-{i}) | {n+i})))
        fs.append(tuple(sorted((B-{n+i}) | {i})))
    return sorted(fs)

def all_faces(facets):
    faces = {0:{()}}
    for F in facets:
        m=len(F)
        for k in range(1,m+1):
            faces.setdefault(k,set()).update(combinations(F,k))
    return faces

def rank_f2(rows):
    piv={}
    rank=0
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j in piv:
                x ^= piv[j]
            else:
                piv[j]=x
                rank += 1
                break
    return rank

def betti_mod2(facets):
    faces=all_faces(facets)
    maxk=max(faces)
    ranks={}
    for k in range(2,maxk+1):
        lower=sorted(faces[k-1])
        idx={f:i for i,f in enumerate(lower)}
        rows=[]
        for f in sorted(faces[k]):
            mask=0
            for j in range(k):
                sub=f[:j]+f[j+1:]
                mask ^= 1<<idx[sub]
            rows.append(mask)
        ranks[k-1]=rank_f2(rows) # boundary C_{k-1} -> C_{k-2}; k=size
    verts=len(faces.get(1,[]))
    b=[]
    # homological dimension d corresponds faces size d+1
    for d in range(maxk):
        c=len(faces.get(d+1,[]))
        rd=ranks.get(d,0)        # rank boundary C_d -> C_{d-1}
        rnext=ranks.get(d+1,0)   # rank boundary C_{d+1} -> C_d
        bd=c-rd-rnext
        if d==0:
            bd -= 1
        b.append(bd)
    return b, faces

def decomposition(n, faces):
    A=set(range(n)); B=set(range(n,2*n))
    Xfac=[tuple(sorted((A-{i})|{n+i})) for i in range(n)]
    Yfac=[tuple(sorted((B-{n+i})|{i})) for i in range(n)]
    X=all_faces(Xfac); Y=all_faces(Yfac)
    # every full-complex face belongs to X or Y
    full=set().union(*[set(v) for v in faces.values()])
    union=set().union(*[set(v) for v in X.values()]) | set().union(*[set(v) for v in Y.values()])
    assert full == union
    inter=set().union(*[set(v) for v in X.values()]) & set().union(*[set(v) for v in Y.values()])
    expected={()}
    expected |= {(v,) for v in range(2*n)}
    expected |= {(i,n+j) for i in range(n) for j in range(n) if i!=j}
    assert inter == expected
    # The intersection is the crown graph K_{n,n}-M.
    V=2*n
    E=n*(n-1)
    assert E-V+1 == n*n-3*n+1
    # Check the bases of X and Y are exactly boundaries of (n-1)-simplices.
    Xbase={()}
    Ybase={()}
    for k in range(n-1):
        Xbase.update(combinations(range(n),k+1))
        Ybase.update(combinations(range(n,2*n),k+1))
    assert tuple(range(n)) not in Xbase
    assert tuple(range(n,2*n)) not in Ybase
    gotX={f for f in set().union(*[set(v) for v in X.values()]) if set(f)<=A}
    gotY={f for f in set().union(*[set(v) for v in Y.values()]) if set(f)<=B}
    assert gotX == Xbase
    assert gotY == Ybase

def main():
    summaries=[]
    for n in range(4,9):
        facets=facets_from_graph(n)
        assert facets == expected_facets(n)
        b,faces=betti_mod2(facets)
        decomposition(n,faces)
        r=n*n-3*n+1
        exp={}
        exp[2]=r
        exp[n-2]=exp.get(n-2,0)+2
        nonzero={d:x for d,x in enumerate(b) if x}
        assert nonzero == exp, (n,nonzero,exp)
        summaries.append(f"{n}:{','.join(f'b{d}={v}' for d,v in sorted(nonzero.items()))}")
    print("VERIFY_OK n=4..8 " + " ".join(summaries) + " intersection=K_n,n-minus-M")
if __name__=="__main__":
    main()
