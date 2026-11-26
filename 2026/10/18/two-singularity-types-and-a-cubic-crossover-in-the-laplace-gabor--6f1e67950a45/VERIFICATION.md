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

For 0≤x≤1, the positive and negative halves of the Zak series sum to e^(−λx)/(1−e^(−λ)w^(−1)) + e^(−λ(1−x))w/(1−e^(−λ)w) for w=e^(2πiω). The frequency-step-1/2 frame operator sums the two squared Zak moduli at w and −w; combining the geometric factors yields 2(HP+4Q) with angular period 2π in 4πω. Uniform x gives two inverse branches of H, whose Jacobians sum to 1/(λ√(h²−h0²)); the energy change of variables contributes 1/(2P) and normalized angle contributes 1/(2π). Thus the stated density is a probability density, not an eigenvalue counting law. For u=cos θ the derivative numerator is affine in u and increasing in H. At H=h0 and u=−1 its controlling factor is 2(1−e^(−λ))²(e^(−2λ)+3e^(−λ)+1), and at u=1 the numerator is a sum of positive terms. This proves angular monotonicity, isolates the smooth saddle and seam corner, and gives a positive global minimum 2(sech λ−sech² λ). Substitution gives the stated energies and the Hessian entries Aλ, −Bλ. In the saddle normal form, rescaling and rotating the local coordinates gives product energy, Jacobian 1/√(AλBλ), and two hyperbola branches; with normalized angular measure this gives log coefficient 1/(π√(AλBλ)). At the seam, on each side the normal derivative is −4λ tanh λ, and the tangential quadratic term is (3/2)tanh²λ sech²λ. Inverting the normal map removes the angular interval of length 2√(δ/bλ) on the high-energy side; the two normal branches give the claimed symmetric density-difference coefficient. The regular parts are C¹ near the seam energy except at the collision, where the seam term is bounded and does not affect the leading logarithm. Setting c=cosh λ gives c³−2c²−c+1=0, with exactly one root above 1; substituting c=1+2cos(2π/7) follows from the seventh-root-of-unity identity. These are two singular mechanisms, not two distinct levels at the collision. CHECK.py and VERIFICATION.md were read, not executed; the checker compares finite direct Zak evaluations and numerical density asymptotics with programmed coefficients, not an independent symbolic derivation or a uniform crossover test.

## originality

PASS

Do not credit existence, extremal bounds, or an explicit Zak fiber as distinct here. The supported contribution is the normalized pushforward law with two interior singularity mechanisms, their constants and one exact exchange of energy ordering. The closest inspected indexed records have overlapping fibers and stronger asymmetric frame bounds, but their findings address extrema, not the spectral density or its crossover.

## value

PASS

A canonical spectral law for a classical frame model distinguishes an interior log divergence and a seam loss of angular measure. The difference between the two mechanisms, their exact constants and one crossing are information beyond sharp frame bounds, and the quadrature makes the law usable for other trace-per-cell observables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
