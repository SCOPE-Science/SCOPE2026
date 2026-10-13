#!/usr/bin/env python3
"""Reproduce finite checks for the power-domination leaf-corona theorem.

Only the Python standard library is required. Enumerates all graph-isomorphism
representatives on 1 through 6 vertices (graph6 fixture) and all initial sets.
Finite verification supplements, but never replaces, the mathematical proof.
"""
from collections import defaultdict
import sys

GRAPH6_CODES = ['@', 'A?', 'A_', 'B?', 'BG', 'Bo', 'Bw', 'C?', 'C@', 'CB', 'C`', 'CJ', 'CF', 'Ck', 'CN', 'Cl', 'C|', 'C~', 'D??', 'D?C', 'Dg?', 'DOC', 'Dw?', 'DBC', 'D@c', 'DgC', 'DJC', 'Dl?', 'D?{', 'DBc', 'Dh_', 'DwC', 'D|?', 'D@{', 'Dx_', 'DJc', 'DbW', 'Dhc', 'Des', 'DjW', 'Db[', 'D`{', 'Dlc', 'D]o', 'DJ{', 'DF{', 'Djs', 'D]w', 'Df{', 'Dl{', 'Dn{', 'D~{', 'E???', 'E??G', 'EC?G', 'EI??', 'EJ??', 'ECa?', 'E?EG', 'E?D_', 'EK?G', 'ECaG', 'EC_W', 'E?Bo', 'EBc?', 'EY?O', 'EJA?', 'EKa?', 'EGEG', 'EQ_O', 'ECaW', 'EBCW', 'E@cW', 'EJc?', 'EHs?', 'Ehc?', 'E?Bw', 'EhP?', 'EsCO', 'EiGO', 'EBe?', 'Ej?G', 'E`EG', 'ECd_', 'EK_W', 'ECeW', 'EB{?', 'EJw?', 'EOkW', 'Elc?', 'ErW?', 'E?Fw', 'EC{O', 'E@dW', 'EG}?', 'E]a?', 'EYWO', 'E]_O', 'EQKo', 'EsCW', 'EKaW', 'EJe?', 'EBy?', 'Ehd?', 'EhEG', 'EJaG', 'E~A?', 'EzW?', 'Ejs?', 'Ev@_', 'EB{G', 'EhX_', 'E^_O', 'EJwG', 'E`Xg', 'E~?G', 'EtaG', 'Eht?', 'EtoO', 'EB}?', 'EXSg', 'Eld?', 'EJy?', 'Exd?', 'EYOw', 'ERUO', 'EZEG', 'ElEG', 'EheO', 'E{CW', 'E~@_', 'El{?', 'E~a?', 'E~_O', 'EzW_', 'Ejt?', 'EjsG', 'Ez`_', 'Eju?', 'Ev`_', 'EXSw', 'E~AG', 'Er`o', 'EB}G', 'Exe_', 'E?~o', 'EhMg', 'EyUG', 'Ele_', 'EJyG', 'EhdW', 'EhNG', 'Ehf_', 'EhUg', 'En{?', 'E~H_', 'E~`_', 'El{G', 'EZSw', 'E~@g', 'E?~w', 'E|e_', 'EyuG', 'EyVG', 'E~aG', 'ElfO', 'E^eG', 'E^MG', 'Exf_', 'EO~o', 'Ehew', 'Elf_', 'ElMg', 'EtTg', 'ElUg', 'E~{?', 'En{G', 'En}?', 'E_~w', 'EjtW', 'E^mG', 'E^Mg', 'EjvG', 'Elfo', 'Exv_', 'ErXw', 'Ehfw', 'EzNG', 'E^NG', 'EyUw', 'E~|?', 'E~Xo', 'En}G', 'E~wW', 'EyVw', 'ER~g', 'E}^G', 'Ep~o', 'El^g', 'E~{W', 'E~z_', 'Ep~w', 'E~^G', 'EznW', 'E~~G', 'E~nW', 'Ez~w', 'E~~w']


def decode_graph6(code):
    n = ord(code[0]) - 63
    assert 1 <= n <= 6
    bitstream = ''.join(f'{ord(c)-63:06b}' for c in code[1:])
    graph = {v:set() for v in range(n)}
    j = 0
    for v in range(1,n):
        for u in range(v):
            if bitstream[j]=='1':
                graph[u].add(v)
                graph[v].add(u)
            j += 1
    return graph


def role(r,l,c,rho):
    if r == 0 and l == 1:
        return 1  # agent, initially observed root and leaf
    if r == 0 and l == 0 and c == 0 and rho == 0:
        return 2  # unobserved target root
    return 0      # observed root, not eligible as an agent


def mask_from_children(t,mask):
    k0 = bool(mask&1)
    k1 = bool(mask&2)
    allow_p0 = (k1 if t == 2 else (k0 or k1))
    allow_p1 = (t in (1,2) and k0)
    return int(allow_p0)+2*int(allow_p1)


def transition(aggregate,child,parent_r):
    seen_child_r,b0,b1,b2 = aggregate
    r,l,c,f0,f1 = child
    cmask=f1 if parent_r else f0
    child_role=role(r,l,c,parent_r)
    out=[]
    for t,b in ((0,b0),(1,b1),(2,b2)):
        can_pair=(t==1 and child_role==2) or (t==2 and child_role==1)
        no_edge=bool(cmask&1)
        edge=bool(cmask&2) and can_pair
        k0=bool(b&1) and no_edge
        k1=(bool(b&2) and no_edge) or (bool(b&1) and edge)
        out.append(int(k0)+2*int(k1))
    return (int(seen_child_r or r),*out)


