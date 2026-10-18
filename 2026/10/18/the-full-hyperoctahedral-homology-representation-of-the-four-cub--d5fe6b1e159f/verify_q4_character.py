#!/usr/bin/env python3
"""Exact finite verification for the full cube-automorphism homology character.

Requires only Python 3 standard library. All graphs and actions are rebuilt from
four-bit vectors; chain complexes use the augmented empty-face convention.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

N=16
ADJ=[sum(1<<(v^(1<<i)) for i in range(4)) for v in range(N)]
PERMS=list(permutations(range(4)))
IDENTITY=tuple(range(4))


def parity(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))


def independent_faces():
    good=[False]*(1<<N)
    good[0]=True
    faces=[]
    for s in range(1,1<<N):
        b=s&-s;v=b.bit_length()-1;p=s^b
        good[s]=good[p] and not (p&ADJ[v])
        if good[s]:faces.append(s)
    return faces


def matching_dag(faces):
    faceset=set(faces)
    unmatched=set(faces)
    pairs=[];by_pivot=[]
    for v in range(N):
        bit=1<<v
        selected=[]
        # Iteration order fixed for reproducibility; pairs are vertex-disjoint.
        for s in faces:
            if s in unmatched and not s&bit and s|bit in unmatched:
                selected.append((s,s|bit))
        for lo,hi in selected:
            assert lo in unmatched and hi in unmatched
            unmatched.remove(lo);unmatched.remove(hi)
        pairs.extend(selected);by_pivot.append(len(selected))
    matched=set(pairs)
    # Reverse matched incidences in the downward Hasse diagram.
    indeg={s:0 for s in faces}
    outgoing={s:[] for s in faces}
    edges=0
    for s in faces:
        t=s
        while t:
            b=t&-t;t-=b;lo=s^b
            if lo not in faceset:continue
            if (lo,s) in matched:
                a,z=lo,s
            else:
                a,z=s,lo
            outgoing[a].append(z);indeg[z]+=1;edges+=1
    q=deque(s for s in faces if indeg[s]==0)
    count=0
    while q:
        s=q.popleft();count+=1
        for t in outgoing[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    critical=Counter(s.bit_count()-1 for s in unmatched)
    assert count==len(faces), (count,len(faces))
    return by_pivot, critical, edges, count


def act(v,t,p):
    out=t
    for i in range(4):
        if v>>i&1:out^=1<<p[i]
    return out


def fixed_orbit_independence_polynomial(t,p):
    action=[act(v,t,p) for v in range(16)]
    marked=set();orbits=[]
    for v in range(16):
        if v not in marked:
            o=[];x=v
            while x not in marked:
                marked.add(x);o.append(x);x=action[x]
            assert x==v
            orbits.append(sum(1<<z for z in o))
    valid=[]
    for o in orbits:
        if all(not (ADJ[v]&(o^(1<<v))) for v in range(16) if o>>v&1):
            valid.append(o)
    links=[]
    for i,o in enumerate(valid):
        mask=0
        for j,r in enumerate(valid):
            if i!=j and any(ADJ[v]&r for v in range(16) if o>>v&1):
                mask|=1<<j
        links.append(mask)
    cache={0:1}
    def z(s):
        if s in cache:return cache[s]
        bit=s&-s;k=bit.bit_length()-1
        # Independent-set alternating sum P(-1)=P(delete)-P(delete closed neighborhood)
        cache[s]=z(s^bit)-z(s&~(bit|links[k]))
        return cache[s]
    return z((1<<len(valid))-1)


def weight3_character(t,p):
    val=0
    for u in range(16):
        if u.bit_count()!=3:continue
        support=[i for i in range(4) if u>>i&1]
        if sorted(p[i] for i in support)!=support:continue
        reindexed=[support.index(p[i]) for i in support]
        val+=parity(reindexed)*(-1 if (u&t).bit_count()%2 else 1)
    return val


def signed_simplicial_character(faces,t,p):
    """Independent signed simplicial fixed-face Lefschetz evaluation."""
    action=[act(v,t,p) for v in range(16)]
    acc=1   # negative reduced empty-face contribution
    for face in faces:
        ids=[v for v in range(16) if face>>v&1]
        images=[action[v] for v in ids]
        if sum(1<<v for v in images)!=face:continue
        sign=parity(images)
        acc+=((-1)**len(ids))*sign
    return acc


def predicted_character(t,p):
    return parity(p)*(sum(p[i]==i for i in range(4))-1)+weight3_character(t,p)


def run():
    faces=independent_faces()
    profile=Counter(s.bit_count() for s in faces)
    assert [profile[i] for i in range(1,9)]==[16,88,208,228,128,56,16,2]
    counts, critical, incidences, visited=matching_dag(faces)
    assert counts==[176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1],counts
    assert len(faces)==742 and sum(counts)==367
    assert critical==Counter({0:1,3:7}),critical
    assert incidences==2816 and visited==742
    # The acyclic Morse matching has one critical 0-cell and seven 3-cells;
    # the Morse CW complex is thus a wedge of seven 3-spheres over Z.
    characters={}
    for p in PERMS:
        for t in range(16):
            obtained=fixed_orbit_independence_polynomial(t,p)
            expected=predicted_character(t,p)
            assert obtained==expected,(t,p,obtained,expected)
            direct=signed_simplicial_character(faces,t,p)
            assert direct==obtained,(t,p,direct,obtained)
            characters[t,p]=obtained
    assert len(characters)==384 and Counter(characters.values())==Counter({1:188,-1:161,-3:24,3:6,5:4,7:1})
    Fourier={}
    for u in range(16):
        v=sum(((-1 if (t&u).bit_count()%2 else 1)*characters[t,IDENTITY]) for t in range(16))
        assert v%16==0
        Fourier[u]=v//16
    assert Fourier=={u:(3 if u==0 else 1 if u.bit_count()==3 else 0) for u in range(16)}
    def fixed_component(u,p):
        s=sum(((-1 if (t&u).bit_count()%2 else 1)*characters[t,p]) for t in range(16))
        assert s%16==0
        return s//16
    for p in PERMS:
        assert fixed_component(0,p)==parity(p)*(sum(p[i]==i for i in range(4))-1)
        for u in [7,11,13,14]:
            expected=0
            support=[i for i in range(4) if u>>i&1]
            if sorted(p[i] for i in support)==support:
                expected=parity([support.index(p[i]) for i in support])
            assert fixed_component(u,p)==expected,(u,p,fixed_component(u,p),expected)
    assert sum(characters.values())==0
    print('VERIFY_OK vertices=16 faces=742 matching_pairs=367 critical=1x0+7x3 acyclic_incidences=2816 group=384 rank_H3=7 translation=3+4 all_character_checks=384 globally_fixed=0')

if __name__=='__main__':run()
