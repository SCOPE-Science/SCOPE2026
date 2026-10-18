#!/usr/bin/env python3
"""Complete independent finite enumeration of the Pappus edge-Kempe graph.
Vertices 0..8 are affine points (x,y), vertex 3*x+y; vertices 9..17 are
nonvertical affine lines y=m*x+b, indexed 9+3*m+b, over F_3.
Only the standard Python library is used. Results are mathematical data.
"""
import itertools, collections, json, argparse

P = range(9)
L = range(9,18)
E = sorted((3*x+y, 9+3*m+(y-m*x)%3) for x in range(3) for y in range(3) for m in range(3))
assert len(E)==27 and len(set(E))==27
inc = {v:[] for v in range(18)}
for i,(u,v) in enumerate(E):inc[u].append((i,v));inc[v].append((i,u))
assert all(len(inc[v])==3 for v in range(18))
FULL=(1<<27)-1
# Explicit incidence-to-standard-LCF isomorphism, no graph library needed.
# The standard Pappus graph has LCF notation [5,7,-7,7,-7,-5]^3.
ISO=[0,14,10,2,16,6,8,4,12,1,15,11,17,7,3,5,13,9]
off=[5,7,-7,7,-7,-5]
LCF={tuple(sorted((i,(i+1)%18))) for i in range(18)}
LCF |= {tuple(sorted((i,(i+off[i%6])%18))) for i in range(18)}
assert len(LCF)==27 and {tuple(sorted((ISO[u],ISO[v]))) for u,v in E}==LCF

# Enumerates all bijections of nine points to nine incident lines; no others
# can exist because every perfect matching covers each point exactly once.
def enumer_matchings(k,used_lines,edge_mask):
    if k==9:
        yield edge_mask; return
    for i,l in inc[k]:
        b=1<<(l-9)
        if not used_lines&b:
            yield from enumer_matchings(k+1,used_lines|b,edge_mask|1<<i)
M=sorted(enumer_matchings(0,0,0));MS=set(M)
assert len(M)==42
F=sorted({tuple(sorted((a,b,FULL^a^b))) for a,b in itertools.combinations(M,2) if not a&b and (FULL^a^b) in MS})
assert len(F)==20
index={f:i for i,f in enumerate(F)}

def bichrom_cycles(a,b):
    sel=a|b; ngh={v:[] for v in range(18)}
    for i,(u,v) in enumerate(E):
        if (sel>>i)&1:ngh[u].append(v);ngh[v].append(u)
    assert all(len(ngh[v])==2 for v in range(18))
    visited=set();cycles=[]
    for v in range(18):
        if v in visited:continue
        stack=[v]; comp=set()
        while stack:
            u=stack.pop()
            if u in comp:continue
            comp.add(u);stack.extend(ngh[u])
        assert not comp & visited
        visited.update(comp)
        mask=0
        for i,(u,w) in enumerate(E):
            if u in comp and w in comp and (sel>>i)&1: mask|=1<<i
        assert mask.bit_count()==len(comp)
        cycles.append((tuple(sorted(comp)),mask))
    assert len(visited)==18
    return cycles

def perm_sign(a):
    perm=[]
    for p in P:
        lines=[l-9 for i,l in inc[p] if a>>i&1]
        assert len(lines)==1
        perm+=lines
    return 1 if sum(perm[i]>perm[j] for i in P for j in range(i+1,9))%2==0 else -1

def coloring_sign(f):
    result=1
    for a in f:result*=perm_sign(a)
    return result

edges=set(); prof=[]; signs=[];switchers=collections.defaultdict(set)
for j,f in enumerate(F):
    sig=coloring_sign(f);signs.append(sig)
    p=[]
    for aidx,bidx in itertools.combinations(range(3),2):
        other=3-aidx-bidx
        a,b=f[aidx],f[bidx]
        cycles=bichrom_cycles(a,b)
        p.append(tuple(sorted(len(c[0]) for c in cycles)))
        for nodes,mask in cycles:
            candidate=tuple(sorted((a^mask,b^mask,f[other])))
            k=index[candidate]
            if k==j:continue
            assert coloring_sign(candidate)==sig, 'parity invariant failed'
            edge=tuple(sorted((j,k)));edges.add(edge);switchers[edge].add((j,aidx,bidx,nodes))
    prof.append(tuple(sorted(p)))

