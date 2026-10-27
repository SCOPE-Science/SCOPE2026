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

# Computational checks

The included `checker.py` enumerates all \(m\)-by-\(m\) matrices \(A,B\) in each listed small prime field, retains those satisfying \(A^2=0\), \(AB+BA=0\) and \(\operatorname{rank}\begin{psmallmatrix}A&B\0&A\end{psmallmatrix}=m\), and tallies \(\operatorname{rank}A\). The implementation performs modular Gaussian elimination and matrix multiplication; it does not merely print the formula being tested. It also divides by the full maximal-rank square-zero class size and checks resulting rational probabilities.

Tested combinations: \(m=1,2\) for \(q=2,3,5,7\), and \(m=3\) for \(q=2\). The checker reports nine cases, 145348 tested block pairs, and `ALL_MAXIMAL_SQUAREZERO_COMMUTATION_TESTS_PASSED` in the included `check_output.txt`.

These exhaustive instances are direct corroboration of the finite formulas but do not establish the universal counting identity for arbitrary prime powers or the infinite-dimensional asymptotics. The proof of those claims is in `RESULT.md`; no independent mathematical audit was performed.
