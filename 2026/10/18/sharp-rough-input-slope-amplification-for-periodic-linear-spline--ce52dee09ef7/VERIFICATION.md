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
# Reproduction and scope

Execute `python3 checks/periodic_spline_gain.py` with ordinary Python 3; it uses only the standard library. The script constructs the periodic mass matrix independently over rational numbers, inverts it, integrates the absolute derivative kernel cellwise, tests the periodized Green formula, and checks exact small-degree constants and sampled convergence. It prints an assertion count on successful completion.

The proof requires no numerical limiting argument. The critical universal identities are the integer-line inverse \((A_\infty^{-1})_{ij}=(-q)^{|i-j|}/(2\sqrt3)\) for \(q=2-\sqrt3\), its periodization to the finite inverse, the fact that neighboring finite derivative coefficients have opposing signs or contain exactly one zero, and the explicit absolute-integral calculation. The infinite signed kernel is absolutely integrable; the periodization comparison and its exponentially small tail complete the global claim.

The checker verifies individual finite dimensions, not the infinite theorem, bibliographic originality, or external certification. It uses no third-party papers or remote resources at execution time. Independent audit has not been performed.
