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

The universal result is proved by recovering two intersection distances, counting simultaneous upward and downward intersection changes, and identifying the resulting alternatives with concrete stabilizer automorphisms. The standalone scripts corroborate this proof and are not a substitute for its infinite-parameter argument.

Run with Python 3, standard library only:

```
python3 johnson_refinement_verify.py
python3 johnson_group_verify.py
```

`johnson_refinement_verify.py` checks 91 parameter cases through ground-set size 12 and confirms exact color/profile coincidence, the profile enumerators, the round upper bound, and every neighbor-count identity on all 20,739 vertex instances.

`johnson_group_verify.py` separately generates actual marker-fixing coordinate/complement automorphisms through size 8; all 30 parameter instances (808 vertices in aggregate) have the identical orbit and color partitions. Program outputs are captured without edits in companion `.log` files. Tests below theorem's stated rank are intentional sanity checks. The finite searches do not certify novelty or cover parameters beyond their printed ranges.
