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

# Mathematical verification
The attached standard-library `verify.py` computes the energy-defect matrix of the second-order truncated exponential as exact bivariate rational polynomials. It checks the \(Q_{22}\), \(Q_{12}\), and \(\det Q\) factorizations, the root relation at \(t=3/8\), the degeneracy \(R=-I\) at \(t=1,x=2\), and rational spectral comparisons. Execution returned `VERIFY_OK`.

The universal real-parameter claims follow from the complete inequality proof in `RESULT.md`; finite rational checks do not themselves establish completeness. No external audit, numerical floating-point certification, or theorem-proving assistant was used. The scheme, parameter positivity, and Euclidean norm are necessary scope restrictions.
