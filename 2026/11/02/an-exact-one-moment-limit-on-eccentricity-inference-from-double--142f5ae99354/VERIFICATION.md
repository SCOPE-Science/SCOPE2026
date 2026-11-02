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

# Verification and scope

Run the included `check.py` using Python 3 with the standard library only. The executed file passed exact-rational equivalence and non-equivalence checks for the witness populations, direct event-intersection quadratures for five finite ensembles, six Fourier harmonics, zero-odd/sine coefficients, density normalization, and analytic first-harmonic inversion. The numerical check uses finite midpoint integration and does **not** prove the continuum result; exact formulas in `RESULT.md` provide the proof for arbitrary probability measures.

The source equations refer to an ideal geometric conjunction approximation and require \(\eta<1-e\). Reproduction needs no external observational dataset. Claims about photometric detectability, empirical inference, and nonuniform orientation priors are not tested or proved.
