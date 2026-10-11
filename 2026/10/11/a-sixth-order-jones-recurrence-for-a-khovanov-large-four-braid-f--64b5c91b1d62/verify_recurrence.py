#!/usr/bin/env python3
from functools import lru_cache

# Laurent polynomials in A are dictionaries exponent -> integer coefficient.
def norm(p):
    return {e:c for e,c in p.items() if c}

def add(p,q):
    r=dict(p)
    for e,c in q.items(): r[e]=r.get(e,0)+c
    return norm(r)

def scale(p,n):
    return norm({e:n*c for e,c in p.items()})

def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return norm(r)

def mono(e,c=1): return {} if c==0 else {e:c}
ONE={0:1}
DELTA={2:-1,-2:-1}

def powp(p,n):
    r=ONE
    for _ in range(n): r=mul(r,p)
    return r

@lru_cache(None)
def nc_matchings(points):
    points=tuple(points)
    if not points: return ((),)
    first=points[0]; out=[]
    for j in range(1,len(points),2):
        for a in nc_matchings(points[1:j]):
            for b in nc_matchings(points[j+1:]):
                out.append(tuple(sorted(((first,points[j]),)+a+b)))
    return tuple(out)

BASIS=nc_matchings(tuple(range(8)))
assert len(BASIS)==14

def cyc_to_pos(c): return ('T',c) if c<4 else ('B',7-c)
def pos_to_cyc(p): return p[1] if p[0]=='T' else 7-p[1]
IDENTITY=tuple(sorted((tuple(sorted((i,7-i))) for i in range(4))))

def e_diag(i):
    pairs=[tuple(sorted((i,i+1))),tuple(sorted((7-i,6-i)))]
    pairs += [tuple(sorted((j,7-j))) for j in range(4) if j not in (i,i+1)]
    return tuple(sorted(pairs))

def basis_mul(d1,d2):
    adj={}
    def edge(u,v):
        adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for a,b in d1:
        def m1(p): return ('T',p[1]) if p[0]=='T' else ('M',p[1])
        edge(m1(cyc_to_pos(a)),m1(cyc_to_pos(b)))
    for a,b in d2:
        def m2(p): return ('M',p[1]) if p[0]=='T' else ('B',p[1])
        edge(m2(cyc_to_pos(a)),m2(cyc_to_pos(b)))
    seen=set(); ext=[]; loops=0
    for v in list(adj):
        if v in seen: continue
        stack=[v]; seen.add(v); comp=[]
        while stack:
            w=stack.pop(); comp.append(w)
            for z in adj[w]:
                if z not in seen: seen.add(z); stack.append(z)
        ends=[x for x in comp if x[0] in ('T','B')]
        if not ends: loops+=1
        else:
            assert len(ends)==2
            ext.append(tuple(sorted((pos_to_cyc(ends[0]),pos_to_cyc(ends[1])))))
    return tuple(sorted(ext)),loops

def el_add(x,y):
    z=dict(x)
    for d,p in y.items(): z[d]=add(z.get(d,{}),p)
    return {d:p for d,p in z.items() if p}

def el_scale(x,p):
    return {d:mul(c,p) for d,c in x.items() if mul(c,p)}

def el_mul(x,y):
    z={}
    for d,p in x.items():
        for e,q in y.items():
            f,loops=basis_mul(d,e)
            term=mul(mul(p,q),powp(DELTA,loops))
            z[f]=add(z.get(f,{}),term)
    return {d:p for d,p in z.items() if p}

ID={IDENTITY:ONE}
def sigma(i): return el_add(el_scale(ID,mono(1)),{e_diag(i):mono(-1)})
def word(indices):
    x=ID
    for i in indices: x=el_mul(x,sigma(i))
    return x

BLOCK=word((0,2,1,1,1,1))
TAIL=word((0,2))

# Lambda-polynomials: list coefficient[j](A) for lambda^j.
def lp_mul(p,q):
    r=[{} for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]=add(r[i+j],mul(a,b))
    return r

f1=[mono(2),ONE]                    # A^2 + lambda
f2=[mono(6),scale(ONE,-1)]          # A^6 - lambda
q1=[mono(2),add(add(add(mono(12),scale(mono(8),-2)),scale(mono(4),2)),scale(ONE,-1)),scale(mono(10),-1)]
q2=[scale(mono(2),-1),add(add(add(add(mono(16),scale(mono(12),-1)),scale(mono(8),2)),scale(mono(4),-1)),ONE),scale(mono(14),-1)]
R=lp_mul(lp_mul(f1,f2),lp_mul(q1,q2))
assert len(R)==7

orbit=[TAIL]
for _ in range(6): orbit.append(el_mul(BLOCK,orbit[-1]))
ann={}
for j in range(7): ann=el_add(ann,el_scale(orbit[j],R[j]))
assert ann=={}, ann

def closure_loops(d):
    adj={}
    def edge(u,v):
        adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for a,b in d: edge(cyc_to_pos(a),cyc_to_pos(b))
    for i in range(4): edge(('T',i),('B',i))
    seen=set(); loops=0
    for v in adj:
        if v in seen: continue
        loops+=1; stack=[v]; seen.add(v)
        while stack:
            w=stack.pop()
            for z in adj[w]:
                if z not in seen: seen.add(z); stack.append(z)
    return loops

def bracket(x):
    s={}
    for d,p in x.items(): s=add(s,mul(p,powp(DELTA,closure_loops(d)-1)))
    return s

F0=bracket(TAIL); F1=bracket(orbit[1])
assert F0=={8:-1,4:-1}, F0
assert F1=={14:-1,6:-3,2:1,-2:-4,-6:2,-10:-3,-14:1,-18:-1}, F1

print('VERIFY_OK basis=14 block_terms=%d tail_terms=%d annihilator_degree=6 state_identity=true F0_terms=%d F1_terms=%d' % (len(BLOCK),len(TAIL),len(F0),len(F1)))
