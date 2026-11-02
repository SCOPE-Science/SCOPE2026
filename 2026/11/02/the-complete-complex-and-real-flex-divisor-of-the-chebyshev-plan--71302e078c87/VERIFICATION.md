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

# Mathematical verification and limits

The general proof establishes the smooth plane model, Chebyshev ODE, ternary Hessian factorization, \(\deg G_d=2d-4\), and the real-root exclusion via strict Cauchy–Schwarz. Squarefreeness follows by assuming \(G_d(a)=G_d'(a)=0\), eliminating the third derivative through the ODE, then obtaining both \(av=du\) and \((a^2-4)v^2=d^2u^2\), impossible for \(v\ne0\). These are characteristic-zero equalities; no positive-characteristic assertion is made.

The standalone `verify.py` uses only the Python 3 standard library. It constructs the Chebyshev polynomials by integer recurrence for \(4\le d\le24\), checks the ODE and residual Hessian leading coefficient exactly, tests modular gcds against a single prime, samples integer signs, and verifies the divisor-degree counts. Running it from this package produces `VERIFY_OK`. The finite and modular tests are supplementary and are not certificates of the infinite theorem.

No independent audit or external proof certification has been performed. Primary source comparisons are identified in the references and review; historical priority is provisional.
