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

The dimensionless Toeplitz matrix is positive definite by the integral of a squared trigonometric polynomial against the positive symbol. Integration by parts gives b>0 and pairing the two halves of the c₂ sine integral makes the sign of g the sign of α−1. The integral for b−g has positive integrand proportional to θ^(α−1) sinθ(1+cosθ), so 0<g<b and Δ>3g/2 for α>1. For α≤1 the shifted nonnegative generator has a positive path between any two sites, giving strictly positive entries at every positive time. In symmetric and antisymmetric outer-site coordinates the exponential leaves only entry 13 (and its transpose) able to change sign. It is one half of exp(−(a−g)τ) times H(τ), where H is the stated convex combination of exp((Δ−3g/2)τ) and exp(−(Δ+3g/2)τ), minus one. H has H(0)=0, H′(0)=−2g<0, H″>0 and diverges to +∞, proving exactly one positive crossing. For the asymptotics, g′(1)=Z/(4π) by integrating logθ against sin(2θ), and b(1)=2/π. The analytic continuation of P₁₃/τ to τ=0 is −g+(b²+2ag)τ/2+O(τ²). The implicit function theorem gives the positive root slope πZ/8 and the quadratic error. The analogous derivative equation gives the minimizing slope πZ/16; the negative interval shrinks to zero and the entry is strictly convex on it for α close to one. Substituting gives the dip coefficient −Z²/128. The stated h scaling and α=2 Fourier coefficients are consistent, and independent bisection of the endpoint equation agrees with 0.261185173260985 to its quoted precision.

## originality

PASS

The supported distinct claim is the exact entrywise recovery law and its two transition constants for the three-site principal restriction of the exact Fourier symbol. Neither the stencil/sign split nor the concept or qualitative conclusion of eventual positivity is credited as new. An earlier graph-heat result includes the three-vertex path but uses a provably different generator.

## value

PASS

Three sites are the first principal restriction that includes the second-neighbor coefficient, which is responsible for the positivity loss. This is a natural minimal model where the distinction from a spectral graph power matters. The exact last negative interval and its shrinking duration and depth quantify a transient that the qualitative eventual-positivity theory does not resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
