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
# Finite verification

The accompanying `artifacts/verify.py` is standard-library Python using integer arithmetic only. It checks complete defining gcds for \(2\le k\le160\); computes all prime-adic minima across every \(2\le q\le n\) for \(3\le n\le1200\); and checks the explicitly constructed valuation-attaining coefficient for each qualifying prime-power component for \(3\le n\le12000\). The complete finite replay output is embedded as `artifacts/replay.txt`. These checks verify arithmetic and implementation, while the infinite claim is established by the symbolic interpolation, Kummer and digit-sum proof.
