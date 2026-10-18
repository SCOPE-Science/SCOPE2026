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

# Reproducibility and proof boundaries

Use `python3 verify.py` to independently build the full finite adjacency and negative-Laplacian matrices. The script checks exact fourth-order transition and return probabilities for all \(72\) integer size pairs \(1\le a\le8\), \(1\le b\le9\), including both source orientations; it also compares vertex-resolved full-matrix time evolution against the classification for \(42\) size pairs at three nonzero times. No external packages are needed.

The all-size conclusion is justified by the two-dimensional bright block, the two dark invariant spaces, the antiunitary identity when \(b=2a-1\), and the explicitly calculated general clique-return coefficient. Finite parameter checks and finite numerical time samples are not an exhaustive or infinite certification. Independent audit and independent experimental validation have not been performed.
