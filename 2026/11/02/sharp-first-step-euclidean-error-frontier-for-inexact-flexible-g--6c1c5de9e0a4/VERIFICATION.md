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

Run `python3 verify.py` from the directory containing this file. The verifier requires only the Python 3 standard library and prints `VERIFY_OK` upon successful completion.

The script checks 99 exact-rational projection/algebra instances and 27,461 numerical instances, including attained two-mode amplification, critical thresholds, the plateau value, and comparisons of the derived closed form against a discrete tolerance grid. It operates directly on a two-dimensional real SPD system with the specified inexact first preconditioner action; the same matrices appear in the proof. Floating comparisons use explicit tolerances and are not interval arithmetic.

The general claim is established analytically by the FGMRES projection identity, the two-dimensional SPD spectral-compression bound, the singular-vector attainment construction, and a one-variable maximization. The empirical checks neither certify infinite domains nor establish historical originality or correctness of floating-point FGMRES implementations.
