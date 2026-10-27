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

# Reproducibility and scope

The mathematical proof is self-contained in `RESULT.md`. To replay the separate finite cross-check, run `python verify_component_size_phase.py` with an ordinary Python interpreter; the script uses only the standard library. It independently enumerates every labeled edge configuration for \(2\le n\le6\) and verifies the exact factorial covariance formula at \(p\in\{1/5,2/5,4/5\}\). It checks every feasible threshold-order relation for \(3\le n\le80\) by comparing integer powers of rational numbers, avoiding floating-point approximations to logarithms or roots. At \(n=5\), \(p=13/40\), the exact formulas give \(\operatorname{Cov}(N_2,N_3)>0>\operatorname{Cov}(N_1,N_4)\).

Observed execution output:

```text
EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n= 2
EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n= 3
EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n= 4
EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n= 5
EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n= 6
EXACT_STRICT_BALANCE_AND_GLOBAL_THRESHOLD_ORDER_PASS n<=80
COEXISTING_COVARIANCE_SIGNS_PASS n=5 p=13/40
VERIFY_OK
```

The checks do not exhaust infinitely many sizes or edge probabilities. Generality follows from the displayed exact combinatorial identity, the integral representation, the strict convexity inequality, and the telescoping endpoint computation. The prior exact factorial tuple enumeration is explicitly credited to Sun's Proposition 3.2. Independent audit is not performed.
