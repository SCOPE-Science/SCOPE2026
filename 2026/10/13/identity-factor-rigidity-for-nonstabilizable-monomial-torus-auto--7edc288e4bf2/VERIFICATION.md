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

# Reproduction and logical verification

Execute `python3 verify_matrix.py` with Python 3's standard library. Its exact-integer output was `IDENTITY_MONOMIAL_INPUT_CHECK_OK`. This checks determinant \(1\), characteristic polynomial \(t^3+t-1\), discriminant \(-31\), and absence of rational roots of the monic cubic; together with the sign check at \(0\) and \(1\), these verify that the example meets the required spectral hypotheses.

The unrestricted result is established by the proof in `RESULT.md`; it is not inferred from code or a finite model census. Essential independent mathematical checks carried out in the same review were: (i) finite Laurent supports force periodic divisors to depend only on the fixed variables; (ii) the divisor-orbit obstruction rules out contraction of nonperiodic prime divisors under an algebraically stable conjugate; (iii) deleting finitely many invariant contracted divisors gives a factorial ring whose units have the explicit free basis; (iv) divisor localization on a smooth rational projective model provides the stated exact boundary sequence; (v) effective resolution pullback yields a nonnegative boundary matrix, intertwining character pullback and Neron--Severi pullback; (vi) its peripheral complex eigenvalue contradicts Perron--Frobenius; and (vii) the spectral irrationality follows from the impossible integer \(0<\beta^m<1\).

The proof uses standard facts about birational pullbacks, rational smooth projective varieties, and monomial first dynamical degrees, with the relevant primary literature cited in `RESULT.md`. No computational search over projective models was attempted. Independent verification and a comprehensive earlier-literature equivalence search have not been performed.
