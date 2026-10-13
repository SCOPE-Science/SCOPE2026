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

The accompanying `verify.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks the concrete \(\kappa=16\) witness, not the quantified theorem by finite enumeration.

The checker verifies: the displayed matrix and right-hand side; the Stieltjes off-diagonal sign pattern; exact positivity of all leading principal minors; the relation \(B=I-A/16\); the five look-ahead Nesterov iterates with \(\beta=3/5\); the exact negative value \((x_5)_1=-77/31250000000\); the exact nonnegative solution of \(Ax=b\); the path identities \((C^3)_{14}=1\) and \((C^4)_{14}=6\); and independent evaluation of the degree-four iterate polynomial.

The universal claims for all SPD Stieltjes matrices and all \(\kappa>9\) are established analytically in `RESULT.md`. The finite checker is a reproducibility aid and is not an exhaustive proof over matrices, dimensions, or condition numbers.
