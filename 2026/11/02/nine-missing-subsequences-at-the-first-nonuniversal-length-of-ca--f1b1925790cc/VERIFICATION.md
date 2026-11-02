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

## Reproducibility checks

Run `python3 checker.py`. The script constructs canonical alternating-gap words at six even values of the number of ones and binary Cantor iterates at three ranks, enumerates all binary target subsequences at the two relevant lengths, and checks complete universality and exactly the nine specified missing words. It also checks 27 larger-gap variants for six ones. The finite checks independently test the formulas; the all-rank result is established by the proof in `RESULT.md`.

## Scope and limits

The checker is an executable finite test, not a proof for unbounded length; the proof derives the general statement and supplies explicit base witnesses. Independent scientific audit has not been performed.
