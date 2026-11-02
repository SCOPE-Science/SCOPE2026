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
# Exact reproducibility and boundaries

Invoke `python verify.py` with a SymPy 1.x installation satisfying `requirements.txt`. The exact verifier constructs the finite field \(\mathbb F_{25}\) as a quadratic extension, enumerates all 806 projective lines over \(\mathbb F_5\) and all 407526 over \(\mathbb F_{25}\), then computes the complete six-cell characteristic-five Gröbner-basis upper bounds. It subsequently computes tangent ranks in full four-coordinate Plücker charts and local-jet quotient lengths modulo degrees two and three, and checks Frobenius orbits.

The saved standard output `verify.stdout` records `LINE_COUNTS_BY_FIELD 4 40`, the cell dimensions \((26,9,4,0,1,1)\), the tangent ranks (four of rank three and 36 of rank four), the four doubled local jets, the total reduced support 40 and scheme length 44, and cycles of lengths one (four) and two (eighteen). It ends with `VERIFY_OK`.

Finite point enumerations alone are not geometric completeness proofs. The result uses exact Gröbner quotient dimensions to bound all geometric solutions in every echelon cell. The only slack occurs at one big-cell point with nontrivial tangent. The local length assertion uses exact truncated local ideals and Nakayama's lemma. All four doubled coordinate lines are rational over \(\mathbb F_5\); nilpotents do not affect the closed-point zeta function.

The calculation is limited to the displayed six-term quartic in characteristic five. It does not decide whether a different intended equation has 48 lines; an independent historical review has not been conducted.
