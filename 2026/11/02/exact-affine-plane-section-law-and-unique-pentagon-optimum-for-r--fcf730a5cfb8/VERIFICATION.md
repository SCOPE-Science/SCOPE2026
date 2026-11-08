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

Let the three equatorial vertices be a unit-circumradius equilateral triangle at heights ±h, h>0. For invariant unoriented affine-plane measure dσ(u)dt conditioned on hitting the prism, the angular normalizer is average width h+c, c=3sqrt(3)/4; counting intersections with the nine edges gives mean polygon vertex number 3(h+sqrt(3))/(h+c). Sorting triangle projections a1<a2<a3 and setting b=h|u_z|, the pentagon offset range equals [a3−a1−2b]_+−[a2−a1−2b]_+−[a3−a2−2b]_+. Spherical sector integration via ∫[k sinθ−2h cosθ]_+ sinθ dθ=(k/2) arctan(k/(2h)) yields p5(h)=3Ψ(h)/(π(h+c)), with Ψ as explicitly stated in RESULT.md. Only generic 3,4,5-gons occur; using mean and total probability gives p3=4+p5−mean, p4=mean−3−2p5. The proof of unique global maximum uses Q(t)=2F_t(π/6)−F_t(π/2), A(t),B(t) positive integrals, strict decrease of A/B by ordered logarithmic derivatives, and strict negative Q″ while Q′≥0, forcing H(h)=(h+c)Ψ′−Ψ to cross once. Independently matched direct angular integral to closed p5 at h=.1,.4095,.8,1,10 and bracketed h*=.409522670306... with max p5≈.11265019621. Correct h→0 and h→∞ expansions follow from those integrals. These numerical checks support but cannot replace the all-h sign argument.

## originality

PASS

PASS, qualified. Brandenburg/De Loera/Meroni study combinatorial slice chambers and optimal individual sections, not distribution under the invariant affine-plane measure; van der Jagt/Jongbloed/Vittorietti treat random section areas with correct conditional width weighting, not polygon vertex types for triangular prisms. The 1995 prism stereology study and 2024 random-section angle-density paper are highly relevant but complete math was inaccessible (Oxford authorization blocked by vpn_disconnected). They remain explicit historical-priority risks, not automatic O failure; no accessible text decisively establishes full coverage.

## value

PASS

The intrinsic invariant-affine-plane distribution is a canonical stereological model; polygonal section-type probabilities are natural observables of a prism. The exact all-aspect-ratio distribution and globally unique aspect-ratio optimizer differ from optimizing the size or shape of a single section. The regular-faced prism not optimizing p5 is a concrete geometric insight, and the formula is useful as a benchmark for stochastic-geometry reconstruction. This is a complete one-parameter family classification, not a trivial tiny numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
