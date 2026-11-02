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

# Reproducibility checks

Run `python verify.py` in the directory containing `verify.py` after installing the stated SymPy dependency from `requirements.txt`. The verifier derives the transfer matrices from four-node Lagrange differentiation independently of its published-coefficient derivation, checks all rational identities by symbolic simplification, and confirms reciprocal symmetry and singular-ratio limits. Its completed output was:

`VERIFY_OK: symbolic recurrences, Schur factors, reciprocal symmetry, endpoint sharpness, 7 eigenvalue spot checks`

The seven rational-ratio samples are illustrative only; the proof of the continuum of ratios is the strict polynomial-positivity argument in `RESULT.md`. The verified claim is confined to homogeneous BDF3, fixed positive alternating ratios, and two-step *spectral* damping. No independent scientific verification has been performed.
