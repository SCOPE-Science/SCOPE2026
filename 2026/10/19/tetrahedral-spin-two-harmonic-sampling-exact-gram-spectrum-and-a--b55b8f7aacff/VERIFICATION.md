---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

The result treats the unit-sphere trace-free intrinsic Hessian of exact-degree complex scalar spherical harmonics at the four tetrahedral vertices, with the explicit tangent frame in RESULT.md. The Gram matrix is normalized by dividing the sampling Gram operator by the scalar \(2\ell+1\) from the spherical addition theorem.

Run `python3 check_exact.py` from this directory. The standard-library-only checker computes all Legendre derivatives of orders zero through four at \(-1/3\) by an exact rational recurrence, checks the complete rank sequence through degree 24, and checks \(\lambda_{\ell,j}\ge D/25\) for every \(4\le\ell\le24\) and all three branches. It also independently generates harmonic homogeneous polynomials as the rational nullspace of the Laplace operator and computes the exact trace-free Hessian observation ranks through degree seven. The successful replay printed three PASS lines.

Run `python3 check_gram.py` with SymPy installed. It derives the three nonidentity two-by-two tetrahedral Gram blocks using the differentiated addition-theorem identity, applies every Klein-four character, and checks the exact eigenvalue factorization symbolically. Its successful replay printed one PASS line. Code files are embedded exactly as executed, not supplied as screenshots or run-log substitutes.

Run `python3 reproduce_tetra.py` with SymPy installed to check the low-degree inequalities using the finite Rodrigues expansion, derive the character-block spectra using directional Taylor coefficients, and evaluate the three rational tail constants at degree 25. The minimum low-degree branch ratio is \(4/81\) at degree four. The infinite-degree step is analytic: the classical Bernstein interior bound, the correctly differentiated Legendre ODE, and monotone rational estimates bound each relative eigenvalue perturbation by a constant strictly below one for every degree at least 25. Neither finite enumeration nor a successful run alone proves the unrestricted theorem.
