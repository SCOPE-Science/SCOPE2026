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
# Reproducibility and limits

The enclosed `verify.py` is a standalone Python 3 program using only built-in modules. Run `python3 verify.py` in the directory containing this file and the script. It checks exact rational identities for truncated harmonic partition weights and first renewal moments at cutoffs 2 through 24. It constructs positive partition weights, brackets and bisects the unique escape-rate root for several cutoffs and moving critical parameters, tests finite residuals, and reports the leading and first-corrected predictions. The observed terminal marker is `VERIFY_OK`.

The mathematical proof of uniqueness of the positive root, the uniform leading limit for all \(\theta_n\to1\), and the Euler correction for compact detuning sets is contained in `RESULT.md`. No finite verification run certifies an infinite limit, an exhaustive parameter census, or historical uniqueness of a theorem. The underlying finite determinant identity is explicitly attributed to Knight--Munday. An independent audit has not been performed.
