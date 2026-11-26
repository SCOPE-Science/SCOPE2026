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

On both arcs h± conjugates the base to translation, and the skew term goes to zero at the fixed endpoints. Interpolating the translation and the vertical term gives an isotopy by homeomorphisms. Each point of an open arc has a neighborhood inside a translation strip of width <1, hence is wandering; both endpoint fibers are fixed. The lift of the base fixes the endpoints of each interval, giving bounded horizontal displacement. In the other coordinate, sin(2π(s+j)) is constant along the orbit and the sum of the amplitudes is uniformly Oβ(n^(1−β)), by ordering the negative tail by increasing distance from the cutoff. This proves uniform convergence of the normalized lift displacement to zero. For entropy, the same sum estimate and summability of the tail derivative bound the Lipschitz constants of ALL partial Birkhoff sums by Oβ(n^(1−β)) on each unit strip, including across the continuous piecewise-smooth cutoff. A mesh at that inverse scale suffices for each of O(n) central strips. On the far negative tail the base trajectories all stay near r for large n. At fixed fractional mesh coordinate u, all amplitude differences between two strips have the same sign at every time (and the sine factor is fixed), so the largest partial-sum difference is the endpoint difference. Binning those endpoint values gives O(n^(1−β)) additional choices per u and hence O(n^(2−2β)) there; changing u to its mesh point uses the uniform Lipschitz bound. The positive tail and fixed circles cost O(1), and the zero-cocycle second arc costs O(n). The spanning bound O(n^(2−β)) also proves zero topological entropy. For the lower bound, Ω(n) separated transit times j in [n/3,2n/3] are detected at time j by the base coordinate; h+(u) for u∈[0,1/8] stays uniformly away from either endpoint. Within each transit strip, until k=floor(j/2) all amplitudes are on the increasing negative tail and of order n^(−β). Differentiation over u∈[0,1/8] gives ∂u B_k≥cβ n^(1−β). Thus a mesh of spacing K n^(β−1) produces endpoint lift differences >4ε. Differences increase in time and the one-step increments are <ε for large n, so a first crossing of ε gives a difference in (ε,2ε], genuine circle separation before k<n. These two separations give Ω(n^(2−β)) at fixed small ε and the required exponent. The argument is for each real 0<β<1, not merely sampled parameters. The frozen script was inspected only; no numerical simulation is needed for the proof.

## originality

PASS

The supported distinct result is the whole open interval (1,2) among zero-topological-entropy, identity-isotopic T² homeomorphisms with singleton rotation set, here even zero for the specified lift. The closest actual passages do not cover these simultaneous conditions. The comparison is not a claim that noninteger polynomial entropy, torus skew products, or singleton rotation sets in isolation are new.

## value

PASS

The result supplies an explicit continuum of intermediate growth exponents in the exact realization class posed in Corrêa's Problem 1. It separates sublinear unwrapped drift (hence zero rotation) from growth of distinguishable orbit segments and shows why a slowly decaying resonant term amplifies transit-strip complexity without giving positive topological entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
