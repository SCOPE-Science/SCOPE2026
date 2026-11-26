---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Use the fixed normalization ℓᵀx=1 even when the perturbed matrices lose their common left vector. An independent contraction argument is to conjugate by diag(ℓ), making every unperturbed normalized map a positive column-stochastic map on the usual probability simplex. In ℓ¹ distance on the zero-sum tangent space its contraction coefficient is at most 1−d times a common positive lower entry bound: subtract the constant matrix of that lower bound and use its vanishing on zero-sum vectors. The perturbed normalized maps and their tangent derivatives are jointly continuous on the compact simplex, since the denominators are uniformly positive. For small signed δ they remain uniformly contracting. Pullback limits along the bi-infinite stationary chain therefore exist, are past-measurable and depend continuously on δ, by a geometric bound on the sum of the map differences. The same contraction makes arbitrary starting populations have the same time-average log multiplier as the stationary pullback process. Markov ergodicity gives the expectation formula, with multiplier ρ_k+δℓᵀH_k x_t^δ in state k. Its zeroth-order part does not depend on x, and bounded difference quotients give the claimed two-sided derivative by dominated convergence, without differentiating the stationary composition. Conditional means satisfy the stated j,k recursion because x_t is past-measurable and the next state conditional on the past and E_t=k has law P_{·k}. The positive block matrix has left eigenvector (ℓᵀ,…,ℓᵀ) at one, so Perron–Frobenius gives uniqueness, and the normalized block masses solve Pπ=π. This yields the general derivative, entry formula and elasticity sum. In iid environments the current state is independent of the pullback composition; cancellation of the strictly positive factors proves the all-singleton iff and the stated subset mean criterion. Independent replay `cd /workspace && python checks/independent_replay.py 3` verified the noncommuting example, correlated block moments and iid comparison by exact affine scalar recursions. The frozen finite-word and simulation evidence is diagnostic only; none is used to justify differentiability or the infinite-horizon identities.

## originality

PASS

The supported distinct claim is the exact finite Perron computation for arbitrary strictly positive common-left Markov families with fixed environmental law, including arbitrary additive directions not preserving the hypothesis, and the resulting exact iid iff. Environment-specific perturbations, general random-product sensitivities, disproof of broad frequency proportionality, and the total-elasticity identity are prior context and not credited as new. Direct comparisons at the available statement level found no covering finite formula or iid characterization; the inaccessible closest full texts remain substantive priority risks, not negative evidence.

## value

PASS

The common-left condition is restrictive and deliberate: it makes an exact, finite, reusable derivative computation possible while allowing arbitrary contrast and noncommuting matrices and without constraining the perturbation to preserve the condition. This replaces a long random-product average for the specified class with one finite linear computation, separates base growth from correlation-dependent responses, and gives an exact positive iid criterion rather than another disproof example. The known sum of elasticities and the general Perron or random-product principles alone are not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
