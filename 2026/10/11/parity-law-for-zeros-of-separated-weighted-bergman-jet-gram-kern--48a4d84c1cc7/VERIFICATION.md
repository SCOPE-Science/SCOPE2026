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

# Reproducibility checks and limits

The proof's exact structural steps are: the weighted half-plane Bergman kernel normalization; the mixed-derivative Pochhammer identity; the four-term reduction to a quadratic in \(t^d\); strict gamma log-convexity for distinct derivative orders; exhaustive arguments of all \(d\)-th roots; and surjectivity of the reciprocal-difference coordinate onto the lower half-plane.

The companion `check_twojet.py` was executed from the actual packaged source, using `mpmath` at 55 decimal digits. It reported successful agreement of four direct Fourier–Laplace integral evaluations with the closed mixed-derivative kernel formula and success in 560 root-count tests, including boundary roots for odd gaps with real coefficients. The integral discrepancies were all below \(10^{-25}\) in relative size. To reproduce, execute `python -m pip install -r requirements.txt`, followed by `python check_twojet.py`, from the directory containing both files.

These tests verify representative normalizations, signs and counts. They are not exhaustive across continuous weights, complex coefficients or unbounded derivative orders. The proof, not the tests, covers those infinite ranges. Independent external audit or validation has not been performed.
