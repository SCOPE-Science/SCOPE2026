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

Run `python3 verify_hex.py` with Python 3 standard library. The script enumerates every clique and every six-cycle on fourteen concrete eligible graphs, reconstructs the closed-neighborhood union and verifies all nonlocal simplices equal the predicted alternating triangles. It calculates the reduced simplicial homology dimensions by full boundary elimination over \(\mathbb F_2\) and \(\mathbb F_3\), comparing to \(b-t\) and \(t\). It also samples eligible graphs with a fixed seed and verifies the same entire simplex-decomposition property. The expected final indicator is `VERIFY_OK 14 homology instances, 28 exact rank checks, 252 complete face-decomposition stress tests`.

The verified examples do not prove the all-parameter theorem or identify integral torsion. Integral homotopy follows from the explicit elementary collapse of the neighborhood complex and the CW disk cancellation in `RESULT.md`. The reproducibility program does not perform independent external audit.
