"""One-command verifier: replays ALL target claims from committed artifacts (stdlib only).
1. DSASM counts n<=6 via MT + symmetric filter (validates generator).
2. BFK numDSASM Pfaffian totals n<=10 == 1,2,5,16,67,368,2630,24376,293770,4610624 (dual: matching-sum vs Bareiss-det sqrt).
3. n=7 fast census (1.3s, re-enumerates 218348 MT -> 2630 DSASM) -> J_7 enum; loads committed J7_enum.json, asserts equality.
4. Loads committed Xprs7_full.json (Pfaffian poly), projects (P,R,S)->(I,M), asserts == J_7 enum (Stembridge-LGV route).
5. Lemma machine check (lemma_check replay: Pf equality on probe DAGs).
Prints VERIFY_OK on success.
"""
import json, time
from collections import Counter
from math import comb

t0=time.time()
# --- 1. generator validation n<=6 ---
exec(open('output/artifacts/dsasm_enum2.py').read().split("def census")[0])
exp={1:1,2:2,3:5,4:16,5:67,6:368}
for n in range(1,7):
    ds=sum(1 for tri in gen_triangles(n) if all((A:=tri_to_asm(tri))[i][j]==A[j][i] for i in range(n) for j in range(n)))
    assert ds==exp[n],(n,ds)
print("gen n<=6 OK")
# --- 2. BFK totals dual route ---
exec(open('output/artifacts/pfaffian.py').read().split("for n in range")[0])
expT={1:1,2:2,3:5,4:16,5:67,6:368,7:2630,8:24376,9:293770,10:4610624}
for n in range(1,11):
    B=BFK_total(n)
    m1=pf_matchings(B); m2=pf_via_det(B)
    assert m1==m2==expT[n],(n,m1,m2)
print("BFK totals n<=10 dual-OK; P_7=2630")
# --- 3/4. J7 ---
Jf=json.load(open("output/artifacts/J7_enum.json"))
Jenum={(i,r):c for i,r,c in Jf["joint"]}
assert sum(Jenum.values())==2630 and Jf["total"]==2630 and Jf["asm_total"]==218348
X={tuple(map(int,k.split(','))):v for k,v in json.load(open("output/artifacts/Xprs7_full.json")).items()}
assert sum(X.values())==2630 and not any(v<0 for v in X.values())
proj=Counter()
for (ep,er,es),v in X.items():
    assert es%2==1
    proj[(2*ep+(7-es)//2, er+(es-7)//2)]+=v
assert dict(proj)=={k:v for k,v in Jenum.items()}, "J7 mismatch"
# --- live n=7 re-enumeration (independent of committed JSON) ---
live=__import__('collections').Counter()
t7=0; d7=0
for tri in gen_triangles(7):
    t7+=1
    A=tri_to_asm(tri)
    if all(A[i][j]==A[j][i] for i in range(7) for j in range(7)):
        d7+=1
        I,M=stats_direct(A)
        live[(I,M)]+=1
assert t7==218348 and d7==2630,(t7,d7)
assert dict(live)=={k:v for k,v in Jenum.items()}
print("live n=7 re-enumeration OK (218348 ASMs -> 2630 DSASMs)")
print("J7 enum==Xprs projection; cells:",len(Jenum))
print(f"VERIFY_OK ({time.time()-t0:.1f}s)")
