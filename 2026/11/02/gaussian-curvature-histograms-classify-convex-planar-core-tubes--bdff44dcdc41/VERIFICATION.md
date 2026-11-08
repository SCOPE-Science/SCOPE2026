---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Independently rederived planar-core tube parametrization X(s,θ)=γ(s)+r(cosθ n(s)+sinθ e3), Jacobian r(1−rκ(s)cosθ) and K=−κ(s)cosθ/[r(1−rκ(s)cosθ)]. Positive κ and 0<r<reach ensure smooth embedding and monotone K↔u=κ cosθ. The essential support endpoints give 1/K_++1/K_-=2r², recovering r, then κmax. Reweighting µ by (1−r² K) removes area bias; even moments of κ through ∫ k^(2j)/(1−r² k)^(2j−1) dµ determine ν via compact Hausdorff moment determinacy of κ², with L=2π/Eν κ. Area 2πrL, enclosed volume πr²L follow tubular integration. Conversely (r,ν) determines µ. Support functions h_m=R+R ε cos(mφ)/(1−m²), m≥2, yield radii of curvature R(1+ε cos mφ)>0, period-substitution equal normalized curvature histograms, and distinct rotational symmetry orders (noncongruence). Common sufficiently small r exists for the family with fixed R,ε since curvature radii uniformly ≥R(1−ε). Independently computed a 240×240 angular quadrature for m=2,3,4,5 (230400 sample pairs), matching reversed radius r²=.0144, second curvature moment 0.11417199038, and identical K² area moments to 1e−12. Numerical checks are supplementary to exact moment proof.

## originality

PASS

Qualified PASS. Earlier work of Tunçer–Yoon–Karacan (2011) fully inspected in accessible Wiley HTML §§3–4, theorems 3.2–3.5, and Saad et al. (2024) OA abstract/topical summary establish local tube curvature/Weingarten and focal properties, not area-pushforward inverse probability classification. The new statement is identifiable r and arclength κ-histogram from scalar unlabeled Gaussian-K law, plus exact nonidentifiability of shape through harmonic support examples. Published Resultary findings address convex curve curvature sampling/Hessian but no comparable histogram inverse. The forward formula and total tube area/volume are classical, explicitly not claimed novel. Related geometric probability transforms might contain same theorem under other terminology.

## value

PASS

A complete inverse-data identifiability result: determine exactly which physical tube radius, curve length, and core-curvature distribution are recoverable from an unlabeled intrinsic scalar law, and prove strong nonrigidity by infinitely many noncongruent cores. The histogram is natural and geometrically observable, rather than an arbitrary computed moment. This explicitly separates reconstructible geometric parameters from unavailable shape information, without falsely claiming finite-sample stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
