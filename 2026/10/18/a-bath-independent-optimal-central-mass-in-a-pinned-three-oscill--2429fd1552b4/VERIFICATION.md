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

# Verification and scope of computational checks

Run `python verify.py` with Python 3 and SymPy to reproduce the algebraic checks. The script constructs the reduced stationary Sylvester equations from the displayed physical drift matrices and evaluates their exact determinant, solves for the required cross covariance, and verifies the proposed rational conductance and reciprocal-conductance square identity symbolically. It also tests the derivative and both rational special values for unit friction and unit pinning.

As a separate implementation, the script reconstructs the full six-dimensional stationary Ornstein–Uhlenbeck covariance from twenty-one linear equations for eight rational mass/pinning/friction triples with unequal positive bath temperatures. It verifies the full Lyapunov residual exactly and matches the resulting bath heat currents to the theorem. The mathematical proof of uniqueness applies to all real parameters in the stated domain, not merely the tested values.

The proof has not been independently audited, and the literature-overlap comparison does not guarantee bibliographic uniqueness. No proof of a quantum analogue, an unpinned stationary-position law, or a result for unequal endpoint frictions is provided.
