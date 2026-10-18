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

# Verification notes

The attached `verify.py` was executed with exact rational arithmetic for all integer dimensions \(2\le m\le16\), checking every antipodal prefix/suffix identity, every apex/interior replacement identity, and the determinant magnitude \(1/2\). It also compared convex-hull volume losses with the exact \(2^{m-2}\) prediction independently for seven dimensions \(2\le m\le8\) when SciPy was available. The execution reported `VERIFY_OK`. The complete proof is symbolic; the finite experiment cannot establish the general theorem. Prior results on directed-edge and root-polytope faces and Catalan volumes were inspected for coverage; an equivalent older historical statement cannot be categorically excluded. Independent mathematical validation has not been performed.
