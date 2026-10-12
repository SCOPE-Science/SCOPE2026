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

`verify.py` uses exact binary arithmetic. It checks the affine two-graph parity equations, support size \(2^{n-1}\), two-to-one graphing parametrization, and the incidence-rank identity \(n-c(H)\) through \(n=7\), exhaustive over edge subsets through \(n=5\).

Replay: `python verify.py`

Expected: `VERIFY_OK 8448 exact assertions`

The code verifies the finite linear algebra only; the uniqueness and equal-mass measure theorem is literature input from Braunfeld--Jahel--Marimon.
