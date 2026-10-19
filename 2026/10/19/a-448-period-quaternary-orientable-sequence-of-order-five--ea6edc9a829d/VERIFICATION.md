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

The complete witness is in `witness.txt` (\(448\) characters). Run `python3 verify.py` alongside it. The checker exhausts the \(448\) circular factors of length \(5\), verifies no palindrome or pair of reversal-equivalent factors, independently builds the circular windows in two ways, and checks all four symbol counts are \(112\). Its exact output is included in `verification_output.txt`.

**Logical conclusion:** the supplied cyclic word is orientable of order five with least period \(448\). This proves a constructive lower bound on the maximal period, not that longer cycles are impossible. No optimization-solver output or external certificates are required. This is a self-review only. Independent audit has not been performed.
