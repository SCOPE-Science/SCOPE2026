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

# Reproducible checks and proof limits

Run \(\texttt{python3 check\_nested.py}\) with standard Python 3 in the same directory. Its explicit greatest-fixed-point game on guarded singleton or \(E_2\)-related pair maps is a check independent of the coded capped-profile criterion. The complete small-instance and sampled larger-instance comparisons total \(7335\) tested model pairs: \(1007\) for one colour through six elements and \(6328\) for two colours through four elements. Tests compare two genuinely different computations, not only two implementations of the proposed formula. The checker also evaluates the canonical-size summation by direct enumeration for one and two colours and checks the symbolic identity for four colours.

Expected output includes the lines \(\texttt{PROFILE\_VS\_GUARDED\_GAME\_OK 1 6 102 1007}\), \(\texttt{PROFILE\_VS\_GUARDED\_GAME\_OK 2 4 112 6328}\), and \(\texttt{NESTED\_EQUIVALENCE\_GF\_CHECK\_OK}\).

These finite observations are not an infinite proof. The proof in RESULT.md explicitly builds guarded formulas for each two-level profile and establishes the guarded back-and-forth property for arbitrary nonempty structures. The sharp bound follows from classwise minimum witnesses and a finite exact sum, independently of the game samples.

The checker does not establish novelty, historical completeness, optimality of the rank-five threshold, or correctness for signatures outside the stated scope. Independent auditing has not been performed.
