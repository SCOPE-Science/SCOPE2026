---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

On ℓ²(Z³) with H0 symbol ε(k)=2Σ_j(1−cos k_j), two-site Birman–Schwinger reduction gives determinant 1−λ²[G0(κ)²−Gr(κ)²]. Strict heat-kernel positivity gives 0<Gr<G0, and both positive factors G0±Gr strictly decrease in κ, establishing a unique simple negative outlier iff λ>(g²−h_r²)^(-1/2). Spatial midpoint reflection swaps equal-and-opposite defect signs while bipartite staggering sends H0 to 12−H0, yielding exactly one matching upper outlier. At λc the threshold-state Fourier numerator is nonzero at k=0, hence /ε(k) in L1 but not L2; it gives bounded decaying non-ℓ² resonance. Since G0(0)−G0(κ)~√κ/(4π) while G0−Gr changes O_r(κ), expansion yields the stated 16π²/(a_r² λc^6) quadratic binding onset. Newtonian lattice Green tail Gr(0)~1/(4π|r|) gives λc−1/g~1/(32π²g³|r|²); g−h_e1=1/6 follows from cubic symmetry. Independently integrated 3D heat kernel with SciPy ive: g=0.25273100985866287, h_e1=0.08606434319199875, λc≈4.208302041223322, with separation n² penalty tending toward 0.196143842. These finite quadratures corroborate constants only.

## originality

PASS

Classical rank-one lattice defect thresholds and resonance behavior are acknowledged; the exact opposite-sign two-site zero-sum perturbation is not rank one. The inspected 2018 source addresses a centered impurity plus an entire symmetric nearest-neighbor shell, not a neutral arbitrary-separation pair. A related 2D opposing pair has unconditional binding, a genuinely different dimension-three phase. The exact all-separation neutral threshold and 1/|r|² penalty were not established by the inspected sources. Full 2009 same-dimensional impurity paper inaccessible: material residual priority risk.

## value

PASS

Neutral pairs are canonical balanced impurity perturbations and have a distinct sharp 3D onset threshold versus single attractive sites and 2D pairs. The theorem gives all-separation critical coupling, symmetric outliers, a clear resonance boundary and a quantitative price of nearby repulsion: a natural motivated spectral result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
