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

The theorem is proved symbolically for every \(p,q\ge3\). The finite computation is a regression check, not an extrapolation or certificate for untested parameters.

Run `python3 artifacts/verify.py`. The script uses only the Python standard library. It constructs every function on the underlying sets for \(P_{3,3}\) and \(P_{3,4}\), filters by order preservation, and computes the induced first-homology rank directly from images of the explicit edge-cycle basis. It checks the closed self-map and rank-profile formulas in both cases. For \(P_{3,3}\), it additionally constructs the full graph whose edges join pointwise-comparable continuous maps and checks that there is one component of size \(375\) and \(576\) singleton components.

Expected output is stored in `artifacts/verification_output.txt`; a successful replay ends with `VERIFY_OK`.

Limits: the enumerations cover only two parameter pairs. They do not prove the all-parameter statement, do not search the literature, and do not establish independent validation. The infinite claim depends on the written classification and homology argument in `RESULT.md`.
