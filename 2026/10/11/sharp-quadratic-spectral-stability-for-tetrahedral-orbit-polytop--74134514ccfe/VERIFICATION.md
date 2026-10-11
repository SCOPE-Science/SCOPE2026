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
The analytic proof was checked from the primary weight formulas and cubic characteristic factor. Its key exact identities are \(p(L)=d^2(2a-1-L)\), with \(L^2=a^2+s^2+d^2\), and \(L^2-(2a-1)^2=((11a-3)(1-a)+4d^2)/4\) for \(a\ge1/2\). These establish the infinite-family claim without enumeration.

The packaged `verify.py` reconstructs the cubic coefficients exactly on a rational grid, checks the completed-square identity exactly, and performs a numerical symmetric-eigenvalue sanity check. Its finite output is supporting reproducibility only, not a completeness certificate for the real parameter simplex.
