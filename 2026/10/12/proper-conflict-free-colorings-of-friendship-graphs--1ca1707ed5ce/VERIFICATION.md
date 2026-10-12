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

The analytic proof in `RESULT.md` is the primary evidence.

`artifacts/verify.py` reconstructs \(F_k\), properness, and the proper conflict-free condition directly from adjacency. It exhaustively checks \(F_1,F_2,F_3\) for every palette size through the number of vertices and compares the direct definition with the singleton-leaf characterization.

It also constructs a PCF coloring for every claimed used-color count for all \(2\le k\le20\). Independently, it enumerates every proper three-coloring of the \(kK_2\) leaf matching for \(2\le k\le8\) and verifies the closed minimum-color count.

Replay output:

`ALL CHECKS PASSED; proper_colorings_checked=247410; pcf_colorings_checked=234798; spectrum_constructions=380; minimum_count_formula_k=2..8; minimum_counts={2: 96, 3: 576, 4: 1536, 5: 3840, 6: 9216, 7: 21504, 8: 49152}`

These computations are finite corroboration only. The arbitrary-\(k\) statements follow from the exact neighborhood argument and inclusion-exclusion proof.
