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

# Reproducible exact checks

Run `python3 verify.py` from a directory containing that standalone file. Only the Python standard library is used (`fractions.Fraction`, `math.comb`); there is no network or external data dependency.

The executable reconstructs the species-frequency-one profile for each \(2\le N\le15\) and for all \(1\le a\le b\le N\). It tests every strict interior maximum using exact comparisons. The per-site normalized monotonicity condition is also tested on each profile. The expected exhaustive summary is:

`VERIFY_OK census_pairs=679 scaled_profiles=679 direct_subsets=65536 sole_two_peak_profile=(15,2,9) peaks=(2,7)`

The executable additionally enumerates all \(32{,}768\) site subsets for each of two concrete fifteen-site communities, one with disjoint species occupancy sets and the other with nested occupancy sets, checking every depth's direct empirical average against the hypergeometric formula. This is logically distinct from iterating possible occupancy sizes.

The finite enumeration is exhaustive only over the stated bounded integer domain. It neither establishes any infinite-domain pattern nor addresses statistical estimation under imperfect detection. The source documents and public literature comparisons are described in `RESULT.md` and `REVIEW.md`; exact arithmetic verifies the finite claims but cannot certify originality.
