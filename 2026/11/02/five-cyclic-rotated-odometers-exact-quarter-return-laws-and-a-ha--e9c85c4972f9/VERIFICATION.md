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

# Verification

Run `python verify_fifths.py` from this directory using Python 3. The script is standalone, relies only on `fractions` and `collections`, and compares complete exact-rational interval partitions, times and moments for five rotations. It verifies each interval of the five-cycle island against its exact affine image, and verifies that the whole interval is partitioned by the periodic island and the first-quarter return tower. It prints `PASS: five complete first-return partitions, means, variances, 5-cycle, full partition` on success.

No probabilistic sampling or finite-precision numerical test is involved. All unbounded behavior of the original dyadic map is absorbed by the exact first-return band identity; every surviving first-return branch terminates by time ten. The program does not establish results for other permutations, all invariant measures, or publication novelty. Independent external validation has not been carried out.
