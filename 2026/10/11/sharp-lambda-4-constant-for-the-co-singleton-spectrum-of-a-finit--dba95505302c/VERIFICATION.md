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

The proof was checked at the level of definitions, normalization, boundary cases, derivative signs, and equality conditions. With normalized counting measure, Parseval identifies the Fourier coefficient \\(\\ell^2\\) norm with \\(\\|f\\|_2\\), and the conversion from the unnormalized vector quotient to the normalized \\(L^4/L^2\\) quotient contributes the required factor \\(N\\).

`artifacts/verify.py` performs exact rational checks of the closed form and equality witness for every \\(4\\le N\\le100\\), deterministic numerical checks on complex mean-zero vectors for \\(4\\le N\\le20\\), and deterministic tests of the pair-smoothing inequality. The theorem itself is proved analytically for every finite abelian group of order \\(N\\ge4\\); finite computation is used only as a reproducibility check.

No claim is made for nonabelian groups, arbitrary character subsets, or the full equality classification at orders below four.
