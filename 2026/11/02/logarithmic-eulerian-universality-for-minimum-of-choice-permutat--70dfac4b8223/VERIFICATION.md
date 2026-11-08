---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Fresh k-with-replacement picks from each remaining ordered set yield independent rank coordinates J_m with survival ((m−j)/m)^k. An adjacent descent occurs exactly for J_(m−1)<J_m. This gives the exact p_(m,k) formula and 1-dependence. The power-increment identity 2Σr^k Δr=m^(2k)−ΣΔr² and strict increase of Δr for k≥2 prove p_(m,k)<1/2, while k=1 gives equality. Fixed-k power sums yield p_m=1/2−[k(k−1)/(2(2k−1))]/m+O_k(m⁻²), hence logarithmic mean deficit. Coupling J_m=ceil(mY_m) with i.i.d. minimum-of-k uniforms yields at most 4k/(m−1) expected descent-indicator mismatches and W1 ≤4kH_(n−1); the mean gap gives matching Ω(logn). Adjacent covariance controls variance n/12+O_k(logn), and coupling plus the classical Eulerian 1-dependent CLT gives normality. Independent exact rational weighted permutation enumeration checked 20 pairs n=2..6,k=1..4; infinite limiting statements rely on proof.

## originality

PASS

Travers already derives the independent nonuniform relative ranks in the exact k-card-minimum model, and this antecedent is credited. Global permuton laws/long patterns, s-Eulerian sequence results, uniform/Mallows one-dependent descent theorems and determinantal processes do not state the current local n-dependent bias coefficient, sharp logarithmic Wasserstein order and CLT for these stage-dependent coordinates in inspected statements. Equivalent latent rank-statistics formulas remain a priority risk.

## value

PASS

Establishes a sharp local-vs-global behavior contrast: a strongly biased removal order has Eulerian Gaussian fluctuation and variance at leading order yet a model-specific logarithmic bias. A quantitative sharp-order Wasserstein coupling is useful for distributional approximation beyond a routine relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
