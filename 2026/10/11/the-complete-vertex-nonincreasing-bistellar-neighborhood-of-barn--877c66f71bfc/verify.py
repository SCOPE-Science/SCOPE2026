#!/usr/bin/env python3
from itertools import combinations, permutations
B={tuple(sorted(x)) for x in [
(1,2,4,5),(2,3,5,6),(1,3,4,6),(1,2,3,7),(4,5,6,7),(1,2,4,7),
(2,4,5,7),(2,3,5,7),(3,5,6,7),(1,3,6,7),(1,4,6,7),(1,2,3,8),
(4,5,6,8),(1,2,5,8),(1,4,5,8),(2,3,6,8),(2,5,6,8),(1,3,4,8),(3,4,6,8)]}
BG={tuple(sorted(x)) for x in [
(1,2,3,7),(1,2,3,8),(1,2,4,5),(1,2,4,7),(1,2,5,8),(1,3,5,6),
(1,3,5,7),(1,3,6,8),(1,4,5,7),(1,5,6,8),(2,3,4,6),(2,3,4,8),
(2,3,6,7),(2,4,5,8),(2,4,6,7),(3,4,6,8),(3,5,6,7),(4,5,7,8),
(4,6,7,8),(5,6,7,8)]}
V=tuple(range(1,9))
def faces(F,k): return {tuple(sorted(c)) for f in F for c in combinations(f,k)}
def fvec(F): return tuple(len(faces(F,k)) for k in range(1,5))
def m23(F):
    E,T=faces(F,2),faces(F,3); out=[]
    for t in sorted(T):
        inc=[f for f in F if set(t)<=set(f)]
        if len(inc)==2:
            opp=tuple(sorted((set(inc[0])|set(inc[1]))-set(t)))
            if len(opp)==2 and opp not in E and set(inc)=={tuple(sorted(set(t)|{x})) for x in opp}:
                out.append((t,opp))
    return out
def m32(F):
    E,T=faces(F,2),faces(F,3); out=[]
    for e in sorted(E):
        inc=[f for f in F if set(e)<=set(f)]
        if len(inc)==3:
            opp=tuple(sorted(set().union(*(set(f) for f in inc))-set(e)))
            if len(opp)==3 and opp not in T and set(inc)=={tuple(sorted(set(e)|(set(opp)-{v}))) for v in opp}:
                out.append((e,opp))
    return out
def m41(F):
    out=[]
    for v in V:
        inc={f for f in F if v in f}
        nbr=tuple(sorted(set().union(*(set(f)-{v} for f in inc)))) if inc else ()
        if len(nbr)==4 and inc=={tuple(sorted({v}|(set(nbr)-{w}))) for w in nbr} and nbr not in F:
            out.append((v,nbr))
    return out
def up(F,t,o):
    G=set(F)-{f for f in F if set(t)<=set(f)}
    for v in t:G.add(tuple(sorted(set(o)|(set(t)-{v}))))
    return G
def down(F,e,o):
    G=set(F)-{f for f in F if set(e)<=set(f)}
    for v in e:G.add(tuple(sorted(set(o)|(set(e)-{v}))))
    return G
def pf(F,p):
    d={i:p[i-1] for i in V}
    return {tuple(sorted(d[x] for x in f)) for f in F}
def iso(F,G):
    for p in permutations(V):
        if pf(F,p)==G:return p
    return None
def act(s,p):return tuple(sorted(p[x-1] for x in s))
assert fvec(B)==(8,27,38,19) and fvec(BG)==(8,28,40,20)
a=m23(B); b=m32(B); c=m41(B)
assert a==[((1,2,3),(7,8)),((4,5,6),(7,8))]
assert b==[((1,5),(2,4,8)),((1,6),(3,4,7)),((2,4),(1,5,7)),((2,6),(3,5,8)),((3,4),(1,6,8)),((3,5),(2,6,7))]
assert c==[]
A=[p for p in permutations(V) if pf(B,p)==B]
assert len(A)==12
assert {(act(a[0][0],p),act(a[0][1],p)) for p in A}==set(a)
assert {(act(b[0][0],p),act(b[0][1],p)) for p in A}==set(b)
U=[up(B,*x) for x in a]; D=[down(B,*x) for x in b]
assert all(fvec(x)==(8,28,40,20) and iso(x,BG) for x in U)
assert all(fvec(x)==(8,26,36,18) for x in D)
R=D[0]
assert all(iso(x,R) for x in D)
assert iso(R,B) is None and iso(R,BG) is None
print("VERIFY_OK f=8,27,38,19 aut=12 move23=2 orbit23=2 target23=BG move32=6 orbit32=6 target32_f=8,26,36,18 target32_classes=1 move41=0")
