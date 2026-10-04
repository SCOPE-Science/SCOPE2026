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

The general claim is checked directly from the defining order.

1. Left translation is free because \(ag=g\) implies \(a=e\).
2. There is one orbit at every level and the quotient order is exactly the total level order, so \(\mathcal K(X_H/G)\) is a simplex.
3. The map \(\rho(g,-1)=(g,-1)\) and \(\rho(g,i)=(g,r)\) for \(i\ge0\) is order-preserving, equivariant, fixes the two-level subspace, and satisfies \(x\le\rho(x)\).
4. In the two-level graph, the geometric orbit has two vertices and \(r+1\) distinct edge orbits, hence first Betti rank \(r\).
5. At level \(1\), the minimal open neighborhood contains \((g,-1)\) and \((gh_1,-1)\), two distinct points with the same quotient image, so the finite orbit map is not a covering.

The included checker stress-tests the formulas on cyclic, Klein-four, and symmetric examples. From the package root, run:

`python3 artifacts/verify.py`

Expected output:

`VERIFY_OK samples=C3,V4,S3 finite_orbit=chain geometric_orbit_betti=1,2,2 quotient_not_covering`

These finite examples verify implementation details and boundary behavior only; they do not replace the symbolic proof for arbitrary finite \(G\).
