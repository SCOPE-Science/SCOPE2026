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

The analytic reduction uses the directional mixed-neighborhood confidence rule on a three-vertex undirected path. For each sampled edge, the center's neighborhood distance is zero, whereas the endpoint's transitive distance is half the endpoint gap. Under the stated inequalities, these facts force the exact iid affine recursion.

The proof independently establishes: full-range almost-sure liminf and limsup using arbitrary-length fair-edge runs; unique stationary law from synchronous contraction; its Bernoulli-series representation and exact moments; ergodic occupation from a two-sided stationary construction; and the uniform stationary law and exact finite-time Wasserstein formula at \(\rho=1/2\).

The included `verify.py` was executed from its delivered working directory and passed 808 rational directional update checks, 27 exact finite-law / quantile-integral checks, and eight moment identities. The checks are finite corroborations and are not substituted for the parameter-uniform proof. The result does not assert uniform convergence in total variation or any behavior outside its parameter wedge.
