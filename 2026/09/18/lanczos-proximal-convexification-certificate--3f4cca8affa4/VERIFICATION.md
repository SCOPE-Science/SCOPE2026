---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Chen–Lu §2.4 assumes Q+γ⁻¹I≻0; Eq. (11) specifies the 0.01 margin but calls the Lanczos output only an estimate. The frozen theorem explicitly conditions the counterexample on use of the ordinary smallest Ritz value, not on unverifiable implementation details. Scalar spectral translation gives exactly the error budget θ−λmin<δβ, which for negative λmin also implies γ>0. For every m, at the displayed start the m Krylov columns form an invertible scaled Vandermonde on the m distinct positive coordinates. Thus θ=δ/(m+1), and 0<s=mδ/(m+1)<1 for 0<δ<1. Positive and negative shifted eigenvalues coexist. Full column rank persists locally; K(KᵀK)^−1/2 is a continuous orthonormal basis there, hence the strict inequalities persist, also at nonzero components in the negative eigendirection. This gives positive failure probability for usual continuous random starts with full support, not for all possible distributions supported elsewhere. The sample m=4 gives s=1/125 and shifted minimum −124/125. Symmetry gives ‖Q‖₂≤β, so the shifted minimum is at least (δ−2)β and s≥(δ−1)β. The enclosure-only threshold really is strict: diag(−1,1) with its positive eigenspace witnesses 1<δ≤2, including singularity at 2; for 0<δ≤1 the stated diag(−1,0) works in the general class, or take diag(−1,δ/2) for a strictly indefinite witness. The Gershgorin lower bound and max-shift repair give margin ηβ in exact arithmetic; certified floating-point use must maintain a rigorous lower bound. The bundled rational examples were inspected, not run, and are not evidence for the continuum or all-m claims.

## originality

PASS

The fact that extreme Ritz values can miss an extreme eigenvalue and the use of spectral lower bounds are existing ideas. The distinct result supported here is the precise PDNQP Eq. (11) no-certificate analysis, especially the all-budget open-set witness with positive proximal denominator and the sharp enclosure-only boundary for that rule. The scalar-shift and Gershgorin formulas are not separate novelty claims.

## value

PASS

This resolves a concrete interface between a proposed factorization-free initialization and its solver's strong-convexity hypothesis. The witness distinguishes a seemingly admissible positive proximal parameter from actual convexification and persists under perturbation for every finite budget, while the sharp norm-only boundary explains why an a posteriori spectral lower bound is preferable to inflating the heuristic margin. It does not assert actual solver failure or divergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
