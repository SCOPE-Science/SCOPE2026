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
# Verification of the finite homotopy theorem

Execute `python3 CHECKER.py` from the same directory. Standard-library Python 3 is sufficient. Expected success marker: `C10K3_INTEGRAL_MORSE_HOMOTOPY_OK`.

The code reconstructs, rather than imports, all 216257 nonempty independent sets on 30 vertices. The face vector is `(30,375,2560,10545,27456,46385,52080,40245,22460,9594,3330,955,210,30,2)` in dimensions 0..14. The pivot matching has 108121 pairs. Its directed Hasse graph has 1502070 covers; complete topological sorting visits every face. Its critical cells comprise one vertex, eight 5-cells and six 6-cells. The exact signed integral 8-by-6 differential is printed, and the 5-by-5 minor has determinant +1. The active six-row block is a connected hexagon incidence matrix. The consequences are reduced integral homology \(\mathbb Z^3\) in degree 5 and \(\mathbb Z\) in degree 6 and no other reduced homology. The geometric conclusion follows from Hurewicz/attaching-map classification for the 4-connected two-level CW model.

An independently implemented elementary-free-face reduction leaves 67111 cells and gives mod-two and mod-three Betti vectors supported only in degrees 5 (dimension 3) and 6 (dimension 1). This is corroboration, not the integral proof.

**Limit:** Nothing here checks a uniform theorem for other parameters or constitutes independent external validation.
