---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The exact stationary monomial recursion follows by applying L=(-mu*x+kappa*y)∂x +D∂yy +r[f(x,0)-f(x,y)]; its quadratic h solves -Lh=x²-M20. Stationary Green–Kubo 2E[(x²-M20)h] and direct carré-du-champ 2D(Bx+2Cy)²+r(Bxy+Cy²)² give equal long-time rates, martingale CLT follows from ergodicity, bounded polynomial moments and Lindeberg. Matched OU covariance is identical because E[Y0Yt]=2D/r exp(-rt); Gaussian Wick integration gives SigmaG, with explicitly positive excess 8D²κ⁴(21r²+24rmu+8mu²)/[mu²r³(r+mu)³(r+2mu)]. The ratio derivative is negative using a stated globally positive polynomial. Independently computed unit rates Sigma_reset=68/3 and SigmaG=5 and checked derivative identity.

## originality

PASS

The originating active particle article proves model moments, stationary covariance and ordinary time-dependent statistics, explicitly credited; it does not derive the integrated fourth-order Green–Kubo variance excess, its exact positive formula and sharp five-to-one parameter-identifying monotonicity. Generic resetting and OU frameworks do not directly supply this comparison.

## value

PASS

The theorem distinguishes two processes invisible to all second-order position statistics by a canonical integrated quadratic observable, gives an exact variance-rate amplification and uniquely recovers the reset/confinement ratio; natural for stochastic identification, not merely renaming an existing covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
