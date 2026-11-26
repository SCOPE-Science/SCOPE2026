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

Reassessed the complete corrected RESULT.md under repairs/2. The original circle theorem passes, but the original extension to arbitrary reset-free motions listed only transform/support and absorption conditions and omitted excursion renewal, which the asserted general formulas require. For a counterexample to the unrestricted extension, start uniformly at site h∈{0,1}, retain h as a hidden mode, and use hit hazard κ_h>0 when the current site equals h and zero otherwise, with κ_0≠κ_1. In the reset-free model from h this gives nonconstant φ_λ(h)=κ_h/(κ_h+λ). Persistent resets keep the hit hazard κ_h. Fresh uniform positional resets flip between matching and nonmatching sites at rate a=r/2, holding h fixed. Their conditional hit transform is κ_h(s+a)/[(s+κ_h)(s+a)+as], strictly less than the persistent κ_h/(s+κ_h) for s,r>0. Both hit almost surely. The repaired extension requires independent excursions with reset-free law conditional on each restart site, eliminating this counterexample. The discounted first-hit and first-reset terms are respectively u=φ_(s+r) and r(1−u)/(s+r); conditional renewal and independent site renewal put the site average on opposite sides of g(u)=(s+r)u/(s+ru). Strict concavity proves the repaired comparison precisely at nonconstant u. Circle Brownian motion renews, and folding gives the absorbing/reflecting problem with uniform distance and φ=cosh(k(ℓ−x))/cosh(kℓ). Integrating φ and its reciprocal separately yields the stated means. Positive partial fractions show strict decrease from T_0 to an unattained zero infimum in A. For Q the derivative of cosh(z)∫sech−z−z³/3 is strictly positive by Cauchy–Schwarz and the difference vanishes at zero, proving the unique zero-rate optimum without asserting positive-rate monotonicity. Independent replay `python3 /workspace/review-evidence/reproduce.py 2` confirms both low-rate expansions in exact arithmetic, and corroborates the means and transform ordering by Simpson quadrature at eight ring rates and forty (s,r) comparisons. The high-rate terms follow analytically from the limits of coth, arctan(sinh), and cosh. The proof, not the quadrature, covers all parameters.

## originality

PASS

Reassessed on the narrower, renewal-only claim. The exact circle renewal ingredients are already available for fresh iid draws and for an individually fixed site; substituting the geometry and integrating does not itself constitute novelty. The supported distinction is the matched uniform ensemble's opposite global optima relative to the same unreset mean, with strict same-geometry all-rate inequalities and a comparison of transforms across those two protocols. The checked earlier statements do not give that combination or directly imply the persistent strict sign against the unreset baseline. The Jensen step and the renewal assumption are elementary, not independent novelty claims.

## value

PASS

The repaired claim retains the central quantitative contrast. The two protocols have identical marginal target-distance sampling, yet remembering just one latent anchor flips the global role of resets: one policy improves over unreset at every positive rate, while the other worsens at every such rate despite zero first derivative at the baseline. The high-rate ratio grows exponentially, and the renewed transform comparison describes more than a mean. The omitted nonrenewal extension is unnecessary to the mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
