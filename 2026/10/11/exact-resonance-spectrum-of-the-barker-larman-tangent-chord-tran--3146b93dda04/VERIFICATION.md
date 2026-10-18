---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For tangent line x=nθ+s tθ, the two section endpoints satisfy √(1+s²)−R−ε f(θ+atan s)=0, with simple roots s±(0)=±S, S=√(R²−1), and F_s=±S/R. Implicit differentiation gives s+'=R f(θ+β)/S and s-'=−R f(θ−β)/S, hence DT[f]=R/S [f(θ+β)+f(θ−β)] and Fourier multiplier 2R/S cos(kβ), β=acos(1/R). For β/π irrational no zeros; for reduced a/b, cos(πka/b)=0 iff 2ka=b(odd), possible exactly when b even, with k=(b/2)(odd). Zero k=0 remains nonresonant. Second-order implicit root expansion yields ε²[(f'_+f_+−f'_-f_-)/S²−(f_+²+f_-²)/(2S³)], and for resonant single fundamental cosine, derivative products cancel, f_+²+f_-²=2sin²(kθ), giving −ε² sin²(kθ)/S³. Independent direct floating root solutions at R=√2,k=2 and R=2/√3,k=3, θ=0.217/0.4 showed symmetric second differences converge to −0.17682304 and −4.51388128 respectively, matching analytic predictions; numerical regressions not the all-radius proof. C² radial perturbations retain positive curvature since curvature numerator starts R²>0 and contain the inner unit disk for small ε; 'smooth' in the text should be interpreted as at least C², not arbitrary C∞ regularity. Local differential kernel does not establish nonlinear inversion or all nonlinear resonant combinations.

## originality

PASS

Barker--Larman 2001 poses tangent-hyperplane section determination and partial results; its complete article remained unavailable, and an authorized Oxford attempt with the DOI returned a WRONG ARTICLE (D.G. Rogers on Helge Tverberg, same journal volume pp.1–6, instead of Barker--Larman pp.79–96). This mismatch is treated as no full-text inspection, not noncoverage. Makai--Martini 2016 full arXiv source addresses local determination in near-inner-body asymptotics, explicitly notes planar differentiating difficulties, and does not state the fixed-positive-gap concentric-disk Fourier diagonalization in its relevant analysis. Matthews 2026 polygon reconstruction is restricted to polygons, not a smooth perturbative spectrum. The four exact arithmetic resonance classes, including quadratic visibility, were not located as implications of these materially reviewed statements. Residual risk due to inaccessible 2001 original is expressly retained.

## value

PASS

The motivating Barker--Larman reconstruction problem asks whether tangent-chord data determine an unknown outer convex body. A complete Fourier multiplier of the local data map and an exact classification of all exceptional gap radii are natural spectral obstructions/diagnostics, and showing that a fundamental kernel harmonic becomes visible at quadratic order precisely distinguishes first-order noninjectivity from nonlinear invisibility. The work is a relevant structural result even without settling global uniqueness or providing ill-conditioned irrational inverse estimates; a mere numerical first resonance would not be comparably useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
