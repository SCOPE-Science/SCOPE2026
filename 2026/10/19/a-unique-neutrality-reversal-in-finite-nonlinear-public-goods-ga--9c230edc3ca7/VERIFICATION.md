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

# Reproducible verification

Run `python3 verify.py`; only standard-library dependencies are used. The packaged verification checks the hypergeometric payoff formula for \(4\leq N\leq11\), \(3\leq n<N\), selected positive integer multiplication factors, and every interior cooperator count. It uses exact rational factorial moments, rather than a floating-point approximation, for the finite identities.

The same script checks prefix endpoints, the total-prefix identity, independent solutions of the Fermi birth-death recursion, two exact-rational cumulative-payoff witnesses, unique numerical neutrality crossing brackets, and selected large-population approximations to the integral formula. It completed 1777 assertions on the packaged source file, without missing imports or external assets.

**Analytical limits:** The strict-convexity theorem proves uniqueness for uncountably many real intensities; the script alone does not. Uniform Riemann-sum convergence and strict convexity of the limiting integral prove the population-size asymptotic; numerical quadrature alone does not. The exact classifications apply to the stated affine multiplier and Fermi/exponential-fitness update rules, not all evolutionary games.

Independent scientific audit: not performed.
