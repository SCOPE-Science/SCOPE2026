#!/usr/bin/env python3
from itertools import product
from collections import deque


def poset(p,q):
    # elements 0..p-1 are minimal; p..p+q-1 are maximal
    n=p+q
    le=[[False]*n for _ in range(n)]
    for i in range(n): le[i][i]=True
    for a in range(p):
        for b in range(p,n): le[a][b]=True
    return le


def maps(p,q,r,s):
    src=poset(p,q); tgt=poset(r,s)
    ns=p+q; nt=r+s
    out=[]
    for f in product(range(nt), repeat=ns):
        ok=True
        for x in range(ns):
            for y in range(ns):
                if src[x][y] and not tgt[f[x]][f[y]]:
                    ok=False; break
            if not ok: break
        if ok: out.append(f)
    return out,tgt


def lemap(f,g,tgt):
    return all(tgt[a][b] for a,b in zip(f,g))


def comparable(f,g,tgt):
    return lemap(f,g,tgt) or lemap(g,f,tgt)


def classify(f,p,q,r,s):
    A=f[:p]; B=f[p:]
    level = all(x<r for x in A) and all(x>=r for x in B)
    alpha_nonconst = len(set(A))>1
    beta_nonconst = len(set(B))>1
    isolated = level and alpha_nonconst and beta_nonconst
    return isolated


def retract(f,p,q,r,s):
    A=f[:p]; B=f[p:]
    # On the non-isolated component: singleton bottom A takes priority.
    if len(set(A))==1 and A[0] < r:
        return A[0]
    assert len(set(B))==1 and B[0]>=r
    return B[0]


def const_map(y,p,q):
    return (y,)*(p+q)


def components(fs,tgt):
    n=len(fs); seen=[False]*n; comps=[]
    for i in range(n):
        if seen[i]: continue
        seen[i]=True; dq=deque([i]); c=[]
        while dq:
            u=dq.popleft(); c.append(u)
            fu=fs[u]
            for v in range(n):
                if not seen[v] and comparable(fu,fs[v],tgt):
                    seen[v]=True; dq.append(v)
        comps.append(c)
    return comps


def check_case(p,q,r,s):
    fs,tgt=maps(p,q,r,s)
    expected_total=r**p*s**q + s*((r+1)**p-r**p) + r*((s+1)**q-s**q)
    expected_iso=(r**p-r)*(s**q-s)
    assert len(fs)==expected_total, (p,q,r,s,len(fs),expected_total)
    isos=[i for i,f in enumerate(fs) if classify(f,p,q,r,s)]
    assert len(isos)==expected_iso
    comps=components(fs,tgt)
    sizes=sorted((len(c) for c in comps), reverse=True)
    assert len(comps)==expected_iso+1
    assert sizes[0]==len(fs)-expected_iso and sizes[1:]==[1]*expected_iso
    big=set(max(comps,key=len))
    assert all(i in big for i,f in enumerate(fs) if not classify(f,p,q,r,s))
    # Constants are exactly a copy of the target and lie in the big component.
    index={f:i for i,f in enumerate(fs)}
    constants=[const_map(y,p,q) for y in range(r+s)]
    assert all(index[c] in big for c in constants)
    # Retraction is defined on every map in K, fixes constants, and is monotone.
    for i in big:
        y=retract(fs[i],p,q,r,s)
        assert 0<=y<r+s
        if fs[i] in constants:
            assert y==fs[i][0]
    blist=list(big)
    for ii,i in enumerate(blist):
        f=fs[i]; rf=const_map(retract(f,p,q,r,s),p,q)
        # The symbolic proof uses one-sided comparability at each vertex.
        assert comparable(f,rf,tgt)
        for j in blist:
            g=fs[j]
            if lemap(f,g,tgt):
                rg=const_map(retract(g,p,q,r,s),p,q)
                assert lemap(rf,rg,tgt)
                # Contiguity check for every comparable pair: union of the
                # edge with both retracted vertices is totally ordered.
                U=[f,g,rf,rg]
                for a in range(len(U)):
                    for b in range(a+1,len(U)):
                        assert comparable(U[a],U[b],tgt)
    return len(fs), len(comps), sizes[0], expected_iso


def main():
    cases=[(2,2,2,2),(2,2,2,3),(2,3,2,2),(2,3,3,2),(3,2,2,3)]
    for c in cases:
        total,ncomp,big,iso=check_case(*c)
        print(f"case={c} maps={total} components={ncomp} main={big} isolated={iso}")
    print("VERIFY_OK")

if __name__=='__main__':
    main()
