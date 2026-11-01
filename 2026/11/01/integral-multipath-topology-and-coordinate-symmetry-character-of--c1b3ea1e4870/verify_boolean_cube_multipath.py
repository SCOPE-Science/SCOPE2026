#!/usr/bin/env python3
"""Exact finite checks for the rank-oriented Boolean four-cube multipath complex.

Python >=3.9, standard library only. Run from any working directory.
The simplicial Morse matching is checked against the entire Hasse graph.
"""
import itertools
import json
from pathlib import Path
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import comb

HERE = Path(__file__).resolve().parent
D = 4
N = 1 << D

def fac(k):
    sources = [a for a in range(N) if a.bit_count() == k]
    sinks = [b for b in range(N) if b.bit_count() == k+1]
    edges = [(a,b) for a in sources for b in sinks if a & b == a]
    all_faces = [0]
    for j,(a,b) in enumerate(edges):
        all_faces += [f | (1<<j) for f in all_faces if all((u!=a and v!=b) for i,(u,v) in enumerate(edges[:j]) if f>>i & 1)]
    return edges,sorted(all_faces)

def greedy_certificate(edges,faces):
    full=set(faces)
    pairs=[]
    for j in range(len(edges)):
        for f in faces:
            g=f|(1<<j)
            if not (f>>j)&1 and f in full and g in full:
                pairs.append((f,g))
                full.remove(f);full.remove(g)
    assert sum(f==0 for f,g in pairs)==1
    # Work in the nonempty simplicial face poset: unmatch its 0-cell.
    pairs=[(f,g) for f,g in pairs if f]
    critical=sorted(set(faces)-{0}-{x for p in pairs for x in p})
    return sorted(pairs),critical

def acyclic_nonempty(faces,pairs):
    face=[f for f in faces if f]
    idx={f:i for i,f in enumerate(face)}
    upper={(a,b) for a,b in pairs}
    degree=[0]*len(face)
    adj=[[] for _ in face]
    incidence=0
    for g in face:
        for j in range(g.bit_length()):
            if g>>j & 1:
                f=g^(1<<j)
                if f==0:continue
                incidence+=1
                if (f,g) in upper: u,v=idx[f],idx[g]
                else: u,v=idx[g],idx[f]
                adj[u].append(v);degree[v]+=1
    queue=deque(i for i,d in enumerate(degree) if d==0)
    scanned=0
    while queue:
        i=queue.popleft();scanned+=1
        for j in adj[i]:
            degree[j]-=1
            if degree[j]==0:queue.append(j)
    return scanned==len(face),incidence

def betti_mod2(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    ranks={}
    for k in range(1,max(bydim)+1):
        lower={f:i for i,f in enumerate(bydim[k-1])}
        basis={};rank=0
        for g in bydim[k]:
            b=0
            for j in range(g.bit_length()):
                if g>>j&1:b^=1<<lower[g^(1<<j)]
            while b:
                p=b.bit_length()-1
                if p in basis:b^=basis[p]
                else:basis[p]=b;rank+=1;break
        ranks[k]=rank
    betti={k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in bydim.items()}
    return ranks,betti

def cycle_type(p):
    seen=set();typ=[]
    for v in range(D):
        if v in seen:continue
        w=v;n=0
        while w not in seen: seen.add(w);n+=1;w=p[w]
        typ.append(n)
    return tuple(sorted(typ,reverse=True))

def action_on_mask(p,mask):
    return sum(1<<p[j] for j in range(D) if mask>>j&1)

def trace_top(edges,faces,p):
    lookup={edge:i for i,edge in enumerate(edges)}
    perm=[lookup[(action_on_mask(p,a),action_on_mask(p,b))] for a,b in edges]
    trace=-1  # augmented empty simplex (reduced Lefschetz number)
    for f in faces:
        if f==0:continue
        moved=0;image=[]
        for i in range(len(edges)):
            if f>>i&1:
                moved|=1<<perm[i]
                image.append(perm[i])
        if moved!=f:continue
        inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        trace+=(-1)**(f.bit_count()-1+inv)
    return trace

def poly_mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):z[i+j]+=a*b
    return z

def direct_dp_arcs(edges):
    # A different enumeration: never construct the rank factors, only enforce
    # the defining constraints on outgoing and incoming arcs of the DAG.
    @lru_cache(None)
    def rec(i,out_used,in_used):
        if i==len(edges):return (1,)
        a,b=edges[i]
        skip=rec(i+1,out_used,in_used)
        ans=list(skip)
        if not(out_used>>a&1 or in_used>>b&1):
            take=rec(i+1,out_used | (1<<a), in_used | (1<<b))
            if len(ans)<len(take)+1:ans.extend([0]*(len(take)+1-len(ans)))
            for j,x in enumerate(take):ans[j+1]+=x
        return tuple(ans)
    return list(rec(0,0,0)),rec.cache_info().currsize

