---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Exact mathematical verification consists of the positional characterizations, closure under pointwise meet and join, the acyclic dependency argument for decrementing an eligible particle position, and the distance/median deductions in `RESULT.md`. The proof applies to all nonempty fixed-weight sectors with run bounds at least two except the simultaneously alternating case.

Finite replay commands:

```bash
python verify_descent.py
g++ -O2 -std=c++17 verify_bfs.cpp -o verify_bfs
./verify_bfs
```

Both implementations construct feasible configurations from first principles. The Python program checks valid coordinatewise meet and join and proves finite monotone reachability by an explicit coordinate-decrement search. The independent C++17 program enumerates bitmasks, computes swaps directly, and compares shortest graph distances from exhaustive breadth-first searches to the one-position earth-mover formula. These are finite consistency tests, not independent validation of the infinite theorem.

Limits: no computer enumeration proves the all-parameter statement; no automated certification of novelty or independent audit has been carried out. The simultaneous no-`00`/no-`11` boundary example is explicitly excluded from the theorem.
