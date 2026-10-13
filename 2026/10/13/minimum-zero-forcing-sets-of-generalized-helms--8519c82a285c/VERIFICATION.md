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

The standalone checker builds each generalized helm directly from the center, cycle-spoke vertices, and pendant bundles. For each tested parameter pair it enumerates every subset of cardinality \(m(s-1)+1\), computes ordinary zero forcing closure from the adjacency relation, and compares the answer with the stated center-type/saturated-bundle classification. It independently computes synchronous propagation time and checks that the two types have times \(2\) and \(3\), respectively.

For layers one below the claimed minimum containing at most \(100{,}000\) subsets, the checker also exhausts every subset and confirms that none is zero forcing. It verifies the family counts \(s^m\) and \(m s^{m-1}\) separately, rather than only their sum.

The packaged run reports:

`VERIFY_OK profiles=10 subset_checks=969903 classification_checks=2527 propagation_checks=2527 lower_checks=69801 max_order=22`

The finite computation is a stress test, not an infinite certificate. The all-parameter result rests on the written bundle obstruction and complete one-extra-vertex case analysis. No external solver or precomputed table is used.
