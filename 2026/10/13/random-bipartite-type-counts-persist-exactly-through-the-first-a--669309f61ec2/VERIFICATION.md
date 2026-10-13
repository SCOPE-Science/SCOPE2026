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

The argument is exact. For an injective boundary tuple of length \(k=\min(m,n)\), a mixed tuple has fewer than both triggering thresholds and is closed. An all-point tuple triggers precisely when \(m=k\), adjoining exactly \(n-1\) lines; because this is still fewer than \(n\), closure stops. The all-line case is dual. Thus the only enlarged closures are the stated one or two same-sort types and have size \(m+n-1\).

The bundled `verify.py` independently recomputes the bipartite-pattern sequence and its Stirling transform through arity seven and checks the boundary-exception arithmetic for \(2\le m,n\le8\). Its terminal line is `VERIFY_OK 149 exact assertions`.
