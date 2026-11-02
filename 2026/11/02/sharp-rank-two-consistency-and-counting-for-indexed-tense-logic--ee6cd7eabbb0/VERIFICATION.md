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

The ordinary standalone checker `checker.py` recomputes depth-one profiles from explicit finite directed relation tables and compares them with the proposed two-step signature, rather than trusting the construction's nominal labels. It checks every one of the sixteen realizable variable-free one-relation profiles; the unrestricted finite graph enumeration gives cumulative observed counts \(2,8,14,16\) through one, two, three and four vertices. Additional reproducible fixed-seed checks cover cases with two converse pairs and up to three atom colours. Run using `python checker.py` in this directory; the expected final line is `ALL_CHECKS_OK`.

The general proof is symbolic; finite enumeration alone is not a proof for all numbers of colours or converse pairs. The correctness, priority, and value reviews are not independent audits.
