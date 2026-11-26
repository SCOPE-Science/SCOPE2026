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

The equilibrium and characteristic polynomial give a transverse crossing with real-part derivative 1/(2b) and a stable third direction for each fixed b>0. With q=(1,i,0) and p=q/2, the critical quadratic interaction B(q,q̄) is zero; h20 has third component −10i/(b+2i). The projected interaction gives G21=5i/(b+2i), so the stated normalization gives a positive l1=5/(b²+4). The real cubic coefficient of the complex amplitude equation is Re(G21)/2. Thus the squared leading complex radius is −α(b²+4)/(10b); x has leading oscillation 2r. The linear imaginary eigenvalue has zero α derivative; Im(G21)/2 times the squared radius gives the frequency shift −α/4 in physical (not rescaled) time. The radial Floquet exponent is −α/b+o(|α|); the other tends to −b. To justify the period remainder, the shooting equations with initial (x,y,z)=(ρ,0,α/b+ζ) may be written analytically after dividing x and y by signed ρ, since their subsystem is homogeneous in (x,y). At ρ=0, α=ζ=0, T=2π, the derivative of the x/ρ return residual in α is π/b, its T derivative is zero, the y/ρ residual has T derivative −1, and the z residual has ζ derivative exp(−2πb)−1 and zero α and T derivatives. Analytic implicit reduction gives a signed branch. In a signed parameter ε with α=−ε², the two signs are opposite extrema of the same locally unique orbit, so the period is even and analytic in ε; 1/Ω therefore has the claimed O_b(α²) remainder. The conclusion is local with no uniform claim at b=0 or at unbounded b.

## originality

PASS

The original chameleon-system paper covers this exact field at b=1, including the direction and instability of the cycle and quantitative focus data. Credit those precedents, not just a qualitative result. The specified all-b coefficient, physical amplitude and damping-independent derivative are distinct results in the examined evidence; they are not obtained by rescaling the b=1 bifurcation statement or instantiating its raw focus number.

## value

PASS

This adds a usable local benchmark for a previously studied flow. The derivative is measured in the original time variable and is invariant across all fixed positive dampings even while the physical amplitude and real Hopf coefficient change. This parameter cancellation and the precise small saddle-cycle expansion provide more information than the familiar qualitative Hopf classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
