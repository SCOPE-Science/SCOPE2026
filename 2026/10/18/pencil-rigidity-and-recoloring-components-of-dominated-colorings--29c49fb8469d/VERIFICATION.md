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

# Reproduction and proof boundaries

The proof is combinatorial, valid for every finite projective plane of order \(q\ge2\), and does not depend on computer output. The essential infinite steps are the sharp line-cover union bound, its concurrency equality case, and the fact that two distinct off-center points determine the unique support line of a color class.

Two standalone verification programs use only the Python standard library and run by executing `python3 exhaustive.py` and `python3 constructive_check.py`. `exhaustive.py` derives points and lines of \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\), enumerates every possible nonempty dominated color class on one incidence side, forms all set partitions into the minimum number of classes, computes allowed moves without assuming the theorem, and validates the component and center structures. `constructive_check.py` independently constructs the pencil color classes, directly verifies all class-dominance conditions, and reconstructs every one-vertex exchange by optimal matching between unlabeled classes.

The included `exhaustive_output.json` and `constructive_output.json` are the exact standard-output files of these commands. Agreement includes the counts \(21\), \(52\), \(441\), \(2704\), \(49\), and \(169\). The finite checks do not certify the all-orders theorem; its quantified proof is supplied in RESULT.md. No external scientific audit has been performed.
