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

# Reproducible scientific checks

The complete standalone program is `checks/check_spectrum.py`. It requires Python 3 and NumPy, with no network access or downloaded scientific data. Run `python checks/check_spectrum.py` from the directory containing `checks`.

The program constructs the two-by-two stationary drift and diffusion matrices directly from binding, dissociation, catalysis and substrate-input stoichiometry, and independently inverts the spectral resolvent. Across 1,200 deterministic-seed random draws spanning five decades in rate constants (including the zero-dissociation boundary), it checks the full and heuristic rational spectral formulas, their difference factorization and sign criteria and the zero-frequency identity. It separately constructs 100 positive physical steady states, solves their stationary Lyapunov equation as a four-by-four linear problem, and checks the substrate variance against the source formula. It reports `PASS 5000 independently computed comparisons; max_rel=3.047e-09` when executed with its deterministic inputs. Arithmetic uses standard floating-point precision with stated tolerances; the reported maximum relative discrepancy is not an error bound for arbitrary parameter values.

An independent symbolic manipulation verifies that subtracting the two exact rational spectra yields the claimed quadratic polynomial in squared frequency, with symbolic residual exactly zero. The universal theorem is analytically proved by positivity of its coefficients and the elementary root-sign classification; the random numerical checks only test implementation consistency and physical normalization. No external independent audit was performed.
