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

# Verification record

The theorem is proved analytically in `RESULT.md`. The runnable `checker.py` uses Python 3 standard-library modules only; run it as `python3 checker.py` from the extracted package directory. Its most recent execution passed 10,167 finite consistency assertions, including independently assembled polynomial least-squares systems and direct kernel calculations. It printed the candidate positive critical point 7.540314189594786 and the corresponding limiting scaled squared error 1.791269160760916.

All universal quantifiers, interference-window classifications, uniqueness, and asymptotic optimality rest on the displayed mathematical proof rather than the tests. The checker does not prove a transcendental root enclosure or rule out a historical equivalent theorem. The computations require ordinary floating-point arithmetic; the exact claim defines the constants through equations and inequalities. Independent audit remains not performed.
