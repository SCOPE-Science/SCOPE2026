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

# Verification scope

The claim concerns positive classical solutions of \(\dot u=v^p\), \(\dot v=\alpha u-\beta v\) with \(\alpha,\beta>0\), \(p>3\), and the eventually monotone phase variable \(v\). Equation \((Y^2)'=2\alpha v^p-2\beta Y\) follows by the chain rule without approximation. Iterating its integrated energy identity twice gives the coefficients \(d=-\beta/(q+1)\) and \(e=\beta^2q/[2c(q+1)^2]\). The final error is integrable, making the orbit-dependent limit exact. The proof supplies the three explicit error exponents and the nonzero quintic logarithmic coefficient. Comparing two exact phase equations gives a positive exponential formula for the difference of their finite parts, because its denominator is asymptotic to twice a positive power of the memory coordinate.

# Checks and boundaries

The accompanying script `verify_algebra.py` was executed successfully after creation from its actual package path; its exact symbolic identities check only coefficient arithmetic. The analytic proof independently establishes positivity, finite-time blow-up, eventual monotonicity, and convergence. No finite calculation asserts an infinite-dimensional or infinite-tail result. The theorem does not determine the finite-part constant directly from the initial data, prove extensions to \(p\le3\), or settle originality beyond the literature inspected. Independent audit: not performed.
