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

The algebraic normalization \(K_\alpha(z,w)=(1-z\overline w)^{-(\alpha+2)}\), incidence parameter \(\cos\phi=\sqrt{1-d^2}\), multiplier \(M_\alpha\), and limiting gamma constant are derived in `RESULT.md`. The `verify_chord.py` script re-evaluates the multiplier maximization for four allowed exponents and checks its grazing convergence at several offsets; the execution output was `CHECK_OK: endpoints, variational max, glancing asymptotic`.

This is a finite sanity test, not an exhaustive or infinite certificate. The infinite-dimensional Fredholm essential spectrum follows analytically from the Hilbert--Schmidt remainder estimate, Fourier diagonalization and Weyl sequences. No finite matrix or numerical optimization was substituted for those steps. The essential-norm limit does not assert norm convergence to a nonzero operator at the collapsed chord.
