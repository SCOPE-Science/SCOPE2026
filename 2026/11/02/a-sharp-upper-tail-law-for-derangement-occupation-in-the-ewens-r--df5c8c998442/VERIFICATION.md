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

# Reproducibility
Run `python3 verify.py` with the Python standard library. This replays the exact-rational moment/path checks, independent Markov recursions, queue simulation with fixed seed, and renormalized moment convergence tests. The completed execution passed 126 assertions.

The code does not implement a symbolic proof of the Tauberian theorem. Infinite-product convergence, ordered-time factorization, and endpoint asymptotics require the arguments in RESULT.md. The Monte Carlo estimates are subject to sampling error and use fixed horizon 19, whose ignored exponential tail is at most \(e^{-19}\). The exact-rational checks cover finitely many parameters and steps, not all cases.
