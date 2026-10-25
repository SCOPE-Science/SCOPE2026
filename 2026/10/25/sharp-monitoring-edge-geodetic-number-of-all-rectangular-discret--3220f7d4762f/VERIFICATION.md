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

# Verification and reproducibility

The standalone Python source `verify_rectangular_torus.py` requires Python 3.9 or later and uses only the standard library. Run `python verify_rectangular_torus.py` in a directory containing that file. The matching direct output appears in `verification_output.txt`.

The verifier checks 1,936 independently generated placements over the parameter range \(5\le m\le36\), \(m\le n\le80\), including exactly three observations in every column and the required cyclic-gap bounds in all rows and columns. It also independently checks the gap characterization against the original edge-deletion distance definition over all 4,064 vertex subsets of cycles with lengths 5 through 11. Finally, it checks the original shortest-path distance-change condition for all 1,422 edges of 14 rectangular tori, including both exceptional matrices.

No finite test alone establishes the universal formula; the proof for all admissible parameters uses the exact block-endpoint inequality and its two-step induction. Every stated computational check was reproduced from the standalone source. This is not an independent audit or externally certified result.
