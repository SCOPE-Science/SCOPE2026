"""Independent verifier (lane-300): replays every claimed number from stored
block lists only. Usage: python3 artifacts/verify.py  (run from output/)."""
import sys, json
sys.path.insert(0, "artifacts")
from sts_lib import (verify_sts, pasch_fast, pasch_bruteforce, aut_order,
                     find_iso, sha_of_system, canon_system)

fails = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))
    if not cond:
        fails.append(name)

# --- STS(13) census ---
c = json.load(open("artifacts/census13.json"))
check("c13.solutions==14400", c["solutions"] == 14400, str(c["solutions"]))
check("c13.ntypes==2", len(c["types"]) == 2)
T = [(t["name"], [tuple(b) for b in t["blocks"]], t["pasch"], t["aut"], t["count"], t["sha"])
     for t in c["types"]]
for nm, R, P, Au, cnt, sha in T:
    ok, msg = verify_sts(R, 13)
    check("c13.%s.sts" % nm, ok, msg)
    check("c13.%s.pasch_fast==%d" % (nm, P), pasch_fast(R, 13) == P,
          str(pasch_fast(R, 13)))
    check("c13.%s.pasch_brute==%d" % (nm, P), pasch_bruteforce(R) == P,
          str(pasch_bruteforce(R)))
    check("c13.%s.aut==%d" % (nm, Au), aut_order(R, 13) == Au,
          str(aut_order(R, 13)))
    check("c13.%s.sha" % nm, sha_of_system(R) == sha, sha_of_system(R))
check("c13.counts", sorted(t["count"] for t in c["types"]) == [1920, 12480],
      str(sorted(t["count"] for t in c["types"])))
check("c13.counts_sum", sum(t["count"] for t in c["types"]) == c["solutions"])
check("c13.paschset", sorted(t["pasch"] for t in c["types"]) == [8, 13])
check("c13.noniso", find_iso(T[0][1], T[1][1], 13, limit=1) == [])
check("c13.autset", sorted(t["aut"] for t in c["types"]) == [6, 39])

# --- STS(15) witnesses ---
w = json.load(open("artifacts/witness15_anti.json"))
A = [tuple(b) for b in w["blocks"]]
ok, msg = verify_sts(A, 15)
check("w15anti.sts", ok, msg)
check("w15anti.pasch_fast==0", pasch_fast(A, 15) == 0, str(pasch_fast(A, 15)))
check("w15anti.pasch_brute==0", pasch_bruteforce(A) == 0, str(pasch_bruteforce(A)))
check("w15anti.aut==60", aut_order(A, 15) == 60, str(aut_order(A, 15)))
check("w15anti.sha", sha_of_system(A) == w["sha"], sha_of_system(A))

g = json.load(open("artifacts/witness15_pg32.json"))
G = [tuple(b) for b in g["blocks"]]
ok, msg = verify_sts(G, 15)
check("w15pg32.sts", ok, msg)
check("w15pg32.pasch_fast==105", pasch_fast(G, 15) == 105, str(pasch_fast(G, 15)))
check("w15pg32.pasch_brute==105", pasch_bruteforce(G) == 105, str(pasch_bruteforce(G)))
check("w15pg32.aut==20160", aut_order(G, 15) == 20160, str(aut_order(G, 15)))
check("w15pg32.sha", sha_of_system(G) == g["sha"], sha_of_system(G))
check("w15anti_vs_pg32.noniso", find_iso(A, G, 15, limit=1) == [])

print("VERIFY_" + ("OK" if not fails else "FAILED: %r" % fails))
sys.exit(1 if fails else 0)
