#!/usr/bin/env python3
"""Exact integral homotopy certificate for the Desargues higher-independence complex.

Python 3 standard library only. Every potential vertex subset is tested;
integer signs and discrete-Morse incidences are independently reconstructed.
"""
from collections import Counter, defaultdict, deque

N = 20

def graph():
    a = [0] * N
    for i in range(10):
        for u,v in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)):
            a[u] |= 1 << v
            a[v] |= 1 << u
    assert all(x.bit_count() == 3 for x in a)
    assert sum(x.bit_count() for x in a)//2 == 30
    return a

def local_test(mask, adj):
    x=mask
    while x:
        b=x & -x
        u=b.bit_length()-1
        if (adj[u] & mask).bit_count()>1:
            return False
        x-=b
    return True

def component_test(mask, adj):
    left=mask
    while left:
        b=left & -left
        left-=b
        front=b
        count=1
        while front:
            v=(front & -front).bit_length()-1
            front &= front-1
            new=adj[v] & left
            count+=new.bit_count()
            if count>2:
                return False
            left ^= new
            front |= new
    return True

def boundary(mask):
    x=mask
    i=0
    while x:
        b=x & -x
        yield mask^b, (-1 if i & 1 else 1)
        x-=b
        i+=1

def binary_rank(columns):
    pivot={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p not in pivot:
                pivot[p]=col
                break
            col ^= pivot[p]
    return len(pivot)

def main():
    adj=graph()
    faces=set()
    for mask in range(1 << N):
        q=local_test(mask,adj)
        assert q==component_test(mask,adj), ('membership mismatch',mask)
        if q:
            faces.add(mask)
    assert len(faces)==62049 and 0 in faces
    bydim=defaultdict(list)
    for m in faces:
        if m:
            bydim[m.bit_count()-1].append(m)
    expected=(20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5)
    assert tuple(len(bydim[d]) for d in range(12))==expected
    assert not bydim[12]
    facets=Counter()
    for m in faces:
        if m and not any((m|(1<<v)) in faces for v in range(N) if not m>>v&1):
            facets[m.bit_count()]+=1
    assert dict(facets)=={8:65,9:540,10:234,12:5},facets
    unmatched=faces-{0}
    pairs=[]
    for v in range(N):
        bit=1<<v
        for m in list(unmatched):
            if not (m&bit) and m|bit in unmatched:
                unmatched.remove(m)
                unmatched.remove(m|bit)
                pairs.append((m,m|bit))
    assert len(pairs)==31000 and 2*len(pairs)+len(unmatched)==len(faces)-1
    critical=sorted(unmatched,key=lambda m:(m.bit_count(),m))
    assert Counter(m.bit_count()-1 for m in critical)=={0:1,6:3,7:44}
    critical6=[m for m in critical if m.bit_count()==7]
    critical7=[m for m in critical if m.bit_count()==8]
    assert critical6==[0x10b54,0x22a52,0x2a24a]
    matched_up=dict(pairs)
    succ=defaultdict(list)
    indegree=Counter()
    incidences=0
    for m in faces:
        if not m:
            continue
        for face,_ in boundary(m):
            if face==0:
                continue
            if matched_up.get(face)==m:
                a,b=face,m
            else:
                a,b=m,face
            succ[a].append(b)
            indegree[b]+=1
            incidences+=1
    assert incidences==400760
    queue=deque(m for m in faces if m and indegree[m]==0)
    visited=0
    while queue:
        m=queue.popleft();visited+=1
        for v in succ[m]:
            indegree[v]-=1
            if indegree[v]==0:
                queue.append(v)
    assert visited==len(faces)-1, 'Nonacyclic gradient matching'
    # Integral Morse differential in dimensions 7 -> 6.
    # Eliminate matched (6,7)-cell pairs through unit-pivot signed boundary substitutions.
    lower6={m:u for m,u in pairs if m.bit_count()==7}
    assert len(lower6)==7395
    columns={}
    for c7 in critical7:
        acc=defaultdict(int)
        for f,s in boundary(c7):
            acc[f]+=s
        steps=0
        while True:
            candidate=next((f for f,s in acc.items() if s and f in lower6),None)
            if candidate is None:
                break
            upper=lower6[candidate]
            bnd=dict(boundary(upper))
            coefficient=acc[candidate]*bnd[candidate]
            for f,s in bnd.items():
                acc[f]-=coefficient*s
            steps+=1
            assert steps<20000
        assert all(s==0 or f in critical6 or f not in lower6 for f,s in acc.items())
        columns[c7]=tuple(acc[f] for f in critical6)
    assert columns[0x18e94]==(1,0,0)
    assert columns[0x55292]==(0,0,1)
    assert columns[0x61664]==(0,1,0)
    # Three minor columns form a determinant -1; thus boundary is split surjective.
    # For an additional independent check, compute direct mod-2 simplicial ranks.
    wanted={5:6708,6:9202,7:7398,8:2951,9:509}
    for degree,expected_rank in wanted.items():
        rows={f:i for i,f in enumerate(bydim[degree-1])}
        def columns_for_degree():
            for m in bydim[degree]:
                col=0
                for f,_ in boundary(m):
                    col ^= 1 << rows[f]
                yield col
        assert binary_rank(columns_for_degree())==expected_rank,degree
    assert len(bydim[7])-wanted[7]-wanted[8]==41
    assert len(bydim[6])-wanted[6]-wanted[7]==0
    print('DESARGUES_IND2_INTEGRAL_HOMOTOPY_VERIFIED')
    print('faces',len(faces)-1,'morse_pairs',len(pairs),'critical_6',len(critical6),
          'critical_7',len(critical7),'incidences',incidences,'three_unit_minor',-1,
          'mod2_Betti7',41)

if __name__=='__main__':
    main()
