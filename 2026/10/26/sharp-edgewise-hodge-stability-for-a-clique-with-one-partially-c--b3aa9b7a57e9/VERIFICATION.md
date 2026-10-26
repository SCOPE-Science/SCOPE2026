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

# Reproducibility
The accompanying `verify_projection.py` uses only Python's standard library. Run `python verify_projection.py` next to this file. The program builds the Laplacian of a clique plus a vertex attached to a specified subset, inverts \(L+\mathbf1\mathbf1^\mathsf T/n\) by exact-rational row operations, computes every edge-projection row, and verifies row-sum and threshold identities for \(2\le r\le8\) and \(1\le h\le8\).

Observed output: `PASS: 2884 exact-rational row and threshold comparisons for 56 graphs.` Every comparison uses exact rational numbers, not floating point. The proof in `RESULT.md`, rather than finite enumeration, establishes all-size results. No independent audit has been performed.
