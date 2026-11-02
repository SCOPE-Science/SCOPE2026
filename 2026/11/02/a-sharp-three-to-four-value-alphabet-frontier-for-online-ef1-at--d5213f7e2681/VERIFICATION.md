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

The included standard-library checker `verify.py` was executed directly from this package's intended source. It exhaustively enumerates the binary \(n=2,3,4\) cases, every two-agent ternary three-good case, and both possible final decisions in every adaptive four-level branch. See `RESULT.md` for proof of unrestricted cases. No finite enumeration establishes the full arbitrary-\(n\) claim independently, and no external audit has been performed.
