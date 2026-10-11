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

# Mathematical verification and reproducibility

The universal proof is the positive John contact certificate in `RESULT.md`: for \(k\ge1\), all \(k^2+2k\) normalized facet contacts lie on the unit sphere, the positive weights sum to the identity of size \(2k\), and their first moment vanishes. The key exact identities are \(2a+t=1\) and \(t^2=a^2(2-1/k)\).

Run `python3 verify_john_order.py` with the separately installed `numpy` and `sympy` Python libraries. The code independently constructs the inverse matrix from the claimed parameters, verifies polynomial divisibility by \((2k+1)t^2+(4k-2)t-(2k-1)\), and checks every facet normal and both John matrix identities for all \(1\le k\le60\). Its expected concluding line reports **77,470** tested facet instances. Float tolerances and the finite range are explicitly visible in the script.

This script is not an exhaustive enumeration over all dimensions and its numerical tolerance is not an exact certificate for those dimensions. The formal polynomial checks are symbolic, while the geometry for arbitrary \(k\) follows from the written algebraic proof.
