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

The reproducibility script `certify.py` uses only Python 3.9+ standard-library modules and exact integers and fractions. Execute `python3 certify.py`; a successful execution ends with `SUCCESS: c > 2.741607; no conditional assumption is used in the constant bound`.

The script checks all 31 even local counts through \(h=64\), independently verifies the counts through \(h=44\) by inclusion-exclusion, and checks the exact rational aggregate, integer-floor finite Euler-product factor, tail estimate and threshold. Exact integer arithmetic makes these evaluations deterministic; the mathematical completeness of the CRT recurrence and tail inequality is explained in `RESULT.md`. No computation of the infinite local series or proof of an unconditional prime-gap asymptotic is attempted.
