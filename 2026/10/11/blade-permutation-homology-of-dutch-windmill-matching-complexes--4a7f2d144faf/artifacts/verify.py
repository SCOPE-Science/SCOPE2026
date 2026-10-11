#!/usr/bin/env python3
from itertools import permutations


def parity(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv % 2 else 1

def cycles_count(p):
    n=len(p); seen=[False]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=p[j]
    return c

def fixed_count(p): return sum(i==p[i] for i in range(len(p)))

def a(r):
    x0,x1=1,0
    if r==0: return x0
    if r==1: return x1
    for _ in range(2,r+1):
        x0,x1=x1,x1-x0
    return x1

def formula_character(n,m,p):
    assert m>=4
    if m%3==1:
        k=(m-1)//3
        return parity(p)**k
    if m%3==2:
        k=(m-2)//3
        return (parity(p)**k)*(2*fixed_count(p)-1)
    raise ValueError('only noncontractible residue classes tested')

def symbolic_character(n,m,p):
    c=cycles_count(p); f=fixed_count(p)
    A=a(m-2); B=a(m-3)
    # exact invariant-matching alternating orbit sum
    F=A**c - 2*f*B*(A**(c-1))
    Lred=-F
    d=n*((m-1)//3)-1 if m%3==1 else n*((m-2)//3)
    return ((-1)**d)*Lred

def graph_edges(n,m):
    # edge (blade,t): t=0 left spoke, 1..m-2 internal, m-1 right spoke
    E=[]; endpoints={}
    for b in range(n):
        for t in range(m):
            e=(b,t); E.append(e)
            if t==0: uv=('c',(b,1))
            elif t==m-1: uv=((b,m-1),'c')
            else: uv=((b,t),(b,t+1))
            endpoints[e]=uv
    return E,endpoints

def enumerate_matchings(n,m):
    E,ends=graph_edges(n,m)
    out=[]
    def rec(i,used,chosen):
        if i==len(E):
            out.append(tuple(chosen)); return
        rec(i+1,used,chosen)
        e=E[i]; u,v=ends[e]
        if u not in used and v not in used:
            chosen.append(e); used.add(u); used.add(v)
            rec(i+1,used,chosen)
            used.remove(u); used.remove(v); chosen.pop()
    rec(0,set(),[])
    return out

def action_edge(e,p): return (p[e[0]],e[1])

def brute_character(n,m,p,matchings):
    # Reduced Lefschetz number from signed traces on augmented simplicial chains.
    L=-1  # empty simplex contribution in degree -1
    for M in matchings:
        if not M: continue
        S=set(M)
        if {action_edge(e,p) for e in M} != S:
            continue
        # orientation sign of permutation induced on simplex vertices (= graph edges)
        ordered=sorted(M)
        image=[action_edge(e,p) for e in ordered]
        pos={e:i for i,e in enumerate(ordered)}
        q=[pos[e] for e in image]
        sgn=parity(q)
        L += ((-1)**(len(M)-1))*sgn
    d=n*((m-1)//3)-1 if m%3==1 else n*((m-2)//3)
    return ((-1)**d)*L

def cycle_type(p):
    n=len(p); seen=[False]*n; ls=[]
    for i in range(n):
        if not seen[i]:
            j=i;l=0
            while not seen[j]: seen[j]=True;l+=1;j=p[j]
            ls.append(l)
    return tuple(sorted(ls,reverse=True))

# recurrence and period check
seq=[a(r) for r in range(12)]
assert seq == [1,0,-1,-1,0,1,1,0,-1,-1,0,1], seq
print('path_alternating_sequence',seq)

for n in (2,3):
    for m in (4,5,7,8):
        matchings=enumerate_matchings(n,m)
        vals={}
        for p in permutations(range(n)):
            sc=symbolic_character(n,m,p)
            fc=formula_character(n,m,p)
            bc=brute_character(n,m,p,matchings)
            assert sc==fc==bc,(n,m,p,sc,fc,bc)
            vals.setdefault(cycle_type(p),fc)
            assert vals[cycle_type(p)]==fc
        # reduced Euler characteristic has expected magnitude and sign at identity
        p=tuple(range(n)); d=n*((m-1)//3)-1 if m%3==1 else n*((m-2)//3)
        rank=1 if m%3==1 else 2*n-1
        assert formula_character(n,m,p)==rank
        print('case',{'n':n,'m':m,'matchings_including_empty':len(matchings),'top_degree':d,'rank':rank,'class_character':sorted(vals.items())})
print('VERIFY_OK')
