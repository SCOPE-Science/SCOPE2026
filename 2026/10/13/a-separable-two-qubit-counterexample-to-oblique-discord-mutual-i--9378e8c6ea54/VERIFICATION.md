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

Execute `python3 verify.py` with a standard Python 3 interpreter. The verifier checks exact rational input and output Alice matrices, verifies both normalized basis vectors and the defining dual-basis action, establishes the unnormalized success probability \(659/867\), computes the characteristic discriminants of all three relevant qubit matrices, and checks that the physical success-branch effect has spectrum \(\{5,5/9\}\) before common rescaling.

For the decisive entropy difference, the routine never relies on floating-point comparisons: the square roots are enclosed by integer inequalities at denominator \(10^{10}\), and each natural logarithm is bounded by an exact Fraction expansion and a proven atanh-series remainder. With 12 terms after dyadic argument reduction, the generated rational lower bound is strictly above \(1/30\) nat and the upper bound strictly below \(1/20\) nat. Only the human-readable approximations of the rational bounds use floating-point conversion.

The proof concerns one finite-dimensional counterexample, not a completeness or classification result. No external audit or certification is represented.
