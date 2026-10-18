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

# Verification and limits

The infinite-dimensional proof uses norm-analytic differentiation of the square root at a strictly positive operator, the inverse Sylvester integral, the unilateral-shift identity \([S,S^*]=-P_0\), and explicitly normalized approximate endpoint eigenvectors. Each is written in `RESULT.md` and is independent of numerical simulation. The formula \(AL+LA=i[A,B]\) and the projection signs have been reconstructed directly.

The standalone script `verify.py` checks 79 finite-dimensional instances in exact complex dyadic arithmetic. It tests the rank-two first derivative and the Sylvester equation and reports `PASS`; finite tests do not verify the infinite-dimensional conclusions. The proof gives a lower bound \(\liminf_{t\downarrow0}d_+(t)/t^2\ge6\) but does not compute the exact limit. No uniform-in-dimension remainder is claimed. No independent review has been performed.
