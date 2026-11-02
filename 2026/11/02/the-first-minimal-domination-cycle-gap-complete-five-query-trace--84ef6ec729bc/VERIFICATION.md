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

The programs `verify_cycle11.py` and `independent_check.py`, with data `cycle11_certificate.json`, are standalone Python checks. Both were executed from the delivered project directory, without external datasets or third-party packages.

The first performs exhaustive enumeration of all vertex subsets for cycles of orders three through eleven, checks the private-neighbor minimality criterion, verifies exact VC dimensions for those finite orders, enumerates all \(462\) five-query supports of the eleven-cycle, checks a four-query shattering support, and replays a complete depth-five query tree. The second independently defines minimality by single-vertex removal, evaluates the exact adaptive version-space recurrence, and reconstructs the full five-query spectrum and the tree witness validity.

The universal product statements are deduced mathematically from componentwise minimality, the additivity of VC dimension and Littlestone dimension on disjoint-domain products, and vertex transitivity of equal-length cycle unions. The programs do not independently certify the product lemma for every multiplicity, nor do they decide arbitrary connected cycle sizes beyond eleven.

Expected final markers:

`ALL_CYCLE11_MINIMAL_DOMINATION_CHECKS_PASS`

`ALL_INDEPENDENT_CYCLE11_CHECKS_PASS`

Self-review only; independent scientific audit has not been performed.
