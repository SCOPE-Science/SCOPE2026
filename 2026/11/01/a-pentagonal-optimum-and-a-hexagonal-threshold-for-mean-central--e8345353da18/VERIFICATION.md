---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For central-plane sections of right regular n-gonal prisms with circumradius1 and half-height h>0, the angular separation probability of an edge endpoint pair for Haar normals equals its endpoint angle/pi, since the two sign-disagreement sectors occupy 2theta of 2pi. Generic section vertices correspond bijectively to crossed prism edges, so linearity of expectation yields (2n/pi)[atan h+2asin(sin(pi/n)/sqrt(1+h²))]. The n vertical edges have angle 2atan h and 2n rim edges angle 2asin(sin(pi/n)/sqrt(1+h²)). Differentiation produces (2n)/(pi(1+h²))*[1-2s h/sqrt(h²+c²)], s=sin(pi/n), c=cos(pi/n); q(h)=h/sqrt(h²+c²) strictly increases to1. For n=5, 2s>1, so unique global maximum at h=(3+sqrt5)/4, E=5.246274819729384...; for every n>=6, 2s<=1 implies strict increase and no finite maximizer. Expanding atan and asin proves n=6 gap 3/(2pi h³)+O(h^-5) and n>=7 gap [2n/pi]*(1-2sin(pi/n))/h+O_n(h^-3). Independent direct-angle and derivative checks corroborate selected values but are not used for infinite quantifiers.

## originality

PASS

A best-of-knowledge distinct theorem about the expectation and sharp aspect-ratio regimes of Haar CENTRAL sections of regular n-gonal prisms. Previously published central rectangular-box hexagon probabilities cover n=4 and a different full distribution; previously published mean-square width for regular prisms concerns a different observable. A general edge-angle expectation identity is known/elementary and is not claimed as new. The specific five-versus-six sharp maximizer/threshold is not implied by inspected combinatorial slicing or width statements. A particularly relevant 2026 polytope slicing paper was inaccessible in complete full text: its abstract only cannot establish a whole-paper negative; institutional retrieval blocked by VPN, recorded as residual risk. Similarly two older stereology papers were abstract-only; inaccessible plausible sources alone do not force O failure.

## value

PASS

The expected combinatorial size of a uniformly oriented central section is a natural convex/stochastic-geometric observable, and the height-to-circumradius ratio is an intrinsic normalized parameter. The unique regular-pentagon finite optimum and the hexagon cancellation changing the asymptotic rate supply a sharp, interpretable and nontrivial phase transition across the entire natural n>=5 prism family. The angular identity is elementary, but the exact complete extremal classification is worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
