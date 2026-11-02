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

The finite exhaustive checker `lorenz_verify.py` uses exact integer arithmetic to compare every allocation's partial sums against the three-case formula over 685 small parameter profiles and 2,127,810 labeled assignments, including no-good and single-agent boundaries. A separate exact rational loop probes the nonintegral-ratio construction. These checks confirm instances, not universal quantifiers; the two-step majorization proof in RESULT.md is the source of the theorem.

Run: `python3 lorenz_verify.py`
Expected: `VERIFY_OK profiles=685 assignments=2127810 rational_boundary=all_coprime_pq_tested`

The source paper arXiv:2610.04417v1 and related bivalued-preference literature were read and compared. The finding has only self-review; independent audit has not occurred.
