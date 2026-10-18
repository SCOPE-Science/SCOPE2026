---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a,b>=2 and P={0<=v_j<=u_i<=1}, the a+b+ab primitive facet normals are columns of a signed graph-incidence matrix on boundary nodes 0,1 and a+b coordinate nodes. Active edges at any face form subgraphs whose connected components cannot join 0 to 1. Their incidence matrix has totally unimodular nonzero maximal minors and saturated image, so the toric local class-group cokernel is free with rank equal to active-edge count minus rank, the cycle rank. Either p upper coordinates are 0 (forcing all lower 0, active block K_{p+1,b}, rank p(b-1)), or q lower coordinates are 1 (K_{q+1,a}, rank q(a-1)); these cases are disjoint. Otherwise every mixed active equality sits at unique common min upper/max lower value t in (0,1), yielding K_{r,s}, rank (r-1)(s-1), with other active stars acyclic. The alternative forest case is rank 0. TU makes all locally simplicial cones regular, hence local Q-factoriality iff smoothness. At fixed vertices maximal rank ab-min(a,b), versus Friedl global ab. A new independent complete face enumeration using vertex-set intersections and disjoint-set active-edge cycle counting confirmed the rank formula at every face for six (a,b) pairs (2,2),(2,3),(3,2),(3,3),(4,2),(2,4), with respectively 51,151,151,463,459,459 faces; this finite experiment is supplementary to the symbolic proof. Manually checked a=b=2 fixed vertices: empty vertex rank 0, one upper rank1, two upper rank2; separately read the supplied exact facecheck.py logic.

## originality

PASS

The local orbit-by-orbit free abelian class-group rank formulas and Q-factorial=smooth conclusion on this entire two-level family are not stated in primary Friedl global class-group theorem or Lakshmibai–Mukherjee singular-stratum methodology as inspected. TU toric class sequence and graph cycles are standard ingredients explicitly credited. Best of knowledge with risk of existing equivalent specialization of general results.

## value

PASS

Natural local singularity invariant throughout all torus-orbit strata of projective complete-bipartite Hibi varieties. It quantifies non-Q-factorial defect and its torsion-free nature at every orbit, gives smooth/Q-factorial coincidence, and exact maximal local/global rank gap. Valuable for divisors and birational or singularity studies beyond isolated fixed points, with genuine all-parameter structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
