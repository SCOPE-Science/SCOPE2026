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

Fix d≥2, and split the quotient directions into span(1) and its perpendicular; the coupling eigenvalues are d+1 and 1. On the diagonal α=(d+1)h, and each x_σ solves α sin x_σ=π, giving the two distinct antipodal prime-two orbits. At the representative x_σ set t=α cos x_σ. The recentered two-step return has derivative 1−t²=−1−ε and chain-rule second and third derivatives π(3t+t²) and 4t²+3t³+t⁴−3π²(1+t). Thus as t²=2 the flip coefficient g''²/4+g'''/6 is (2+t)(5π²+2)/2>0. Dividing the two-step return's second iterate minus the identity by the offset y gives a smooth function with strict local concavity, maximum 2ε+O(ε²) at y=O(ε), and negative values at fixed close endpoints. There are exactly two nonparent roots for ε>0 and none for ε<0; the return exchanges them because its only nearby fixed point is the parent. They have offsets ±sqrt(ε/B_σ)+O(ε); differentiating yields longitudinal four-step multiplier 1−4ε+O(ε^(3/2)). The leading ratio sqrt(B_−/B_+)=sqrt(2)−1, and oddness exchanges the two cycles (mapping a representative neighborhood to the other cycle's antipodal neighborhood). At the parent the transverse four-step derivative is q_d I with q_d=(1−2/(d+1)²)²∈(0,1). The projected four-step fixed-point equation has invertible perpendicular derivative (q_d−1)I, so its unique local transverse solution is the invariant diagonal. This excludes all nondiagonal local daughters on both sides. All transverse multipliers along each daughter equal q_d+O_d(sqrt(ε)), proving attraction in the full quotient for each fixed d. Neither global attraction nor stability in an unquotiented common-rotation direction is asserted. Independent finite brackets for ε=10⁻⁴ and 4·10⁻⁴ supported the offsets and multipliers; the uploaded code was read, not run, and the existence, count and stability follow from the local analysis rather than the brackets.

## originality

PASS

The parent cycles and their −1 crossing are acknowledged antecedents. The supported distinct result is the simultaneous supercritical pair of prime-four births with explicit branch coefficients and locally exhaustive stability in the entire star quotient for every fixed d. No inspected match provides this theorem or directly implies its signed coefficients and transverse conclusion. Exact scalar-slice and parent-record access limitations are retained below.

## value

PASS

The result resolves what becomes of both antipodal two-cycles once they lose longitudinal stability, including whether transverse perturbations preserve the attraction and whether other nearby daughters can exist. The simultaneous locally exhaustive result distinguishes a visible diagonal four-cycle from a true sink of the star quotient and supplies exact measurable branch splitting. It is not just a generic period-doubling assertion or rediscovery of the parent threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
