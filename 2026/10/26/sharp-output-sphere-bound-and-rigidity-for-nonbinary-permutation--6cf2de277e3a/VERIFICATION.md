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

# Verification of the theorem

The standalone `verify.py` is standard-library Python 3. It independently creates the union of all permutation outputs across all exactly-length-\(k\) windows and evaluates the endpoint-changing anagram count by multinomial enumeration and inclusion-exclusion. For each input it compares the two sphere cardinalities. Where \(q\ge k\), it additionally checks the sharp bound, the necessity and sufficiency of the repetition-free-window condition, and the exact maximizing-center count. Finite tests include repeated-letter inputs and the strict inequality at nonmaximizers.

The actual execution output in `verification_output.txt` records 43 parameter triples and 100,978 input words and terminates in `VERIFY_OK`. The tests include \(q<k\) instances as cross-checks for the support identity, but do not claim the sharp-maximizer formula in that regime. The full theorem for all \(q\ge k\ge4\) and \(n\ge k\) relies on the written argument, not empirical extrapolation. No external mathematical certification or independent audit was performed.

Reproduction: `python verify.py`.
