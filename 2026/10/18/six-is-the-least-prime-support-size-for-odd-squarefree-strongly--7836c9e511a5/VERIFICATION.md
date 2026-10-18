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

The mathematical argument is given in `RESULT.md`. Run `python certificate.py` and `python independent_check.py` using Python 3 and standard-library modules. The two programs use independent prime-enumeration and subset-sum implementations: trial division with a dictionary of reachable states, and an Eratosthenes sieve with bitset reachability.

Both complete with positive assertions for precisely 87 abundance-admissible \((r,s)\) prime pairs; 45 survive \(n\equiv1\pmod4\); none of those 45 has an omitted-pair sum equal to \(\sigma(n)-2n\). The explicit six-prime witness is checked with disjoint complementary divisor pairs whose total omitted sum is \(60630\). The non-computational reduction of an *unbounded* five-prime problem to these 45 possibilities is part of the proof, not a finite experiment.

These are ordinary same-model mathematical and computational checks. Independent mathematical audit has not been performed; the source and originality comparisons carry the residual possibility of unindexed earlier coverage.
