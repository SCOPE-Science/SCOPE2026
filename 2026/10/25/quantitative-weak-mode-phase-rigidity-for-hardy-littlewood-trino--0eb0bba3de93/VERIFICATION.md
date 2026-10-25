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

# Reproducibility and scope

Execute `python verify_weak_mode.py` with Python 3 and SciPy installed. The observed output was:

`VERIFY_OK gamma_integrals=4 phase_grid=32 linear_slopes=4 radius_bounds=4`

These checks compute the signed gamma quotient independently of the cosine integral for four degree/exponent pairs, verify four explicit positivity-radius parameters, sample 32 phase intervals, and check four weak-mode contrasts. The numerical tests use finite precision and are corroborative only. The uniform angular second-derivative inequality, exact beta integral, and gamma-ratio argument in RESULT.md supply the infinite proofs. At higher degrees the illustrative phase-grid amplitude exceeds the deliberately conservative certified threshold; this is not used to enlarge the proved parameter range.

The displayed phase response concerns the \(p\)-th power integral, not its positive \(p\)-th root, although strictly increasing transformations preserve its phase extrema. The exact contrast is taken first at \(\rho\downarrow0\), then at large degree with fixed fractional exponent; no interchange of these limits is claimed.
