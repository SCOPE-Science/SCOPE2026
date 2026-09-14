"""FINAL deterministic verifier: 22-edge P6-free linear 13-graph + density corollary + block-rigidity lemma.
No randomness. Prints a certificate transcript."""
import itertools, json, time

def load_edges(path):
    return [tuple(e) for e in json.load(open(path))]

def check_linear(edges):
    seen=set()
    for e in edges:
        if len(set(e))!=3: return False, ("non-triple", e)
        for p in itertools.combinations(sorted(e),2):
            if p in seen: return False, ("repeated pair", p)
            seen.add(p)
    return True, ("all %d pairs distinct"%len(seen),)

def find_P6_dfs(edges, limit=1):
    m=len(edges); esets=[set(e) for e in edges]
    adj=[[] for _ in range(m)]
    for i in range(m):
        for j in range(i+1,m):
            if len(esets[i]&esets[j])==1:
                adj[i].append(j); adj[j].append(i)
    found=[]
    def dfs(path, used):
        if len(found)>=limit: return True
        if len(path)==6:
            found.append(tuple(path)); return True
        last=path[-1]
        earlier=set().union(*[esets[x] for x in path[:-1]]) if len(path)>1 else set()
        for nb in adj[last]:
            if nb in path: continue
            link=esets[last]&esets[nb]
            if link & earlier: continue
            if (set(esets[nb])-link) & used: continue
            if dfs(path+[nb], used|esets[nb]):
                if len(found)>=limit: return True
        return False
    for s in range(m):
        if dfs([s], set(esets[s])):
            if len(found)>=limit: break
    return found

def brute_P6_free(edges):
    """Independent implementation: ordered 6-tuples, direct vertex-disjointness check."""
    m=len(edges); esets=[set(e) for e in edges]
    nchecked=0
    for tup in itertools.permutations(range(m),6):
        nchecked+=1
        ok=True
        for i in range(5):
            if len(esets[tup[i]]&esets[tup[i+1]])!=1: ok=False; break
        if not ok: continue
        for i in range(6):
            for j in range(i+2,6):
                if esets[tup[i]]&esets[tup[j]]: ok=False; break
            if not ok: break
        if not ok: continue
        if len(set().union(*[esets[t] for t in tup]))==13:
            return False, tup, nchecked
    return True, None, nchecked

def gen_cyclic_sts13():
    S=set()
    for b in [(0,1,4),(0,2,7)]:
        for i in range(13):
            S.add(tuple(sorted((b[j]+i)%13 for j in range(3))))
    return sorted(S)

t0=time.time()
B=load_edges("output/artifacts/best13_22.json")
assert len(B)==22 and len(set(v for e in B for v in e))==13
lin,info=check_linear(B)
print("B: linear =",lin,info, flush=True)
assert lin
p=find_P6_dfs(B,limit=1)
print("B: DFS P6 hits =",len(p), flush=True)
assert len(p)==0
free,wit,nc=brute_P6_free(B)
print(f"B: brute P6-free ={free} (checked {nc} ordered 6-tuples)", flush=True)
assert free
from collections import Counter
print("B: degree seq =",sorted(Counter(v for e in B for v in e).values()), flush=True)
print("B: density 22/13 = %.6f > 5/3 = %.6f"%(22/13,5/3), flush=True)

# rigidity lemma: two disjoint punctured-STS13 12-blocks admit no extra cross triple
S=gen_cyclic_sts13()
A=[e for e in S if 12 not in e]
assert len(A)==20
shift=lambda e: tuple(sorted(x+13 for x in e))
Bp=[shift(e) for e in A]
E24=A+Bp
assert len(find_P6_dfs(E24,limit=1))==0
VA=set(v for e in A for v in e); VB=set(v for e in Bp for v in e)
pairs=set()
for e in E24:
    for p in itertools.combinations(sorted(e),2): pairs.add(p)
V=sorted(VA|VB)
cands=[t for t in itertools.combinations(V,3)
       if not (set(t)<=VA or set(t)<=VB)
       and all(tuple(sorted(p)) not in pairs for p in itertools.combinations(t,2))]
print("cross-candidates:",len(cands), flush=True)
bad=[t for t in cands if find_P6_dfs(E24+[t],limit=1)]
print("cross triples creating P6: %d/%d; keeping P6-free: %d"%(len(bad),len(cands),len(cands)-len(bad)), flush=True)
assert len(bad)==len(cands)
print("RIGIDITY LEMMA CERTIFIED: no single cross triple can be added to the 24v/40e two-block union.", flush=True)
print("elapsed %.1fs"%(time.time()-t0), flush=True)
print("ALL FINAL CHECKS PASSED", flush=True)
