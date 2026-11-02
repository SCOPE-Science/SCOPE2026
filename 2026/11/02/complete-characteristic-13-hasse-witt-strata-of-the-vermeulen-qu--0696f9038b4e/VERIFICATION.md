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

# Verification and scope

Run `python3 verify.py` with Python 3.9 or later (standard library only). The program independently reconstructs the \(3\times3\) characteristic-\(13\) Hasse–Witt coefficient matrix by sparse multiplication and by the multinomial theorem. It checks all zero off-diagonal entries, factorisations, coprimality of the two cubic Hasse factors by enumerating their roots over \(\mathbb F_{169}\), separation of singular parameters, all six nonordinary parameters, and the companion quartic's diagonal matrix \(11I_3\). Its projective point counts in \(\mathbb F_{13}\) independently check characteristic-thirteen trace congruences for four parameter values and for the companion quartic. The uniform theorem also uses the standard cohomological coefficient-extraction theorem and the diagonal semilinear-Frobenius stable-rank argument. Finite-field enumeration does not on its own prove the algebraic-closure statement. No external validation was undertaken.
