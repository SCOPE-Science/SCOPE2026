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

Run the supplied \(\texttt{verify.py}\) under Python 3 with NumPy and SciPy installed. It uses the full forward Markov transition operator on all two-bit configurations for each of six graphs, computes the exact-pair terminal absorption distributions numerically using sparse linear solves, and separately checks the proposed ancestral six-class stationary masses with rational arithmetic. The forward transition builder does not use the backward-ancestry formulas. Test outcome at package creation: 3,648 absorbing-pair outcome comparisons passed with tolerance \(3\times10^{-10}\); 196 exact-rational pairs passed the normalization and balance tests. Tested small graphs do not establish the general theorem; the proof in RESULT.md does. The star correlation and large-size limits are algebraic consequences, not empirical extrapolations. No external independent audit is claimed.
