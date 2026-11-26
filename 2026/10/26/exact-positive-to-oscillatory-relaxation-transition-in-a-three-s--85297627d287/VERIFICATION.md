---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The graph of W is primitive and its Perron normalization is similar to W/λ_+. Direct determinant expansion gives p(x)=(x−1)(x²−wx−1)−s². The signs at −1,0,1,+∞ bracket one simple root in each of (−1,0),(0,1),(1,∞). The sum of the non-Perron roots is 1+w−λ_+, with the sign of p(1+w)=w²−s², because both lower-root factors are positive at 1+w. This proves the exact modulus comparison, including which mode wins and the equality case. At w=s the factorization is (x−1−s)(x²−1+s); multiplying the corresponding positive left and right Perron coordinates gives the stated stationary law. In the window w=sτ, τ=e^(−ξ), the equation for x=1+sz is z(2z−τ+s(z²−τz))−1=0. The two near-one roots have first-order coefficients (τ±√(τ²+8))/4, with O(s²) errors in x by simplicity. Vieta gives the remaining root −1+sτ/2+O(s²). Normalization gives gap coefficients √(τ²+8)/2 and (3τ+√(τ²+8))/4; their minimum switches at τ=1. The stationary weight at state 0 tends to 1/(1+2z_+²), which is the claimed L(ξ); the remaining two weights become equal, and the transitions converge to 0→0 and 1↔2. This proves cylinder convergence to the mixture. The two maximizing components are the zero-energy fixed point and alternating orbit; the threshold concerns the selected relaxation mode, not a change in the set of maximizing measures.

## originality

PASS

The supported distinct contribution is the exact finite-temperature positive-versus-negative sub-Perron mode comparison, together with the associated normalized critical-window gap. The static ground-state competition, bridge-exponent comparison and fixed-potential selection overlap materially with prior work and are not credited as new.

## value

PASS

This primitive Gibbs family contains the simplest competing fixed and alternating components. Equilibrium weights alone cannot identify whether the leading relaxation alternates, or on what scale the gap closes. The exact all-temperature switch together with its two different critical-window gap branches gives a motivated, useful spectral boundary. It is not merely an evaluation of stationary weights or a check of a single numerical parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
