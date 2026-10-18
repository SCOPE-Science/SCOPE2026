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
# Verification of the exact finite certificate

Execute `python CHECKER.py` from the directory containing that file. Python's standard library is sufficient; no compiled algebra package is required.

The checker first produces exactly 120 unique vertices as four-vectors whose doubled coordinates lie in \(\mathbb Z[\varphi]\), represented as integer pairs. It confirms every point has unit norm and that all 14,400 pairwise inner products lie in the stipulated nine-level set. For each of the nine distance levels it counts all 120 intermediate points to obtain multiplication coefficients, and it verifies the resulting class-product identity **for every pair** of vertices. These exhaustive checks justify applying exact polynomial arithmetic to the full 120-by-120 Gram matrix rather than guessing a spectrum from a few eigenvalue samples.

The exact Gram identities are checked for cutoffs one through eight. Rational Vandermonde inversion of integer matrix-power traces yields rank sequence \((1,5,14,30,55,91,116,120)\), cutoff-seven eigenvalue multiplicities \((4,91,16,9)\) for scaled eigenvalues \((0,120,210,280)\), and cutoff-eight multiplicities \((55,16,45,4)\) for scaled eigenvalues \((120,210,280,480)\). The checker also certifies that the constant vector has normalized Gram eigenvalue one and that the stated cubic polynomial is the full Gram inverse.

The finite checker cannot alone establish global weighted optimality because weights range over a continuum. That conclusion follows from the transitive-permutation averaging and Rayleigh-quotient argument in `RESULT.md`. It likewise does not verify novelty or classify cases outside the finite 600-cell configuration. No independent audit has been performed.
