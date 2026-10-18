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

# Reproducibility and limits
The accompanying `panhandle_verify.py` is a self-contained Python 3 program using only `fractions.Fraction` and `itertools.combinations`. Running `python3 panhandle_verify.py` enumerates 140 parameter triples, 23,440 incidence-vector vertices, and 616,260 exact support/containment checks. It independently verifies both the proposed candidate centers and all coordinate/tail support extrema. It is not a proof by exhaustive finite experimentation: the proof for all integer parameters is in `RESULT.md`.

The published Proposition 4.4 halfspace description is explicitly identified as an imported mathematical premise and a primary source. The reduction from reflection containment to a linear system, the matching lower and upper bounds, and the equality-stratum analysis are laid out in full in the result. No computer algebra, nonstandard libraries, random sampling, or unrecorded search-table data are needed to reproduce the local checks. Independent audit has not been performed.
