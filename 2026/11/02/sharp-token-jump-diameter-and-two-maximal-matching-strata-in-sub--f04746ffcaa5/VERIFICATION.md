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

# Reproducibility and mathematical checks

Run `python VERIFY.py` from any directory; the checker has no third-party dependencies. It constructs the edge–vertex incidence graph from unordered pairs, enumerates candidate matchings independently, tests the original matching and inclusion-maximality conditions, and builds every legal token-jump adjacency.

Direct enumerations for orders \(n=3,4,5,6\) contain respectively \(5,34,449,7366\) maximal matchings. The size-\(n\) counts are \(2,30,444,7360\), the size-\(n-1\) counts are \(3,4,5,6\), and maximum-tier degrees are \(0,4,10,18\). Exhaustive BFS establishes maximum-tier diameters \(5,6\) at \(n=4,5\), and a directed-cycle witness has eccentricity \(8\) for \(n=6\). Full all-pair constructive routing checks use \(900\) and \(197136\) ordered pairs at orders \(4,5\); a fixed-seed reproducible sample checks \(2000\) ordered pairs at order \(6\). All program assertions passed in the reported run.

Finite checks are not proofs for arbitrary \(n\). The separate proof verifies the two-layer classification, exact neighbor count, cycle-breaking bound, and disjoint-cycle lower-bound witness for every integer \(n\ge4\). No independent audit has been performed, and the verifier does not attempt to establish publication priority.
