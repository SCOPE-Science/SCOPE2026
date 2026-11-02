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

# Verification details

Execute `python3 verify.py`. This standalone program uses only Python's standard library. It checks the eight modular residues required in the proof at exponent \(2^{10}\) and the exact even coefficient identity \(8128\); it tests 165 large modular Stirling differences across \(n=10,11,12,13\), including explicit collision boundaries, and independently reconstructs three Stirling values from their recurrence. All checks returned:

`VERIFY_OK coefficient_residue=4096 even_binomial_sum=8128 cases= 165 independent_recurrence_pairs= 3`

The recurrence proof of stability modulo \(8192\), the general higher-order valuation bound, and the comparison of exact odd/even valuations are mathematical arguments, not consequences of testing finitely many cases. The equality boundary is a lower bound only. No external audit has been performed.
