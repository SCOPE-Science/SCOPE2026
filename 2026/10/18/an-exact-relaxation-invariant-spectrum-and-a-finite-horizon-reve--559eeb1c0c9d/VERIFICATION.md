---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the ordered pair (reflection first in the second line), use the frame at each line. If Q is rotation by pi/m, the first pair's linear part multiplied on the right by Q is K=[[c,0],[(1-lambda)sin(pi/m),lambda*c]]. Conjugation by Q^j includes the wrap-around because Q^m=-I, giving M=-K^m. The off-diagonal geometric sum for K^r is c^r tan(pi/m)(1-lambda^r), also valid at 0 and 1. This proves both eigenvalues and the exact power law. The affine offsets affect only the constant term; rho(M)=c^m<1 gives the unique globally attracting fixed point, and (1,tan(pi/m)) attains the asymptotic rate. At lambda=1 the power is scalar; for lambda<1 its first column has norm strictly greater than c^(mk) for every k>=1. This is a comparison relative to each method's own fixed point, including inconsistent lines. Independent replay: python3 /workspace/branches/replay_exact_audit.py 3 symbolically multiplies the original pairs at m=3,4,6 with indeterminate relaxation and compares the first two powers exactly. The frozen checker was inspected, not run; its reported finite trials are not the universal proof.

## originality

PASS

Best of the inspected evidence: the identifiable distinct claim is the joint all-relaxation spectrum and strict all-positive-horizon optimum for the specified cyclic fan, not the algorithm, local convergence in general, or the separate projection and unrelaxed endpoints. No equivalent or dominating theorem was established in the checked sources.

## value

PASS

This canonical symmetric affine test includes inconsistent instances and separates a spectral factor from the worst achievable error after any prescribed number of cycles. Knowing the common spectral radius alone gives no preference among relaxation weights, while the exact power law supplies a strict preference on the finite-cycle operator norm. This is a useful benchmark for tuning and for testing claims that relaxation improves cyclic DR; it does not compare feasibility residuals or different fixed points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
