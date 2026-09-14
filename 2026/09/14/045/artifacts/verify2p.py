"""Final bounded verification: recompute 11 stored certs under second prime P2 + symmetry check."""
import sys, json
sys.path.insert(0,"output/artifacts")
from fast_ag import AGfast, toeplitz_center, delta_of_M, sig_of_parts, P1, P2
from collections import Counter
j=8; T=[1,3,6,6,6,6,6,3,1]
data=json.load(open("output/artifacts/sweep_v2.json"))
print("certs:",len(data))
ok_all=True
for i,e in enumerate(data):
    F={eval(k):v for k,v in e["F"].items()}; l=tuple(e["l"])
    a1=AGfast(F,j,p=P1); a2=AGfast(F,j,p=P2)
    h1, h2 = a1.H, a2.H
    M1=a1.rankmat(l); M2=a2.rankmat(l)
    sameH = (h1==T and h2==T)
    sameM = (M1==M2).all()
    J,P,okj=AGfast.jdt(M1,j)
    t1,_=toeplitz_center(M1); t2,_=toeplitz_center(M2)
    c=Counter((p,nu) for p,nu,m in P for _ in range(m))
    sym=all(c.get((p,j+1-nu-p),0)==m for (p,nu),m in c.items())
    r1,d1=delta_of_M(M1,j); r2,d2=delta_of_M(M2,j)
    match=(list(r1)==e["r"] and list(d1)==e["delta"] and sig_of_parts(P)==tuple(map(tuple,e["jdt"])))
    line=f"{i} H_T={sameH} M1==M2={sameM} toeplitz={t1}&{t2} jdt-ok={okj} sym={sym} r,d-match={match} r={r1} d={d1}"
    print(line,flush=True)
    if not (sameH and sameM and t1 and t2 and okj and sym and match): ok_all=False
print("ALL_OK=",ok_all)
