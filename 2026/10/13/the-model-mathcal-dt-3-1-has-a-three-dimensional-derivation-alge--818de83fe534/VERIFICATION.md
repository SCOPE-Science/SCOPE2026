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
The packaged checker `artifacts/verify.py` uses exact rational arithmetic and no external symbolic-algebra package.

It reconstructs the three printed products of \(\mathcal{DT}_3^1\), checks all seven tridendriform identities on all ordered basis triples, and then generates the linear derivation equations for all three operations.

Exact row reduction gives rank \(6\) in the nine matrix variables, hence derivation-space dimension \(3\).

The checker verifies that the kernel is spanned by
\[
H=\operatorname{diag}(1,2,1),
\qquad
U=E_{21},
\qquad
V=E_{23},
\]
and checks
\[
[H,U]=U,
\qquad
[H,V]=V,
\qquad
[U,V]=0.
\]

The checker returns `VERIFY_OK`.
