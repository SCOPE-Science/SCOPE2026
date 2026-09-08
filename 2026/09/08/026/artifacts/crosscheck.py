#!/usr/bin/env python3
"""Step 3: independent cross-checks + minor certs + CSV."""
import json, csv
from itertools import combinations

N = 8
data = json.load(open("output/artifacts/reps.json"))
rows = json.load(open("output/artifacts/tutte_table.json"))
print("types:", len(rows))

def rank_of_masks(lines):
    r = [0] * (1 << N)
    for s in range(1, 1 << N):
        pc = bin(s).count("1")
        if pc <= 2:
            r[s] = pc
        else:
            r[s] = 2 if any((s & ~ln) == 0 for ln in lines) else 3
    return r

def t20_subsetsum(r):
    tot = 0
    for a in range(1 << N):
        tot += (-1) ** (bin(a).count("1") - r[a])
    return tot

def maskstr(em):
    return "{" + ",".join(str(i) for i in range(N) if (em >> i) & 1) + "}"

ok = True
for d in rows:
    r = rank_of_masks(d["lines"])
    v = t20_subsetsum(r)
    if v != d["t20"]:
        print("MISMATCH type", d["type"], v, d["t20"])
        ok = False
print("subset-sum cross-check:", "ALL OK" if ok else "FAIL")

# labeled sum + divisibility
s = sum(d["count"] for d in rows)
print("labeled sum:", s, "=433038?", s == 433038)
print("all counts divide 40320:", all(40320 % d["count"] == 0 for d in rows))

# sorted table -> CSV
rs = sorted(rows, key=lambda d: (-d["t20"], d["type"]))
with open("output/artifacts/tutte_t20_table.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rank", "type", "n_lines", "lines", "labeled_count", "nbases", "T20"])
    for k, d in enumerate(rs, 1):
        w.writerow([k, d["type"], len(d["lines"]),
                    ";".join(maskstr(em) for em in d["lines"]) or "uniform(no lines)",
                    d["count"], d["nbases"], d["t20"]])

W = rs[0]
print("W: type", W["type"], "lines", W["lines"], "T", W["t20"])

# Fano check: Fano plane lines (7 triples on 0..6): standard representation
# Fano with points 0..6: lines 012,034,056,135,146,236,245 (one common encoding)
FANO = [{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}]
def triples_of(lines):
    S = set()
    for em in lines:
        pts = [i for i in range(N) if (em >> i) & 1]
        for a in range(len(pts)):
            for b in range(a+1, len(pts)):
                for c in range(b+1, len(pts)):
                    S.add((pts[a],pts[b],pts[c]))
    return S

for d in rows:
    if len(d["lines"]) == 7 and d["count"] == 240:
        print("candidate Fano+free: type", d["type"], [maskstr(e) for e in d["lines"]])
        # find free point: point on no line
        on = [0]*N
        for em in d["lines"]:
            for i in range(N):
                if (em>>i)&1: on[i]+=1
        print("  point incidences:", on)
        # try each deletion e: restriction to remaining 7 pts should have exactly 7 triples = Fano
        T = triples_of(d["lines"])
        for e in range(N):
            rem = sorted(set(range(N))-{e})
            tr = sorted(t for t in T if e not in t)
            print(f"  del {e}: ntrip={len(tr)} trips={tr}")
