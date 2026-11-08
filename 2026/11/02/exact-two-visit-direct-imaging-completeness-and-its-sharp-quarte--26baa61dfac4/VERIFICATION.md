---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fixed pair of orbital directions u1,u2 with dot product cosΔ, random inclination and initial phase are equivalent to a uniform line-of-sight vector. Failure at each visit is the disjoint antipodal cap pair |l·ui|>h, h=√(1−τ²). Pairwise intersections of signed caps have center separations δ and π−δ, yielding missed fraction [L(δ)+L(π−δ)]/(2π). Spherical excess yields L(s)=2π−4hβ−2γ on 0<s<2asinτ, and direct differentiation gives L′(s)=−2√(1−h²/cos²(s/2)), vanishing at tangency. Its strictly decreasing magnitude makes the probability monotone with the stated plateau for τ<1/√2 and unique quarter-orbit optimum otherwise. The rank-two sum of projectors ui ui^T has largest eigenvalue 1+|cosΔ|, attained at a signed bisector, proving the worst-case separation a√((1−|cosΔ|)/2). The tangent-cap overlap integral behaves as 4ε^{3/2}/3 with ε≈2√2(τ−τc), yielding the claimed constant. Independently integrated the physical detection event over 900,000 spherical test directions for five cases and verified the cap formula/maximum grids.

## originality

PASS

Repeated-visit direct-imaging completeness and probability calculation are classical. Brown–Soummer define accumulated/dynamic completeness and Monte Carlo orbital sampling; Stark and others numerically optimize revisit timing with richer constraints. In accessible texts those methods do not state a closed two-visit all-threshold lens formula, full optimizer plateau, sharp all-orientation guarantee or 3/2 onset. The claim is therefore only the exact idealized special-case theorem, not a new generic imaging algorithm or realistic mission optimum.

## value

PASS

The exact two-visit probability/guarantee question is a natural baseline for instrument scheduling when the orbit period/radius and geometric IWA are fixed. It distinguishes a whole interval of certain-detection spacings from a unique quarter-period optimum and quantifies the sharp 3/2 onset of unavoidable misses. The exact result is useful for unit-testing richer numerical completeness simulators, without claiming to optimize operational missions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
