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

# Verification notes

Run `python3 verify.py` using Python 3's standard library. The program constructs multivariate integer polynomials for the two affine branches and their four-step composition, checks six exact polynomial identities (trace, determinant, affine fixed-point denominator, two critical orbit coordinates, boundary trace), and checks four-step closure, admissibility and Schur stability for three rational witnesses. Output observed: `PASS: 6 exact multivariate polynomial identities and three rational period-four witnesses`.

The logical proof of the universal necessity/sufficiency and the boundary asymptotics is written in `RESULT.md`. Finite arithmetic checks do not establish the theorem for all real parameters; that quantification follows from the displayed strict inequalities, closed-form algebra and continuity. No independent audit has been conducted.
