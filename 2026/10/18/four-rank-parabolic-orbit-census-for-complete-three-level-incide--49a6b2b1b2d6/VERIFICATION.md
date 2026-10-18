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

# Verification and limitations

The attached standalone `three_layer_rank_checker.py` uses only the Python 3 standard library. Execute it as `python3 three_layer_rank_checker.py`. It verifies exact four-rank histograms for 13 parameter combinations using finite-field elimination, including \(q=2,3,4,5\), and separately tests full parabolic-conjugation orbit partitions for four small cases. Expected terminal markers are `ALL_THREE_LAYER_RANK_CHECKS_PASSED 13` and `ALL_PARABOLIC_ORBIT_CHECKS_PASSED`.

The exhaustive finite checks are not an infinite certificate. General correctness rests on explicit analysis of (1) simultaneous base changes for the maps \(A,B\), (2) the quotient of long blocks \(C\) by affine unipotent conjugation, (3) the full residual action on kernel and cokernel, and (4) Gaussian subspace and injection counts, all in `RESULT.md`.

The formula counts labelled parabolic-group orbits and orbit cardinalities, not isomorphism classes under arbitrary ambient linear transformations, and is limited to complete three-level incidence algebras. Earlier nilradical orbit finiteness and Jordan-type marginals are not claimed as novel. Independent mathematical audit: not performed.
