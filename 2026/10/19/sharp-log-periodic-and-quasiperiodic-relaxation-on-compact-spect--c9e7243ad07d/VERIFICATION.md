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

# Reproducibility and analytical verification

The proof in `RESULT.md` establishes the equalities for every \(b>1\), \(\alpha>0\) and admissible integer time without relying on floating-point computation. For the optimizer, inspect the exact adjacent-ratio identity and the inequalities \(L_b\le nb^{-k_b(n)}<bL_b\). For the sharp phase constants, differentiate the explicit periodic profile and use \(L_b<\alpha<bL_b\). The single-scale density step uses integer approximation to \(L_b b^{j+t}\). The two-scale density step uses irrational-line density followed by logarithmic approximation of real times with integers; this justifies all subsequential limits rather than only bounds.

The optional artifact `verify.py` uses only Python's standard library. It tests seven distinct parameter pairs and 101 integer times for each pair, compares adjacent-coordinate and normalized formulas, checks extremal intervals, tests sample single-scale phases, and evaluates the two-ladder norm identity for three smoothness exponents. A run against the packaged source passed 2,440 finite consistency assertions. The finite tests cannot certify the infinite-dimensional supremum or dense phase conclusions; those are proved analytically.

The single-scale and dual-scale source balls are genuinely compact because their defining positive spectral source operators have entries tending to zero. The original dynamics is strongly stable but does not converge in full operator norm; this is not contradicted by the stated uniform rate on compact source balls. The generalization to arbitrary spectral measures and potential literature equivalence remain unproved.
