"""Independent verifier: checks hook-freeness, beta round-trip, counts, Anderson cross-check."""
import json
def conj(lam):
    if not lam: return []
    return [sum(1 for x in lam if x>j) for j in range(max(lam))]
def hooks(lam):
    if not lam: return []
    c=conj(lam); h=[]
    for i,r in enumerate(lam):
        for j in range(r): h.append((r-j)+(c[j]-i)-1)
    return h
def beta_of(lam):
    l=len(lam); return sorted(lam[i]+l-1-i for i in range(l))
def part_of(B):
    d=sorted(B,reverse=True); l=len(d); return [d[i]-(l-1-i) for i in range(l)]
def size_of(B): return sum(B)-len(B)*(len(B)-1)//2
def flush(B,s):
    S=set(B); return all((b-s) in S for b in S if b>=s)
d=json.load(open("census_data.json"))
for key,triple in [("family_457",[4,5,7]),("family_567",[5,6,7])]:
    F=d[key]
    assert len(F["cores"])==F["count"], key
    assert sum(F["size_histogram"].values())==F["count"], key
    for c in F["cores"]:
        lam=c["partition"]; B=c["beta"]
        assert beta_of(lam)==B, (key,lam,B)
        assert part_of(B)==lam, (key,lam)
        assert size_of(B)==c["size"]==sum(lam), (key,lam)
        hs=hooks(lam)
        for t in triple: assert all(h%t!=0 for h in hs),(key,lam,t,hs)
        for t in triple: assert flush(B,t),(key,lam)
    print(key,"count",F["count"],"max",F["max_size"],"OK")
p=d["pair_crosscheck"]
assert p["pair_45_count"]==p["anderson_45"]==14 and p["pair_56_count"]==p["anderson_56"]==42
print("Anderson (4,5)=14 (5,6)=42 cross-check OK")
def enum_flush(s,t):
    N=s*t-1; out=[0]; B=[False]*(N+1)
    def rec(b):
        if b>N: out[0]+=1; return
        B[b]=False; rec(b+1)
        if (b<s or B[b-s]) and (b<t or B[b-t]): B[b]=True; rec(b+1); B[b]=False
    rec(1); return out[0]
assert enum_flush(4,5)==14 and enum_flush(5,6)==42
print("order-ideal enumeration replay OK")
print("VERIFY_OK")
