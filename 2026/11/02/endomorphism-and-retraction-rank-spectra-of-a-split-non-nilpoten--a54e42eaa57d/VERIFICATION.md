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

# Reproduction and boundaries

With Python 3, execute `python verify.py` alongside this document. The script independently loops over all linear maps on the explicit algebra in six prime-field cases and tests the bracket-preserving identity and idempotency by direct matrix multiplication, before tallying image ranks. The exhaustive cases are \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\).

The run produced `VERIFY_OK: 6 exhaustive prime-field cases and 30 algebraic consistency cases`. The independent direct counts for \((n,q)=(4,2)\) were \([1,77,550,372,24]\) for all endomorphisms and \([1,40,44,13,1]\) for idempotents, ordered by increasing rank. For \((n,q)=(3,3)\), the respective counts were \([1,56,102,12]\) and \([1,18,4,1]\). The additional 30 checks verify polynomial totals and nonnegativity for more parameters but do **not** exhaustively enumerate matrices over extension fields.

The unrestricted theorem relies on the tensor-factorization, inclusion-exclusion, and projection-counting arguments in `RESULT.md`, not finite observations. The asymptotic uses the exact full-matrix nullity distribution and a quantified negligible-mass comparison. Exact bibliography relevance and remaining possible priority risk are given in `REVIEW.md`.
