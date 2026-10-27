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

The accompanying `check.py` constructs the channel directly, enumerates all received vectors produced by each source word, and builds exact parent sets. It checks each positive inverse multiplicity, the full consistent-receiver distribution polynomial, the exact number of inconsistent singleton receivers, and the sharp worst-case value. The included `check.out` contains the recorded outcome and parameter cases. Run `python3 check.py` from the directory containing these files.

The enumeration is finite; the proof in RESULT.md establishes the unrestricted parameter theorem. No external or independent validation is claimed.
