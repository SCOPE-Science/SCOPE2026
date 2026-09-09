#!/usr/bin/env python3
"""Class-resolved Hurwitz (2,3,7) generation profiles for PSL(2,p), p in {13,29}.
Stdlib only. Exact enumeration of SL(2,p)/{+-I} with canonical reps.
Usage: python3 verify_hurwitz.py P [out.json]
"""
import sys, json
from collections import deque

def run(p):
    I = (1, 0, 0, 1)
    def neg(M): return tuple((-x) % p for x in M)
    def can(M):
        M = tuple(x % p for x in M); N = neg(M)
        return M if M <= N else N
    def mul(A, B):
        a,b,c,d = A; e,f,g,h = B
        return can((a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h))
    def inv(M):
        a,b,c,d = M  # det=1
        return can((d, (-b) % p, (-c) % p, a))
    def pw(M, k):
        R = I
        for _ in range(k): R = mul(R, M)
        return R
    def order(M):
        M2 = M
        for k in range(1, 200):
            M2 = mul(M2, M) if k > 1 else M
            if M2 == I: return k
        raise ValueError("order too big")
    # enumerate SL(2,p)
    elts = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a*d - b*c) % p == 1:
                        elts.append(can((a,b,c,d)))
    elts = sorted(set(elts))
    n = len(elts)
    assert n == p*(p*p-1)//2, (p, n)
    idx = {g:i for i,g in enumerate(elts)}
    G = p*(p*p-1)//2
    # generators of G (images of elementary matrices)
    u = can((1,1,0,1)); v = can((1,0,1,1))
    ui, vi = inv(u), inv(v)
    gens = [u, ui, v, vi]
    # conjugacy classes via BFS conjugation by gens
    def conj(g, h):  # h g h^{-1}
        return mul(mul(h, g), inv(h))
    seen = {}
    classes = []  # list of (rep, members)
    for g in elts:
        if g in seen: continue
        orb = set([g]); q = deque([g])
        while q:
            x = q.popleft()
            for h in gens:
                y = conj(x, h)
                if y not in orb: orb.add(y); q.append(y)
        for x in orb: seen[x] = len(classes)
        classes.append((g, orb))
    assert sum(len(o) for _,o in classes) == G
    # label classes: group by order, sort by trace-pair
    def tr(M):
        a,b,c,d = M; return (a+d) % p
    info = []
    for ci,(rep,orb) in enumerate(classes):
        o = order(rep)
        t = tr(rep); tp = tuple(sorted((t, (-t) % p)))
        info.append(dict(ci=ci, order=o, size=len(orb), tracepair=list(tp), rep=list(rep)))
    # name classes: order + letter
    from collections import defaultdict
    byord = defaultdict(list)
    for e in info: byord[e['order']].append(e)
    for o in byord: byord[o].sort(key=lambda e: e['tracepair'])
    name = {}
    for o, lst in byord.items():
        for j,e in enumerate(lst):
            e['name'] = f"{o}{chr(65+j)}"
            name[e['ci']] = e['name']
    def cls_of(g): return name[seen[g]]
    # class element lists
    members = {e['name']: [] for e in info}
    for g in elts: members[cls_of(g)].append(g)
    # locate 2A, 3A, 7-classes
    c2 = [e for e in info if e['order']==2]; c3=[e for e in info if e['order']==3]
    c7 = sorted([e for e in info if e['order']==7], key=lambda e:e['name'])
    assert len(c2)==1 and len(c3)==1, [c2,c3]
    C2, C3 = c2[0]['name'], c3[0]['name']
    # Frobenius constants via fixed-x0 fiber count + full-count crosscheck
    x0 = members[C2][0]
    triples = []
    for e7 in c7:
        T = e7['name']
        S = [y for y in members[C3] if cls_of(mul(x0,y))==T]
        k = len(S)
        Nfiber = len(members[C2])*k
        # crosscheck: full pair count
        S3 = members[C3]
        full = sum(1 for x in members[C2] for y in S3 if cls_of(mul(x,y))==T)
        assert full == Nfiber, (T, full, Nfiber)
        triples.append(dict(type=f"({C2},{C3},{T})", T=T, N=Nfiber, k_fiber=k))
    # centralizer of x0
    C = [c for c in elts if mul(c,x0)==mul(x0,c)]
    # generation verdict per type: C-orbits on fiber S, BFS subgroup order per rep
    def suborder(x, y):
        yi = inv(y)
        got = set([I]); q = deque([I])
        while q:
            z = q.popleft()
            for w in (mul(z,x), mul(z,y), mul(z,yi)):
                if w not in got: got.add(w); q.append(w)
        return len(got)
    results = []
    for t in triples:
        T = t['T']
        S = [y for y in members[C3] if cls_of(mul(x0,y))==T]
        # C_G(x0)-orbit reps
        reps = []; used = set()
        for y in S:
            if y in used: continue
            reps.append(y); q = deque([y]); used.add(y)
            while q:
                z = q.popleft()
                for c in C:
                    w = conj(z, c)
                    if w in S and w not in used: used.add(w); q.append(w)
        assert sum(1 for _ in used) == len(S)
        orders = [(y, suborder(x0,y)) for y in reps]
        gen = [(y,o) for y,o in orders if o==G]
        maxo = max(o for _,o in orders)
        results.append(dict(type=t['type'], N=t['N'], n_reps=len(reps),
                            verdict='GENERATES' if gen else 'NON-GENERATING',
                            max_suborder=maxo,
                            witness=[list(y) for y,_ in gen[:1]]))
    # containment: standard Borel (upper-triangular) & monomial test
    def in_borel(g): return g[2]==0
    def in_monomial(g): return (g[1]==0 and g[2]==0) or (g[0]==0 and g[3]==0)
    for r in results:
        if r['verdict']=='NON-GENERATING' or True:
            pass
    out = dict(p=p, G=G, genus=1+G//84, Gdiv84=(G%84==0),
               classes=[{k:e[k] for k in ('name','order','size','tracepair')} for e in sorted(info,key=lambda e:e['name'])],
               triples=results)
    return out, dict(elts=elts, mul=mul, inv=inv, order=order, cls_of=cls_of,
                     members=members, C2=C2, C3=C3, G=G, I=I, x0=x0)

