#!/usr/bin/env python3
"""Exact standalone certificate checker for an icosahedral graph filtration.

Run `python3 VERIFY.py` to replay every assertion, or `python3 VERIFY.py
--generate` to reconstruct the accompanying certificate. Standard library only.
"""
import collections
import itertools
import json
import pathlib
import sys

# Vertices 0,11 are poles. Vertices 1..5 and 6..10 form two rings.
N = 12
edge_set = set()
for i in range(5):
    for a,b in (
        (0,1+i),(11,6+i),(1+i,1+(i+1)%5),
        (6+i,6+(i+1)%5),(1+i,6+i),(1+i,6+(i-1)%5)
    ):
        edge_set.add(tuple(sorted((a,b))))
EDGES = sorted(edge_set)
ADJ = [sum(1 << (b if a == v else a) for a,b in EDGES if v in (a,b))
       for v in range(N)]
EXPECTED_F = [
    [1,12,36,20],
    [1,12,66,140,105],
    [1,12,66,200,345,300,60],
]
EXPECTED_CRITICAL = [
    {0:1,1:7,2:2},
    {0:1,2:4,3:24},
    {0:1,4:40},
]
EXPECTED_BETTI = [
    {1:6,2:1},
    {3:20},
    {4:40},
]

def allowed_union_find(mask, degree_limit):
    for v in range(N):
        if mask & (1 << v) and (ADJ[v] & mask).bit_count() > degree_limit:
            return False
    parent = list(range(N))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for a,b in EDGES:
        if mask & (1<<a) and mask & (1<<b):
            aa, bb = root(a), root(b)
            if aa == bb:
                return False
            parent[aa] = bb
    return True


def allowed_dfs(mask, degree_limit):
    seen = set()
    for v in range(N):
        if mask & (1<<v) and (ADJ[v] & mask).bit_count() > degree_limit:
            return False
    def visit(v, parent):
        seen.add(v)
        for w in range(N):
            if w == parent or not ((mask & (1<<w)) and (ADJ[v] & (1<<w))):
                continue
            if w in seen or not visit(w,v):
                return False
        return True
    for v in range(N):
        if mask & (1<<v) and v not in seen and not visit(v,-1):
            return False
    return True


def faces(d):
    return {mask for mask in range(1 << N) if allowed_union_find(mask,d)}


def fvector(faces_):
    c=collections.Counter(m.bit_count() for m in faces_)
    return [c[i] for i in range(max(c)+1)]


def pairing(faces_):
    remaining=set(faces_)
    matches=[]
    for v in range(N):
        for lo in sorted(remaining):
            hi=lo|(1<<v)
            if hi!=lo and hi in remaining:
                remaining.remove(lo)
                remaining.remove(hi)
                matches.append((lo,hi))
    return matches,remaining


def hasse_dag_check(faces_, matches):
    # Original unmatched cover arrows go DOWN, reversed matched arrows go UP.
    match_set=set(matches)
    indeg={m:0 for m in faces_}
    succ={m:[] for m in faces_}
    num_covers=0
    for hi in faces_:
        for v in range(N):
            if not hi & (1<<v):
                continue
            lo=hi^(1<<v)
            if lo not in faces_:
                continue
            num_covers+=1
            src,dst=(lo,hi) if (lo,hi) in match_set else (hi,lo)
            succ[src].append(dst)
            indeg[dst]+=1
    queue=collections.deque(m for m in faces_ if indeg[m]==0)
    count=0
    while queue:
        m=queue.popleft()
        count+=1
        for x in succ[m]:
            indeg[x]-=1
            if indeg[x]==0:
                queue.append(x)
    assert count==len(faces_), ('cyclic Morse matching',count,len(faces_))
    return num_covers


def signed_boundary(mask, universe):
    vertices=[v for v in range(N) if mask & (1<<v)]
    return {mask^(1<<v): (-1 if i%2 else 1)
            for i,v in enumerate(vertices) if mask^(1<<v) in universe}


