#!/usr/bin/env python3
"""Exact small-graph directed-linear-forest homology census. Requires SymPy.

Enumerates every unlabeled simple undirected graph of order at most five,
forms its symmetric digraph, and computes integral boundary Smith forms.
"""
from itertools import combinations, permutations
from collections import Counter
import json
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def all_graphs(n):
    pairs=list(combinations(range(n),2)); q=len(pairs)
    # Vertex permutations induce permutations of unordered graph edges.
    transforms=[]
    for p in permutations(range(n)):
        index={e:i for i,e in enumerate(pairs)}
        transforms.append(tuple(index[tuple(sorted((p[a],p[b])))] for a,b in pairs))
    representatives=set()
    for m in range(1<<q):
        orbit=[]
        for t in transforms:
            z=0
            for i,j in enumerate(t):
                if m>>i&1:z|=1<<j
            orbit.append(z)
        representatives.add(min(orbit))
    return pairs,sorted(representatives)


def simplices(n,undirected_edges):
    arcs=sorted({(a,b) for u,v in undirected_edges for a,b in ((u,v),(v,u))})
    faces={0:[]}
    for r in range(1,min(n,len(arcs)+1)):
        fl=[]
        for I in combinations(range(len(arcs)),r):
            indeg=[0]*n; outdeg=[0]*n; succ={}; good=True
            for i in I:
                a,b=arcs[i];indeg[b]+=1;outdeg[a]+=1
                if indeg[b]>1 or outdeg[a]>1:good=False;break
                succ[a]=b
            if not good:continue
            for v in succ:
                seen=set(); x=v
                while x in succ:
                    if x in seen:good=False;break
                    seen.add(x);x=succ[x]
                if not good:break
            if good:fl.append(sum(1<<i for i in I))
        if fl:faces[r]=fl
    return arcs,faces


def boundary_smith(arcs,faces):
    smith={};rank={}
    for k in range(2,max(faces.keys(),default=0)+1):
        hi=faces.get(k,[]);lo=faces.get(k-1,[])
        index={f:i for i,f in enumerate(lo)}
        B=zeros(len(lo),len(hi))
        for j,m in enumerate(hi):
            bits=[i for i in range(len(arcs)) if m>>i&1]
            for z,i in enumerate(bits):B[index[m^(1<<i)],j]=1 if z%2==0 else -1
        D=smith_normal_form(B,domain=ZZ)
        factors=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
        smith[k-1]=dict(sorted(Counter(factors).items()))
        rank[k-1]=len(factors)
    return smith,rank


def main():
    census={};witnesses=[]
    for n in range(1,6):
        possible,reps=all_graphs(n)
        census[n]={'isomorphism_types':len(reps),'torsion_types':0}
        for mask in reps:
            ee=[e for i,e in enumerate(possible) if mask>>i&1]
            arcs,faces=simplices(n,ee)
            smith,rank=boundary_smith(arcs,faces)
            bad=[(k,d,a)for k,ct in smith.items()for d,a in ct.items()if d>1]
            if bad:
                census[n]['torsion_types']+=1
                witnesses.append({'n':n,'edges':ee,'mask':mask,
                   'f_vector':[len(faces.get(k,[])) for k in range(1,n)],
                   'boundary_smith':smith,'boundary_ranks':rank,
                   'torsion_entries':bad})
    assert [census[n]['isomorphism_types'] for n in range(1,6)]==[1,2,4,11,34]
    assert [census[n]['torsion_types'] for n in range(1,6)]==[0,0,0,0,1]
    assert len(witnesses)==1
    w=witnesses[0]
    assert len(w['edges'])==7
    degrees=Counter(v for uv in w['edges'] for v in uv)
    assert sorted(degrees.values())==[2,2,2,4,4]
    assert w['f_vector'][:4]==[14,54,60,12]
    assert w['boundary_smith'][1]=={1:13}
    assert w['boundary_smith'][2]=={1:40,2:1}
    assert w['boundary_smith'][3]=={1:12}
    print(json.dumps({'census':census,'unique_witness':w,'integral_homology':
        {'H0':'Z','H1':'Z/2','H2':'Z^7','H3':'0'}},sort_keys=True))

if __name__=='__main__':main()
