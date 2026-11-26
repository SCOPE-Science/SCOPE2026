---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The regular isotropic-coordinate extension of the subextremal Kerr t=0 slice is complete, vacuum and two-ended; its stationary axial shift has zero spatial divergence, hence tr K=0. The outer horizon sphere is a MOTS with A=4πS₂, S₂=2Mr₊, and J=aM. BCK eq. (22) is the exact outward-unit-normal stability operator at this spin. Its strictly positive simple principal eigenfunction, normalized by its integral, is fixed by rotations. The axisymmetric reduction therefore gives the full principal eigenvalue. The Legendre form comparison for the reduction gives λ₂≥2/S₂+min V; the smooth trial u=89+33z² belongs to the spherical operator domain. An independent integer-interval replay evaluated the exact BCK potential and checked monotonicity, enclosed the Rayleigh quotient by panel integration, and bounded the Temple variance using a fixed center (the variance at the true Rayleigh quotient can only be smaller). With outward integer rounding it proved λ₁>0.0826332 and λ₁A>2.3696992, while 8δ<1.220747, as well as the frozen area and deficit intervals. This verifies the stated counterexample, its quantitative headline bounds and stability without relying on the missing source script. The frozen Temple chain rounded the variance and then rounded the lower bound in the unsafe direction by about 8×10⁻⁸; the asserted result is nevertheless independently certified using tighter bounds. An analytic sign and margin check is also available: substituting f=√R into the exact operator gives Hf/f=c₀+c₁/R. For subextremal Kerr c₁≥0 and the minimum is c₀+c₁/S₂=(r₊²−a²)/S₂². Integrating Hf against the positive ground state gives λ₁A≥4π(r₊−M)/M, already larger than 8δ at this spin, though weaker than the headline numerical bound.

## originality

PASS

The available sources establish the exact Kerr operator, qualitative horizon stability/rigidity, or slow-spin eigenvalue perturbations. None of the checked distinct sources gives the quantitative violation in the deficit window; in particular neither sign stability nor substitution into a published eigenvalue formula supplies it. One must derive a quantitative comparison, such as the record's Temple argument, from the old operator. This is a best-of-knowledge pass for the counterexample, not a novelty claim for Kerr's operator, Temple's inequality, or broader near-extremal asymptotics.

## value

PASS

The claim separates qualitative extremal rigidity from a particular quantitative spectral estimate in the exact Kerr family, where the relevant deficit, spin and stability normalization are fixed by geometry. A strict, well-separated counterexample to the stated coefficient in its admitted window is useful even at one point: it prevents using that coefficient in any general estimate of this form. The gap is not a rounding or convention artifact. This is not evidence against every linear vanishing law or for a particular exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
