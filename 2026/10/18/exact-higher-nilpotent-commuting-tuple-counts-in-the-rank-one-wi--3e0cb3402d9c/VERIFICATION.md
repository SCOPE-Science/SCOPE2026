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

# Verification of the higher Witt commuting-tuple formula

Run `python verify_witt_commuting_tuples.py` in the same directory. The self-contained standard-library checker enumerates coefficient vectors for derivations on \(\mathbb F_q[t]/(t^p)\), builds the linear operator on monomials, and checks nilpotence by matrix multiplication. It independently calculates the commutator matrices and counts common-neighbor intersections for triple and quadruple tuples. The tested cases are \((p,q)=(5,5),(3,3),(3,9)\); the last uses a genuine irreducible-quadratic model of \(\mathbb F_9\). The \(p=3\) checks test a boundary beyond the primary theorem's \(p\ge5\) domain.

Observed exact counts at \((5,5)\) are \(625,6625,108625,2418625\) for arities one to four; they agree with the closed expression. The checker prints `VERIFY_OK_WITT_ALL_ARITY_NILPOTENT_COMMUTING` only after all checks succeed.

**Limits:** Computer enumeration is exhaustive only in the stated small finite fields and arities. It does not establish the dimension of the algebraic variety or the formula for arbitrarily large fields and arities, which follow from the proof in `RESULT.md`. No independent audit has been performed.
