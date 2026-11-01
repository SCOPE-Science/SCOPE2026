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

Run `python3 artifacts/theta_two_config_verify.py` using the standard Python 3 library. The checker constructs graph edges and unordered disjoint-support cubical cells afresh. It verifies the exact cell-count formulas, all signed two-boundaries square to zero, the two-stage complete sequence of free square collapses, connectivity of the one-skeleton, and all claimed signed Lefschetz traces. Every permutation is tested for three through seven arms, and every cycle type for eight through ten arms. Its output is stored in `artifacts/theta_two_config_verify.out` and finishes with `VERIFY_OK`. The proof for arbitrary \(m\ge3\) is the combinatorial free-face classification and symbolic fixed-cell enumeration in RESULT.md, not extrapolation of finite tests. Only rational equivariant representation identification is asserted. Independent audit has not been performed.
