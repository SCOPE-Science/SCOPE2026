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

# Mathematical verification

The symbolic argument in `RESULT.md` is self-contained. The independent finite program is `checks/verify.py`; execute with `python3 checks/verify.py` (Python 3.9+ and NumPy). It builds the original hub–arm block matrix before forming the Jacobi matrix, tests every predicted finite-volume eigenvalue and the strict boundary criterion for 2310 parameter-size instances with \(2\le N\le16\), directly diagonalizes the full \(4N\)-site Hamiltonian when \(N\le8\), includes destructive-interference and parallel-hop cases, and checks the cubic small-flux coefficient.

The half-line theorem, its \(c=0\) case, the potential extra zero hub eigenstate, and the all-size finite threshold are proved by the recurrences and exact resolvent in `RESULT.md`. Random finite tests do not prove any of these infinite or all-parameter statements. External independent audit remains unperformed.
