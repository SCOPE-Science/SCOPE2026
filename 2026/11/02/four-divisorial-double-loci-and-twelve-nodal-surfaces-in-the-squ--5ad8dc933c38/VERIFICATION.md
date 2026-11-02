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

Run `python verify.py` in an environment with SymPy installed. The program returns `VERIFY_OK` after exact integer/rational-polynomial computations. It verifies:

- Identity of the two expressions for the bidegree-\((4,2)\) discriminant;
- the determinant \(-4A^2B^2(A-B)^2\) of its exponent quadratic form;
- the transverse binary discriminant \(16uv(s+u)(s+v)\);
- the three critical coefficient derivatives on \(A=0\), \(B=0\), and \(A=B\);
- vanishing of all partial derivatives on the sixteen proposed irreducible singular components;
- rank-three transverse Hessians at representatives of all five surface-component kinds.

The exhaustive proof of the singular-locus **support** is the differentiation and case analysis in `RESULT.md`; the verifier's Hessian examples are nondegenerate witnesses rather than exhaustive point enumerations. The report does not assert reduced Jacobian-scheme structure, global resolution, or analytic classification at component intersections. No independent validation is claimed.
