---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The sum-zero edge-difference torus is the full relative-phase quotient, with two tangent directions. In the chart (a,b,−a−b), F_h(z)−Pz=(2π,0,−2π) is exactly the two residual equations and the preserved sum. At h=57/50 I independently certified the stated box with exact rational arithmetic: a separate preconditioner is the exact inverse of a rational Taylor midpoint Jacobian, Machin's formula bounds π, and Taylor remainders bound the trigonometric errors. The derivative drift has row-sum bound 7hr since component cosine displacements are at most r,r,2r. Defect <10⁻⁹ and contraction factor <10⁻⁵ give strict inclusion in the radius-10⁻⁸ box and a genuine zero by Banach's theorem. Independent uniform entry bounds for the co-rotating derivative give −1.56<tr<−1.55 and 0.70<det<0.71 across the box, so all three strict quadratic Schur inequalities hold. Permutation equivariance gives F_h³=(P⁻¹F_h)³; its derivative at the orbit point is B³, which contracts in both eigenvalue directions. Distinct representatives in (−π,π) ensure prime period three. Each point of the orbit has two positive coordinates and one negative in this representative interval, while each reflected point has one positive and two negative; oddness gives a disjoint sink orbit. The two uniform twists have tangent multipliers −71/100. The implicit-function theorem (I−B invertible) and strict stability give persistence near h=57/50; the travelling sinks have open positive-measure basins, excluding almost-global attraction by the twists there.

## originality

PASS

Bounded pass for the specific two twisted sinks and two hyperbolic travelling prime-three orbits coexisting at h=57/50, and the resulting obstruction beyond the descent range. The same Huygens map and the twists are known, and older identical-frequency Kuramoto equations give exactly this map after the signed change K=−3h. The directly inspected older three-oscillator analysis studies the opposite sign in its equal-frequency phase portrait and does not certify the prime-three coexistence here. The inaccessible 2025 article remains a material priority risk; no noncoverage inference is drawn from its abstract or from failed retrieval.

## value

PASS

This supplies a rigorous motivated witness in the gap between the triangle's global descent range and the twists' local stability range. An explicit hyperbolic travelling sink, in fact two, gives positive-measure alternative basins that persist, directly distinguishing local twist stability from almost-global twist attraction. The rational parameter is useful as a reproducible witness rather than a claim that this exact parameter is a bifurcation threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
