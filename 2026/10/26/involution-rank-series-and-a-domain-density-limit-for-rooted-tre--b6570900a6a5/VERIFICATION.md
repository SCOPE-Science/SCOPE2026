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

## Finite computational checks

Run `python3 verify_tree_involutions.py` using the Python standard library. It directly constructs partial maps for heights \(0\)–\(3\) and tests every map for equality with its partial inverse, matching all domain-rank polynomial coefficients. There are \(1,7,127,32767\) maps at these heights. It then checks recurrences beyond enumeration through height \(6\), checks the independent first-moment recurrences and approximates the rigorously defined binary domain-density constant. The script finishes with `ALL_ROOTED_TREE_PARTIAL_INVOLUTION_CHECKS_PASSED`.

## Proof boundaries

The all-height polynomial identity follows from a disjoint root-child decomposition, not finite enumeration. The existence of the density limit uses a summable increment bound for exact integer recurrences. Concentration uses conditional independence at each fixed finite upper frontier and a vanishing exceptional-frontier probability. The numerical value is a consequence of rigorously convergent expressions. Historical novelty cannot be certified by this checker; previously known unrefined counts are explicitly attributed to OEIS A332757.
