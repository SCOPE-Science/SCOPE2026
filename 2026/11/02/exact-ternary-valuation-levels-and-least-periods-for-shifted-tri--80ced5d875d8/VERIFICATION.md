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

# Reproducible checks and limitations

Run `python3 verify_tribonacci_shift_three.py` using standard Python 3. The verifier recomputes the integer matrix power \(M^{13}\), the three root classes modulo \(13\), derivative units modulo three, and unique lifts through \(3^7\). For the first six positive valuation levels it builds all six congruence classes and tests both maximal proper period candidates. An independent recurrence loop checks the valuation prediction at each of the first 125000 indices modulo \(3^7\), with valuations capped at seven.

Recorded result: `VERIFY_OK matrix_power=13 roots_mod13=3,8,10 derivative_mod3=2,2,2 lifted_levels=7 least_period_levels=6 direct_terms=125000 explicit_integer_root=-1`.

The finite tests do not certify all indices or levels. The infinite classification requires the argument using \(M^{13}=I+3B\), the three-adic binomial-series difference bound, and unique zero lifting. No external or independent certification is asserted.
