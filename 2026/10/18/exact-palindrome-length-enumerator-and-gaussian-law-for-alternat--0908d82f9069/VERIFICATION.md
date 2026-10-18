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
# Reproduction of finite checks

Execute `python3 verify.py` with Python 3.9 or later, using only the standard library. The program does three logically distinct checks: complete direct subset-position enumeration for every prefix through length 17; independent recurrence extraction from the rational generating function against a half-word combinatorial computation to length 75; and agreement of the specialization \(t=1\) with the known binary alternating-word Fibonacci totals through length 75. Expected final line: `VERIFY_OK`.

The rational generating function and Gaussian limit are proved symbolically in `RESULT.md`. The direct subset enumerations are finite checks, not evidence of an infinite theorem by themselves. There is no independent external validation; the mathematical assessment is a self-review only.
