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

With fixed Q and stationary motile mass 1/(r+1), the Green–Kubo normalization for E|R_t-R_0|^2/(4t) is one half the integral of the propulsion dot-product correlation. Conditional on the switching path the Brownian first harmonic supplies exp(-D_R t), so the integral is absolutely convergent. To replay the resolvent independently, condition on the first switch: with Z_+=D_R+r lambda-i Omega and Z_-=D_R+lambda+i Omega, the integrals for an endpoint motile indicator obey I_+=1/Z_++r lambda I_-/Z_+ and I_-=lambda I_+/Z_-. Solving gives the frozen complex quotient and hence F. Any initial-state correction to the mean-square-displacement integral is bounded, by switching mixing in the earlier time times Brownian damping in the lag. The derivative numerator is r(a_0+a_1 x+a_2 x^2): a_0>0, and with K=(r+1)+(r-1)y^2, a_2=4y^2-K^2 changes sign exactly at K=2y. For r<=r_c the linear coefficient is strictly positive, including at threshold; above it the quadratic has one positive and one negative root since a_0>0>a_2. This gives strict monotonicity or a unique finite maximum over lambda>0 at fixed r. Using the positive root in the form (a_1+sqrt(a_1^2-4a_0 a_2))/(-2a_2) gives its divergence and leading coefficient y-1. Independent symbolic evaluation of the y=r=2 example gives x_*=5/3 and active values 1/20, 1/30, 1/26 in units v^2/D_R at the maximum, vanishing and rapid switching, respectively; supporting calculations are in /workspace/branches/9afb8076-b472-4f01-89b1-a1ea7d837b24/record2-check.md. The printed reciprocal root is exactly correct but can suffer subtraction cancellation near threshold when a_1>0; the expression above is preferable there in finite precision. This is a numerical-evaluation caveat, not a defect in the theorem. verify.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

The distinct contribution supported here is the exact fixed-rate-ratio threshold, uniqueness of the finite maximum, and its sharp escape coefficient for on/off propulsion coupled to equal opposite angular drifts. Neither a generic diffusion resonance nor computation by a first-harmonic resolvent is credited as new. Strong same-day indexed material uses a different rest drift and a different optimization domain; the formula and optimizer do not coincide even on a matched test ray.

## value

PASS

Optimizing speed of long-time spreading while the motile fraction remains fixed separates kinetic effects from a change in average motile occupancy. The exact transition between a finite optimum and a monotone large-rate approach, with a sharp inverse-distance divergence, answers a natural global question not contained in computing the diffusivity alone. It is a single-particle long-time result, not a theorem on finite-time search or interacting swimmers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
