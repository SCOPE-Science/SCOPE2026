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

# Reproducible verification

Run `python3 verify.py` with a standard CPython installation; no third-party modules or downloaded data are required. The program checks 416 exact-rational identities for the three asymptotic coefficient equations and the signed lag across four matrices, thirteen integer choices of the anchoring parameter and two nonzero anchors. It additionally checks 36 finite-trajectory assertions on twelve linear systems/parameter choices by comparing simulations at 40,000 and 120,000 iterations, including one-step residual and tracking-lag trends and finite numerical values. The full reported total is 452 explicit assertions.

The exact coefficient identities check key algebraic signs but do not replace the proof of infinite-time convergence. The mathematical proof supplies the missing uniform contraction-product estimate, the summation estimate and the Neumann resolvent expansion. Finite runs do not establish any universal or asymptotic theorem. The code uses double-precision floats for trajectory tests and exact `fractions.Fraction` arithmetic for coefficient identities; the matrix inverse routine is restricted to two-by-two examples in the checker only. The theorem covers every finite dimension independently of this checker.
