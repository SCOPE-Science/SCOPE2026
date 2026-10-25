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

The standalone `check.py` verifies the symbolic discriminant, the real-root parameterization and its derivative, and branch optimality with deterministic numerical comparisons of eigenvalue spectra. The numerical suite also compares the original four-dimensional physical state matrix with the reduced cubic on sampled positive masses and spring constants. Run with `python check.py`; dependencies and minimum versions appear in `requirements.txt`.

Finite spectral comparisons cannot prove uniqueness over continuous parameters or exclude an undiscovered prior publication. Both are handled, respectively, by the mathematical proof and by a limited, expressly nonexhaustive literature comparison. There has been no independent audit.
