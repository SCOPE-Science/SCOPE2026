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

The self-contained checker `verify.py` can be run with `python verify.py` and only the Python standard library. A checked run reported `PASS: 212 finite-chain and asymptotic-rate assertions`.

**Exact finite tests.** Uniform initial distributions, seven through nine labels, block sizes three and four, and families of one to three forbidden pairs are evaluated with rational arithmetic. Probabilities of avoiding all forbidden pairs are reproduced by two genuinely different constructions: full Johnson-subset dynamics and the marked-label killed chain. The comparisons include nine successive time steps for each configuration.

**Asymptotic coefficient tests.** For block sizes three, four and five and several overlap patterns, a normalized power iteration of the substochastic killed kernel estimates its Perron eigenvalue. Its rescaled deficit approaches \(2(r-1)|E(F)|\), with a monitored first-order error and monotone improvement over the tested sample sizes.

These finite computations do not prove the limit theorem, convergence-rate bounds, or originality. The mathematical proof in `RESULT.md` uses finite-dimensional analytic spectral perturbation, factorial moments and a separate expectation tail bound. Independent mathematical audit remains unperformed.
