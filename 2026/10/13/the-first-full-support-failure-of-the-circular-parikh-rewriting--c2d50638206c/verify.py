#!/usr/bin/env python3
import itertools, json, math
from fractions import Fraction
from pathlib import Path

A="abc"
def rotations(w): return [w[i:]+w[:i] for i in range(len(w))]
def canon(w): return min(rotations(w))

def sc(w,p):
    d=[1]+[0]*len(p)
    for ch in w:
        for j in range(len(p)-1,-1,-1):
            if p[j]==ch:d[j+1]+=d[j]
    return d[-1]

def key_dp(w):
    n=len(w);rs=rotations(w)
    return (w.count("a"),w.count("b"),w.count("c"),
            Fraction(sum(sc(r,"ab") for r in rs),n),
            Fraction(sum(sc(r,"bc") for r in rs),n),
            Fraction(sum(sc(r,"abc") for r in rs),n))

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def L(ch):
    M=[[int(i==j) for j in range(4)] for i in range(4)]
    if ch=="a":M[0][1]=1
    elif ch=="b":M[1][2]=1
    elif ch=="c":M[2][3]=1
    else:raise AssertionError
    return M

def PM(w):
    M=[[int(i==j) for j in range(4)] for i in range(4)]
    for ch in w:M=mm(M,L(ch))
    return M

def key_matrix(w):
    reps=sorted(set(rotations(w)));m=len(reps)
    mats=[PM(r) for r in reps]
    av=[[Fraction(sum(X[i][j] for X in mats),m) for j in range(4)] for i in range(4)]
    return (av[0][1],av[1][2],av[2][3],av[0][2],av[1][3],av[0][3])

def moves(s):
    n=len(s);out=set()
    for lx in range(n-3):
        ly=n-4-lx;x=s[:lx]
        if s[lx:lx+2]=="ac" and s[-2:]=="ca":
            y=s[lx+2:lx+2+ly]
            if y.count("b")*(x.count("a")-x.count("c"))==x.count("b")*(y.count("a")-y.count("c")):
                out.add(x+"ca"+y+"ac")
        for alpha in "ac":
            bar="c" if alpha=="a" else "a"
            if s[lx:lx+2]==alpha+"b" and s[-2:]=="b"+alpha:
                y=s[lx+2:lx+2+ly]
                if x.count(bar)*(len(y)+y.count("b")+3)==y.count(bar)*(len(x)+x.count("b")+3):
                    out.add(x+"b"+alpha+y+alpha+"b")
    return out

def nbr(v):
    z=set()
    for r in rotations(v):
        for t in moves(r):z.add(canon(t))
    z.discard(canon(v));return z

def pair_edge(v,u):
    for r in rotations(v):
        for t in moves(r):
            if canon(t)==canon(u):return True
    for r in rotations(u):
        for t in moves(r):
            if canon(t)==canon(v):return True
    return False

def phi(n):
    x=n;r=n;p=2
    while p*p<=x:
        if x%p==0:
            while x%p==0:x//=p
            r-=r//p
        p+=1
    if x>1:r-=r//x
    return r

def necklace_formula(n):
    return sum(phi(d)*3**(n//d) for d in range(1,n+1) if n%d==0)//n

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text())
for n in range(1,7):
    V=sorted({canon("".join(t)) for t in itertools.product(A,repeat=n)})
    assert len(V)==necklace_formula(n)
    for w in V:assert key_dp(w)==key_matrix(w)
    F=[w for w in V if all(ch in w for ch in A)]
    G={}
    for w in F:G.setdefault(key_dp(w),[]).append(w)
    amb={k:sorted(v) for k,v in G.items() if len(v)>1}
    adj={w:set() for w in F}
    for w in F:
        for u in nbr(w):
            if u in adj:
                assert key_dp(u)==key_dp(w)
                adj[w].add(u);adj[u].add(w)
    # Second edge engine.
    adj2={w:set() for w in F}
    for i,w in enumerate(F):
        for u in F[i+1:]:
            if key_dp(w)==key_dp(u) and pair_edge(w,u):
                adj2[w].add(u);adj2[u].add(w)
    assert adj==adj2

    connected=0;bad=[]
    for k,vs in amb.items():
        W=set(vs);seen=set();comps=[]
        for s in vs:
            if s in seen:continue
            st=[s];seen.add(s);c=[]
            while st:
                x=st.pop();c.append(x)
                for y in adj[x]&W:
                    if y not in seen:seen.add(y);st.append(y)
            comps.append(sorted(c))
        if len(comps)==1:connected+=1
        else:bad.append((vs,comps,k))
    S=cert["summary_by_length"][str(n)]
    assert S["necklaces"]==len(V)
    assert S["full_support_necklaces"]==len(F)
    assert S["nontrivial_M_classes"]==len(amb)
    assert S["M_ambiguous_full_support_necklaces"]==sum(len(x) for x in amb.values())
    assert S["CE_connected_classes"]==connected
    assert S["CE_disconnected_classes"]==len(bad)

assert cert["summary_by_length"]["5"]["nontrivial_M_classes"]==1
assert cert["summary_by_length"]["5"]["CE_disconnected_classes"]==0
assert cert["summary_by_length"]["6"]["nontrivial_M_classes"]==8
assert cert["summary_by_length"]["6"]["CE_connected_classes"]==5
assert cert["summary_by_length"]["6"]["CE_disconnected_classes"]==3

expected=[
    ["aabcbc","ababcc"],
    ["aacbcb","abaccb"],
    ["abacbc","abcacb","abcbac"],
]
got=[x["words"] for x in cert["length6_exceptional_classes"]]
assert got==expected
for C in cert["length6_exceptional_classes"]:
    for w in C["words"]:
        assert not nbr(w)

print("VERIFY_OK lengths=1..6 necklaces=3,6,11,24,51,130 full_support=0,0,2,9,30,91 n5_Mclasses=1 n5_disconnected=0 n6_Mclasses=8 n6_connected=5 n6_disconnected=3 exceptional_sizes=2,2,3 isolated_members=7 matrix_engines=2 rule_edge_engines=2")
