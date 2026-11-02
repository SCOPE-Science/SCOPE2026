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
# Reproducibility and limitations

Run `python3 verify.py` using only the Python 3 standard library. This checks numerically the number of stationary points, signs of the integral rising-time imbalance, the quadrature-phase closed-form duration, the small-amplitude coefficient, the cubic derivative moment, the critical square-root coefficient, and zero-asymmetry symmetry phases. Observed output: `PASS: 54 root-count/sign checks; phase-locked formula;` and `quadratic coefficient, cubic moment and critical scaling checks`; the benchmark duration excess is 0.134074996409853 for \(a=1\), \(\phi=\pi/4\).

The proof, not the finite numerical tests, establishes the exact sign for all \(0<a<2\) and all phase values. Critical terms use closed-form algebraic and trigonometric identities. No independent audit or empirical comparison has been performed. The limiting expansion is one-sided; no extension past the degeneracy is claimed.
