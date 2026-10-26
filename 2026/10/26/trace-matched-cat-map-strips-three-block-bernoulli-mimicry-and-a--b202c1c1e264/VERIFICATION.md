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

Run `python3 verify.py` with standard-library Python. The program computes exact normalized Haar areas using rational vertices and clipping by linear inequalities. It exhausts all \(q^3\) three-word cases for \(q=3,4,5\) and checks all \(q\) four-word cases `000d` for the same traces. The code tests exact `Fraction` equality rather than floating-point tolerance and also checks representative trace-\(q\) matrices for determinant one.

The analytical proof, not these finite tests, establishes the general statement for every integer \(q\ge3\), every trace-\(q\) determinant-one matrix, and every nonzero integer observation row. The tests cannot establish originality or unrestricted correctness on their own. The full text of Percival–Vivaldi (1987) was not available for a complete priority comparison. Independent audit has not been performed.
