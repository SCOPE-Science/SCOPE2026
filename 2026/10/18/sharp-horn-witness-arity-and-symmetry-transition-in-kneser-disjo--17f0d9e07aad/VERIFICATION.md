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

# Reproducible checks

Run `python3 verify_kneser.py` using only the Python standard library. It independently generates the incidence relation of disjointness between two copies of every \(k\)-subset and computes double-prime closures without using the closed-form formula. It then compares closures and closed-set counts, computes the Möbius function by its defining recurrence, checks explicit modular-law obstructions, exhaustively computes premise-witness minima for cases with at most ten attributes, and enumerates small Johnson-graph automorphisms from adjacency. It reports `VERIFY_OK` on success.

The small-instance test is exhaustive for input families with at most thirteen attributes, uses seeded checks otherwise, and enumerates automorphism groups only for small specified parameters. The mathematical proof in `RESULT.md` is required for the unbounded theorem. In particular the code does not establish novelty, publication priority or independent validation.

Expected key lines from the checked run:

```
CLOSURE_MOBIUS_MODULARITY_OK 12 cases
AUTOMORPHISM_OK 4 2 720
AUTOMORPHISM_OK 5 2 120
AUTOMORPHISM_OK 6 2 720
VERIFY_OK
```
