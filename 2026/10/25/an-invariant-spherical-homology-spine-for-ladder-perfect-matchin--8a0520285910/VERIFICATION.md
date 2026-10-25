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

The proof applies to every integer \(k\geq1\) and uses a homotopy-pushout induction. Its critical checks are: (1) the exact first-rung versus first-horizontal-pair dichotomy; (2) the equality of intersections with the perfect-matching complex of the last \(n-2\) columns; (3) the same intersection diagram for blockwise perfect matchings; (4) a uniform equivariant deformation retraction of each two-edge component to its barycenter; and (5) the orientation sign of reversing join factors. Only an ordinary homotopy equivalence is claimed for the inclusion.

The standalone `checker.py` enumerates perfect matchings, all their simplicial subfaces, and the blockwise subcomplex, and recomputes oriented augmented-chain Lefschetz sums for identity, row swap, reversal, and their product. Results:

| Column count | Nonempty faces | Blockwise tiling facets | Row swap on top homology | Reversal on top homology |
|---:|---:|---:|---:|---:|
| 2 | 6 | 2 | +1 | +1 |
| 4 | 60 | 4 | +1 | -1 |
| 6 | 546 | 8 | +1 | -1 |
| 8 | 4920 | 16 | +1 | +1 |
| 10 | 44286 | 32 | +1 | +1 |

Direct mod-two boundary reductions separately verify precisely one reduced Betti number in the expected degree at widths 2, 4, 6 and 8. The program terminates with `VERIFY_OK`. These finite computations do not prove any all-width statement or an integral homology classification on their own. The structural proof establishes those claims independently. No independent audit has been performed.
