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

# Reproducible mathematical verification

Run the standalone scientific reproduction program with `python VERIFY.py` in an environment containing Python 3, NumPy and SciPy. The actual execution reported `PASS 307 exact rational, spectral, asymptotic and endpoint checks`.

The finite checks independently construct \(G_n\), the triangular sweep factor and its exact rational inverse in dimensions \(2\) through \(8\); they compare the resulting matrix against an explicit pass of individual coordinate minimizations and verify the strictly positive Perron block. They calculate the full numerical eigenvalue spectrum and check agreement with the unique exponential-root prediction. Additional dimensions through \(1000\) check the Lambert \(W_{-1}\) limit and its finite-size coefficient, and fixed dimensions check the second-order near-simplex expansion. The included source is the complete reproduction program; no external data files are required.

The matrix checks concern finitely many parameter instances and are **not** a substitute for the universal spectral proof, for the limiting integral, or for exact error estimates. Numerical eigenvalue calculations can become inaccurate near singularity; the proof of each infinite-quantifier statement instead uses exact algebra, the Perron--Frobenius theorem, a uniform quadrature estimate, or Taylor expansion with bounded derivatives.

This package has not undergone an independent audit or independent validation. The self-review addresses mathematical correctness, literature overlap and mathematical value with the stated source-access limitations.
