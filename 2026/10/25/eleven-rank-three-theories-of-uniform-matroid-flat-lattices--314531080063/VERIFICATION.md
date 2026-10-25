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

# Verification record

The exact orbit recurrence in `verify_types.py` was executed successfully with every positive parameter pair through ground-set size 25; its log is `verify_types_output.txt`. It reports eleven rank-three types, rank stabilization at six, the two universal seven-row profiles, and the 121-flat sharp bound.

The independently coded `verify_direct.cpp` was compiled with a C++17 compiler and run on all twelve smallest parameter models, representing eleven distinct theories. It enumerates actual subsets rather than four-region orbits, and compares third-flat adjacency-to-inclusion profiles directly. `compare_direct.py` verified equality of its complete pointed-type signatures with the orbit calculations. The original output is `verify_direct_output.txt`.

The infinite statements are established by the explicit four-cell integer inequalities and their symbolic endpoint case reduction in `RESULT.md`. The finite replay cannot by itself verify infinitely many sizes; the seven-row algebraic profile lemma is the critical mathematical proof step. The literature overlap comparison was not an exhaustive search of all historical print material. No independent validation has been performed.
