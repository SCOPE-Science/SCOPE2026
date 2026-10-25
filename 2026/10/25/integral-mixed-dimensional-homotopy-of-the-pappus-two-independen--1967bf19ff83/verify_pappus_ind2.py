#!/usr/bin/env python3
"""Exact reproducible finite certificate for the Pappus-graph 2-independence complex.
Requires Python 3.10+, standard library only.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256

N = 18
# Hamiltonian cyclic presentation of the Pappus graph.
CHORDS = [(0,5),(1,8),(2,13),(3,10),(4,15),(6,11),(7,14),(9,16),(12,17)]
EDGES = sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} | set(CHORDS))


def make_graph():
    adj = [set() for _ in range(N)]
    for u,v in EDGES:
        adj[u].add(v)
        adj[v].add(u)
    assert len(EDGES)==27 and all(len(a)==3 for a in adj)
    return adj


def forbid_triples(adj):
    out=set()
    for v in range(N):
        ns=sorted(adj[v])
        for i in range(len(ns)):
            for w in ns[i+1:]:
                out.add((1<<v)|(1<<ns[i])|(1<<w))
    return sorted(out)


def enumeration(adj, triples):
    M=1<<N
    faces=bytearray(M)
    faces[0]=1
    mask_ne=[sum(1<<u for u in adj[v]) for v in range(N)]
    found=[]
    for x in range(1,M):
        z=x&-x; v=z.bit_length()-1; y=x^z
        if not faces[y]: continue
        # Adding v is legal precisely if there is no induced connected triple containing v.
        if (mask_ne[v]&y).bit_count()>1:continue
        if any((y & mask_ne[u] &~z) for u in adj[v] if y & (1<<u)):continue
        faces[x]=1
        found.append(x)
    # Independent proof of the face predicate via induced-component BFS, for ALL 262144 subsets.
    for x in range(M):
        remaining=x
        all_small=True
        while remaining and all_small:
            v=(remaining&-remaining).bit_length()-1
            visited=1<<v
            frontier=[v]
            while frontier:
                u=frontier.pop()
                for w in adj[u]:
                    bit=1<<w
                    if x&bit and not visited&bit:
                        visited |= bit
                        frontier.append(w)
            if visited.bit_count()>2:
                all_small=False
            remaining &=~visited
        if bool(faces[x])!=all_small:
            raise AssertionError(('face predicate mismatch',x))
    assert len(found)==20651 and len(triples)==54
    assert sum(faces)==20652
    return faces,found


def match(faces, ordered_faces):
    active=bytearray(faces)
    matched_lower={}
    upper_partner={}
    for v in range(N):
        bit=1<<v
        for x in ordered_faces:
            if x&bit or not active[x]:continue
            y=x|bit
            if faces[y] and active[y]:
                active[x]=active[y]=0
                matched_lower[x]=y
                upper_partner[y]=x
    critical=[x for x in ordered_faces if active[x]]
    assert len(critical)==11 and len(matched_lower)==10320
    assert Counter(x.bit_count()-1 for x in critical)=={0:1,5:9,6:1}
    return critical,matched_lower,upper_partner


def acyclicity(ordered_faces,matched_lower):
    # Check ALL oriented face incidences, independently of the matching construction.
    M=1<<N
    in_complex=bytearray(M)
    for x in ordered_faces:in_complex[x]=1
    indegree=[0]*M
    outs=[[] for _ in range(M)]
    relations=0
    for upper in ordered_faces:
        for j in range(N):
            bit=1<<j
            if not upper&bit: continue
            lower=upper^bit
            if not lower:continue
            assert in_complex[lower]
            if matched_lower.get(lower)==upper:
                tail,head=lower,upper
            else:
                tail,head=upper,lower
            outs[tail].append(head)
            indegree[head]+=1
            relations+=1
    queue=deque(x for x in ordered_faces if indegree[x]==0)
    done=0
    while queue:
        x=queue.popleft()
        done+=1
        for y in outs[x]:
            indegree[y]-=1
            if indegree[y]==0:queue.append(y)
    assert done==len(ordered_faces),('directed cycle',done,len(ordered_faces))
    assert relations==sum(x.bit_count() for x in ordered_faces)-N
    return relations


def morse_boundary(critical,matched_lower):
    c5=[x for x in critical if x.bit_count()==6]
    c6=[x for x in critical if x.bit_count()==7]
    assert len(c5)==9 and len(c6)==1
    ids={x:i for i,x in enumerate(c5)}
    @lru_cache(None)
    def reduced(face):
        if face in ids:return {ids[face]:1}
        upper=matched_lower.get(face)
        if upper is None:return {}
        # Unit coefficient of face in boundary(upper), with ascending vertex orientation.
        bits=[j for j in range(N) if upper&(1<<j)]
        dropped=(upper^face).bit_length()-1
        pivot=(-1)**bits.index(dropped)
        a=defaultdict(int)
        for j,v in enumerate(bits):
            if v==dropped:continue
            for k,z in reduced(upper^(1<<v)).items():
                a[k]-=pivot*((-1)**j)*z
        return {k:z for k,z in a.items() if z}
    vector=[0]*len(c5)
    for j,v in enumerate(i for i in range(N) if c6[0]&(1<<i)):
        for k,z in reduced(c6[0]^(1<<v)).items():
            vector[k]+=(-1)**j*z
    assert vector==[0]*9,('nonzero signed Morse boundary',vector)
    return c5,c6,vector,reduced.cache_info().currsize


def main():
    adj=make_graph()
    triples=forbid_triples(adj)
    faces,found=enumeration(adj,triples)
    c,l,u=match(faces,found)
    relation_count=acyclicity(found,l)
    c5,c6,vector,cache=morse_boundary(c,l)
    fv=Counter(x.bit_count()-1 for x in found)
    assert fv=={0:18,1:153,2:762,3:2394,4:4806,5:6027,6:4428,7:1728,8:308,9:27}
    assert c==[1,13104,26146,39186,52230,74340,100486,135576,148618,183554,196812]
    assert relation_count==sum((d+1)*count for d,count in fv.items())-18
    print('EDGES',len(EDGES),'PATH_TRIPLES',len(triples),'SUBSETS',1<<N)
    print('F_VECTOR',sorted(fv.items()))
    print('FACES',len(found),'MATCHING_PAIRS',len(l),'RELATIONS',relation_count)
    print('CRITICAL',[(hex(x),x.bit_count()-1) for x in c])
    print('SIGNED_MORSE_BOUNDARY',vector,'REDUCTION_CACHE',cache)
    print('VERIFY_OK')
if __name__=='__main__':main()
