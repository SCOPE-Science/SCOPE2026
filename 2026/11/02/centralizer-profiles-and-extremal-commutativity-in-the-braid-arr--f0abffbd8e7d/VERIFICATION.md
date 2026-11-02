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

# Reproducibility checks

`python3 face_band_verify.py` enumerates every face as a surjective word of block indices and applies the intersection-product definition directly. For \(0\le n\le5\), all ordered pairs were tested for commutation; each individual centralizer matched the predicted block-size expression; and the aggregate counts were \(1,1,7,73,1015,17641\). The last output line was `VERIFY_OK`.

These are full finite checks for those sizes, **not** an infinite proof. The algebraic argument in RESULT.md covers every \(n\ge1\), including block-size extremes and the limiting law. No independent audit or external mathematical certification is represented.
