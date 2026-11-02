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

Exact-rational standalone check: `python3 verify.py`. The check enumerates the rays determined by the linear switching relations in the two leaf differences, compares the exact maximum with the theorem formula for 216 positive mass triples, and evaluates each explicit extremizer. It also evaluates the counting-measure and strongly imbalanced-center benchmarks. These finite checks cannot by themselves prove the theorem for all positive real masses. The symbolic case analysis and continuity/monotonicity proof are in RESULT.md.
