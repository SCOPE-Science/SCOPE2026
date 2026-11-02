"""Exhaustive recurrence certificate for three-state excitation on G(5,1) and G(5,2)."""
import itertools, json, hashlib, struct
from collections import Counter, defaultdict, deque
from pathlib import Path

P=[3**i for i in range(10)]
N=3**10

def make_graph(k):
    neigh=[set() for _ in range(10)]
    def edge(i,j):
        assert i!=j;neigh[i].add(j);neigh[j].add(i)
    for i in range(5):
        edge(i,(i+1)%5)
        edge(5+i,5+((i+k)%5))
        edge(i,5+i)
    assert all(len(t)==3 for t in neigh)
    assert sum(map(len,neigh))==30
    return [tuple(sorted(x)) for x in neigh]

def evolve(s,neigh):
    colors=[(s//p)%3 for p in P]
    out=0
    for i,x in enumerate(colors):
        if x==0:
            z=int(any(colors[j]==1 for j in neigh[i]))
        elif x==1: z=2
        else: z=0
        out+=z*P[i]
    return out

def evaluate(k):
    neigh=make_graph(k)
    nxt=[evolve(s,neigh) for s in range(N)]
    deg=[0]*N
    for y in nxt:deg[y]+=1
    remaining=[True]*N
    q=deque(i for i,v in enumerate(deg) if v==0)
    peeled=[]
    while q:
        x=q.popleft(); assert remaining[x];remaining[x]=False;peeled.append(x)
        y=nxt[x];deg[y]-=1
        if deg[y]==0:q.append(y)
    period=[0]*N;distance=[-1]*N;orbitid=[-1]*N;cycles=defaultdict(list)
    for s in range(N):
        if not remaining[s] or distance[s]>=0:continue
        v=s;orbit=[]
        while distance[v]<0:
            distance[v]=0;orbit.append(v);v=nxt[v]
        assert v==s
        l=len(orbit);identity=len(cycles[l]);cycles[l].append(orbit)
        for c in orbit:
            period[c]=l;orbitid[c]=(l,identity)
    for x in reversed(peeled):
        y=nxt[x]
        distance[x]=distance[y]+1
        period[x]=period[y]
        orbitid[x]=orbitid[y]
    assert all(d>=0 for d in distance)
    assert all(p>0 for p in period)
    total_cycle=Counter({l:len(c) for l,c in cycles.items()})
    basin=Counter(period)
    first_entry=Counter((distance[i],period[i]) for i in range(N))
    max_entry=max(distance)
    assert sum(l*cnt for l,cnt in total_cycle.items())==sum(1 for d in distance if d==0)
    assert sum(basin.values())==N
    assert sum(first_entry.values())==N
    assert all(nxt[x]==x for x in cycles[1][0])
    # Exhaustive adjacency-preserving bijections; no external graph library.
    order=[0]
    for u in order:
        for v in neigh[u]:
            if v not in order: order.append(v)
    assert len(order)==10
    mapped={};used=set();perms=[]
    def backtrack(j):
        if j==10:
            perms.append(tuple(mapped[i] for i in range(10)))
            return
        u=order[j]
        for v in range(10):
            if v in used: continue
            if any(((a in neigh[u]) != (b in neigh[v])) for a,b in mapped.items()): continue
            mapped[u]=v;used.add(v)
            backtrack(j+1)
            used.remove(v);del mapped[u]
    backtrack(0)
    assert all(all(((j in neigh[i]) == (perm[j] in neigh[perm[i]])) for i in range(10) for j in range(10)) for perm in perms)
    assert len(set(perms))==len(perms)
    orbit_key={min(o): (l,i) for l,li in cycles.items() for i,o in enumerate(li)}
    geom={}
    for l,items in sorted(cycles.items()):
        unseen=set(range(len(items)));class_sizes=[]
        while unseen:
            idx=min(unseen);orb=items[idx]
            images=set()
            for perm in perms:
                # time-orbit representative can be any phase
                shifted=[]
                for s in orb:
                    sp=sum(((s//P[i])%3)*P[perm[i]] for i in range(10))
                    shifted.append(sp)
                images.add(orbit_key[min(shifted)][1])
            assert len(images)>0
            unseen-=images
            class_sizes.append(len(images))
        assert sum(class_sizes)==len(items)
        geom[str(l)]=sorted(class_sizes)
    cert=Path(__file__).with_name(f"transition_gp5{k}.bin")
    regenerated=struct.pack("<"+"I"*N,*nxt)
    if cert.exists():
        assert cert.read_bytes()==regenerated, "transition table mismatch"
    else: cert.write_bytes(regenerated)
    assert len(cert.read_bytes())==4*N
    assert hashlib.sha256(cert.read_bytes()).hexdigest()==hashlib.sha256(b"".join(v.to_bytes(4,"little") for v in nxt)).hexdigest()
    least_witness=min(i for i,d in enumerate(distance) if d==max_entry)
    assert distance[least_witness]==max_entry
    witness=[least_witness]
    while distance[witness[-1]]>0:
        witness.append(nxt[witness[-1]])
    assert len(witness)==max_entry+1
    exception=7 if k==1 else 8
    exceptional_orbit=min(cycles[exception],key=lambda orb:min(orb))
    q=min(exceptional_orbit)
    exceptional_trace=[q]
    for j in range(exception):
        exceptional_trace.append(nxt[exceptional_trace[-1]])
    assert exceptional_trace[-1]==q and len(set(exceptional_trace[:-1]))==exception
    result={
      'sharp_entry_witness':{'initial_state':least_witness,'state_trace_to_first_periodic':witness,'eventual_period':period[least_witness]},
      'exceptional_cycle_witness':{'primitive_period':exception,'state_trace':exceptional_trace},
      'graph':f'GP(5,{k})','num_vertices':10,'num_edges':15,'state_count':N,
      'automorphisms':len(perms),
      'primitive_orbits':dict(sorted(total_cycle.items())),
      'basin_by_primitive_period':dict(sorted(basin.items())),
      'first_entry_by_time_period':[{'first_entry':t,'period':l,'count':v} for (t,l),v in sorted(first_entry.items())],
      'max_first_entry':max_entry,
      'geometric_cycle_class_sizes':geom,
      'sample_cycle_representative':{str(l):min(min(o) for o in items) for l,items in cycles.items()},
      'transition_sha256':hashlib.sha256(cert.read_bytes()).hexdigest()
    }
    # independently check cycle local minimality from each orbit (not inferred from labels)
    for l,arr in cycles.items():
        for orbit in arr:
            assert len(set(orbit))==l
            for i,v in enumerate(orbit):assert nxt[v]==orbit[(i+1)%l]
    return result

if __name__=='__main__':
    out={f'GP(5,{k})':evaluate(k) for k in (1,2)}
    path=Path(__file__).with_name('python_results.json')
    regenerated=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if path.exists():
        assert path.read_text(encoding='utf-8')==regenerated, "result certificate mismatch"
    else: path.write_text(regenerated,encoding='utf-8')
    print(json.dumps({name:{key:rec[key] for key in ('primitive_orbits','basin_by_primitive_period','max_first_entry','automorphisms','geometric_cycle_class_sizes')} for name,rec in out.items()},indent=2))
    print("PASS: all labelled configurations, binary certificates, published summaries, and symmetry orbits")
