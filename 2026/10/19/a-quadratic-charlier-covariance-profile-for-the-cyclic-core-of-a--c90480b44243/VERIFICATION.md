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
Execute `python3 mapping_degree_profile_check.py` with a standard Python 3 installation. The executable enumerates mapping digraphs of sizes 2–6, verifies the exact conditional histograms and cyclic-core distribution, tests the three small-indegree conditional mean identities, and computes exact rational finite covariance signs for sizes 20, 50, 100, 200 and 400. The reproduced output is `CHECKS_OK 207`.

The limiting formula is not inferred from the finite computations. The mathematical argument uses the rooted-forest conditional degree law, fixed-degree asymptotic binomial expansions, the Rayleigh weak limit, and convergence of requisite moments. No independence or growing-degree uniformity is established.
