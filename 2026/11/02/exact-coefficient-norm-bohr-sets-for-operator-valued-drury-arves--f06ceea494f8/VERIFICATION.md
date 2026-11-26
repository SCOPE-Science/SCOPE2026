---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The kernel expansion gives squared monomial norms alpha!/|alpha|!. Testing the multiplier on each unit constant vector bounds each coefficient norm by the reciprocal monomial norm. For a normalized monomial, the product with another basis monomial has squared norm equal to the factorial norm ratio in RESULT.md:52–59. The numerator is one term of the multivariate Vandermonde sum, so the weight is at most one; the vacuum attains one. Distinct shifted basis vectors are orthogonal. The diagonal sum of these norm-one multipliers is contractive on a separable coefficient space and saturates all coefficient norms. In countably many variables the degree-n diagonal block is bounded by ||z||_2^n, so there is no analytic convergence problem for the operator series; the norm majorant itself may diverge, in which case finite diagonals give arbitrarily large values. For finite d, Cauchy–Schwarz on each degree bounds the sum by a polynomial factor times ||z||_2^n. The axial profile, degree-four nonradial witness, first-degree large-support obstruction, and diag(1,w_j) unanchored witness follow. The disk 2-by-2 witness is inside the claimed earlier radius and has norm sum 10/9. Independent corroboration: `python3 -B /workspace/review_checks.py 3` checked 1,450 exact factorial ratios and exact inequalities for the two witnesses; finite checks do not replace the proof. This is not a sharp result for every fixed finite coefficient dimension.

## originality

PASS

The closest known same-space and same-normalization pointwise result is scalar; it does not apply to sums of separate operator norms. The operator-order literature uses a different majorant, and the stronger-looking Allu–Halder disk radius is contradicted within its stated operator-valued class. On the checked evidence the unrestricted coefficient-dimension, zero-anchored, factorial-weighted pointwise formula is distinct. No priority is claimed for the scalar threshold, the normalized-monomial calculation as a technique, or a fixed matrix-size optimum.

## value

PASS

The exact amplification of a natural scalar Bohr problem is not just a radius change: it gives a nonradial pointwise set, loss of every positive Euclidean inradius in infinitely many variables, and a finite counterexample to a plausible norm-sum generalization. The single multiplier attaining all bounds identifies precisely why the scalar estimate does not transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
