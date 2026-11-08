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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or newer; no external dependencies are required. The included script was executed from the generated research-package directory and printed:

```
PASS: 458 deterministic checks (all-parameter proofs are analytic).
```

The checks cover: the power-clock root and bracket; uniqueness-consistent derivative signs for ten housekeeping strengths in the limiting model; monotonic trend and both endpoint expansions; the strict negativity of the analytical threshold derivative numerator across a finite time grid; Bernoulli convexity and the exact slope identity at seven finite-affinity parameter settings; and the small-housekeeping stationary clock and optimal-efficiency predictions at fourteen parameter/cost combinations. The program uses deterministic bisection and standard-library elementary functions. It does **not** use finite sampling as a substitute for the all-parameter sign proof, a certified interval enclosure, or a proof of the asymptotic order symbols.

Reconstruction of the critical mathematical steps requires only the exact Bernoulli relative-entropy formula, differentiation of the logistic odds ratio, strict convexity, the large-time expansions of the first derivative, and the elementary inequality \(e^{2s}>1+2s\). The limiting statement is at fixed physical parameters as housekeeping tends to zero; the separate weak-affinity theory keeps normalized housekeeping fixed. Numerical evaluation at very small housekeeping may require increased precision beyond ordinary double precision to resolve the efficiency deficit reliably. The result is reviewed here but has not undergone independent audit.
