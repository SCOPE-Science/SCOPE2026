---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The definition forbids a third distinct edge joining endpoints of two selected edges; selected edges need not be disjoint. Reconstructed exact direct edge-conflict predicates and the six legal same-column masks. For n>=7 only separations 0,1,2 matter, yielding 17 pair states and 37 shifts. A 0/-1 potential transforms the weight 1-|mask| to nonnegative deficiencies 0,1 with zero-cost matrix B0 (24 transitions) and unit-cost B1 (13). Independently multiplied full integer 17x17 matrices to establish B0^8=B0^2 and exact tr(B1 B0^(j-1)) for j=1..8 as (1,1,4,2,4,6,2,2); direct digraph inspection gives unique zero-deficiency 6-cycle. Trace recurrence counts all zero-deficiency and exactly-one-deficiency closed cyclic words, proving all n formulas. Independent tests checked third-edge geometry and optimum counts n=7..30. All-order conclusion uses exact finite matrix identity, not extrapolation from bounded n.

## originality

PASS

Chelladurai et al introduced EOP. Brešar–Samadi proved general cubic upper bound n and equality characterization, and Brešar et al proved Cartesian-product lower bound and a *vertex* packing result for prisms. Those do not enumerate all maximum EOP edge sets or give complete n mod6 spectrum in the inspected texts. Equivalent injective edge-color classes and induced-star families were considered explicitly.

## value

PASS

The exact optimal cardinality and all optimizer multiplicities for an infinite canonical cubic graph family form a natural structural classification. Counting 6,2n,4n optima and the sharp mod-six defect goes beyond simply invoking the known cubic bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
