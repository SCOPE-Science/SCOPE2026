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

The analytic proof uses Fourier diagonalization, irreducibility over rational coefficients of the dyadic cyclotomic polynomial, positivity, and support cardinality four; the irrational example uses the explicit algebraic factorization. These arguments hold for every integer \(k\ge3\).

The standalone Python program `dyadic_weighted_check.py` was executed with Python 3 and SymPy. It exhaustively checked all unordered four-point supports on cyclic groups of orders 8, 16 and 32 for five explicit positive rational weight patterns, with exact cyclotomic reductions. Sampled cases were checked by an independently coded per-frequency exact reduction and numerical Fourier evaluation. The maxima and extremal equal-weight configurations agreed with the theorem. The irrational polynomial factorization was checked symbolically and its precise Fourier-zero classes verified at orders 8, 16, 32 and 64. The finite computations are cross-checks, not proofs for arbitrary group size or for untested coefficient patterns.

No independent validation or outside mathematical audit has occurred. Publication priority is not certified.
