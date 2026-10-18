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

The exact scalar threshold follows by maximizing the cubic per-capita growth \(-a+Rs-ks^3\); its maximum vanishes when \(k=4R^3/(27a^2)\). The vector comparison is at the maximal coordinate, which is valid for every nonnegative trajectory of a regular graph. Stability follows from diagonalizing the symmetric adjacency matrix. At the critical fold, the Jacobian's simple zero eigenvalue and its negative mean-free spectrum justify transverse exponential convergence, and averaging yields the critical quadratic drift coefficient \(-R\). The scalar comparison provides a \(t^{-1}\) lower and upper bound for above-threshold starts, so exponentially small errors cannot alter the limiting amplitude.

Run `python VERIFY.py` with the dependency from `requirements.txt`. The script checks exact symbolic factorization, Jacobian eigenvalues, and a parameter example. These computations do not verify any infinite-time claim by enumeration. The proof in `RESULT.md` supplies the requisite infinite-time arguments.

Originality cannot be certified independently by these computations. General cooperative-systems literature could encompass the statement in an abstract form, and the full text of the closest older Smith (1986) paper was not accessible through available channels.
