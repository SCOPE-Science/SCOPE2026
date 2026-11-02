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

# Reproducibility and verification limits

Run `python3 verify.py` with Python 3 and SymPy installed. The included `verification-output.txt` is the exact recorded successful execution output. The program constructs the symmetric quintic with the hyperplane equation substituted, differentiates exactly, and evaluates the full four-by-four local Hessian in the last-coordinate-one affine chart. It checks nonzero determinants for the diagonal and signed nodes in characteristic three and the signed node in characteristic five.

It independently exhausts the prime-field projective points on the defining equations in characteristics three and five, tests singularity using the full six-coordinate Jacobian criterion, and verifies equality with the union of coordinate boundary and signed torus points. It reports 35 boundary points, ten signed nodes and one diagonal node in characteristic three, and 75 boundary points plus ten signed nodes in characteristic five. The output terminates in `VERIFY_OK`.

These computations are exact but finite. Infinite-field geometric completeness, the local ordinary-double-point classification over algebraic closures, and all-extension rational point counts are established by the symbolic arguments in `RESULT.md`; the program does not purport to certify every finite extension. No claim about a global resolution or about the nonreduced structure of the singular scheme is checked or made.
