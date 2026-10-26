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

The accompanying `checker.py` uses exact SymPy rational arithmetic and independently constructs the normalized six-state master equation. It verifies the reduced 4-by-4 determinant, reproduces its bond current for three unrelated positive parameter sets, checks the degree bound on the rational numerator in those cases, and reconstructs the exact sharp example at its reversal. The proof of the universal bound is the rank-two adjugate argument in `RESULT.md`; the finite checks do not prove the claim by enumeration.

An independent audit has not been performed. Bibliographic priority remains subject to independent literature review.
