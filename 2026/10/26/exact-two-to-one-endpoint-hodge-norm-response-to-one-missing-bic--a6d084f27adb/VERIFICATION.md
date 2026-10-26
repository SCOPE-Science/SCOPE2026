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

Run `python verify_punctured_biclique.py` with Python 3 and no third-party dependencies. The program constructs the incidence Laplacian directly, grounds one vertex, performs exact rational Gaussian elimination, forms both projected edge-vector columns, and checks their operator norms and maximizer types against the closed formulas for every \(2\le m,n\le7\). The expected output is `PASS 36 parameter pairs, 693 exact rational projector columns; both norms and extremal edge orbits`.

The symbolic argument in `RESULT.md` covers all integer \(m,n\ge2\). The finite checker does not certify the infinite family by itself. No independent audit was performed.