def morse_boundary(faces_, matches):
    # Exact elementary unimodular chain contractions, no field divisions.
    living=set(faces_)
    bd={m:signed_boundary(m,living) for m in living}
    for lo,hi in matches:
        assert lo in living and hi in living
        pivot=bd[hi].get(lo,0)
        assert abs(pivot)==1, ('nonunit cancellation',lo,hi,pivot)
        for x in list(living):
            if x==hi: continue
            a=bd[x].get(lo,0)
            if a:
                assert x.bit_count()==hi.bit_count()
                for y,b in bd[hi].items():
                    if y==lo: continue
                    c=bd[x].get(y,0)-a*pivot*b
                    if c:
                        bd[x][y]=c
                    else:
                        bd[x].pop(y,None)
                bd[x].pop(lo,None)
        living.remove(lo)
        living.remove(hi)
        del bd[lo]
        del bd[hi]
        for x in living:
            bd[x].pop(hi,None)
    assert set(bd)==living
    for m in living:
        for y,a in bd[m].items():
            assert y in living and y.bit_count()+1==m.bit_count()
        dd=collections.defaultdict(int)
        for y,a in bd[m].items():
            for z,b in bd[y].items():
                dd[z]+=a*b
        assert all(x==0 for x in dd.values())
    return bd


def mod2_betti(faces_):
    by_size=collections.defaultdict(list)
    for m in faces_:
        if m: by_size[m.bit_count()].append(m)
    rank={}
    for size in sorted(by_size):
        lower=sorted(by_size.get(size-1,[]))
        row={m:i for i,m in enumerate(lower)}
        pivots={}
        for hi in by_size[size]:
            col=0
            for lo in signed_boundary(hi,faces_):
                if lo in row:
                    col^=1<<row[lo]
            while col:
                k=col.bit_length()-1
                if k in pivots: col^=pivots[k]
                else:
                    pivots[k]=col
                    break
        rank[size]=len(pivots)
    result={}
    for size in sorted(by_size):
        dim=size-1
        beta=len(by_size[size])-rank.get(size,0)-rank.get(size+1,0)
        if dim==0: beta-=1  # all stages are connected
        if beta: result[dim]=beta
    return result


def describe(faces_, matches):
    assert len(faces_)>0
    incident_count=hasse_dag_check(faces_,matches)
    bd=morse_boundary(faces_,matches)
    unmatched=sorted(set(faces_)-{x for p in matches for x in p})
    assert len(bd)==len(unmatched)
    assert set(unmatched)==set(bd)
    return {
        'pair_count':len(matches),
        'cover_count':incident_count,
        'pairs':[[lo,hi] for lo,hi in matches],
        'critical':unmatched,
        'critical_by_dimension':{
            str(k):v for k,v in sorted(collections.Counter(m.bit_count()-1 for m in unmatched).items())},
        'morse_differential':{str(x):{str(y):a for y,a in sorted(bd[x].items())}
                              for x in unmatched if bd[x]},
    }




def determinant(a):
    n=len(a)
    total=0
    for p in itertools.permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=(-1 if inversions%2 else 1)
        for i in range(n): term*=a[i][p[i]]
        total+=term
    return total


def sphere_core_test(F0):
    # Independent triples form a closed surface; all remaining edges are chords.
    triangles=[m for m in F0 if m.bit_count()==3]
    edges=[m for m in F0 if m.bit_count()==2]
    incidence=collections.Counter()
    for tri in triangles:
        for v in range(N):
            if tri & (1<<v):incidence[tri^(1<<v)]+=1
    assert len(triangles)==20 and len(incidence)==30
    assert set(incidence.values())=={2}
    # Each vertex link in the two-dimensional core is a single 5-cycle.
    for v in range(N):
        neighbors={w for w in range(N) if (1<<v)|(1<<w) in incidence}
        assert len(neighbors)==5
        link_edges=[]
        for tri in triangles:
            if tri & (1<<v):
                a,b=[w for w in range(N) if tri & (1<<w) and w!=v]
                link_edges.append((a,b))
        degree=collections.Counter(w for a,b in link_edges for w in (a,b))
        assert len(link_edges)==5 and set(degree)==neighbors
        assert set(degree.values())=={2}
        start=next(iter(neighbors))
        seen={start}
        todo=[start]
        while todo:
            u=todo.pop()
            for a,b in link_edges:
                w=b if a==u else (a if b==u else None)
                if w is not None and w not in seen:
                    seen.add(w)
                    todo.append(w)
        assert seen==neighbors
    # The closed connected surface has chi=12-30+20=2, hence is S^2.
    core_edges=set(incidence)
    core_graph={v:set() for v in range(N)}
    for edge in core_edges:
        a,b=[v for v in range(N) if edge & (1<<v)]
        core_graph[a].add(b);core_graph[b].add(a)
    reached={0};stack=[0]
    while stack:
        for w in core_graph[stack.pop()]:
            if w not in reached:reached.add(w);stack.append(w)
    assert len(reached)==N and N-len(core_edges)+len(triangles)==2
    extra=sorted(set(edges)-core_edges)
    assert len(extra)==6
    assert collections.Counter(v for e in extra for v in range(N) if e & (1<<v))==collections.Counter({v:1 for v in range(N)})
    return {'triangles':20,'surface_edges':30,'surface_vertices':12,
            'surface_euler':2,'extra_edges':extra}