from collections import Counter
assert Counter(prof)=={((6,6,6),(18,),(18,)):18,((6,6,6),)*3:2}
assert Counter(signs)=={1:10,-1:10}
assert len(edges)==36
N={i:set() for i in range(len(F))}
for a,b in edges:N[a].add(b);N[b].add(a)
assert Counter(len(v) for v in N.values())=={3:18,9:2}
comp=[];seen=set()
for i in range(len(F)):
    if i in seen:continue
    q=[i];one=set()
    while q:
        v=q.pop()
        if v in one:continue
        one.add(v);q.extend(N[v])
    seen.update(one);comp.append(one)
assert len(comp)==2 and sorted(map(len,comp))==[10,10]
assert len({coloring_sign(F[v]) for v in comp[0]})==1
assert len({coloring_sign(F[v]) for v in comp[1]})==1
assert coloring_sign(F[next(iter(comp[0]))]) != coloring_sign(F[next(iter(comp[1]))])
for one in comp:
    hub=[v for v in one if len(N[v])==9]
    assert len(hub)==1
    h=hub[0];per=one-{h}
    assert N[h]==per
    peripheral={v:N[v]&per for v in per}
    assert all(len(neigh)==2 for neigh in peripheral.values())
    done=set();cyc_sizes=[]
    for v in per:
        if v in done:continue
        todo=[v];orbit=set()
        while todo:
            w=todo.pop()
            if w in orbit:continue
            orbit.add(w);todo.extend(peripheral[w])
        done.update(orbit)
        assert all(peripheral[w]==orbit-{w} for w in orbit), 'not a disjoint triangle'
        cyc_sizes.append(len(orbit))
    assert sorted(cyc_sizes)==[3,3,3]
print('VERIFY_MATCHINGS_OK vertices=18 edges=27 matchings=42 one_factorizations=20 named_edge_colorings=120')
print('VERIFY_KEMPE_OK switch_edges=36 components=10+10 each_component=K1_join_3K3')
print('VERIFY_BICHROM_OK central=2_profile_6+6+6_three_pairs peripheral=18_profile_18+18+6+6+6')
print('VERIFY_PARITY_OK signs=10+10 each_parity_sector_is_one_component diameter_each=2')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',default=None);ap.add_argument('--check-certificate',default=None)
    args=ap.parse_args()
    if args.certificate or args.check_certificate:
        cert={'definition':'Pappus incidence: p=3*x+y; l=9+3*m+b; y=m*x+b mod 3, x,y,m,b in {0,1,2}',
            'edges':E,'lcf_vertex_isomorphism':ISO,'one_factorizations_edge_masks':[[format(a,'07x') for a in f] for f in F],
            'switch_edges_factorization_indices':sorted([list(e) for e in edges]),
            'bichromatic_cycle_profiles':[ [list(c) for c in p] for p in prof],
            'parity_signs':signs,
            'connected_components':[sorted(x) for x in comp],
            'graph_isomorphism':'two disjoint copies of K_1 join (K_3 disjoint union K_3 disjoint union K_3)'}
        if args.certificate:
            with open(args.certificate,'w',encoding='utf8') as f:json.dump(cert,f,sort_keys=True,indent=2,ensure_ascii=False);f.write('\n')
            print('VERIFY_CERTIFICATE_WRITTEN',args.certificate)
        if args.check_certificate:
            with open(args.check_certificate,'r',encoding='utf8') as f:actual=json.load(f)
            assert actual==json.loads(json.dumps(cert)), 'certificate does not agree with complete recomputation'
            print('VERIFY_CERTIFICATE_OK factorization_masks=20 adjacency_rows=36 parity_and_profiles=true')