def words_and_containment(p, data, aux):
    """For each triple: shortest-word witness (if generating) in base Hurwitz pair,
    Borel/monomial containment search (if non-generating)."""
    elts, mul, inv, order = aux['elts'], aux['mul'], aux['inv'], aux['order']
    members, cls_of, G, I = aux['members'], aux['cls_of'], aux['G'], aux['I']
    C2, C3 = aux['C2'], aux['C3']
    # base Hurwitz pair: A=x0 (2A), B in 3A with A*B of order 7 (first generating type)
    A = aux['x0']
    B = None
    for t in data['triples']:
        if t['verdict']=='GENERATES':
            y = tuple(t['witness'][0])
            # find y as element: need actual y with <A,y>=G; witness stored is matrix
            B = y
            break
    if B is None:
        return {'base_pair': None, 'note': 'no generating type; word search skipped'}
    assert order(mul(A,B))==7 and cls_of(B)==C3
    Bi = inv(B)
    # Cayley BFS shortest words
    from collections import deque
    par = {I: None}; lab = {}
    q = deque([I])
    step = [(A,'A'),(B,'B'),(Bi,'Bi')]
    while q:
        z = q.popleft()
        for w,s in step:
            v = mul(z,w)
            if v not in par: par[v]=z; lab[v]=s; q.append(v)
    assert len(par)==G, (len(par),G)
    def word(g):
        s=[]
        while g!=I: s.append(lab[g]); g=par[g]
        return ''.join(reversed(s)) if s else '1'
    # for each generating triple, witness = (word of some generating pair)
    # search: for each y in fiber, word available; find one with full suborder
    wit = {}
    for t in data['triples']:
        T=t['T'] if 'T' in t else t['type'].split(',')[2].rstrip(')')
        S=[y for y in members[C3] if cls_of(mul(A,y))==T]
        wy = None
        for y in S:
            # subgroup order check
            yi=inv(y); got=set([I]); qq=deque([I])
            while qq:
                z=qq.popleft()
                for w_ in (mul(z,A),mul(z,y),mul(z,yi)):
                    if w_ not in got: got.add(w_); qq.append(w_)
            if len(got)==G: wy=y; break
        if wy is not None:
            wit[t['type']]={'w2':'A','w3':word(wy),'prod_order':order(mul(A,wy)),
                            'w3_class':cls_of(wy),'suborder':G}
    # containment for non-generating triples
    cont = {}
    for t in data['triples']:
        if t['verdict']!='NON-GENERATING': continue
        T=t['type'].split(',')[2].rstrip(')')
        S=[y for y in members[C3] if cls_of(mul(A,y))==T]
        y0=S[0]
        found=None
        for g in elts:
            gi=inv(g)
            ax=mul(mul(g,A),gi); by=mul(mul(g,y0),gi)
            if ax[2]==0 and by[2]==0:
                found={'subgroup':'Borel C13(?) upper-triangular','via_conjugation_by':list(g)}; break
            if ((ax[1]==0 and ax[2]==0) or (ax[0]==0 and ax[3]==0)) and \
               ((by[1]==0 and by[2]==0) or (by[0]==0 and by[3]==0)):
                found={'subgroup':'split-torus normalizer (monomial)','via_conjugation_by':list(g)}; break
        cont[t['type']]=found or {'subgroup':f'exact proper subgroup order {t["max_suborder"]} (no Borel/monomial conjugate; non-generation already certified by exhaustive rep test)','via_conjugation_by':None}
    return {'base_pair':{'A':list(A),'B':list(B),'AB_order':7,
                         'diff_ATLAS':f'|AB|=7 vs ATLAS standard ab={p}; words below are non-standard by construction'},
            'witnesses':wit,'containment':cont,'cayley_size':len(par)}

if __name__=='__main__':
    p=int(sys.argv[1])
    data,aux=run(p)
    extra=words_and_containment(p,data,aux)
    data.update(extra)
    out=sys.argv[2] if len(sys.argv)>2 else f'hurwitz_psl2_{p}.json'
    json.dump(data,open(out,'w'),indent=1)
    print(f"p={p} |G|={data['G']} genus={data['genus']} classes={len(data['classes'])}")
    for t in data['triples']: print(" ",t['type'],'N=',t['N'],'reps=',t['n_reps'],t['verdict'],'maxsub=',t['max_suborder'])
    print(json.dumps({k:v for k,v in extra.items() if k!='witnesses'},indent=1)[:1500])
