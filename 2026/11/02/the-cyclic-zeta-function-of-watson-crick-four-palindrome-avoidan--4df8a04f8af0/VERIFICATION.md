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

# Exact reproduction instructions

Place `verify.py` next to `RESULT.md` and run `python3 verify.py` with a standard Python 3 interpreter. It requires no third-party packages. A successful run prints `VERIFY_OK`.

The program explicitly constructs the 64 triple states and admissible transitions, computes all 64 exact integer traces and then all 65 determinant coefficients through Newton identities, and compares the complete determinant against the factorization in `RESULT.md`. This checks a finite polynomial identity; the formal trace/log-determinant proof extends that identity to all positive word lengths.

The program also checks forward and reverse reachability, performs independent exhaustive word checks for linear and circular lengths 1 through 8, and checks linear-word recurrences on four even alphabet sizes through length 16. These additional tests do not prove infinite claims by themselves. Numerical values of the algebraic root and capacity are approximations; their exact definitions appear in `RESULT.md`.

No independent audit has been performed.
