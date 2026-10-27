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

# Reproducibility and limits

Run `python verify_joint_roots.py` with Python 3 and no third-party packages. The observed output was:

```
VERIFY_OK 3191 checks; 5-clock joint-valley probability 2/15
```

The exact checks enumerate all \(5!\) orderings of five independent clocks to obtain the two-valley probability \(2/15\); count all cyclic minima over every permutation of cycle sizes 5 through 8 to reproduce the mean \(K/3\) and variance \(2K/45\); enumerate all two-valued survivor masks at sizes 7 and 8 with probabilities \(1/2\) and \(1/3\) and check the triple-survivor variance identity; and verify for all feasible subsets on cycles 5–7 that inserting a root changes any fixed gap count by at most two.

The actual infinite proof, not the finite checks, establishes the \(O_x(K^{-1/8})\) conditional error and the Gaussian/Gumbel independent joint limit. The proof invokes the published marginal Gaussian process limit and classical dependency-graph Poisson approximation; it does not prove a Gaussian convergence rate, quantify a growing-gap joint regime, or establish priority by itself.
