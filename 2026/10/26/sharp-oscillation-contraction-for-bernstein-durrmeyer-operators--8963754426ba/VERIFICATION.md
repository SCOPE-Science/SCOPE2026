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

# Verification of the mathematical assertion

The complete analytic argument is in `RESULT.md`. Check the following steps rather than treating finite tests as an infinite certificate: every posterior normalization \(Z_k>0\); likelihood-ratio monotonicity with endpoint atoms; single-crossing equality of variation and a CDF gap; stochastic ordering; the convex mixture bound; attainability at two endpoint rows; the common-interior-mass strict inequality; continuous approximation of the measurable extremal indicator; and symmetry of the stationary joint kernel.

Run `python3 verify.py`. It uses exact rational fractions for \(n=1,\dots,6\) and four atomic measures (including endpoint atoms, asymmetric weights, and a degenerate one-interior-atom posterior). It verifies every posterior-pair variation bound, a grid of mixed rows, reversibility/stationarity, and the uniform-measure closed form \(1-2^{-n}\). Expected terminal marker: `ALL_EXACT_CHECKS_PASSED`.

Numerical tests do not certify any universal quantifier or originality. The explicit theorem uses \(\mu((0,1))>0\); measures lacking this property are not included. The single-step coefficient is optimal but its \(m\)-fold power is only a valid bound, not claimed optimal for each \(m>1\). Two relevant historical manuscripts were not retrieved in full, so literature coverage is best-knowledge rather than exhaustive. Independent audit has not been performed.
