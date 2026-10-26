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

# Reproduction and scope

Run `python verify.py` with NumPy and SymPy. The deterministic program uses a fixed random seed and reports 622 checks, including exact real-integer characteristic-polynomial and Hilbert–Schmidt adjoint identities for small matrix Kraus maps, numerical comparisons for larger complex examples, exact growth comparisons for the noncompact isometry model, and support checks for increasing finite truncations of a noncompact nilpotent-plus-finite-corner example.

These tests concern finite matrices. They are neither exhaustive over operators nor substitutes for Step 1 (norm closure of finite-rank Kraus maps and orthonormal weak-null obstruction), Step 3 (Riesz projection stability and equality of nonzero algebraic multiplicity across distinct Banach ideals), or Step 4 (the Gelfand spectral-radius bridge). The proof requires \(\sum_j\|X_j\|^2<\infty\); no conclusion is claimed for merely strong Kraus convergence.

The independent audit has not been performed. The mathematical proof and provenance are documented in RESULT.md and REVIEW.md.
