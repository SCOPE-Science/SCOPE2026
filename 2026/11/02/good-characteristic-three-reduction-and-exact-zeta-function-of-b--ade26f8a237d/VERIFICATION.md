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

# Verification

Run `python3 verify.py` with Python 3.10 or later. The script uses only standard-library integer and polynomial arithmetic. It checks the projective counts for \(\mathbb F_3\) and \(\mathbb F_9\), the predicted second count from the zeta numerator, and the four-by-four Hasse–Witt coefficient matrix from the polynomial \((e_2e_3)^2\) after elimination of \(e_1\).

Geometric smoothness over the algebraic closure follows from the two-value Jacobian argument in RESULT.md and is **not** inferred from finite-field enumeration. The \(\mathbb Q\)-isogeny of the generic Bring Jacobian is an explicit cited input from Braden and Disney-Hogg, Proposition 4.5, not certified by this verifier. No independent audit has been performed.
