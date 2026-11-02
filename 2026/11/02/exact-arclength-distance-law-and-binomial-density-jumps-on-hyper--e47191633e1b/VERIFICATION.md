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

# Reproducibility and scientific limits

Run `python3 artifacts/verify_metric_cube.py` using Python 3 standard library only. It prints exact rational reference mean/variance in low dimensions, then confirms the equality of the direct four-endpoint shortest path and the classified formula for 133,347 fully enumerated ordered edge-pair/rational-position instances, dimensions 1–6. It checks symbolic piecewise-affine integration of total probability, mean and second moment for dimensions 1–25, and exact rational one-sided density jump interpolation for dimensions 3–25. Computations reproduce finite instances of the stated result, but the all-dimensional proof is the mathematical argument in RESULT.md. No general weighted-cube or Euclidean-chord claim was verified. The earliest precisely day-dated historical source in the listed references is 2007-12-05; the older 1982 sources are month/year dated in the accessed evidence. Historical priority against inaccessible complete texts and independent mathematical review are not established.
