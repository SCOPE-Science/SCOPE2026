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

# Verification details

Run `python3 check_parity_logic.py` with Python 3 standard library. It deterministically enumerates every labelled loop-free undirected bipartite graph on each vertex set of size one to five, exactly \(1,2,7,41,376\) graphs respectively. For each graph it evaluates 400 generated formulas and 400 generated programs, with all program operations and formula connectives from the theorem, and checks all vertices plus the mandatory canonical witnesses. Output:

`PARITY_LOOP_INTERSECTION_OK {1: 1, 2: 2, 3: 7, 4: 41, 5: 376} 400 400`

The program sample is deterministic and bounded in syntactic depth. Only the mathematical induction establishes the unrestricted theorem. No independent audit or formal proof assistant assessment has been performed.
