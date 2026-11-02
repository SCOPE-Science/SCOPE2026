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

# Verification of the rook-graph extremal enumeration

The self-contained `verify.py` uses only Python 3's standard library and recomputes rook-graph adjacency from the definition. It does not use the row-column proof criterion to decide whether a subset is a fort: for each blue vertex it counts actual white neighbors and tests whether the count equals one. It then finds the smallest tested fort size by increasing white-subset cardinality from one to four, and compares the count to the theorem. The proof supplies a four-cell construction for every graph, so sizes one through four suffice for the tested orders.

Command: `python3 verify.py`.

Successful results in the extracted checker were `FORT_COUNTS_OK, subsets 360898` for 20 graphs satisfying \(2\le m\le n\le7\) and \(mn\le48\), and eight `ZERO_FORCING_OK` checks for \((2,2)\), \((2,3)\), \((2,4)\), \((2,5)\), \((3,3)\), \((3,4)\), \((3,5)\), and \((4,4)\). The forcing tests independently simulate repeated standard blue-vertex forces and compare the size-four fort condition with failed forcing for every candidate at the minimum white cardinality.

Critical infinite-proof steps to inspect independently are the forcing-closure reduction, the exact white-neighbor formula at each blue cell, the exhaustive four occupancy regimes, and separation of the double-occupied thin-board patterns from full-column transversals. The classification and orbit formulas are proved for all indicated integer dimensions; no finite computation is used as an infinite certificate.

The independent mathematical audit has not been performed; no external verification status is asserted.
