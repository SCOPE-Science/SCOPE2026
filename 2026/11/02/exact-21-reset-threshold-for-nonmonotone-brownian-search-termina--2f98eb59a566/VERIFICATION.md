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

The reproducibility file `verify.py` checks the nonstandard global inequality using exact rational arithmetic only. Run `python3 verify.py` in this directory. It reports 159 dyadic intervals considered, 80 disjoint accepted leaves spanning \([1/2,19/20]\), maximum depth 10, and the strict lower witness for \(A_{22}(6/7)>2\). No Monte Carlo or floating-point data enter the certification. Elementary endpoint and monotonicity arguments remain mathematical proof obligations explicitly written in `RESULT.md`.

The derivation concerns the mean stopping time at either absorption or exhaustion of the reset budget. It does not prove a fixed number of positive-rate turning points beyond the existence of a minimum and later maximum, and it does not establish success-conditioned search performance or independent external validation.
