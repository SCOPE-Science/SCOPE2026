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
# Reproducible checks

Run `python verify.py` using only the Python standard library. The script constructs binary subspaces, checks pairwise-zero intersections, explicitly enumerates all surviving generator columns and the unordered sum-to-target pairs, checks disjointness of the pairs and compares coordinate histograms with the exact four-level theorem. It performs 36 complete configurations including two independent invertible ambient-coordinate transformations in each parameter case. It additionally checks the generator rank and all nonzero message weights for the two \([22,5,10]_2\) witnesses. The accompanying `verification_output.txt` records all configurations and concludes with `DISTANCE_EXAMPLES_OK` and `RECOVERY_SPECTRA_OK 36 exact tests`.

The all-parameter proof is in `RESULT.md`: complement pair counting, simultaneous normal form and subtraction of the deleted columns. These finite tests cannot certify untested dimensions or historical originality. Independent audit has not been performed.
