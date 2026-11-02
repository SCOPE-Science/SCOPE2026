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

# Reproducibility and limits

Use Python 3 (standard library only) and run `python3 verify.py`. The script reconstructs each binary checkerboard cut adjacency row from the offsets \(\{-2,-1,0,1\}\), removes exactly two selected edges by XOR toggles, and computes ranks over \(\mathbb F_2\) with a bit-level pivot elimination. It enumerates every \(n\in\{4,8,\ldots,64\}\), every \(1\le d<n\), and every two offsets, for \(8{,}448\) individual double-edge configurations. All matched the claimed rank increments and the undamaged base rank; counts by increment \(0,1,2\) were respectively \(240,3312,4896\).

The script was executed with all assertions enabled; the original output is embedded as `verification_output.txt`. This computational check is finite. The universal result is supplied by the algebraic proof in `RESULT.md`, including the dependent rank-two-update case and all boundary parameters. No external independent validation is asserted.
