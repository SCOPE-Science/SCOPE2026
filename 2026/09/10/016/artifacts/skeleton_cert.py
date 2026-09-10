"""Structural separation certificate for lane-519 (stdlib only).
Fixed distinguished triple set B = Bose STS(63) on V0 (same vertex labels as baselines).
Certifies: symdiff(G*,H*) >= |H* cap B| - |G* cap B| (since H*B edges outside G* lie in H*\\G*).
Also replays the fixed flag inequality F = Phi-4/5 signs on any archived pair.
Usage: python3 skeleton_cert.py [baselines.json]
"""
import json, sys
path = sys.argv[1] if len(sys.argv) > 1 else 'baselines.json'
d = json.load(open(path))
V = d['V']
MOD = V // 3
assert V == 3 * MOD and MOD % 2 == 1, "needs Bose order"
inv2 = (MOD + 1) // 2
B = set()
for i in range(MOD):
    B.add((i*3+0, i*3+1, i*3+2))
for xx in range(MOD):
    for yy in range(xx+1, MOD):
        z = ((xx+yy)*inv2) % MOD
        for a in range(3):
            B.add(tuple(sorted((xx*3+a, yy*3+a, z*3+((a+1)%3)))))
sG = set(map(tuple, d['G']))
sH = set(map(tuple, d['H']))
gB = len(sG & B)
hB = len(sH & B)
sd = len(sG ^ sH)
cert = hB - gB
print(f"V={V} |B|={len(B)} (Bose STS triple set, fixed from vertex labels)")
print(f"|G* cap B|={gB}  |H* cap B|={hB}  retention gap={cert}")
print(f"certificate: symdiff >= {cert} (Bose edges in H* outside G*)")
print(f"exact symdiff={sd}  cert-holds={sd >= cert}  threshold-pass={sd >= V*V/200}")
print(f"cert ratio={cert/V**2:.4f}  exact ratio={sd/V**2:.4f}  threshold ratio=0.0050")
assert sd >= cert and sd >= V*V/200
# flag signs replay
from collections import Counter
def phi(edges):
    pair = {}
    for i,(x,y,z) in enumerate(edges):
        for p in ((x,y),(x,z),(y,z)):
            a,b = (p[1],p[0]) if p[0]>p[1] else p
            pair[(a,b)] = i
    def gp(a,b):
        if a>b: a,b=b,a
        return pair.get((a,b),-1)
    hi=lo=nd=0; m=len(edges)
    for i in range(m):
        S1=set(edges[i])
        for j in range(i+1,m):
            S2=set(edges[j])
            if S1&S2: continue
            nd+=1; t=sum(1 for u in S1 for w in S2 if gp(u,w)>=0)
            if t>=8: hi+=1
            if t<=5: lo+=1
    return hi/nd-lo/nd-0.8
G=[tuple(e) for e in d['G']]; H=[tuple(e) for e in d['H']]
fG=phi(G); fH=phi(H)
print(f"F(G*)={fG:.4f} (<0: {fG<0})  F(H*)={fH:.4f} (>0: {fH>0})  opposite-signs={ (fG<0)!=(fH<0) }")
print("SKELETON_CERT_OK")
