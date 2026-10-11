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

# Exact rational verification

Run `python3 c6_verify_exact.py c6_exact_certificate.json` in a directory containing both provided files. The checker uses only the Python 3 standard library. It reconstructs all 60 dual vertices from five saturated inequalities, verifies the 12 edge molecules, constructs all 150 norming tensors and 360 norm tensors, verifies each exact rational upper decomposition and its \(17/14\) coefficient bound, and verifies the explicit 5-by-5 rational matrix with numerical radius \(1\) and operator norm \(17/14\).

The finite certificate is mathematically exhaustive because the result independently proves that its enumerated families contain all primal and dual extreme points. Reproducing the calculations verifies the arithmetic steps but does not provide an independent external audit, a complete weighted-cycle formula, or a guarantee that no prior equivalent result exists.
