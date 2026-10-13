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
The proof was checked symbolically before packaging. The universal fixed-step statement is an identity: the off-diagonal entry of \((I-sA)^2\) is \(sc(2-s(a+d))\), while both diagonal entries are sums of squares. The adaptive generic statement is an eigenbasis limit and does not depend on numerical experiments.

The embedded `verify.py` reconstructs the displayed rational/radical witness using exact arithmetic in \(\mathbb Q(\sqrt{19729})\). It verifies the SqS3 norm ratio, the raw squared-stage vector, the completed final fixed-point update, and the exact integer inequalities establishing the negative coordinates. It uses only the Python standard library.

Unproved limits: no claim is made for nonsymmetric maps, dimensions above two, safeguarded/clipped variants, or the excluded rank-one case with zero non-Perron eigenvalue.
