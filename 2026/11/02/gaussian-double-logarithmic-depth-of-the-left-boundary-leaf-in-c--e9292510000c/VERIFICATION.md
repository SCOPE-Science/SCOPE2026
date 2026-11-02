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

# Reproducible finite verification and mathematical limits

Run `python3 verify_boundary.py` using Python 3 and its standard library. The checker produces 383 passed assertions. It enumerates all ordered rooted binary shapes with at most eight leaves and compares the induced left-boundary depth distributions with an independent direct recurrence. It verifies exact harmonic-mixture transition probabilities using rational arithmetic, tests moment recurrences, and numerically evaluates finite first through fourth potential-drop moments and finite height expectations/variances.

The exact proof is in RESULT.md. In particular the infinite-limit argument uses a harmonic Riemann-sum estimate for potential drops, a stopped descending Markov chain, the martingale central limit theorem and an expected-time bound on the terminal segment. Numerical examples are **not** offered as an infinite-size proof, and a finite checker cannot rule out missing assumptions in the martingale argument. No independent mathematical audit has been performed.
