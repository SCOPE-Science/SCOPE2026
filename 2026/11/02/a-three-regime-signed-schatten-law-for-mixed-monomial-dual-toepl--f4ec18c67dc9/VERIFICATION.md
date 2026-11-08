---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS — On QL² of the unit disk with normalized area, the established S_f S_g product identity gives D=S* S−SS*=|η|²H_{bar z^q}H_{bar z^q}*−H_{bar z^p}H_{bar z^p}*. Angular sectors have rank at most two. Direct disk integrals give A_m(L)=m²/((L+m)(L+2m)), cross-Gram G_pq(L)=pq/((L+p+q)sqrt((L+p)(L+q))), and determinant Δ=p²q²(p−q)²/[(L+p)(L+q)(L+2p)(L+2q)(L+p+q)²]>0. Thus for every nonnegative angular index the characteristic roots (τ±sqrt(τ²+4|η|²Δ))/2 have opposite signs, and remaining negative sectors are finite. Sum of squared Hankel column norms telescopes to m, proving trace class and Tr D=|η|²q−p; orthogonal radial complements give infinite-dimensional kernel. As L→∞, τ=sL⁻²+O(L⁻³), |η|²Δ=gL⁻⁶(1+O(1/L)), giving 2/4 tails when s≠0; at balance |η|=p/q cancellation leaves cubic roots with coefficients (p²/2)(sqrt(13)|p−q|±3(p−q)). Comparison with p-series gives strict Schatten cutoffs 1/2,1/4 or both 1/3. An independent rational Gram check across positive/negative angular sectors corroborated identities; infinite claims follow from the explicit expansions and summability, not the finite check.

## originality

PASS

PASS, qualified. Stroethoff–Zheng (2002) supplies exactly the operator product premise; Kong et al. (2026) treat hyponormal and subnormal criteria. The signed rank-two eigenvalue formulas and critical decay constants are not implied by qualitative positivity or spectral properties of S. The plausible Ding et al. 2020 article could not be read fully because authorized Oxford access was VPN-disconnected after open-source routes failed, so the comparison is not a definitive noncoverage ruling.

## value

PASS

PASS — The exact signed spectrum of a canonical mixed-monomial dual Toeplitz defect includes an abrupt, calculable 2/4-to-3/3 threshold and sharp constants. Determining positive/negative parts separately answers a meaningful non-normal operator-ideal classification, beyond textbook trace-class positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
