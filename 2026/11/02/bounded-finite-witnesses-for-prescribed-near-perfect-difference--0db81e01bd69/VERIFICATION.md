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
The accompanying `verify.py` requires Python 3 standard library only. Run `python3 verify.py`. The observed output was:

```text
VERIFY_OK singleton_shifts=4 target_bounds=8,14,25 compressed_random_finite_seeds= 360 exhaustive_10point_seeds= 808
```

Four seed triples at positive distances \(1,2,5,11\) were extended through the three indicated target bounds; their representation functions equal two at the selected distance and one at every other tested distance. A deterministic pseudorandom collection of 360 finite seeds, together with all 808 qualifying finite subsets of the first ten positive integers, was compressed using the asserted fourth-power component placement, checking exact exceptional multiplicities, uniqueness elsewhere, and the numerical bound. These checks are finite illustrations, not a substitute for the proof of the infinite extension or the universal bounded-witness criterion. Exhaustive decision searches over the huge general bound were not run.
