---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Width W=Σa_i|U_i| and brightness B=VΣa_i^(−1)|U_i| for the same spherical U; Dirichlet(1/2,...,1/2) coordinate squares give E|U_i|=μ_d, E|U_i|²=1/d, E|U_iU_j|=2/(πd). Expansion yields E(WB)/V=1−2/π+2Q/(πd) and EW EB/V=μ_d²Q, hence claimed covariance. Opposite coordinate absolute values have negative covariance by conditioning on |U_1|², thus β_d>0. Strict positivity of cube variance ensures threshold T_d>d². For fixed min=1,max=R, function Q=Σ_{i,j}e^{z_i−z_j} is convex on log-side cube, and reflection z↦logR−z plus fixed endpoints gives central minimizing free z; strict convexity for R>1 gives uniqueness. Separate coordinate convexity forces maxima at cube vertices: k(d−k) optimum floor(d²/4); connected cube gives all intermediate values. Threshold roots and gamma-ratio limits follow. Independently recomputed Q extremizers and both thresholds in d=2,3,4,10 (d=2 R_-=R_+≈1.52017161; d=3 R_-≈1.72912921,R_+≈1.88196752). These finite checks do not substitute for convex proof.

## originality

PASS

Classical Gaussian/spherical width moment work of Kabluchko–Litvak–Zaporozhets (2015/2016) and Finch (2011) provides marginal moments, and generalized weighted folded-normal or polarization formulas can imply the mixed covariance identity; that intermediate identity is not treated as novel on its own. The stated contribution is joint sign classification optimized exactly over all orthotopes at fixed aspect ratio, including two distinct extremizers and high-dimensional threshold scales, not found in inspected older sources. Highly relevant Abas arXiv:2608.03305 and arXiv:2609.26202 address rectangular-box moments and joint width/brightness; only abstracts were accessible: PDF and arXiv HTML retrieval rejected, Zenodo alternative unavailable, authorized institutional paper attempts returned vpn_disconnected. Their potentially dominating moment/optimization coverage is a specific residual risk, not falsely deemed absent. Resultary ranked the identical current record plus different orthotope perimeter/brightness findings.

## value

PASS

A complete sharp same-direction sign law is naturally meaningful: width and hyperplane projection brightness of the same box can switch from positive to negative covariance, with the sign not determined by aspect ratio in d≥3. The theorem identifies all equality shapes and quantifies diverging threshold scales, providing a useful all-dimensional benchmark beyond elementary spherical second moments or one isolated box example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
