#!/usr/bin/env python3
"""Exact combinatorial certificates for 4-robust clique complexes of small grids.

Usage: python grid4_morse.py                 # independently verify bundled certificate
       python grid4_morse.py --generate      # regenerate certificate deterministically

Requires only Python 3 standard library. Vertex (i,j) is encoded by i*n+j;
a nonempty face is its positive integer vertex-bitmask.
"""
import gzip
import json
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import combinations
from math import comb
from pathlib import Path

CASE_LIST = [(3,3), (3,4), (3,5), (4,4), (4,5), (5,5)]
CERTIFICATE = Path(__file__).with_name('grid4_morse_certificate.json.gz')
# Class representatives: e, +90, 180, -90, horizontal, vertical, main diagonal, other diagonal.
EXPECTED_CHARACTERS = {3:[4,0,0,0,0,0,-2,-2],4:[84,0,4,0,-10,-10,-10,-10],5:[560,0,0,0,0,0,-28,-28]}

def face_complex(m,n):
    count=m*n
    adj=[0]*count
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for di,dj in ((1,0),(0,1)):
                if i+di<m and j+dj<n:
                    v=(i+di)*n+j+dj
                    adj[u]|=1<<v
                    adj[v]|=1<<u
    forbidden=[]
    for q in combinations(range(count),4):
        s=sum(1<<v for v in q)
        if all((adj[v]&s)==0 for v in q):forbidden.append(s)
    faces=set()
    # Bipartiteness: any 7 vertices include four from one color class.
    for k in range(1,7):
        for q in combinations(range(count),k):
            s=sum(1<<v for v in q)
            if not any((s&b)==b for b in forbidden):faces.add(s)
    assert all(sum((x>>v)&1 for v in range(count) if (v//n+v%n)%2 == color)<=3
               for x in faces for color in (0,1))
    return faces,forbidden

def parents(face):
    t=face
    while t:
        bit=t&-t;t-=bit
        child=face^bit
        if child:yield child

def upper_graph(faces):
    up={f:set() for f in faces}
    for tau in faces:
        for sig in parents(tau):
            if sig in up:up[sig].add(tau)
    return up

def generator_matching(faces):
    available=set(faces)
    up=upper_graph(available)
    eligible=[]; all_top=[];operations=[]
    for f in available:heappush(all_top,(-f.bit_count(),-f))
    def maybe(f):
        if f not in available or len(up[f])!=1:return
        tau=next(iter(up[f]))
        if tau in available and not up[tau]:heappush(eligible,(-tau.bit_count(),-tau,-f,f,tau))
    for f in available:maybe(f)
    def remove(f):
        available.remove(f)
        for sig in parents(f):
            if sig in available:
                up[sig].discard(f)
                maybe(sig)
    while available:
        pair=None
        while eligible:
            *_,sig,tau=heappop(eligible)
            if sig in available and tau in available and up[sig]=={tau} and not up[tau]:
                pair=(sig,tau);break
        if pair:
            sig,tau=pair
            operations.append(['p',sig,tau])
            remove(tau);remove(sig)
        else:
            while all_top and -all_top[0][1] not in available:heappop(all_top)
            tau=-all_top[0][1]
            assert not up[tau]
            operations.append(['c',tau]);remove(tau)
    return operations

def check_operations(faces,operations,expected):
    avail=set(faces)
    up=upper_graph(avail)
    pairs=set();critical=[];total_pairs=0
    def remove(f):
        avail.remove(f)
        for sig in parents(f):
            if sig in avail:up[sig].remove(f)
    for op in operations:
        if op[0]=='p':
            assert len(op)==3
            _,sig,tau=op
            assert sig in avail and tau in avail
            assert sig.bit_count()+1==tau.bit_count() and sig & tau==sig
            assert up[sig]=={tau} and not up[tau], ('not an elementary free-face collapse',op)
            pairs.add((sig,tau));total_pairs+=1
            remove(tau);remove(sig)
        else:
            assert op[0]=='c' and len(op)==2
            tau=op[1]
            assert tau in avail and not up[tau], ('not a maximal critical face',op)
            critical.append(tau);remove(tau)
    assert not avail
    assert len(faces)==2*total_pairs+len(critical)
    crit_dims=Counter(c.bit_count()-1 for c in critical)
    assert crit_dims=={0:1,5:expected},(crit_dims,expected)
    # Independent verification of Forman acyclicity: reverse every matched Hasse arrow.
    indegree={face:0 for face in faces}
    graph=defaultdict(list)
    for tau in faces:
        for sig in parents(tau):
            if sig not in faces:continue
            if (sig,tau) in pairs:
                source,target=sig,tau
            else:
                source,target=tau,sig
            graph[source].append(target)
            indegree[target]+=1
    queue=deque(f for f in faces if indegree[f]==0)
    seen=0
    while queue:
        source=queue.popleft();seen+=1
        for target in graph[source]:
            indegree[target]-=1
            if indegree[target]==0:queue.append(target)
    assert seen==len(faces),('directed cycle in matched Hasse diagram',seen,len(faces))
    return total_pairs,crit_dims

def dihedral_character(n,faces):
    funcs=[
        lambda i,j:(i,j),lambda i,j:(j,n-1-i),
        lambda i,j:(n-1-i,n-1-j),lambda i,j:(n-1-j,i),
        lambda i,j:(i,n-1-j),lambda i,j:(n-1-i,j),
        lambda i,j:(j,i),lambda i,j:(n-1-j,n-1-i),
    ]
    out=[]
    for transform in funcs:
        mapping=[None]*(n*n)
        for a in range(n*n):
            x,y=transform(a//n,a%n)
            mapping[a]=x*n+y
        assert sorted(mapping)==list(range(n*n))
        reduced_lefschetz=-1 # empty face contributes in reduced Lefschetz sum
        for mask in faces:
            vertices=[p for p in range(n*n) if mask>>p&1]
            transformed=[mapping[p] for p in vertices]
            if sorted(transformed)!=vertices:continue
            inversions=sum(transformed[i]>transformed[j] for i in range(len(vertices)) for j in range(i+1,len(vertices)))
            trace=(-1)**inversions
            reduced_lefschetz+=(-1)**(len(vertices)-1)*trace
        # Only reduced H_5 is present; sign is (-1)^5.
        out.append(-reduced_lefschetz)
    return out

def irreducible_multiplicities(t):
    # D4 classes: e, r^2, {r,r^-1}, {horizontal,vertical}, {diagonal,antidiagonal}
    c=[t[0],t[2],t[1],t[4],t[6]]
    table={'A1':[1,1,1,1,1], 'A2':[1,1,1,-1,-1],
           'B1':[1,1,-1,1,-1], 'B2':[1,1,-1,-1,1],
           'E':[2,-2,0,0,0]}
    out={}
    for name,chi in table.items():
        numerator=sum(size*a*b for size,a,b in zip([1,1,2,2,2],c,chi))
        assert numerator%8==0 and numerator>=0
        out[name]=numerator//8
    assert sum((2 if k=='E' else 1)*v for k,v in out.items())==c[0]
    return out

def verify():
    with gzip.open(CERTIFICATE,'rt',encoding='utf-8') as f: all_data=json.load(f)
    assert sorted(all_data)==sorted(f'{m}x{n}' for m,n in CASE_LIST)
    reports=[]
    for m,n in CASE_LIST:
        label=f'{m}x{n}'
        faces,forbidden=face_complex(m,n)
        assert all_data[label]['independent_4_count']==len(forbidden)
        fvector=[sum(face.bit_count()==k for face in faces) for k in range(1,7)]
        assert all_data[label]['fvector']==fvector
        assert sum((-1)**(k-1)*v for k,v in enumerate(fvector,1))-1 == -comb((m-1)*(n-1),3)
        pairs,crit=check_operations(faces,all_data[label]['operations'],comb((m-1)*(n-1),3))
        if m==n:
            char=dihedral_character(n,faces)
            assert char==EXPECTED_CHARACTERS[n],(n,char)
            assert all_data[label]['dihedral_character']==char
            assert all_data[label]['irreducibles']==irreducible_multiplicities(char)
        reports.append((label,len(forbidden),len(faces),fvector,pairs,crit))
    print('All six grid cases: exact faces, elementary collapses, Hasse-DAG acyclicity, reduced Euler, and D4 characters VERIFIED.')
    for report in reports:print(report)

def generate():
    all_data={}
    for m,n in CASE_LIST:
        faces,forbidden=face_complex(m,n)
        label=f'{m}x{n}'
        operations=generator_matching(faces)
        record={'independent_4_count':len(forbidden),
                'fvector':[sum(face.bit_count()==k for face in faces) for k in range(1,7)],
                'operations':operations}
        if m==n:
            chi=dihedral_character(n,faces)
            record['dihedral_character']=chi
            record['irreducibles']=irreducible_multiplicities(chi)
        all_data[label]=record
        print('generated',label,len(operations),'steps',flush=True)
    with gzip.open(CERTIFICATE,'wt',encoding='utf-8',compresslevel=9) as f:
        json.dump(all_data,f,separators=(',',':'))
    verify()

if __name__=='__main__':
    if sys.argv[1:]==['--generate']:generate()
    else:
        assert not sys.argv[1:]
        verify()
