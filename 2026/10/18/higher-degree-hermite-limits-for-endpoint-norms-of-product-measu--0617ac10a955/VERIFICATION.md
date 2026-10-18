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

# Verification notes

The self-contained `projection_checker.py` is executable using Python 3, NumPy and SciPy. It checks weighted orthogonality on an asymmetric five-atom law and also recomputes the total-degree projection kernels by multi-index summation and tensor-degree recursion for degree three and four on three one-dimensional marginal distributions (uniform, arcsine and discrete asymmetric), in spatial dimensions two through four: 1,281 finite kernel pointwise comparisons. The computation uses numerical quadrature partitioned at all real Hermite zeros to evaluate \(\mathbb E|H_k(Z)|\). For uniform and arcsine laws it prints additional Monte Carlo corner-kernel Lebesgue estimates against the predicted high-dimensional limit at dimensions 80, 180 and 400. These are finite numerical checks, not certified numerical intervals or evidence of the universal limit.

The mathematical proof is complete under the hypotheses stated in RESULT.md, relying on standard bounded-array central-limit convergence, deterministic power-sum bounds, the Hermite generating identity, orthogonality in the product kernel and uniform integrability. No external formal proof assistant, independent referee or infinite numerical certification was used. Unverified historical priority remains a bibliographic limitation.
