---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For hyperbolic three-space curvature -1 and a>1, the spherical function sin(lambda r)/(lambda sinh r), radial measure 4pi sinh²r dr and elementary Laplace sine transforms give \hat f(lambda)=8pi a P(lambda²)/(D_{a-1}D_{a+1}), with P(u)=u²+2(a²+omega²+1)u+(a²-1)²-2(a²+1)omega²-3omega^4. Both D factors are strictly positive and P is strictly increasing for u>=0. Thus the spectral sign on the entire real principal series is decided by P(0), and solving P(0)>=0 yields 3omega^4+2(a²+1)omega² <=(a²-1)² exactly, equality included. Spherical inversion as a positive mixture of positive-definite principal spherical kernels gives sufficiency; radial Plancherel plus the dense compact-test convolution form gives necessity for a>1, and negative P(0) creates an open interval of negative spectrum. Exact independently derived SymPy rational-numerator identity matched and four a-values were sampled; analytic monotonicity is the infinite part of proof.

## originality

PASS

Classical spherical Bochner and Plancherel theorems allow general transform positivity tests, and unmodulated geodesic exponentials have prior positivity results. The exact a,omega hyperbolic-three-space oscillation boundary arises only after a family-specific spectral calculation absent from the materially inspected general source. Priority is qualified because a separate covariance-specific analysis may exist.

## value

PASS

Positive definite isotropic functions are fundamental covariance kernels on curved spaces. This gives the complete admissible oscillation region of a natural two-parameter hyperbolic damped cosine family, with an exact zero-frequency sharp boundary distinct from the Euclidean analogous family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
