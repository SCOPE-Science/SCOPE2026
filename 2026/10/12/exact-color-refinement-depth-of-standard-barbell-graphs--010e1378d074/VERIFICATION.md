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
The proof is symbolic and covers every \(m\ge3\) and \(k\ge0\). The accompanying `verify.py` is a separate direct implementation of ordinary color refinement and checks the claimed stabilization depth for all
\[
3\le m\le20,\qquad 0\le k\le80.
\]
It also checks the exceptional stable six-vertex color class in \(B(3,2)\).

The checker returns:

`VERIFY_OK depth_checks=1458 anomaly_checks=1 m=3..20 k=0..80`

The finite computation is corroborative only. It does not establish the infinite theorem outside the tested range, and no claim of external or independent certification is made.
