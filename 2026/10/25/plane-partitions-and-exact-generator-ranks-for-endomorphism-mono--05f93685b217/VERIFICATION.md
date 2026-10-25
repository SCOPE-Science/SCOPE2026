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

The file `verify.py` is a standalone Python 3 program using only the standard library. Running `python verify.py` performs exact generating-series arithmetic and independently enumerates all permissible finite transformation pairs in degrees three, four, five, and six. It explicitly computes simultaneous-conjugation orbits under all permutations, and for degrees three through five checks essentiality via rank-three square roots independently of the theorem's graph criterion. It prints `VERIFY_OK` only after matching all coefficients and listed minimum generator values.

All assertions were run successfully on the embedded candidate package. The general statement for every \(n\ge5\) is supported by the written orbit-bijection and the prior minimal-generator reduction, not by the finite experiments. No independent external audit has been performed.
