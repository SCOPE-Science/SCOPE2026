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

# Verification

Analytically checked assumptions and quantifiers: fixed geometric parameter, fixed exponent, multinomial samples, weighted duality, Gaussian finite-dimensional limit with summable tail, degenerate Pearson kernel and diagonal bound in the logarithmic critical regime, Poisson cell limit with two uniform tail estimates, and finite-n infinite-moment calculation. No independent validation or automated infinite theorem certification has occurred.

Run `python checker.py` with NumPy installed. The finite script checks exact dual-norm identities by rational arithmetic, exact second moments of binomial Pearson terms, and indexing equivalence of Poisson phase endpoints. With NumPy's fixed random seed it also prints finite simulations at two sample sizes. `checker-output.txt` captures its completed output. All 1,478 assertions passed; the simulation's broad heavy-tail scatter is expected and does not refute convergence in probability of the central regime.

Limitations: numerical trials cannot prove asymptotic statements or originality. Primary textual references are listed in RESULT.md; a broader historical-priority audit may uncover equivalent results.
