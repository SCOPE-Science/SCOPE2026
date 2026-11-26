---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The bundled standalone `wheel_price_verify.py` checks the rotational spectral objective against finite Laplacian inverses (exact rational arithmetic for the matrix calculation). Its fixed-order cheap-rim section compares the predicted coefficient against numerically minimized samples for \(n=3,5,8\) at \(t=10^{-8}\). Those sample comparisons use floating-point trigonometry and bisection, not symbolic limit certificates. Its other checks include the known boundary derivative and fixed-price allocation law. The proof of the cheap-rim law and the exact identity for the inverse rim eigenvalue sum are in `RESULT.md`; the large-wheel-then-cheap-rim limit invokes the cited fixed-positive-price theorem.
