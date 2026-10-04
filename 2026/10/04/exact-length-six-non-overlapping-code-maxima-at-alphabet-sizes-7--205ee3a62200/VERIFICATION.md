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

Run `python3 verify.py`. The script uses only the Python standard library. It performs two independent finite checks after accepting the published structural reduction as a premise:

1. It exhausts every reduced size state for alphabet sizes \(7\), \(8\), and \(9\), checking the claimed maxima and the complete reduced maximizing vectors.
2. For each alphabet size it deterministically builds a code from a maximizing size vector, forms every proper prefix and suffix appearing in the code, and checks that the two sets are disjoint.

The terminal success line is `VERIFY_OK q=7,8,9 reduced_states=66148 direct_codewords=58455`. The script also checks that the best \(k=5\) Blackburn construction at \(q=9\) has size \(33614\), hence the exact optimum improves it by \(258\).

The verifier does not reprove the published reduction theorem, does not classify all maximum codes, and does not test or claim any value for \(q\ge10\).
