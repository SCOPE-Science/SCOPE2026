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

# Verification of the finite root-system filtration

Run `python3 verify_b3_rips.py` from a directory containing `collapse_to_boundary.json`. Python's standard library suffices. The exact run output is `verification_output.txt` and ends in `VERIFY_OK`.

The script checks all 153 unordered Euclidean squared distances, constructs the clique complexes at squared thresholds 0, 1, 2, 3, 4, 5, 6, and 8, and asserts every face vector. It checks connectedness and vertex links of the cuboctahedral-boundary triangulation, the twelve bridging triangles and eight additional short-root triangles at squared threshold 2, the entire 164-pair relative elementary collapse at threshold 3, and mod-two Betti numbers at thresholds 1, 2, and 3. At squared thresholds 4, 5, and 6, it constructs vertex-toggle matchings and checks every edge of the full directed Hasse graph for cycles, together with the sole critical zero-cell. No approximation to distances is used.

The integral wedge classifications rely on the elementary-collapse and CW-cell attachment proofs in RESULT.md; the mod-two calculations are independent supplementary checks, not substitutes for those integral arguments. The exact finite result makes no statement about other dimensions, varying short/long radial ratios, or external independent validation.
