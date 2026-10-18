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

# Reproducibility and verification

Run `python verify.py` with SymPy installed. The script performs algebraic simplification of the Schur complement, the polynomial threshold identity, a symbolic asymptotic limit, and exact full-matrix inverse checks for integer sizes \(2\le m\le11\) at positive rational dampings \(1/20\), \(1/3\), \(1\), \(3\), and \(10\). It also checks leaf-orbit equality and domination over the adjacent nonleaf. Its observed output is `PASS 406 symbolic, exact-matrix and structural assertions`.

The key infinite-parameter proof steps are the semigroup-to-resolvent identity, the strict leaf-dominance rank-one update, and factorization of the resolvent-diagonal difference into a positive denominator and an elementary quadratic numerator. These steps are documented in `RESULT.md`. Finite computations do not certify parameter intervals or exhaust arbitrarily large trees. No formal proof assistant or independent scientific audit was used.
