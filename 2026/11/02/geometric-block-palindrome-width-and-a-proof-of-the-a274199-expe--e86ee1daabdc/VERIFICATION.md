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

Execute the self-contained script \(\texttt{python3 verify.py}\) using Python 3 (standard library only). It compares greedy largest-block-palindrome widths with the unbordered-word recurrence for 84,133 finite word instances; separately computes maximum possible factorization widths by recursively trying **every** outer-border length on 116,901 finite word instances and checks greedy optimality; independently derives normalized-unbordered polynomials, inverts the series through degree 75 and matches it to a direct adjacent-restricted-composition recurrence; reconstructs the defining A274190 triangle through row 80 and checks stabilized A274199 coefficients; and matches the published asymptotic means to four decimal places. On completion it prints \(\texttt{VERIFY\_OK}\).

These finite calculations are not proofs of the infinite distribution or infinite reciprocal-alphabet identity. The proof of those claims is self-contained in RESULT.md except for the credited known greedy shortest-border property; it uses exact bijections, monotone and dominated convergence, and a finite triangular determinant evaluated before its coefficientwise limit.
