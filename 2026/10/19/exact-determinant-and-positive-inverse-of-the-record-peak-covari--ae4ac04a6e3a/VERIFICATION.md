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

# Verification and reproducibility

Run `python3 verify.py` in this directory. The script uses only Python's standard library and exact rational arithmetic; it has no external data dependencies.

Checks performed: all permutation orders for \(3\le n\le8\), with each entry of the exact record–peak cross-covariance compared against direct indicator averages; lower–upper bidiagonal factorization and determinant identities for \(3\le n\le34\); exact rational matrix inversion and strict positivity of every inverse entry for \(3\le n\le13\). The actual standalone script completed with 1,167 assertions passing.

The full theorem for arbitrarily large \(n\) is proved analytically in `RESULT.md`. The finite tests neither enumerate infinitely many cases nor provide external certification. In particular, this artifact has no independent audit or verified priority determination.
