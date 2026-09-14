"""Big corrected sweep V2: STORE (F,l) certs. Cone + Waring + 2-cone sums; dense l-grid; j=8."""
import sys
sys.path.insert(0,"output/artifacts")
from fast_ag import *
import numpy as np, json, itertools
j=8; T=[1,3,6,6,6,6,6,3,1]
Lgrid=[l for l in itertools.product(range(-2,3),repeat=3) if l!=(0,0,0)]
rng=np.random.default_rng(424242)
seen={}
def trial(F):
    ag=AGfast(F,j)
    if ag.H!=T: return False
    for l in Lgrid:
        M=ag.rankmat(l)
        ok,r=toeplitz_center(M)
        if not ok: continue
        J,P,okj=AGfast.jdt(M,j)
        if not okj: continue
        rr,d=delta_of_M(M,j)
        if rr[0]!=6: continue
        if any(x<0 for x in rr): continue
        if any(x<0 for x in d): continue
        s=(sig_of_parts(P),rr,d)
        if s not in seen:
            seen[s]=(dict(F),tuple(int(v) for v in l))
            print(f"NEW l={l} r={rr} d={d} JDT={sorted(P)}",flush=True)
    return True
hit=0
for t in range(900):
    F={}
    for a in range(j,-1,-1):
        for b in range(j-a,-1,-1):
            c=j-a-b
            if a+b<=3:
                F[(a,b,c)]=int(rng.integers(-3,4))
    F={k:v for k,v in F.items() if v!=0}
    if F and trial(F): hit+=1
print("cone hits=",hit,"distinct=",len(seen))
for t in range(300):
    pts=[tuple(int(v) for v in rng.integers(-3,4,3)) for _ in range(9)]
    if any(p==(0,0,0) for p in pts): continue
    if trial(power_F(pts,[1]*9,j)): hit+=1
print("hits=",hit,"distinct=",len(seen))
deltas={}
for (_,r,d) in seen: deltas[d]=deltas.get(d,0)+1
for d,n in sorted(deltas.items()): print(d,"n=",n)
out=[]
for (P,r,d),(F,l) in seen.items():
    out.append({"jdt":[list(t) for t in P],"r":list(map(int,r)),"delta":list(map(int,d)),
                "F":{str(k):int(v) for k,v in F.items()},"l":list(l)})
json.dump(out,open("output/artifacts/sweep_v2.json","w"),indent=1)
print("saved",len(out))
