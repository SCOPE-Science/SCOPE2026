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

# Reproducibility

Run `python3 verify.py` alongside `certificates.json`. Only Python standard-library modules are imported. All asserted objects are regenerated from the binary alphabet and exact Hamming weight four.

The run checks all codeword lengths from four through twelve, all codeword overlaps including self-overlaps, every primitive cyclic class at those lengths, and the 1,296 possible choices of unbordered representatives from the displayed six length-twelve classes. It then confirms the number of successful selections after each single-class deletion.

An actual package-path replay completed successfully with `VERIFY_OK`. The reported maxima are `0, 1, 2, 5, 8, 14, 20, 30, 39`; primitive-necklace bounds are `0, 1, 2, 5, 8, 14, 20, 30, 40`. The six-class compatible-transversal count is zero; the respective five-class counts are `3, 2, 2, 3, 3, 3`.

The checker provides a complete finite proof for these parameters. No formal proof assistant, external validation or infinite extrapolation is claimed. Literature-priority checking remains qualified by potentially unindexed historical work.
