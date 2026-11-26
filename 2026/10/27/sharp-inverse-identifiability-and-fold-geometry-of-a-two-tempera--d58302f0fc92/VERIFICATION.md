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

Independently set B=D−KΣ. The Lyapunov equation makes B skew; symmetry of Σ=K⁻¹(D−B) gives KB+BK=DK−KD. For 2×2 symmetric K the left side is LB, so B₁₂=c(T₁−T₂)/L. The potential torque is (KΣ)₂₁−(KΣ)₁₂=2B₁₂, with the stated sign. Taking the determinant of KΣ=D−B gives detΣ=(T₁T₂+B₁₂²)/detK. The angular integrand after removing the density is −B₁₂ times (xᵀΣ⁻¹x)/|x|², bounded in direction; its radial Gaussian integral contributes 1/√detΣ after angle averaging. Thus the current rate has the opposite sign to torque and its magnitude determines detK at nonzero torque. At fixed L, real positive diagonal roots with product detK+c² are equivalent to 0<detK≤L²/4−c², giving exactly the stated region and fibres, with |m|=|Δ| and nonzero m with ω=0 excluded. The branch gap squared equals a positive multiple of (Wmax−|ω|)(Wmax+|ω|), with nonzero second factor on each nonzero-torque fold, yielding local half-Hölder inverse branches but not a larger exponent. At m=0 one must have c=0 and ω=0, leaving the whole open diagonal segment. The diagonal entries of K⁻¹(D−B) give V=(bT₁−aT₂−2cB₁₂)/detK, which recovers the signed diagonal difference and splits the two branches. On the diagonal segment V=T₁/a−T₂/(L−a) decreases strictly from +∞ to −∞. No statistical inference or sample-path angular derivative is used.

## originality

PASS

The primary literature gives the forward torque and the same ensemble-current angular rate; much of the inverse algebra is directly accessible from those identities and is not a separate discovery of a new forward law. The distinct contribution supported here is the complete constrained inverse problem: exact feasible boundary and global fibre classification, local fold conditioning, and a specified single additional stationary statistic that works even on the zero-torque continuum. No inspected source states a covering inverse or stronger identifiability theorem for these data under the stated trace constraint. The result is an explicit synthesis with modest algebraic novelty; historical priority remains qualified.

## value

PASS

The constrained inverse resolves what can and cannot be identified from two natural stationary observables rather than taking an arbitrary algebraic slice to display a formula. It gives an explicit diagnostic for infeasible noiseless data, demonstrates genuine nonidentifiability and degraded conditioning where branches coalesce, and answers which one additional low-dimensional stationary measurement makes the inverse globally unique. This is meaningful even though the computation uses elementary matrix algebra and does not quantify errors from finite trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
