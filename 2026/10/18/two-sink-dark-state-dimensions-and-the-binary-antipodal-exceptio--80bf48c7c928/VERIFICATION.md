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

# Verification

The accompanying `check_hamming.py` is a standalone checker requiring NumPy and SciPy. Run `python check_hamming.py` in the same folder as this document. It constructs the actual full adjacency matrices and uses matrix eigendecomposition rather than the claimed closed-form rank as the independent comparator. It also compares the Krawtchouk source-survival formula with orthonormal spectral projections and checks no-jump norm decay numerically.

Recorded successful execution: 174 complete rank comparisons; 6366 individual-source spectral projector comparisons; 12 direct no-jump dynamical comparisons. The tested dimensions are binary through six, ternary through three and quaternary through two. The numerical checks are bounded and do not certify the theorem for all dimensions. The infinite-family assertions follow from the explicit character and spectral argument in RESULT.md. There has been no independent audit.
