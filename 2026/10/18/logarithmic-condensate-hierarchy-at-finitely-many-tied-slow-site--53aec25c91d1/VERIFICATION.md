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
# Reproducibility and verification

The accompanying `verify_critical_hierarchy.py` recomputes the finite stationary balance directly rather than trusting the derived transfer or partition formula. Requirements: Python 3, NumPy. Run: `python verify_critical_hierarchy.py`.

The executed checks reported `EXACT_GENERATOR_CASES 60 BALANCED_STATES 1904`, `EXACT_STIRLING_IDENTITIES 70`, and `ALL_FINITE_CHECKS_PASSED`. Numeric runs for three slow sites at slow total \(s=500,2000,8000\) display convergence of the finite rare-sharing coefficient and independent log-exponent CDF values toward the claimed limits; these finite computations are not proofs of the \(L\to\infty\) statements.

Proof-critical infinite assertions checked analytically in `RESULT.md`: (a) directed-ring product invariance and finite irreducibility; (b) polynomial tilt cannot overwhelm geometric large deviations and its central relative variation is negligible; (c) the fixed-column Stirling asymptotic; (d) the harmonic-box joint limits; (e) the leading two-large-site integral and lower-order three-large-site bound; (f) uniformity in the typical slow-mass window for the limit mixing. The limits require fixed \(m\ge3\), \(0<q<1\), \(\rho>q/(1-q)\), and fixed \(\varepsilon\in(0,1/2)\).

No external independent validation has been conducted.
