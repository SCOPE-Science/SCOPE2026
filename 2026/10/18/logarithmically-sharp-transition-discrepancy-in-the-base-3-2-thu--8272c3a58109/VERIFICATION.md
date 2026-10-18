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

# Reproducibility and limits

Run `python3 verification/check_discrepancy.py` using Python's standard library. The checker constructs 150,000 original word symbols, sums adjacent transitions directly over every prefix, and verifies their normalized discrepancies against a separately derived short recursion. It also checks all nine two-step transition cases and exact contraction inequalities for every length from two through 150,000. Finally it tests the explicit base-four/base-nine repunit witnesses for the first 120 positive indices using arbitrary-precision integer arithmetic, confirming both legal-residue chains and exact \(2j\) discrepancy gaps.

The recorded output is in `verification/check_output.txt`. These are finite tests and cannot certify the infinite family on their own. The proof in `RESULT.md`, particularly the two-step identity and the repeated affine transformation, supplies the unbounded quantifiers. No formal proof assistant, external mathematical referee, or independent audit was involved. Historical originality remains subject to independent validation.
