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

Run `python3 checker.py` after extracting the standalone source file. It uses only the Python standard library and checks (i) finite-state optimal adaptive cover probabilities against the independent-collector product law for both starting parts, (ii) finite source stochastic-order inequalities and geometric-CDF log-concavity, (iii) coefficients of the geometric independent-increment factorization, and (iv) the exact harmonic mean formula with a numerical asymptotic check. The checker currently reports 4,661 passing assertions and diagnostics.

These finite tests check concrete instances and the algebraic identities used in the proof; they are not exhaustive over arbitrary part sizes. The all-size stochastic order depends on the independent-delay and log-concavity argument in `RESULT.md`. The limiting laws depend on the infinite-summand variance bound, a standard exponential-maximum limit, and independence of alternating offer streams. No external or independent audit has been performed.
