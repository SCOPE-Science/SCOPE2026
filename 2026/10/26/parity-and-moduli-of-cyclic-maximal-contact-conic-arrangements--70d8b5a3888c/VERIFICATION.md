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
The normal-form calculation is deduced algebraically for all \(n\ge3\); `verify.py` supplies independent exact finite witnesses, not an infinite proof. The script verifies characteristic-zero cases of lengths \(4,6,8\), odd characteristic-zero closure obstructions of lengths \(3,5,7\), and characteristic-two cases of lengths \(3,5,7\) over \(\mathbb F_2\) or \(\mathbb F_8\). It verifies smoothness by the nonzero mixed coefficient in characteristic two and tests every pair's quadratic difference. The exact computation printed `VERIFY_OK`. The theorem requires algebraic closure for extracting square roots and for geometric point uniqueness.
