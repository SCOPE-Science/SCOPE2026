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

Execute `python3 verify_ultrametric.py` with the supplied Python 3 standard-library script in the same directory. No external packages, downloads, or random seeds are needed.

The verifier enumerates all multisets of integer partitions summing to each cardinality \(n\) with \(1\le n\le8\). These are exactly the isometry types of three-distance ultrametrics (allowing distances not realized), because each radius-\(\delta_2\) ball is a multiset of radius-\(\delta_1\) blocks and the overall space is a multiset of such balls. It constructs a canonical distance matrix for each type, computes canonical distance-specific neighbour-colour recursive signatures, and compares global signature histograms across all types.

Observed output: isometry-type counts by cardinality \(1\) through \(8\) were \(1,3,6,14,27,58,111,223\). Among these, one-round collisions occurred only for \(n=8\), consisting of a single two-member class \(\{((1,1,2),(1,1,2)),((1,1,1,1),(2,2))\}\). Two-round collisions did not occur for any \(n\le8\). The program terminates with `ALL TESTS PASSED`.

This exhaustive finite verifier is not an inference from finitely many cases to all ultrametrics. The unbounded-size statement is instead established by the ball-type decoding induction in `RESULT.md`, and the uniqueness of the eight-point ambiguity is established by the explicit integer-partition argument. The code does not test isometry against arbitrary non-ultrametric structures, and no independent audit has been performed.
