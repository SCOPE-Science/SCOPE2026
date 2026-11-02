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

The proof in RESULT.md establishes the universal bound and the matching constructions for every integer committee size and every admissible real-quality profile.

Run `python3 verify.py` in the extracted package directory; Python's standard library suffices. Expected terminal line:

`VERIFY_OK exhaustive_instances=73710 random_instances=3150 tight_witnesses=49`

The program checks all nonempty voter coalitions directly, rather than substituting the structural lemma in the definition. It checks 73,710 small exact-rational quality/approval configurations, 3,150 seeded rational instances, and 49 tightness instances. Enumeration supports reproducibility but is not a proof beyond the sampled finite domains. Independent scientific audit remains unperformed.