def build_certificate():
    assert len(EDGES)==30 and all(a.bit_count()==5 for a in ADJ)
    # Neighbor sets each induce a five-cycle: any forest subset has degree <=2.
    for v in range(N):
        ns={w for w in range(N) if ADJ[v] & (1<<w)}
        assert len(ns)==5
        assert all((ADJ[w] & ADJ[v]).bit_count()==2 for w in ns)
        seen={next(iter(ns))};stack=list(seen)
        while stack:
            w=stack.pop()
            for u in ns:
                if (ADJ[w] & (1<<u)) and u not in seen:
                    seen.add(u);stack.append(u)
        assert seen==ns
    assert all(allowed_union_find(m,d)==allowed_dfs(m,d)
               for d in range(3) for m in range(1<<N))
    F=[faces(d) for d in range(3)]
    assert F[0]<=F[1]<=F[2]
    assert all(faces(d)==F[2] for d in range(3,6))
    cert={'edges':[list(e) for e in EDGES], 'levels':{},
          'zero_stage_surface':sphere_core_test(F[0])}
    for d in range(3):
        assert fvector(F[d])==EXPECTED_F[d]
        pairs,critical=pairing(F[d]-{0})
        data=describe(F[d]-{0},pairs)
        data['f_vector_including_empty']=fvector(F[d])
        assert {int(k):v for k,v in data['critical_by_dimension'].items()}==EXPECTED_CRITICAL[d]
        assert mod2_betti(F[d])==EXPECTED_BETTI[d]
        cert['levels'][str(d)]=data
    assert cert['levels']['0']['morse_differential']=={
        '352':{'260':-1},'1168':{'260':-1}}
    assert cert['levels']['2']['morse_differential']=={}
    stage1=cert['levels']['1']
    critical_two=[m for m in stage1['critical'] if m.bit_count()==3]
    assert critical_two==[100,146,164,1042]
    selected=[616,680,720,1112]
    assert all(m in stage1['critical'] for m in selected)
    delta=stage1['morse_differential']
    a=[[delta.get(str(u),{}).get(str(v),0) for u in selected]
       for v in critical_two]
    det=determinant(a)
    assert abs(det)==1
    cert['stage_one_unimodular_minor']={'rows':critical_two,
                  'columns':selected,'matrix':a,'determinant':det}
    return cert


def main():
    here=pathlib.Path(__file__).resolve().parent
    result=build_certificate()
    path=here/'CERTIFICATE.json'
    if sys.argv[1:]==['--generate']:
        path.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
        print('CERTIFICATE_GENERATED',path.stat().st_size)
        return
    assert not sys.argv[1:], 'Use no arguments or --generate'
    provided=json.loads(path.read_text(encoding='utf-8'))
    assert provided==result
    for d in range(3):
        p=result['levels'][str(d)]
        print('STAGE',d,'faces',sum(p['f_vector_including_empty']),
              'pairs',p['pair_count'],'critical',p['critical_by_dimension'],
              'hasse_covers',p['cover_count'])
    print('STAGE_ONE_UNIT_MINOR',result['stage_one_unimodular_minor']['determinant'])
    print('STAGE_ZERO_CORE',result['zero_stage_surface'])
    print('VERIFIED_ICOSAHEDRAL_FOREST_FILTRATION')


if __name__=='__main__':
    main()
