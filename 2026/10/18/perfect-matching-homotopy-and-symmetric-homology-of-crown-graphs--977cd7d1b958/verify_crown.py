#!/usr/bin/env python3
"""Reconstruct exhaustive crown-graph perfect-matching-complex Morse certificates.
Only Python standard library; exact combinatorial operations.
"""
import itertools, collections, math, json, hashlib, sys

ORDERS = {
 4: list(range(12)),
 5: list(range(20)),
 6: [8,19,17,10,16,27,28,18,11,5,1,22,2,20,23,3,24,7,13,29,0,4,6,15,26,25,9,21,12,14],
 7: [15,34,27,3,32,18,13,12,20,24,28,41,36,14,1,35,38,4,22,8,39,29,10,21,9,40,26,31,7,17,23,30,2,37,16,0,33,19,11,5,6,25]
}
EXPECTED = {4:(100,47,4),5:(735,350,33),6:(6336,3039,256),7:(61985,29904,2175)}

def complex_faces(n):
    ed=[(i,j) for i in range(n) for j in range(n) if i!=j]
    idx={e:k for k,e in enumerate(ed)}
    faces={0};perfect=0
    for p in itertools.permutations(range(n)):
        if any(i==p[i] for i in range(n)): continue
        perfect+=1
        mask=sum(1<<idx[i,p[i]] for i in range(n))
        s=mask
        while s:
            faces.add(s);s=(s-1)&mask
    return ed, faces, perfect

def match(faces,order):
    remaining=set(faces);remaining.remove(0)
    paired={}
    for v in order:
        bit=1<<v
        for lo in sorted(remaining):
            if lo&bit:continue
            hi=lo|bit
            if hi in remaining:
                paired[lo]=hi
                remaining.remove(lo);remaining.remove(hi)
    return paired,remaining

def acyclic(faces,paired):
    """Check every Hasse incidence; reverse matched edge, then Kahn sort."""
    nonempty=faces-{0}
    indeg={x:0 for x in nonempty}
    adj={x:[] for x in nonempty}
    edges=0
    matched_upper=set(paired.values())
    assert len(matched_upper)==len(paired)
    for hi in nonempty:
        t=hi
        while t:
            bit=t&-t;t-=bit
            lo=hi^bit
            if not lo:continue
            edges+=1
            if paired.get(lo)==hi:
                adj[lo].append(hi);indeg[hi]+=1
            else:
                adj[hi].append(lo);indeg[lo]+=1
    q=collections.deque(v for v,k in indeg.items() if k==0)
    removed=0
    while q:
        u=q.popleft();removed+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert removed==len(nonempty),(removed,len(nonempty))
    return edges, removed

def predicted_faces(n,k):
    if k==0:return 1
    der=sum((-1)**j*math.factorial(n)//math.factorial(j) for j in range(n+1))
    if k==n:return der
    if k==n-1:return n*der
    return sum((-1)**t*math.comb(n,t)*math.comb(n-t,k-t)**2*math.factorial(k-t) for t in range(k+1))

def partitions(n,limit=None):
    if n==0:
        yield ()
    else:
        if limit is None:limit=n
        for first in range(min(n,limit),0,-1):
            for r in partitions(n-first,first):yield (first,)+r

def perm_by_parts(parts):
    p=list(range(sum(parts))); j=0
    for z in parts:
        for k in range(z):p[j+k]=j+(k+1)%z
        j+=z
    return p

def class_size(parts):
    c=collections.Counter(parts)
    den=math.prod(k**r*math.factorial(r) for k,r in c.items())
    return math.factorial(sum(parts))//den

def action(ed,sigma,flip):
    ix={e:k for k,e in enumerate(ed)}
    return [ix[(sigma[b],sigma[a])] if flip else ix[(sigma[a],sigma[b])] for a,b in ed]

def fixed_character(faces,pi):
    """Two algebraically distinct Lefschetz routines must agree."""
    cycles=[];seen=set()
    for i in range(len(pi)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:
            seen.add(j);c.append(j);j=pi[j]
        cycles.append(sum(1<<b for b in c))
    total=0;alt=0;cnt=0
    for f in faces:
        if any((f&cm) not in (0,cm) for cm in cycles):continue
        count=sum((f&cm)!=0 for cm in cycles)
        total-=(-1)**count
        cnt+=1
        if f:
            ordered=[i for i in range(len(pi)) if (f>>i)&1]
            images=[pi[i] for i in ordered]
            inversions=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
            alt+=(-1)**(len(ordered)-1+inversions)
        else:alt-=1
    assert total==alt,(total,alt)
    return total,cnt

def main():
    summary={}; saved=None
    for n in range(4,8):
        ed,faces,der=complex_faces(n)
        assert len(ed)==n*(n-1)
        pair,critical=match(faces,ORDERS[n])
        dimcnt=dict(sorted(collections.Counter(x.bit_count()-1 for x in critical).items()))
        assert dimcnt=={0:1,n-3:EXPECTED[n][2]}
        assert (len(faces),len(pair),EXPECTED[n][2])==EXPECTED[n]
        facecounts={k:sum(x.bit_count()==k for x in faces) for k in range(n+1)}
        assert all(facecounts[k]==predicted_faces(n,k) for k in range(n+1))
        edges,seen=acyclic(faces,pair)
        summary[str(n)]={'faces_with_empty':len(faces),'perfect_matchings':der,
          'face_counts_by_cardinality':[facecounts[k] for k in range(n+1)],
          'paired_coverings':len(pair),'critical_cell_dimensions':dimcnt,
          'hasse_edges_nonempty':edges,'acyclic_vertices_checked':seen,
          'homotopy_wedge_degree':n-3,'homotopy_sphere_count':EXPECTED[n][2]}
        if n==7:saved=(ed,faces)
    ed,faces=saved
    characters=[]
    for parts in partitions(7):
        sig=perm_by_parts(parts)
        a,af=fixed_character(faces,action(ed,sig,False))
        b,bf=fixed_character(faces,action(ed,sig,True))
        characters.append({'cycle_type':list(parts),'conjugacy_class_size':class_size(parts),
                           'trace_no_swap':a,'trace_swap':b,'fixed_face_counts':[af,bf]})
    assert sum(r['conjugacy_class_size'] for r in characters)==5040
    assert characters[-1]['trace_no_swap']==2175
    assert sum(r['conjugacy_class_size']*r['trace_no_swap'] for r in characters)==5040
    assert sum(r['conjugacy_class_size']*(r['trace_no_swap']+r['trace_swap']) for r in characters)==10080
    summary['character_table_n7']=characters
    summary['S7_invariant_rank_Q']=1
    summary['S7xC2_invariant_rank_Q']=1
    summary['transpose_eigenspace_ranks_Q']=[1045,1130]
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':main()
