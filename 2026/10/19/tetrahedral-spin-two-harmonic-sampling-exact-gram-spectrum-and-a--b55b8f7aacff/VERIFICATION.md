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

# Reproducible verification

The result treats the unit-sphere trace-free intrinsic Hessian of exact-degree complex scalar spherical harmonics at the four tetrahedral vertices, with the explicit tangent frame in RESULT.md. The Gram matrix is normalized by dividing the sampling Gram operator by the scalar \(2\ell+1\) from the spherical addition theorem.

Run `python3 check_exact.py` from this directory. The standard-library-only checker computes all Legendre derivatives of orders zero through four at \(-1/3\) by an exact rational recurrence, checks the complete rank sequence through degree 24, and checks \(\lambda_{\ell,j}\ge D/25\) for every \(4\le\ell\le24\) and all three branches. It also independently generates harmonic homogeneous polynomials as the rational nullspace of the Laplace operator and computes the exact trace-free Hessian observation ranks through degree seven. The successful replay printed three PASS lines.

Run `python3 check_gram.py` with SymPy installed. It derives the three nonidentity two-by-two tetrahedral Gram blocks using the differentiated addition-theorem identity, applies every Klein-four character, and checks the exact eigenvalue factorization symbolically. Its successful replay printed one PASS line. Code files are embedded exactly as executed, not supplied as screenshots or run-log substitutes.

The infinite-degree step is analytic: the classical Bernstein interior bound for Legendre polynomials, the Legendre ODE and its first two derivatives give normalized eigenvalue perturbation bounds less than one for all degrees at least 25. The rational terminal constants in the theorem are independently evaluated in check_exact.py, but the inequalities themselves are justified explicitly in the proof. Neither finite enumeration nor a successful run alone proves the unrestricted theorem. No external or independent mathematical validation has been performed.
