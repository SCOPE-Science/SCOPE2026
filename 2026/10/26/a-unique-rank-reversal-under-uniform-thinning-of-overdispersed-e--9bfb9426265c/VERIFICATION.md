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

# Verification and scope

The analytic verification uses the standard negative-binomial offspring pgf and the least fixed point of its generating function. The inverse survival map is a strict increasing average of a positive increasing integrand. The ratio of two such inverse maps reduces to a ratio of exponential increments whose logarithmic derivative is strictly positive. Therefore the global classification applies to every positive real parameter in its stated ordering, without relying on finite numerical sampling.

The independent numerical reproduction file is `verify.py`. Run it with Python 3 and SciPy installed. It checks exact symbolic benchmark values by numeric evaluation, 2,500 random opposing-order parameter quadruples at the crossover and on both sides, and 2,000 same-order configurations. This program does not constitute exhaustive verification or independently performed mathematical auditing.

Numerical root solving can have floating-point limitations at extreme parameter ratios. The proof and statements specify continuous real parameter ranges; only the random tests are bounded ranges. Because physical independent Bernoulli thinning requires \(p\in[0,1]\), a mathematical crossover at \(p_*>1\) is not a possible thinning experiment. The theorem does not address finite-population epidemic final sizes, ongoing interventions changing offspring dispersion, or the transmission correlations characteristic of household and contact-network epidemics.
