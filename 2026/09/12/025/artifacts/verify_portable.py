#!/usr/bin/env python3
"""Portable independent replay of the certified radius-two STS(19) roster."""
import json
from pathlib import Path
from itertools import combinations

V = 19
HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "roster_cert.json").read_text(encoding="utf-8"))

def canon(B):
    return tuple(sorted(tuple(sorted(b)) for b in B))

def valid_sts(B):
    if len(B) != 57:
        return False
    pairs = set()
    for b in B:
        for p in combinations(sorted(b), 2):
            if p in pairs:
                return False
            pairs.add(p)
    return len(pairs) == 171

def pair_third(B):
    d = {}
    for b in B:
        for p in combinations(sorted(b), 2):
            d[p] = next(iter(set(b)-set(p)))
    return d

def hex_records(B):
    B = set(canon(B))
    idx = pair_third(B)
    out = []
    for a in range(V):
        for b in range(a+1, V):
            c = idx[(a,b)]
            A, C = {}, {}
            for blk in B:
                if a in blk and b not in blk:
                    x,y = [z for z in blk if z != a]
                    A[x]=y; A[y]=x
                if b in blk and a not in blk:
                    x,y = [z for z in blk if z != b]
                    C[x]=y; C[y]=x
            verts=[x for x in range(V) if x not in (a,b,c)]
            seen=set()
            for s in verts:
                if s in seen: continue
                path=[s]; cur=s; ok=True
                for step in range(40):
                    nxt = A[cur] if step%2==0 else C[cur]
                    if nxt == s: break
                    if nxt in path: ok=False; break
                    path.append(nxt); cur=nxt
                else: ok=False
                if ok:
                    seen.update(path)
                    if len(path)==6:
                        out.append((a,b,c,tuple(path)))
    return out

def do_switch(B,a,b,cy):
    B=set(canon(B)); S=set(cy)
    abl=[x for x in B if a in x and b not in x and set(x)-{a} <= S]
    bbl=[x for x in B if b in x and a not in x and set(x)-{b} <= S]
    assert len(abl)==len(bbl)==3
    N=set(B)
    for x in abl+bbl: N.remove(x)
    for x in abl:
        u,v=[z for z in x if z!=a]; N.add(tuple(sorted((b,u,v))))
    for x in bbl:
        u,v=[z for z in x if z!=b]; N.add(tuple(sorted((a,u,v))))
    assert valid_sts(N)
    return N

def pasch_count(B):
    B=list(canon(B)); n=0
    for six in combinations(range(V),6):
        S=set(six); cont=[b for b in B if set(b)<=S]
        if len(cont)==4:
            deg={x:0 for x in six}
            for b in cont:
                for x in b: deg[x]+=1
            if all(v==2 for v in deg.values()): n+=1
    return n

def mitre_count(B):
    B=list(canon(B)); n=0
    for seven in combinations(range(V),7):
        S=set(seven)
        if sum(1 for b in B if set(b)<=S)==5: n+=1
    return n

def key(B):
    return (pasch_count(B), len(hex_records(B)), mitre_count(B))

for name in ("netto_B","alt_A"):
    c=DATA[name]
    S=set(canon(c["starter"])); C=set(canon(c["child"]))
    assert valid_sts(S) and valid_sts(C)
    assert key(S)==tuple(c["starter_key"])
    assert key(C)==tuple(c["child_key"])
    a,b,cy=c["child_switch"]
    assert do_switch(S,a,b,tuple(cy))==C
    keys={tuple(c["starter_key"]),tuple(c["child_key"])}
    for r in c["reps"]:
        M=set(canon(r["blocks"]))
        assert valid_sts(M)
        k=key(M); assert k==tuple(r["key"]) and k not in keys
        keys.add(k)
        a,b,cy=r["switch"]
        assert do_switch(C,a,b,tuple(cy))==M
    assert len(keys)==c["total"] and c["total"]>=30
    print(name, "OK", c["total"])
print("ALL VERIFIED")
