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

# Computational verification and limits

The standalone `verify_tristate.py` checker performs a symbolic real-resolvent identity (the full three-state complex matrix inverted against the constant vector), checks the exact derivative cubic and its discriminant, isolates the two positive critical roots, and carries out 120 numerical direct matrix solves and nine rate-pattern checks. It was run successfully on the packaged script, with results preserved in `CHECKS.txt`.

The all-real-rate classification is proved mathematically in RESULT.md by real-root signs, not extrapolated from finite sampling. The optional numerical solves are finite corroboration only. The first-public date refers to the identified initial 2016 preprint, not later revisions. Historical-priority uncertainties are in REVIEW.md. Independent audit: not performed.
