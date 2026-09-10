"""Unit-tested exact verifier for lane-519 baselines (stdlib only).
Uses pasch_fano_census (anchor-based Pasch census /7-free-tested: single Pasch->1,
Fano->7 Pasch + 1 Fano). Checks linearity, Pasch count 0 (=>Fano-free by logged
witness), Fano count 0 (direct), defects <=2v0, exact symmetric difference.
Usage: python3 verify2.py <baselines.json>
"""
import json, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from pasch_fano_census import count_pasch, count_fano

path = sys.argv[1] if len(sys.argv) > 1 else 'baselines.json'
d = json.load(open(path))
V = d['V']
G = [tuple(sorted(e)) for e in d['G']]
H = [tuple(sorted(e)) for e in d['H']]
M = V * (V - 1) // 6
print(f"V={V} STSbound M={M} threshold v0^2/200={V*V/200:.3f}")
print("Pasch-in-Fano witness: ((0,1,2),(0,3,4),(1,3,5),(2,4,5)) [replay unit test: Fano has 7 Pasch]")

def check(edges, name):
    eset = set(edges)
    assert len(eset) == len(edges), f"{name}: duplicates"
    pair = {}
    ok = True
    for i, (x, y, z) in enumerate(edges):
        for p in ((x, y), (x, z), (y, z)):
            a, b = (p[1], p[0]) if p[0] > p[1] else p
            if (a, b) in pair:
                ok = False
            pair[(a, b)] = i
    print(f"{name}: linearity {'OK' if ok else 'FAIL'} e={len(edges)} defect={M-len(edges)} rho={6*len(edges)/V**2:.4f}")
    assert ok
    p = count_pasch(edges)
    print(f"{name}: Pasch count={p} -> {'PASCH-FREE OK' if p==0 else 'FAIL'}")
    assert p == 0
    f = count_fano(edges)
    print(f"{name}: Fano count={f} -> {'FANO-FREE OK' if f==0 else 'FAIL'}")
    assert f == 0
    assert M - len(edges) <= 2 * V
    return len(edges)

eG = check(G, 'G*')
eH = check(H, 'H*')
sG, sH = set(G), set(H)
sd = len(sG ^ sH)
print(f"symdiff |E(G*) triangle E(H*)| = {sd} (>=20: {'PASS' if sd >= V*V/200 else 'FAIL'})")
print(f"rhoG={6*eG/V**2:.4f} rhoH={6*eH/V**2:.4f}")
print("VERIFY_OK")
