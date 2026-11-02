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

The proof is a complete, finite connected-component enumeration followed by exact algebraic factorization. The counted-variable table in RESULT.md covers every one of the 64 possible occupied subsets of six independent bonds. Its reduction to \(K=(1-p)(p-g)^2\) establishes the distribution statement uniformly for real \(g,r\in[0,1]\). The strict reversal and two-moment alias then follow by sign and moment calculations.

To reproduce the computational cross-check, run `python3 verify.py` with Python 3 and its standard library. The checker derives the coefficient table using disjoint-set connectivity; it independently computes the original nine-opportunity model via exhaustive 512-case enumeration with breadth-first connectivity. It verifies exact rational instances, normalization, all four mass differences, first three moment differences, full-outbreak ordering, and endpoint cases. The final embedded source passed 338 exact checks.

The numerical/rational checks cannot independently prove the infinite continuum of parameter choices. That part rests on the explicit \(2^6\)-state coefficient table and the algebraic factorization displayed in RESULT.md. The proof does not cover directed infection dynamics or stochastic infectious-period correlations. No independent audit or external certification has been performed.
