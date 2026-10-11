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
# Verification of the sharp two-sector sum inequality

The analytic proof establishes the claim for every bounded operator on any complex Hilbert space; it uses no finite-dimensional reduction, discretized angle grid, or numerical optimization. Its crucial identity is
\[
1+r^2+2r c=(r+c)^2+(1-c^2),\qquad c=\cos(\alpha+\beta).
\]
If \(c\ge0\), the left side is at least \(1\). If \(c<0\), the right side is at least \(1-c^2\), with equality at \(r=-c\in(0,1)\), furnishing a dimension-one saturation. Interchanging the two scalars yields the max formulation. Taking a supremum over unit vectors proves the operator result.

The standard-library script `verify_sector_sum.py` verifies the square-completion identity as a formal polynomial over the integers, the exact rational identities for the sharp \(120^\circ\) separation witness, and the elementary rational inequality for positive scalar perturbations. Run: `python3 verify_sector_sum.py`. Output: `SECTOR_NUMERICAL_RADIUS_SHARP_PHASE_OK`.

The certificate is an algebraic replay check and does not certify the literature comparison or constitute an independent audit. The unrestricted weighted numerical-radius case has not been proved here. An unindexed equivalent result in the operator or complex-plane geometry literature remains possible.
