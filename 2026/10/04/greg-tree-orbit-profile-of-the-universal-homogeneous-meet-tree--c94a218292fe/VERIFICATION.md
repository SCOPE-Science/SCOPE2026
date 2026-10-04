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

The proof is structural. The bundled script `artifacts/verify.py` supplies bounded arithmetic and small-object checks only.

It performs three checks:

1. Canonical enumeration of rooted Greg trees on labeled black vertex sets of sizes \(1\) through \(5\), using set partitions at each possible black or white root.
2. Exact rational coefficient recursion from \((1+x)e^{G(x)}=1+2G(x)\) through degree \(10\), compared with the published initial values of OEIS A005264.
3. Stirling transformation of the injective profile, including the first four all-tuple orbit counts \(1,4,32,416\).

Expected successful terminal line: `VERIFY_OK`.

Finite agreement does not prove the all-\(n\) bijection. The theorem depends on the proof that tuple-generated meet-closures are exactly labeled rooted Greg trees and on ultrahomogeneity of the Fraïssé limit.
