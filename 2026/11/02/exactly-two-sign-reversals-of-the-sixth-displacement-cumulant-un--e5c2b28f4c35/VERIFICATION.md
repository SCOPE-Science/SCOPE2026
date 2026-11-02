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

# Verification instructions and limits

Run `python verify.py` after installing `requirements.txt`. The checker independently reconstructs the sixth Taylor coefficient from the analytic angular Fourier recursion using exact polynomial arithmetic, compares it to the stated rational function, verifies the second-cumulant normalization, computes the exact zero-reset sixth-cumulant limit, counts the polynomial sign changes, and tests four exact rational root brackets. An additional numerical Fourier-matrix/Cauchy-coefficient calculation compares the full operator's first eleven Fourier modes in both directions at five different positive parameter values. These finite comparisons are useful diagnostics but cannot certify the infinite-dimensional theorem; the exact recurrence and the elementary positive-root argument are the proof.

The long-time conclusion assumes the standard analytic principal-eigenvalue spectral separation for a uniformly elliptic compact-angle Markov process with bounded resetting. The full scientific and literature-priority assessment has not been independently audited; the same dynamics' previously known low-order moments are attributed to the cited literature. The verification does not use finite trajectory data as a substitute for proof.
