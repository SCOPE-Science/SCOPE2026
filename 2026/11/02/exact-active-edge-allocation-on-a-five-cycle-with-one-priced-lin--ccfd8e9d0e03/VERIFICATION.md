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

# Reproduction checks

Run `python verify.py` with Python, SymPy and NumPy. The verifier symbolically checks the even and odd eigenvalue-one determinants, the exact five-component eigenvectors, the normalized pairwise-difference identities for every edge, both positive dual multipliers' stationarity equations, the dual cost identity, the rational price derivative, and the negative Bernstein basis coefficients. It checks the exact witness \(q=25/16\) and uses an independently constructed numerical five-by-five Laplacian for ten nontrivial prices and 1,500 nonuniform positive feasible rivals. The check output is 1,520 numerical checks plus the exact symbolic assertions. The numerical loop is not intended as an exhaustive search or an independent proof.

The interval-wide proof is in `RESULT.md`: each denominator is nonzero on \((\sqrt{2/5},4/5)\); spectral traces place the remaining two eigenvalues above \(1\); strict Bernstein signs establish unique parameter inversion; the positive dual combination supplies a global semidefinite bound, and equality determines each individual conductance. The proof does not extend a uniqueness claim to the excluded endpoints. Verification uses this package's own `verify.py`, rather than any historical or unrelated execution output.
