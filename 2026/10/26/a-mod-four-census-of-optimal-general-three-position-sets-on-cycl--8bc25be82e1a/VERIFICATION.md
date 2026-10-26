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

The standalone file `verify.py` uses only the Python standard library. Run `python verify.py` in a directory containing the file.

Its checks independently compare the shortest-path characterization and the four-window characterization on all optimum-size candidate subsets of cycles from order 6 through 15; enumerate all optimum-size subsets from order 6 through 23; check rotation orbit counts through order 18; and use an independent eight-state transfer method through order 120.

Recorded output:

`VERIFICATION_OK orders=6..23 candidate_subsets=2786632 direct_distance_cases=13472 orbit_orders=6..18 transfer_orders=6..120`

The first count includes rejected as well as accepted candidate subsets. All tests passed when executed on the included source. The mathematical proof covers arbitrary order and does not infer an infinite claim from these finite tests. No external audit or independent scientific validation was performed.
