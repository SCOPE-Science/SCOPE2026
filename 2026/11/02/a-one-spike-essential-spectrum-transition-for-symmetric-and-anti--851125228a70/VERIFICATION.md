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

# Mathematical verification

The analytic argument has four checkable steps: reduction to self-adjoint reflected Jacobi blocks; exact Chebyshev formula for both boundary resolvent entries; uniform exterior spectral exclusion; and parity-specific orthogonal Weyl sequences for the band and detached points. The half-line recurrence and threshold arithmetic are written explicitly in the proof.

`VERIFY.py` is a standalone finite-section corroboration script, using Python, NumPy, and SciPy. Invoke `python VERIFY.py` in the directory containing the script. Its completed run reported `PASS: 2371 deterministic finite and recurrence assertions`. It checks all small folded blocks in several spike regimes and quantitative approach to the predicted detached points. Numerical checks do not establish infinite-dimensional essential spectral statements, and no external independent audit has been conducted.