def main():
    factors=[];output=[]
    for k in range(D):
        edges,faces=fac(k)
        fvec=[sum(f.bit_count()==j for f in faces) for j in range(max(f.bit_count() for f in faces)+1)]
        row={'k':k,'edges':len(edges),'faces':len(faces),'face_polynomial_coefficients':fvec}
        if k in (1,2):
            pairs,critical=greedy_certificate(edges,faces)
            assert len(pairs)==78 and len(critical)==6
            assert Counter(f.bit_count()-1 for f in critical)=={0:1,2:5}
            ok,incidences=acyclic_nonempty(faces,pairs)
            assert ok and incidences==432
            r,b=betti_mod2(faces)
            assert r=={1:11,2:37,3:30} and b=={0:1,1:0,2:5,3:0}
            row.update(morse_pairs=len(pairs), critical_dimensions=dict(sorted(Counter(f.bit_count()-1 for f in critical).items())), acyclic=ok, hasse_incidences=incidences, mod2_boundary_ranks=r)
            item={'edges':edges,'pairs':pairs,'critical':critical}
            if k==1:
                if '--write-certificate' in __import__('sys').argv:
                    (HERE/'morse_certificate.json').write_text(json.dumps(item,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
                else:
                    other=json.loads((HERE/'morse_certificate.json').read_text(encoding='utf-8'))
                    assert other==json.loads(json.dumps(item))
        factors.append((edges,faces))
        output.append(row)
    assert output[0]['face_polynomial_coefficients']==[1,4]
    assert output[1]['face_polynomial_coefficients']==[1,12,48,72,30]
    assert output[2]['face_polynomial_coefficients']==[1,12,48,72,30]
    assert output[3]['face_polynomial_coefficients']==[1,4]
    product=[1]
    for row in output: product=poly_mul(product,row['face_polynomial_coefficients'])
    all_arcs=sorted(e for edges,faces in factors for e in edges)
    assert len(all_arcs)==32
    direct,memo_states=direct_dp_arcs(all_arcs)
    assert direct==product
    assert sum(product)==664225 and product[-1]>0
    class_counts=Counter(); wchars={}; topchars={}
    for p in itertools.permutations(range(D)):
        typ=cycle_type(p);class_counts[typ]+=1
        w=trace_top(*factors[1],p)
        wdual=trace_top(*factors[2],p)
        assert w==wdual
        std=sum(p[i]==i for i in range(D))-1
        top=std*std*w*wdual
        if typ in wchars:assert wchars[typ]==w and topchars[typ]==top
        wchars[typ]=w;topchars[typ]=top
    types=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
    assert [class_counts[t] for t in types]==[1,6,3,8,6]
    assert [wchars[t] for t in types]==[5,-1,1,2,1]
    assert [topchars[t] for t in types]==[225,1,1,0,1]
    irrepchars={'trivial':[1,1,1,1,1], 'sign':[1,-1,1,1,-1], 'standard':[3,1,-1,0,-1], 'signed_standard':[3,-1,-1,0,1], 'two_two':[2,0,2,-1,0]}
    sizes=[1,6,3,8,6];v=[topchars[t] for t in types]
    multiplicity={name:sum(sz*x*y for sz,x,y in zip(sizes,v,chi))//24 for name,chi in irrepchars.items()}
    assert multiplicity=={'trivial':10,'sign':9,'standard':28,'signed_standard':28,'two_two':19}
    # The rank-one and rank-two factors are 5 two-spheres each;
    # the two outer factors are 4-point spaces (3 zero-spheres each).
    assert 3*5*5*3==225 and (0+2+2+0+3)==7
    print('BOOLEAN_CUBE_4_MULTIPATH_EXACT_VERIFIED')
    print('rank_factors',json.dumps(output,sort_keys=True))
    print('full_face_polynomial',json.dumps(product))
    print('full_nonempty_face_count',sum(product)-1)
    print('independent_dag_dp_states',memo_states)
    print('S4_rank_middle_H2_characters',[wchars[t] for t in types])
    print('S4_full_H7_characters',[topchars[t] for t in types])
    print('S4_irreducible_multiplicities',json.dumps(multiplicity,sort_keys=True))
    print('homotopy_type','225 copies of S^7')

if __name__=='__main__':main()
