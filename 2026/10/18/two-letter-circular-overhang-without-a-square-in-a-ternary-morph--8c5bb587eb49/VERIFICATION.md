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

The standalone `verify_cyclic_overhang.py` program requires only Python 3. It was run on the actual packaged source text and completed successfully. It checks all twelve seed-window positions in the explicitly written sixth iterate; for every \(k=3,\ldots,8\) and \(a\in\{0,1\}\), it searches the length-\(17991\) prefix for every circular overhang and tests absence of the designated square. It also checks forbidden two-letter factors in that prefix.

These are finite reproducibility checks only. The proof for every \(k\ge3\) is the lifting lemma plus the suffix-code descent and is supplied in `RESULT.md`; no finite enumeration is treated as an infinite certificate. No independent audit has been performed.
