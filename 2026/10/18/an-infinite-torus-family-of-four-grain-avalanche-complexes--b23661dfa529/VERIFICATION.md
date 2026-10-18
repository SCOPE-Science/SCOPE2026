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
Run `python3 check_avalanche_torus.py` with standard Python 3; no additional packages are required. The checker rebuilds the synchronous out-degree-one firing process from its initial state, enumerates all its firing sets and simplices, verifies each free face and maximal coface before every elementary deletion, and compares the resulting simplicial complex to an explicit square-grid quotient. It further checks Euler characteristic, six-cycle links, two-triangle edge incidences, and orientability for all 190 tested parameters.

The proof for arbitrarily large allowed parameters is the index-\(n\) lattice quotient and the unique-outer-diagonal argument in RESULT.md. Finite enumeration alone is not claimed to establish an infinite theorem. Previously unindexed equivalent formulations are a residual literature risk. No independent audit has been carried out.
