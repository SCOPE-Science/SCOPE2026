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

Reproduce with `python verify.py` using Python 3 and SymPy. The checked computations are exact and deterministic: six Gram charts confirm the Cauchy–Binet sum of squared maximal minors equals the Gram determinant and confirm all entries of the Jacobian/cofactor identity by symbolic differentiation and substitution. Every allowable radical stratum for \(4\leq n\leq15\) and \(2\leq k\leq n-2\) passes the symbolic dimension formula.

Expected output:

`VERIFY_OK cauchy_binet_and_jacobian=6 exact_codim_dimension_profiles=verified n=4..15 k=2..n-2`

The complex-geometry assertions for infinitely many \((k,n)\), the irreducibility claim, and the generic ordinary-double-point type are justified by the proof in `RESULT.md`, not computationally certified by these finite samples. No independent audit was performed.
