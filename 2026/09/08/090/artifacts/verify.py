"""Independent verifier: replays the full table from committed generator strings only.
Checks: (1) gcd=1, minimal generation (ed 3); (2) Apery sets; (3) c_i minimality;
(4) Betti R-class certificates; (5) length sets/Delta/catenary at Betti elements;
(6) Delta-union and catenary-max agree with brute-force scan to BOUND;
(7) equality verdicts and extremals. Prints VERIFY_OK on success."""
import json, math, heapq, itertools, sys

BOUND = 400
T = json.load(open("output/artifacts/table.json"))

def facs_of(s, gens):
    n1,n2,n3 = gens
    out=[]
    for a in range(s//n1+1):
        for b in range((s-a*n1)//n2+1):
            r=s-a*n1-b*n2
            if r%n3==0: out.append([a,b,r//n3])
    return out

def Lset(F): return sorted(set(sum(f) for f in F))
def Dset(L):
    L=sorted(set(L))
    return sorted(set(L[i]-L[i-1] for i in range(1,len(L)))) if len(L)>1 else []

def dist(a,b):
    g=[min(x,y) for x,y in zip(a,b)]
    return max(sum(a)-sum(g), sum(b)-sum(g))

def cat(F):
    F=[tuple(f) for f in F]
    if len(F)<=1: return 0
    ds=sorted(set(dist(a,b) for a,b in itertools.combinations(F,2)))
    for N in ds:
        par={f:f for f in F}
        def find(x):
            while par[x]!=x: par[x]=par[par[x]]; x=par[x]
            return x
        for a,b in itertools.combinations(F,2):
            if dist(a,b)<=N:
                ra,rb=find(a),find(b)
                if ra!=rb: par[ra]=rb
        if len(set(find(f) for f in F))==1: return N

def apery(gens):
    m=min(gens); INF=10**9; d=[INF]*m; d[0]=0; pq=[(0,0)]
    while pq:
        x,u=heapq.heappop(pq)
        if x>d[u]: continue
        for g in gens:
            v=(u+g)%m; nd=x+g
            if nd<d[v]: d[v]=nd; heapq.heappush(pq,(nd,v))
    return sorted(d)

def in_sg2(s,o1,o2):
    return any((s-a*o1)%o2==0 for a in range(s//o1+1))

def is_betti(s,gens):
    F=[tuple(f) for f in facs_of(s,gens)]
    if len(F)<=1: return False
    par={f:f for f in F}
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i in range(len(F)):
        for j in range(i+1,len(F)):
            if any(F[i][t]>0 and F[j][t]>0 for t in range(3)):
                a,b=find(F[i]),find(F[j])
                if a!=b: par[a]=b
    return len(set(find(f) for f in F))>1

errs=[]
for row in T["rows"]:
    g=tuple(row["gens"]); glabel=",".join(map(str,g))
    # (1) gcd + ed3 minimality
    assert math.gcd(math.gcd(g[0],g[1]),g[2])==1, glabel
    for i in range(3):
        o=[g[j] for j in range(3) if j!=i]
        assert not in_sg2(g[i],o[0],o[1]), f"{glabel}: gen {g[i]} redundant"
    # (2) Apery
    assert apery(g)==row["apery"], f"{glabel}: apery"
    # (3) c_i minimality: k=c_i works, all smaller fail
    for i in range(3):
        o=[g[j] for j in range(3) if j!=i]; c=row["c_i"][i]
        assert in_sg2(c*g[i],o[0],o[1]), f"{glabel}: c{i}"
        for k in range(1,c):
            assert not in_sg2(k*g[i],o[0],o[1]), f"{glabel}: c{i} not minimal"
        assert c*g[i]==row["cini"][i]
    # (4-5) Betti certs
    bunion=set(); bmax=0
    for bstr,cert in row["betti"].items():
        b=int(bstr)
        assert is_betti(b,g), f"{glabel}: {b} not Betti"
        F=facs_of(b,g)
        assert sorted(map(list,F))==sorted(cert["facs"]), f"{glabel}: {b} facs"
        assert Lset(F)==cert["L"], f"{glabel}: {b} L"
        assert Dset(Lset(F))==cert["D"], f"{glabel}: {b} D"
        assert cat(F)==cert["cat"], f"{glabel}: {b} cat"
        bunion|=set(cert["D"]); bmax=max(bmax,cert["cat"])
    assert sorted(bunion)==row["Delta"], f"{glabel}: Delta"
    assert max(row["Delta"])==row["maxDelta"]
    assert bmax==row["cat"], f"{glabel}: cat max"
    # (6) brute force cross-check: Betti-scan + invariant-scan to BOUND
    brute_betti=[s for s in range(BOUND+1) if is_betti(s,g)]
    assert sorted(map(int,row["betti"].keys()))==brute_betti, f"{glabel}: betti completeness {brute_betti}"
    u=set(); mc=0
    for s in range(BOUND+1):
        F=facs_of(s,g)
        if len(F)>=2:
            u|=set(Dset(Lset(F))); mc=max(mc,cat(F))
    assert sorted(u)==row["Delta"], f"{glabel}: brute Delta {sorted(u)}"
    assert mc==row["cat"], f"{glabel}: brute cat"
    # (7) verdict
    exp="equality" if row["maxDelta"]+2==row["cat"] else "strict"
    assert exp==row["verdict"], f"{glabel}: verdict"
# extremals
cats=[(r["cat"],r["gens"]) for r in T["rows"]]
assert min(c[0] for c in cats)==3
assert T["extremals"]["minimal_catenary"]["gens"] in [[4,6,9],[5,6,9]]
md=max(r["maxDelta"] for r in T["rows"])
attainers=sorted([r["gens"] for r in T["rows"] if r["maxDelta"]==md])
assert md==3 and attainers==[[4,9,11],[5,8,11]], f"maxDelta attainers {attainers}"
mg=T["extremals"]["maximal_delta_gap"]
assert mg["gens"]==[4,9,11] and sorted(mg.get("tied_gens",[]))==[[5,8,11]]
assert mg["witness_element"]==20 and mg["witness_lengths"]==[2,5]
Fw=facs_of(20,(4,9,11))
assert Lset(Fw)==[2,5] and Dset([2,5])==[3]
print(f"VERIFY_OK: 9 rows, Betti-complete to {BOUND}, Delta/brute and cat/brute agree everywhere")
