---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For uniform n-point samples in triangles with AB=1, AC=1-δ/√n, apex angle γ in (0,π/3), the base is strictly shorter in the limit; all pairs with O(n^-1/2) diameter deficit localize at AB or AC. Rescaled corner point clouds are independent Poisson processes at disjoint vertices; at A one Poisson process of intensity 2 in ray coordinates (r,q) simultaneously minimizes r+cq and cr+q, c=cos γ. The two independent endpoint noises have survival exp(-λu²), λ=1/(1-c), while apex joint survival is exp[-Q_c(s,t)] with three quadratic branches s²/c if t≤cs, t²/c if s≤ct, and [(s²+t²)/c-2st]/(1-c²) otherwise. Linearization O(1/n), tightness and continuous mapping yield the min{A_B+U_B,δ+A_C+U_C} limit. Conditioning and integrating yields the displayed four-term exact limiting survival, strict positive dependence at δ=0, and exact one-side crossover for δ≥z. Independently clipped the two rational Poisson threshold triangles for 675 distinct (c,s,t) combinations; union areas equal Q_c/2 exactly, confirming branch normalization but not substituting for the Poisson weak-convergence proof.

## originality

PASS

Wei Lao (2010) Theorem 6.8 covers interior-uniform points of even regular polygons with disjoint antipodal diameter endpoint neighborhoods and independent Weibull contributions. Its odd-polygon overlapping endpoint analysis addresses boundary/edge samples, not area-uniform points of triangles. Schrempp (2015) restricts to a unique major axis and locally curved boundary, while the submitted family has two tied or near-tied major axes meeting at an apex and corners. Appel–Najim–Russo (2002) plausible primary remained inaccessible: arXiv and lawful OA did not yield its complete text, and authorized Oxford retrieval reported disconnected VPN; only abstract/later descriptions were read. This access risk alone does not contradict the distinct two-axis geometry. Best-of-knowledge PASS, not priority guarantee.

## value

PASS

A shared apex couples two apparently competing Weibull extreme distances; the joint void exponent and strict dependent limit identify a natural geometrically forced failure of independence. The critical side-length split δ/√n is the unique scale comparable to extreme deficits and yields a complete crossover distribution. This addresses a real stochastic-geometric boundary between single- and multiple-diameter endpoint laws rather than a routine one-axis substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
