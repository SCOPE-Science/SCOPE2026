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

The survival-transform derivation is analytic. Cross-checks implemented in `verify.py` directly reconstruct the first two moment equations from the absorbing backward generator and compare the explicit moments with derivatives of the full Laplace survival transform at high precision for 48 parameter pairs.

The numerical tangency solution agrees with \(q_c\approx1.2286314004819505853\), \(t_c\approx4.1334526383049528347\); the sample ratio \(q=6/5\) gives two positive crossings. Additional sign and curvature evaluations test representative regimes. All finite tests are diagnostic checks, not proofs of all-parameter uniqueness. The complete proof uses strict log-concavity, endpoint limits, and strict parameter monotonicity, detailed in `RESULT.md`.

Third-party prerequisites for replay: Python, `sympy`, `mpmath`. No external data or network is needed.
