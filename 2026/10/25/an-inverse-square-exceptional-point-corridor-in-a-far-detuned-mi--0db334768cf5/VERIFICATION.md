---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

With x=E+iΓ and γ=(ΓL−ΓR)/2>0, checked the stated 4×4 BdG determinant and exact imaginary-axis polynomial. The substitution s=R^-2, εL=sℓ, y=−γ+sz gives exactly F=z²−8γt²z+ℓ²+4s(γ²ℓ²+(γ²+t²)z²)−4γs²(ℓ²z+z³)+s³(ℓ²z²+z⁴). At s=0 its two low roots are real iff |ℓ|≤4γt². The Jacobian of (F,F_z) in (z,ℓ) at the positive fold is nonzero; IFT gives the real analytic fold and ℓ_*'(0)=−8γt²(2γ²+t²), hence w(R)=4γt²/R²−8γt²(2γ²+t²)/R⁴+O(R^-6). The remaining roots have real parts of order R. The low-rank Schur complement has nonzero offdiagonal and determinant zero, giving geometric multiplicity one at the double-root EP. Fixed t,γ>0 and bounded |R²εL| only, not a global phase diagram. Independent symbolic scaled-F check and source script inspection corroborate the exact setup.

## originality

PASS

The earlier Cayao–Aguado non-Hermitian two-dot Hamiltonian and exceptional-point bands are explicitly credited, but their examined unequal-onsite phase figures and equal-onsite calculations do not derive the uniform R^-2 corridor boundary, next R^-4 coefficient and two/zero-root bifurcation theorem. This is a sharpened quantitative claim, not new model ownership. Later Cayao–Sato treats a Josephson-connected pair of chains, not the single two-dot asymptotic. Search of published Resultary titles yielded no implication-equivalent report.

## value

PASS

The far-detuned quantitative onset and next correction of real-zero energy spectral pinning are a natural, motivated EP boundary in a canonical lossy two-dot model, resolving more than a numerical phase plot. The explicit fold and defectiveness thresholds are useful for asymptotic spectral analyses without claiming conductance observables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
