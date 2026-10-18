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

# Reproducible checks
Run `python3 code/verify_wheel_character.py` with Python 3, standard library only. The script produces the records embedded at `verification/character_checks.txt` and ends in `VERIFY_OK` only when the complete signed-trace comparisons succeed.

Every \(n=3,\ldots,16\) case generates the complete matching-face set of the ordinary wheel complex, with the empty face. For each \(2n\) dihedral graph automorphism, it calculates the induced permutation of the \(2n\) wheel edges, tests setwise simplex invariance, computes the exact inversion sign of the restriction, and sums the augmented alternating chain Lefschetz trace. These \(266\) computed character values match the formula, including its identity cases. Additional exact character averages for \(3\le n\le240\) check divisibility, integrality and the four quotient congruence classes.

The infinity claim relies on the published homology-concentration theorem and the algebraic orbit-graph proof; exhaustive finite tests do not establish it. The script does not perform an independent scientific audit and does not prove novelty.
