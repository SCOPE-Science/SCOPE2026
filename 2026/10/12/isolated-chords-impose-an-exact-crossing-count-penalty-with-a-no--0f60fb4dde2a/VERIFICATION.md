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

The companion standalone `verify.py` is a standard-library exact-rational checker. To reproduce, invoke `python3 verify.py` in the directory containing this document and the script. It enumerates all \(146598\) uniform chord diagrams with \(2\le n\le7\), verifies the exact mixed moment and covariance by direct enumeration, checks \(27\) conditional arc-size cases, and verifies strict sign/decomposition statements for \(499\) integer sizes through \(n=500\).

The exact finite counts are \(3,15,105,945,10395,135135\) at sizes \(2,3,4,5,6,7\). The respective covariances \(\operatorname{Cov}(I_n,X_n)\) are \(-4/9,-1,-32/21,-374/189,-548/231,-3505/1287\). Exhaustive checks are finite; they do not establish the all-size theorem or asymptotic claims. Those follow from the conditioning/counting proof and the ratio-bound tail argument in RESULT.md.

The exhaustive finite checks are separate from the analytic proof, and no independent validation is asserted.
