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

# Verification of the mathematical claim

Execute `python check.py` with SymPy installed. The script verifies the closed inverse Gramian, the three required algebraic identities, the strictly positive coefficient certificates, exact signed-affine integrals for 729 positive integer meshes and all three evaluation vertices (2,187 checks), and the limit \(7/3\) for an explicit one-parameter degeneration. All computations use exact rational arithmetic or exact symbolic algebra, not floating-point tolerance.

The universal all-positive-length assertion relies on an algebraic proof valid for real \(a,b,c>0\), not on exhaustive numerical sampling. The script is an ordinary reproducer of the identities, not a separate audit or external certificate. Historical equivalence and novelty comparisons remain limited to the identified literature and accessible records; independent scientific validation has not been performed.
