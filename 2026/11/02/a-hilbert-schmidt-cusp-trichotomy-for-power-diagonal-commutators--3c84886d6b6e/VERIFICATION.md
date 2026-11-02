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
Exact-rational finite-matrix/lag cross-checks at \(\alpha=1\) and several rational parameters are implemented in the standalone `check.py`, using only the Python standard library. All comparisons were executed on the packaged source. Additional finite positive-term diagnostics inspect coefficient decay and bound the exact classical corner.

The infinite-dimensional statements instead follow from the paper's explicit lag formula, dominated coefficient asymptotics, and Abelian summation. A finite program cannot verify convergence for every dimension or determine novelty. Independent assessment has not been performed.
