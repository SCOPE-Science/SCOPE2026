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

# Verification record

The proof reconstructs both one-particle absorbing-boundary fluxes from the hyperbolic-sine Laplace transforms; the leading image distances are \(d\) and \(L_N-d\). At \(t=b/(c_N+y)\), the omitted images are exponentially smaller, and the complementary error function gives limiting hazards \(e^{-y}\) and \(e^{-2\theta-y}\). Taking the earliest of \(N\) independent paths yields a shifted Gumbel distribution. Direct asymptotics of the two first-exit fluxes establish the complete normalized joint density and asymptotically independent endpoint mark. Fresh independent episodes imply the exact finite-population geometric number of attempts, and a tail bound on the minimum exit time proves the limiting time scale and mean.

Reproduce finite checks by executing `python verify.py` in the extracted directory. Only the Python standard library is required. The script checks three image-series Laplace-transform identities against the exact Dirichlet hyperbolic-sine forms, then evaluates the absorbing-interval image approximation at twelve combinations of \(\theta\) and \(N\), integrates the marked first-exit probability, calculates the centered exit-time CDF at three test points per combination, and checks four exact midpoint symmetry instances. These are finite numerical consistency tests; they are not a proof of uniform asymptotics, uniqueness in the literature, or independent verification. All limiting assertions rest on the written analytic argument. No independent audit or certification has been performed.
