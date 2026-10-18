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

Run `python verify.py` with NumPy and SciPy installed. The checker performs adaptive quadrature for \(m=4,5,7,12\), compares all \(24\) rank weights with independently generated invariant-measure affine cuts, and tests Gaussian-spacing normalization, reflection symmetry, and support cardinality. The observed maximum error in the recorded test was about \(0.00290\) over approximately 608,000 accepted planes in total; each experiment draws 260,000 candidate normals and offsets before rejection. The terminating status was `AFFINE_SIMPLEX_CHECK_OK comparisons=24`.

These computations do not prove the all-dimensional Gaussian-spacing identity or exponent limit: their proofs appear in `RESULT.md`. The rigorous asymptotic ingredient is the \(L^1\) convergence of normalized Gaussian sample ranges and the Gaussian binomial-tail exponent. No source-embedded software performs independent mathematical audit or certifies historical priority.
