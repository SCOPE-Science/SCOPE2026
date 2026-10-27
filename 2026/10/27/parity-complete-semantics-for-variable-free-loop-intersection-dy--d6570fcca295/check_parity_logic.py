"""Finite diagnostics for variable-free loop-intersection dynamic logic.

Tests actual relation semantics against the parity abstraction on finite
undirected bipartite graphs; no finite test substitutes for the theorem.
"""
from itertools import combinations
from random import Random

RNG = Random(59017)

def is_bipartite(n, edges):
    adj = [set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    colors = [-1]*n
    for v in range(n):
        if colors[v] != -1: continue
        colors[v]=0; todo=[v]
        while todo:
            x=todo.pop()
            for y in adj[x]:
                if colors[y] == -1:
                    colors[y]=1-colors[x];todo.append(y)
                elif colors[y]==colors[x]:
                    return False,adj,None
    return True,adj,colors

def close_star(r,n):
    a = set(r)|{(i,i) for i in range(n)}
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in a and (k,j) in a: a.add((i,j))
    return a

def truth_form(f, adj):
    n=len(adj)
    tag=f[0]
    if tag=='t':return set(range(n))
    if tag=='f':return set()
    if tag=='not':return set(range(n))-truth_form(f[1],adj)
    if tag=='and':return truth_form(f[1],adj)&truth_form(f[2],adj)
    if tag=='dia':
        r=relation(f[1],adj)
        good=truth_form(f[2],adj)
        return {u for u,v in r if v in good}
    if tag=='loop':
        r=relation(f[1],adj)
        return {u for u,v in r if u==v}
    raise ValueError(tag)

def relation(p,adj):
    n=len(adj); tag=p[0]
    if tag=='a':return {(i,j) for i in range(n) for j in adj[i]}
    if tag=='test':return {(i,i) for i in truth_form(p[1],adj)}
    if tag=='union':return relation(p[1],adj)|relation(p[2],adj)
    if tag=='inter':return relation(p[1],adj)&relation(p[2],adj)
    if tag=='conv':return {(v,u) for u,v in relation(p[1],adj)}
    if tag=='seq':
        r=relation(p[1],adj);s=relation(p[2],adj)
        return {(u,v) for u,k in r for h,v in s if k==h}
    if tag=='star':return close_star(relation(p[1],adj),n)
    raise ValueError(tag)

def form_abs(f,nonisol):
    tag=f[0]
    if tag=='t':return True
    if tag=='f':return False
    if tag=='not':return not form_abs(f[1],nonisol)
    if tag=='and':return form_abs(f[1],nonisol) and form_abs(f[2],nonisol)
    if tag=='dia':
        s=prog_abs(f[1],nonisol)
        return bool(s) and form_abs(f[2],nonisol)
    if tag=='loop':return 0 in prog_abs(f[1],nonisol)
    raise ValueError(tag)

def prog_abs(p,nonisol):
    tag=p[0]
    if tag=='a':return {1} if nonisol else set()
    if tag=='test':return {0} if form_abs(p[1],nonisol) else set()
    if tag=='union':return prog_abs(p[1],nonisol)|prog_abs(p[2],nonisol)
    if tag=='inter':return prog_abs(p[1],nonisol)&prog_abs(p[2],nonisol)
    if tag=='conv':return prog_abs(p[1],nonisol)
    if tag=='seq':return {(a+b)%2 for a in prog_abs(p[1],nonisol) for b in prog_abs(p[2],nonisol)}
    if tag=='star':
        s=prog_abs(p[1],nonisol)
        return {0,1} if 1 in s else {0}
    raise ValueError(tag)

def gen_form(d):
    if d<=0:return (RNG.choice(['t','f']),)
    tag=RNG.choice(['t','f','not','and','dia','loop'])
    if tag in ['t','f']:return (tag,)
    if tag=='not':return ('not',gen_form(d-1))
    if tag=='and':return ('and',gen_form(d-1),gen_form(d-1))
    if tag=='dia':return ('dia',gen_prog(d-1),gen_form(d-1))
    return ('loop',gen_prog(d-1))

def gen_prog(d):
    if d<=0:return ('a',) if RNG.randrange(2) else ('test',gen_form(0))
    tag=RNG.choice(['a','test','union','inter','conv','seq','star'])
    if tag=='a':return ('a',)
    if tag=='test':return ('test',gen_form(d-1))
    if tag in ['union','inter','seq']:return (tag,gen_prog(d-1),gen_prog(d-1))
    return (tag,gen_prog(d-1))

def all_graphs(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        edges=[e for i,e in enumerate(pairs) if mask>>i&1]
        ok,adj,col=is_bipartite(n,edges)
        if ok:yield adj,col

forms=[gen_form(4) for _ in range(400)]
progs=[gen_prog(4) for _ in range(400)]
counts={}
for n in range(1,6):
    checked=0
    for adj,col in all_graphs(n):
        checked+=1
        for f in forms:
            actual=truth_form(f,adj)
            for v in range(n):
                if (v in actual)!=form_abs(f,bool(adj[v])):
                    raise AssertionError(('formula',n,adj,f,v,actual))
        for p in progs:
            rel=relation(p,adj)
            for v in range(n):
                if not adj[v]:continue
                parity=prog_abs(p,True)
                if any(((col[u]^col[w]) not in parity) for u,w in rel if adj[u]):
                    raise AssertionError(('bad parity',n,adj,p))
                if (0 in parity)!=( (v,v) in rel):
                    raise AssertionError(('bad diagonal',n,adj,p,v))
                if 1 in parity and not all((v,w) in rel for w in adj[v]):
                    raise AssertionError(('missing neighbor',n,adj,p,v))
    counts[n]=checked
print('PARITY_LOOP_INTERSECTION_OK',counts,len(forms),len(progs))
