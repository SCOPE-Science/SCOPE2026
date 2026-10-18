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

Run `python3 verify_integral.py` in the directory containing `certificates/unit_pivots.csv`. The program enumerates every admissible arc subset, constructs exact signed integer boundaries, recomputes and compares the entire 341-pivot sequence, checks the remaining integer matrices, and eliminates the 91 non-tree edge generators using triangular relations. Its output must match `checks/integral.txt`.

Run `python3 verify_independent.py`. Its alternate arc ordering and direct enumeration of all 262144 arc masks reproduce the face-vector and finite-field ranks for four primes. Its output must match `checks/independent.txt`. The field results are corroboration; the integral certificate and the fundamental-group computation support the full homotopy claim.

The pivot certificate's `degree` refers to the boundary between arc-cardinality groups, so a degree-five entry operates on four-dimensional simplices. A pivot is admissible only if its current signed integer boundary coefficient equals the recorded unit. Every Schur complement is integral, and no modular arithmetic is used in the primary integral reduction. The rank vector and all surviving zero maps are checked after all pivots. The vanishing of \(\pi_1\) follows from triangle relations rather than assuming it from homology. The finite four-dimensional CW argument then upgrades the integral result to a homotopy equivalence.

This does not constitute a proof for other complete bipartite orders or an equivariant decomposition.
