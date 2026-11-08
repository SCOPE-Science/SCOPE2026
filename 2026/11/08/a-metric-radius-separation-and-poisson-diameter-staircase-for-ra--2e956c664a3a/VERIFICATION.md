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
# Reproducible checks

The embedded `verify.py` needs only the Python standard library and can be run with `python verify.py`. Its finite exhaustive loops enumerate all subsets of the \(d\)-cube vertex set for \(d=2,3,4\), comparing exact rational probabilities for attaining full Euclidean diameter at retention probabilities \(1/4\) and \(1/2\) with the antipodal-pair independence identity. It separately checks the number of near-antipodal edges and the number of unordered pairs of edges meeting at one vertex. It tests the finite-degree approximation to the asymptotic Poisson mean and simulates independently sampled critical-pair events with a fixed seed.

Observed completion marker: `BERNOULLI_CUBE_METRIC_CHECKS_PASSED`. Checks do not establish the asymptotic Poisson law or the all-dimensional uniqueness of the enclosing ball. Those statements rely on the explicit proof and its probabilistic bounds. Independent audit has not been performed.
