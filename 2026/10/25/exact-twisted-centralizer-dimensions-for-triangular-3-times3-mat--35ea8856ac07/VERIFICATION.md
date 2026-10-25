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

The theorem is proved by an exhaustive symbolic case distinction on the three diagonal coordinates of an arbitrary upper-triangular matrix, followed by three possible multiplicative-resonance equations. The isolated algebraic mechanism is recorded explicitly in `RESULT.md`.

Run `python verify.py` in the directory containing that script. It uses exact finite-field addition and multiplication (including a polynomial-basis model of \(\mathbb F_4\)) and Gaussian elimination on the six scalar equations. Confirmed field/twist tests were \(q=4\) with two twists, \(q=5\) with two twists, and \(q=7\) with four twists; every complete nullity distribution and pair count matched the symbolic formulas, printing `VERIFY_OK`.

Finite checks do not prove the result in arbitrary finite fields. The complete algebraic proof is independent of the program; the program is not an external or infinite certificate. The excluded twists and higher matrix sizes remain outside scope. Independent audit status is not performed.
