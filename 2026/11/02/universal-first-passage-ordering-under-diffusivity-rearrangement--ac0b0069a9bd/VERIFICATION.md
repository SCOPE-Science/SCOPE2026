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

# Verification details

The full continuum result follows analytically from a fixed optical length, a sharp rearrangement inequality, the explicit upper Skorokhod reflection map, and synchronization of renewal attempts. The proof in `RESULT.md` supplies these steps, the first-passage quantifiers, and a continuous construction attaining every intermediate arrangement value.

Running `python verify.py` with standard Python produces:

```
PASS: 66696 finite assertions (rearrangement, reflection coupling, resetting, means)
```

The finite checker executes 720 six-layer material permutations, sampled window-shift checks, 800 shared Brownian-path comparisons, 200 shared deterministic-reset multi-cycle comparisons, 74 Poisson-rate Laplace/mean comparisons, and limiting mean checks. The exact arithmetic of sorting and the independently computed Poisson mean are diagnostics only; the path samples discretize a continuous process and cannot establish pathwise order for all Brownian sample paths.

The continuum proof is insensitive to reset-time moments, provided each reset interval is iid, strictly positive and finite almost surely and independent of the Brownian motion. The independent renewal clock must be identical across designs. The displayed Poisson mean is already established in arXiv:2408.04726v1 Eq. (19), and its appearance here checks normalization rather than originality.

Unresolved scientific limits include the applicability of this optical-coordinate model at discontinuous interfaces versus different stochastic prescriptions, and possible implicit coverage by more general stochastic-comparison and rearrangement theorems. No independent audit or external validation has been performed.