def multiply(p,q):
    out=defaultdict(int)
    for a,pa in p.items():
        for b,pb in q.items():
            out[a+b]+=pa*pb
    return out


def add_shift(dest,source,shift):
    for k,value in source.items():
        dest[k+shift] += value


def tree_polynomial(G,root=0):
    """Rooted finite-state tree DP; counts selected sets, not matchings."""
    parent={root:None}
    order=[root]
    for v in order:
        for u in sorted(G[v]):
            if u not in parent:
                parent[u]=v
                order.append(u)
    assert len(order)==len(G)
    D={}
    for v in reversed(order):
        children=[u for u in sorted(G[v]) if parent.get(u)==v]
        current=defaultdict(lambda:defaultdict(int))
        for r in (0,1):
            for l in (0,1):
                A={(0,1,1,1):{0:1}}
                for u in children:
                    nxt=defaultdict(lambda:defaultdict(int))
                    for aggregate,poly in A.items():
                        for child_state,child_poly in D[u].items():
                            changed=transition(aggregate,child_state,r)
                            add_shift(nxt[changed],multiply(poly,child_poly),0)
                    A=nxt
                for (c,b0,b1,b2),poly in A.items():
                    masks=[]
                    for rho in (0,1):
                        t=role(r,l,c,rho)
                        masks.append(mask_from_children(t,(b0,b1,b2)[t]))
                    state=(r,l,c,masks[0],masks[1])
                    add_shift(current[state],poly,r+l)
        D[v]=current
    answer=defaultdict(int)
    for (_,_,_,f0,_),poly in D[root].items():
        if f0&1:
            add_shift(answer,poly,0)
    return dict(answer)


def forest_polynomial(G):
    unseen=set(G)
    result={0:1}
    while unseen:
        v=min(unseen)
        comp={v}
        queue=[v]
        for w in queue:
            for u in G[w]:
                if u not in comp:
                    comp.add(u)
                    queue.append(u)
        unseen-=comp
        part={v:{u for u in G[v] if u in comp} for v in comp}
        result=dict(multiply(result,tree_polynomial(part,v)))
    return result


def power_dominates(G,selected):
    n=len(G)
    blue=set(selected)
    for v in selected:
        if v<n:
            blue.update(G[v])
            blue.add(n+v)
        else:
            blue.add(v-n)
    while True:
        add=set()
        for v in blue:
            neighbors=(G[v]|{n+v}) if v<n else {v-n}
            white=neighbors-blue
            if len(white)==1:
                add.update(white)
        if not add:
            return len(blue)==2*n
        blue.update(add)


def matching_criterion(G,roots,leaves):
    """Independent test: enumerate all target-saturating matchings, then
    count perfect matchings on the vertex set saturated by each candidate.
    """
    C=set(roots)|set(leaves)
    for v in roots:
        C.update(G[v])
    A=set(leaves)-set(roots)
    U=set(G)-C
    if not U:
        return True
    if len(U)>len(A):
        return False
    targets=sorted(U,key=lambda v:(len(A&G[v]),v))
    nbr=[sorted(A&G[v]) for v in targets]
    if any(not c for c in nbr):
        return False
    def uniquely_restricted(used):
        agents=set(used)
        matches=0
        def count(i,chosen):
            nonlocal matches
            if matches>1:return
            if i==len(targets):
                matches+=1
                return
            for a in nbr[i]:
                if a in agents and a not in chosen:
                    count(i+1,chosen|{a})
        count(0,set())
        return matches==1
    def search(i,used):
        if i==len(targets):
            return uniquely_restricted(used)
        for a in nbr[i]:
            if a not in used and search(i+1,used|{a}):
                return True
        return False
    return search(0,set())


def is_forest(G):
    visited=set()
    def explore(v,p):
        visited.add(v)
        for u in G[v]:
            if u==p:continue
            if u in visited or not explore(u,v):return False
        return True
    for v in G:
        if v not in visited and not explore(v,None):return False
    return True


def main():
    total_graphs=0
    direct_sets=0
    forests=0
    forest_sets=0
    for code in GRAPH6_CODES:
        G=decode_graph6(code)
        n=len(G)
        all_poly=defaultdict(int)
        for bits in range(1<<(2*n)):
            S={v for v in range(2*n) if bits>>v&1}
            R={v for v in S if v<n}
            L={v-n for v in S if v>=n}
            truth=power_dominates(G,S)
            match=matching_criterion(G,R,L)
            assert truth == match,('matching',code,bits,truth,match)
            if truth:all_poly[len(S)]+=1
            direct_sets+=1
        total_graphs+=1
        if is_forest(G):
            via_dp=forest_polynomial(G)
            assert dict(all_poly)==via_dp,('tree_dp',code,via_dp,dict(all_poly))
            forests+=1
            forest_sets+=1<<(2*n)
    # A C4 cyclic ambiguity: the two observed leaf agents see the same
    # two unobserved targets; a perfect matching exists but is not unique.
    C4={0:{1,3},1:{0,2},2:{1,3},3:{0,2}}
    assert not power_dominates(C4,{4,6})
    assert not matching_criterion(C4,set(),{0,2})
    print('PASS: graph-isomorphism representatives:',total_graphs)
    print('PASS: direct power-domination / uniquely restricted matching comparisons:',direct_sets)
    print('PASS: forest representatives with polynomial coefficient checks:',forests)
    print('PASS: directly enumerated forest initial sets:',forest_sets)
    print('PASS: cyclic C4 example distinguishes matching from unique matching')
    print('Example leaf coronas:')
    for n in (1,2,3,4):
        G={v:({v-1} if v>0 else set())|({v+1} if v<n-1 else set()) for v in range(n)}
        print('  base path length',n,':',forest_polynomial(G))

if __name__=='__main__':main()
