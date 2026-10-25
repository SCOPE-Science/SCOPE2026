---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. The domain is real symmetric 2x2 matrices, the nearest positive-semidefinite projection is Frobenius, and input/output norms on the three coordinates (a,c,b) count b once. The Frobenius-isometric transformation to a Lorentz cone yields the mixed-sector Jacobian affine in s=T/r. Its two endpoint matrices are the rank-one oblique projection vf^T and its complement, f^Tv=1, v=(t,1-t,q), f=(t,1-t,2q), q^2=t(1-t). Explicit 3x3 row/column absolute sums give the sharp 3/2 ℓ_1 and ℓ_∞ bounds; the two oblique complementary operators have equal Hilbert norms and squared norm (1-q^2)(1+2q^2)≤9/8. Convexity controls intermediate Jacobians, integration along generic segments and continuity handle switching boundaries. The offdiagonal scaling pair attains ℓ_1, and derivatives as s↑1 with q=1/2 give sharp remaining constants. Independent t-grid endpoint 3-norm calculations corroborated the matrices; the proof, not the sample grid, covers the continuum.

## originality

PASS

PASS on best-of-knowledge: the sharp independent-entry Lipschitz triple is mathematically distinct from standard Frobenius spectral formulas and from standard-coordinate Lorentz projection norms. No examined prior statement implies all three best constants; possible older cross-norm spectral projection theorem remains a priority risk.

## value

PASS

PASS. Independent-entry metrics are the natural three free parameters of a symmetric 2x2 matrix, distinct from the Frobenius metric defining its cone projection. Determining sharp stability constants across ℓ_1, ℓ_2 and ℓ_∞ resolves a concrete norm-change sensitivity problem, with genuinely sharp boundary and attainment differences; it is neither textbook Frobenius nonexpansivity nor arbitrary rescaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
