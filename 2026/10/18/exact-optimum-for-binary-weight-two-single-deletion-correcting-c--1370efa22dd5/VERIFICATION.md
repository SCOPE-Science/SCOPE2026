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

Run `python3 checker.py` from this file's directory. Its expected stdout is embedded in `checker-output.txt`. The checker enumerates every one-deletion descendant of all constructed codewords for lengths 2 through 96; exact compatible maximum sets are computed from scratch by memoized graph recursion for lengths 2 through 8, and shadow/loop premises are spot-checked through length 24.

The mathematical proof of the infinite theorem is self-contained in `RESULT.md`; the code is finite corroboration only. The proof does not imply uniqueness, other weights, or any stronger edit channel. Independent audit has not been performed.
