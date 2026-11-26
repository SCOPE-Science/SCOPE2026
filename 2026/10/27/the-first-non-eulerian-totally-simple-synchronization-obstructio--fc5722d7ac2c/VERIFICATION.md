---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite evidence for the joint census and Eulerian frequency table

`scripts/enumerate.cpp` generates the full labeled code space, tests primitivity and keeps one representative per vertex-isomorphism orbit. It tests every proper partition and every coloring. Compile with `g++ -std=c++17 -O2 scripts/enumerate.cpp -o enumerate` and run `./enumerate 5`; compare representatives and summary to `data/graph_5.csv` and `data/stats_5.txt`. The summary specifies the joint total simplicity and total synchronization counts, with 470 simple, 890 totally synchronizing, and 448 having both properties among the 1,220 primitive classes. For the Eulerian frequency table, retain representative rows with simplicity flag 1, fewer than 32 synchronizing colorings, and target multiplicity two at every vertex. The frequencies at 24, 28 and 30 are 4, 8 and 6.

`python3 scripts/check.py --data-dir data` tests all stored rows, including primitivity, canonicity, lumpability, in-degree and coloring counts. It uses backward reachability of mergeable pairs rather than full-set forward reachability. A stored-row check alone is not proof of exhaustiveness; regeneration from the full labeled candidate universe establishes coverage. The enumeration is an exact finite argument, not formal verification or a theorem at larger orders.
