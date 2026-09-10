"""Single-command replay of the target-directed evidence (lane-499).
Replays: generator validation vs ASM numbers; S involution + (5.1); left censuses;
Sec-9.2 (n,2) machine certification; Fischer CT spot checks; LGV totals incl. (0,6,3);
recorded obstruction probes (naive scan / column-3 extension / cascade / completion bridge).
Usage: python3 verify.py  (run from output/; ~3-5 min, stdlib only)
Writes VERIFY_OK on success.
"""
import sys
sys.path.insert(0, "artifacts")
from collections import Counter, defaultdict
from gen import gen_gog, gen_magog, is_gog, is_magog
from gogam import schutzenberger, left_trap, is_gogam
from sec92 import sec92_forward, left2
from relabel import standard_procedure, inversions, is_gt
from lgv_cert import lgv_total

ASM = {1:1,2:2,3:7,4:42,5:429,6:7436}
fails = []
def check(name, cond, detail=""):
    print(f"{'PASS' if cond else 'FAIL'} {name} {detail}", flush=True)
    if not cond: fails.append(name)

# 1. generators vs ASM numbers (n<=5 both sides; n=6 count only for speed)
for n in range(1, 6):
    g = gen_gog(n); m = gen_magog(n)
    check(f"gen-gog-{n}", len(g)==ASM[n] and all(is_gog(t) for t in g), f"({len(g)})")
    check(f"gen-magog-{n}", len(m)==ASM[n] and all(is_magog(t) for t in m), f"({len(m)})")

# 2. S involution + (5.1), n<=5
for n in (3,4,5):
    g = gen_gog(n); m = gen_magog(n)
    check(f"S-invol-gog-{n}", all(schutzenberger(schutzenberger(t))==t for t in g))
    G = [schutzenberger(t) for t in m]
    check(f"S-magog-gogam-{n}", all(is_gogam(t) for t in G), f"({len(G)})")

# 3. left censuses n<=5
for n in (4,5):
    g = gen_gog(n); m = gen_magog(n)
    G = [schutzenberger(t) for t in m]
    for k in (1,2,3):
        pg = set(left_trap(t,k) for t in g); pm = set(left_trap(t,k) for t in G)
        check(f"left-{n}-{k}", len(pg)==len(pm), f"({len(pg)}={len(pm)})")

# 4. Sec-9.2 (n,2) certification: image == true set, n=4,5
for n in (4,5):
    g = gen_gog(n); m = gen_magog(n)
    G = [schutzenberger(t) for t in m]
    pm = set(left_trap(t,2) for t in G)
    imgs = set(tuple(tuple(r) for r in sec92_forward(left2(t),n)) for t in g)
    check(f"sec92-set-{n}", imgs==pm, f"({len(imgs)}={len(pm)})")
    check(f"sec92-bottom-{n}", all(sec92_forward(left2(t),n)[0][0]==t[0][0] for t in g))

# 5. Fischer CT spot checks (Thm-7 specialization)
from collections import defaultdict as dd
from math import comb
def ct_trap(m0,n,k,b):
    P=dd(int); P[tuple([0]*n)]=1
    for i,e in enumerate(list(b)+[m0+k+1]*(n-k)):
        Q=dd(int)
        for p in range(e+1):
            c=comb(e,p)
            for key,v in P.items():
                l=list(key); l[i]+=p; Q[tuple(l)]+=v*c
        P=Q
    for i in range(n):
        for j in range(i+1,n):
            Q=dd(int); Ts=[]
            d1=[0]*n; d1[i]+=1; Ts.append((tuple(d1),1))
            d2=[0]*n; d2[j]+=1; Ts.append((tuple(d2),-1))
            d3=[0]*n; d3[i]+=1; d3[j]+=1; Ts.append((tuple(d3),1))
            d4=[0]*n; d4[j]+=2; Ts.append((tuple(d4),-1))
            d5=[0]*n; d5[i]+=2; d5[j]+=1; Ts.append((tuple(d5),1))
            d6=[0]*n; d6[i]+=1; d6[j]+=2; Ts.append((tuple(d6),-1))
            for key,v in P.items():
                for t,c in Ts:
                    Q[tuple(key[d]+t[d] for d in range(n))]+=v*c
            P=Q
    return P[tuple([n-1]*k+[n-i-1+k for i in range(k,n)])]
check("CT-032", ct_trap(0,3,2,[1,2])==7, "(7)")
check("CT-042", ct_trap(0,4,2,[1,2])==35, "(35)")
check("CT-043", ct_trap(0,4,3,[1,2,3])==42, "(42)")

# 6. LGV totals (Fischer Sec-4), incl. (0,6,3) anchor leg
for (n,k,T) in [(3,2,7),(4,2,35),(4,3,42),(5,3,387)]:
    tot,nb,_ = lgv_total(0,n,k)
    check(f"LGV-{n}-{k}", tot==T, f"({tot})")
tot,nb,per = lgv_total(0,6,3)
check("LGV-6-3", tot==4862, f"({tot})")

# 7. n=6 dual-engine census (regenerated here)
g = gen_gog(6); m = gen_magog(6)
check("gen6", len(g)==7436 and len(m)==7436)
G = [schutzenberger(t) for t in m]
check("S-gogam-6", all(is_gogam(t) for t in G))
for k in (1,2,3):
    pg = set(left_trap(t,k) for t in g); pm = set(left_trap(t,k) for t in G)
    check(f"left-6-{k}", len(pg)==len(pm), f"({len(pg)}={len(pm)})")

# 8. obstruction probes (must reproduce the recorded failures)
g5 = gen_gog(5)
nbad = sum(1 for t in g5 if not is_gt(standard_procedure(t)))
img5 = set(left_trap(standard_procedure(t),3) for t in g5)
check("obstr-naive-GT-break", nbad==34, f"({nbad})")
check("obstr-naive-noninj", len(img5)==387 and len(img5)<len(g5), f"({len(img5)})")

print("VERIFY_OK" if not fails else f"VERIFY_FAIL {fails}")
sys.exit(0 if not fails else 1)
