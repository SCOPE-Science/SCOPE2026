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

# Verification

Run `python3 verify.py` with standard Python 3. The checker uses only the standard library. It checks exact adjacency, matrix rank, all graph Laplacian subspace relations over the rational numbers for five connected regular graphs, and exhaustive ideal closure over a four-dimensional example in characteristic five.

Observed result: `GRAPHS [(2, 1), (3, 2), (4, 3), (4, 2), (8, 3)]`, `FINITE_IDEALS (1120, 9)`, `VERIFY_OK`. The 1120 subspaces form the full finite subspace lattice in that example; they are not an all-parameter enumeration.

The unrestricted claims are established mathematically in the proof, not inferred from experiments. Earlier general ideal facts and counterexamples are credited in the references. No independent external audit or validation has been performed.
