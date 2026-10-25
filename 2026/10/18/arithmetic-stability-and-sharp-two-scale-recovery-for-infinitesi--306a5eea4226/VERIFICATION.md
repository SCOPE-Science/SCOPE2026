---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For disk radial perturbation, the two chord endpoints at polar angles θ±α remain transverse since sinα>0; implicit differentiation of the line intersection gives D_α f=(f(θ+α)+f(θ-α))/sinα. Thus λ_m=2cos(mα)/sinα, and combined data have squared Fourier multiplier W_m=Σ_j4cos²(mα_j)/sin²α_j. The closure H of the integer orbit of a=(α_j/π) in T^k contains b=(1/2,...,1/2) iff every annihilating integer character h·a in Z has h·b in Z; so the infimum W_m>0 iff some integer relation has odd sum. Rational common zeros satisfy m=(q_j/2)(odd) for each even denominator; intersection exists iff all v_2(q_j) agree, and exact indices are odd multiples of lcm(q_j/2). For two offsets α and 2α with 0<α<π/4, substitute z=cos²(mα) to get W=1+csc²α+(2z-sin²α)^2/(sin²α cos²α), giving uniform lower bound and exact irrational sharpness by dense rotation; convexity in z makes upper coefficient attained at m=0. Check rational (π/6,π/4) table gives min4 and max24. Finite examples supplement analytic character theorem and the square identity.

## originality

PASS

PASS only for the multi-offset stability classification and sharp universal two-scale recovery. A published Resultary theorem on the Barker–Larman tangent-chord transform already gives, after rescaling outer disk radius R to 1 and tangent distance 1 to t=1/R, precisely the present single-offset derivative multiplier 2cos(mα)/sinα and the even-denominator kernel classification. Those subclaims are NOT new. The prior source does not give the torus odd-relation criterion for arbitrary finite offset collections or the sharp α,2α uniform frame bounds; those are the surviving substantive contribution.

## value

PASS

The complete finite-offset stability classification and explicit universally stable *two*-measurement design (with a sharp irrational lower bound) solve a motivated inverse problem: injectivity of each single chord view can fail or be ill-conditioned, whereas paired views can be uniformly reconstructive. The multi-offset frame bound is a meaningful new design principle even though the single-offset Fourier multiplier is already published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
