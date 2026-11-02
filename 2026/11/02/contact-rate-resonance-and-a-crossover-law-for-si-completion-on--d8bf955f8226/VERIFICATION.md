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

# Reproducible verification and scope

The complete proof is in `RESULT.md`. Using Python 3 with the standard library only, run:

```bash
python3 verify_windmill.py
```

The checker independently enumerates all \(2^k\) possible infected subsets of the nonhub vertices for multiple small clique sizes and computes absorption-time moments by exact rational first-step recurrences. It compares the first four raw moments with the independent-stage expression. It also verifies infection cut-rate identities, the closed resonant prefactor \((k-1)^2\), the two-stage finite-time survival expression by CTMC uniformization, and finite-size extreme-value centerings. The recorded check count for the bundled version is 1,733, with every assertion passing.

Finite computations do not prove convergence as \(m\to\infty\). The all-size statements rely instead on conditional exponential-convolution identities, exact rational algebra, independence of the cliques, and uniform exponential moment bounds for the faster stages. The supplied finite-size numerical comparisons are consistency checks and may converge slowly near criticality. All computations are reproducible without external services or unpublished input data.
