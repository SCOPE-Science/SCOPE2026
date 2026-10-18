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

# Reproducibility and scope

Run `python verification.py` from the same directory with Python 3 and the standard library. The actual test execution returned:

`PASS: 512 exact-rational checks; 4 parameter distributions; dyadic transfer, masses, return cylinders and renewal coefficients`

The program checks four finitely supported distributions (one deterministic, three mixtures), including a seven-step contraction depth; 44 transfer equations per distribution; exact closed-form total mass with the infinite dyadic tail; 20 first-return coefficients per distribution; the first 20 renewal coefficients; 12 affine-cylinder Jacobian identities per distribution; and the deterministic-depth covariance identity through lag 30. All rational equalities are exact, not tolerance comparisons.

The unrestricted claims for arbitrary discrete contraction laws, conservativity, iid returns, and stationary covariance come from the written proof in `RESULT.md`. Finite test cases do not certify infinite-support probability laws or measure-theoretic uniqueness. No external independent audit or expert verification has been performed.
