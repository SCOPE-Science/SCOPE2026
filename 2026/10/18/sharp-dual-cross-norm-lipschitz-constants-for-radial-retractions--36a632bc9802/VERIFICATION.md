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

PASS. The exterior derivative DR_p(ru)=r^-1(I-u φ^T), φ_i=sign(u_i)|u_i|^(p-1), and integration on each straight segment proves its supremum is the global Lipschitz constant. Weighted absolute row sums yield 1-a^p+(a/w_i)(Σ_{j≠i}w_j^p)^(1/p)(1-a^p)^((p-1)/p), optimized as F_p(k_i). Weighted column sums yield the conjugate F_{pconj}(k_i). Hölder equality supplies boundary realizing directions; k_i peaks at min weight; the scalar F_s optimizer is unique by strict monotonicity of the derivative equation. Equal weights uniquely minimize B_s, leading dimension orders n^(1/p) and n^(1/pconj), with reversed ordering between n=2 and large n for p≠2.

## originality

PASS

PASS, qualified by older native-norm literature. The p=2 weighted sensitivity law is already published; the non-Hilbert conjugate pair for all p, weighted extremizing directions, and finite-versus-high-dimensional reversal are not implied by that special case or intrinsic-norm radial bounds.

## value

PASS

PASS. Exact cross-norm stability of a canonical nonlinear radial retraction measures anisotropic coordinate-error amplification relevant to Banach geometry and sensitivity analysis. The distinct dual exponents, optimal weights and provable dimension-order reversal give genuine structural behavior not reducible to known p=2 or native-norm constant bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
