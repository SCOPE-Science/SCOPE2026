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

# Verification and reproducibility

The self-contained proof is in `RESULT.md`; its essential identity follows by decomposing a zero-sum vertex coefficient vector into constant part sums and zero-sum within-part residuals. The finite-dimensional Rayleigh bound and secular equation then prove the variable-exponent theorem, including the exact rank drop of the Schoenberg Gram matrix. For \(K_{4,2,2,2}\) at \(2^p=3/2\), the explicit zero-sum witness has exact quadratic value \(3/8\) while each two-part induced graph satisfies \(2^p\Lambda_{ij}\le15/16<1\).

To replay the supplemental checks, run `python3 checker.py` using Python 3 standard library. It tests 315 seeded rational zero-sum vectors across seven nontrivial part profiles, the exact witness, the full and pair threshold ratios, and strictness of all relevant pair restrictions. The tests passed in the packaged working tree. Finite checks do not certify all parameters, exhaustive originality or independent validation.
