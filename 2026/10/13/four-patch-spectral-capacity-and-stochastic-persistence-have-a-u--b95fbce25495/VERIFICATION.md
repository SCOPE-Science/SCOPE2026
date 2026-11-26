---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the full-occupancy finite chain, from each nonempty state there is a positive-probability path of only extinctions to the absorbing state, so each transient backward system is invertible at every positive rate. The independent replay builds the full 15-state backward matrix for each graph and solves it symbolically over the rate variable without orbit lumping. The four rational functions and both factored differences match. The cycle-minus-paw sign is the sign of F: the denominator is positive, F has exactly one descending coefficient sign change, and its constant and leading terms have opposite signs. Exact endpoint substitution verifies the bracket and exact evaluation at rate two gives 237101/648778. The two adjacency characteristic polynomials give strict paw superiority since x³−x²−3x+1 changes sign between 2 and 3. With three links, the star has larger spectral radius than the path, and the numerator of star-minus-path is a positive-coefficient polynomial times λ² over positive factors. At n≤3 each nonempty connected fixed-size stratum has one type. At n=4 the lower link stratum is the tree pair, and the four-link pair arises by removing two adjacent or two disjoint edges from the complete graph. This verifies both levels of minimality under the stated constraints.

## originality

PASS

The supported distinct contribution is the sharp equal-order/equal-link minimal disagreement under full occupancy, with a global exclusion of the smaller link stratum. Older exact all-small-graph computations include the raw instances, but their compared statements do not give the all-rate ordering and exclusion. The later dated Resultary corridor record is an explicit equivalent of the paw–cycle crossing itself, and another later dated record explicitly gives the star–path mean inequality; the crossing and inequality are not distinct standalone claims across the catalogue. These overlaps are credited, but do not establish earlier coverage of the combined sharp minimum or settle priority/provenance.

## value

PASS

Equal order and size hold the patch and link budgets fixed for a motivated comparison of two inequivalent persistence measures. The minimality theorem isolates the first structural obstruction and excludes a reversal on either four-patch tree at any positive rate. The crossover certificate says precisely on what rate side the spectral ranking fails, not just that a counterexample can occur. Value is in the combined sharp boundary and comparison, not in recomputing all small-graph lifetimes or asserting a new general ecological phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
