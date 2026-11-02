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

# Finite checks and logical boundary

The source file `verify.py` runs using Python 3 standard library only and produces `verification_output.txt`. It checks all \(4^4=256\) four-letter words and all \(4^3=64\) possible deletion outputs with exact rational arithmetic. It verifies total dual weight \(25\), the 15 equality-pattern sums and exactly four tight patterns. It separately verifies that every tight `0120` word produces exactly two nonconstant palindromic descendants with a shared outer symbol while no other tight word produces any. Finally it confirms all 24 listed codewords have disjoint deletion-descendant sets and jointly cover all 64 length-three words.

The program’s finite scope is sufficient for the finite equality-pattern classification and for checking the explicit witness. It is not used as a substitute for the upper-bound proof: that proof requires showing that any alleged 25-word correcting code would exactly cover all length-three outputs and then partition a set of three palindromic descendants into pairs, which is impossible. Independent mathematical validation has not been performed.
