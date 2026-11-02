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

# Verification

`STANDALONE_CHECK.py` implements the finite-state Markov process with state (vertex, mask of previously visited endpoints), solves its absorbing mean equations over exact rational numbers, and independently evaluates the Chebyshev mean for each half-length from one through five at resetting probabilities zero, one seventh, one quarter, and one half. It also checks the closed Chebyshev coefficient sequence through degree seventeen, the analytic zero-reset derivative coefficient, and three numerical finite-size approximations to the lattice correction. Direct execution in an isolated package directory with Python's standard library yielded:

```text
PASS: 125 checks; 20 independent finite-state mean comparisons plus polynomial and asymptotic checks
```

The exact rational checks cannot certify the infinite-size inequalities or asymptotic statements. Those are justified analytically by the recurrence, discounted-tail convexity, and uniform expansions in `RESULT.md`. Numerical comparisons of the lattice correction are sanity tests only. Independent audit and externally certified numerical enclosures have not been performed.
