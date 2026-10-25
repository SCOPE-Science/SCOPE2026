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

The theorem uses a symbolic spectral-projector derivation valid for arbitrary positive integer part sizes. The scalar stability numerator \((z-3)^2+3\) is positive for all real \(z\ge0\). Combining projectors gives the exact all-step formulas for cross-part and within-part off-diagonal entries. Positive definiteness supplies the remaining diagonals, and the constant eigenvector supplies stochasticity. For the four-vertex path, exact rational functional calculus and a unique-positive-root quartic give the finite positivity boundary.

The standalone command `python artifacts/verify_pade.py`, with `sympy==1.14.0`, checked scalar and multipartite identities symbolically, all distinct four-vertex-path off-diagonal formulas, and 12,760 exact rational entries on 53 independently assembled multipartite graph matrices at four rational steps. A separate path sign transition was checked at three rational steps. All checks passed.

Numerical enumeration does not prove the infinite result, nor does it certify literature-wide originality. No independently conducted mathematical audit is claimed.
