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

# Reproducibility

Run `python3 certify_heptagon.py` using a standard Python 3 installation from the directory containing the file. The standalone program constructs rational outer bounds for \(\pi\) via Machin's identity and alternating arctangent series, and bounds sine/cosine values via Taylor expansions with explicit rational remainder estimates. It then tests all \(511\) allowed four-normal selections in exact rational interval arithmetic. All \(504\) nonwinning configurations are strictly separated by more than \(1/40\), and exactly seven minima remain. It also checks the indicated interval for the normalized area. Expected successful output begins with `PASS: 511 bounded four-normal selections; exactly seven minimizers.`

The code and proof assume the regular heptagon of circumradius one and its fourteen outward chord normals. The formula for a four-line intersection is mathematically applicable to genuine four-sided intersections. A redundant line leaves a triangular enclosure; those cases are handled separately by the analytical inscribed-circle area lower bound. The computer's finite proof establishes inequalities over a finite exhaustively classified direction set; it does not establish the arbitrary-polygon chord conjecture or any independent external validation.
