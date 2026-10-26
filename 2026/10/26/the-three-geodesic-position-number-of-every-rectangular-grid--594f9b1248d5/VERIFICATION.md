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

Execute `python verify.py` in the directory containing `verify.py`. The program checks that the length-at-most-three geodesic triple generator agrees exactly with an independent Manhattan-betweenness generator. It exhaustively checks optimal cardinalities for 17 rectangles of area at most 18 (429200 total candidate vertex subsets), explicitly checks each of the four local tiles, and checks the number of optimum configurations for three-row widths two through six. It also separately establishes by exhaustive finite enumeration that the general two-position number on the \(3\times4\) grid is seven, versus six for length-three geodesics.

The expected output is in `verification_output.txt` and terminates in `VERIFICATION_OK`. The code contains finite assertions only. The infinite result uses the tile proof in `RESULT.md`, not an enumeration up to a large cutoff.

No independent audit has been performed.
