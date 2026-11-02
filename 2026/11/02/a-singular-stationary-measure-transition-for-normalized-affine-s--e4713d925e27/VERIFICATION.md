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

# Reproducibility

The accompanying `verify.py` executes exact symbolic identities and randomized finite-orbit tests. Run from the package directory using `python verify.py` and a Python 3 installation with SymPy. Its expected terminal line is `PASS: exact symbolic identities, sphere orbit tests, and stability-side trajectories`.

The exact calculations include the two-cycle factorization, involution identity, meridional derivative, critical Jacobian normalization ingredients, and the stability multiplier threshold. Numerical tests sample four-dimensional ambient vectors across critical, subcritical and supercritical parameter choices. Mathematical completeness follows from the proof in `RESULT.md`, not from finite testing.

No independent mathematical validation or publication-priority certification is claimed. The first source date is the date of the original arXiv submission, distinct from the later journal issue date.
