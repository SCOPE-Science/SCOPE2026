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
# Computational verification
Run `python verify.py` with the packages listed in `requirements.txt`. The checker regenerates complex Haar vectors independently, applies the dephasing channel to actual density matrices, computes eigenvalues of partial transposes, compares against the exact statewise threshold, and independently integrates the phase acceptance probability using the product-ratio density. It tests the algebraic CDF, both global finite-visibility bounds, and the sharp expansion at several small positive values of the residual single-qubit coherence. The theoretical proof is separate and uses exact inequalities; the checks establish finite numerical consistency, not an exhaustive or independent audit. The established quantum concurrence identity is attributed to the primary literature.
