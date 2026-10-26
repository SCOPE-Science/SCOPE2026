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

In a Python environment with the packages listed in `requirements.txt`, execute `python verify.py`. The program first checks exact symbolic identities in the parameter \(u\): stochasticity of the proposed weights, the critical square-root identity, the closed-form SLEM, the negative-eigenvalue domination inequality and the asymptotic gap ratio. It then forms the full stochastic matrix for every \(n\in\{3,\ldots,50\}\), compares all eigenvalues with the Fourier-block spectrum, and checks the optimum and standard weighting SLEMs. It also tests 1,080 feasible competitors, including invariant and noninvariant ones.

Actual successful replay output:

```text
VERIFY_OK symbolic identities, spectral blocks and exact closed forms; 48 graph sizes; 48 optimum checks; 48 heuristic checks; 1080 feasible comparisons; asymptotic gap ratio 3/2
```

The universal global optimum is proved analytically in `RESULT.md`: convex symmetrization, Fourier eigenvalue formula, strict convex minimization, and a positive algebraic gap protecting every negative spectral mode. Finite checks cannot establish a theorem for all sizes, uniqueness outside the invariant class, or novelty. No independent mathematical audit has been performed.
