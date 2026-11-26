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

An MMD pair can only be strongly resolved by an endpoint. Conversely, a geodesic through a given pair can be extended at its ends until both endpoints are MMD, and either selected endpoint then strongly resolves the original pair. In the Cartesian product maximality separates by coordinate, so the MMD graph is the direct product of K_q with the antipodal matching or the odd step cycle. The even components are crowns. Their independent sets lie on one side (empty counted once) or are one of the q cross-matched pairs, giving 2(1+t)^q−1+qt² per component. For odd n, adjacent occupied layers must be identical singletons. Aggregating all size-at-least-two layer states by their common neighbors and weight h_q leaves a weighted transfer matrix on empty, q singleton colors and heavy. On the uniform singleton coordinates it restricts to B_q; on the q−1 color differences it acts as t, giving the trace term and its correction. Complementation produces the asserted cover polynomials. In the odd cycles with an empty layer, a singleton run of length ℓ≥2 is improved by full alternating layers, since q⌈ℓ/2⌉>ℓ; isolated full layers yield q⌊n/2⌋, while no empty layer gives n. The only tie is q=n=3. For even n one vertex per component forces its chosen side. In odd n≥5 one vertex cannot force by rotation, and choosing both layers of the unique adjacent pair in the minimum cover forces it: after deleting that pair the remaining odd path has a unique independent set of maximum size. For n=3, q>3, two retained layers distinguish the basis. In K₃□C₃ the distance-2 pairs are precisely those differing in both coordinates; any two vertices fit both some two-layer and some two-color basis. Three vertices in two retained layers using all colors force that two-layer basis, with the dual construction for a two-color basis. This direct boundary check confirms six bases of size six and forcing number three.

## originality

PASS

The standard MMD/vertex-cover equivalence, product reduction and the scalar strong metric dimension are already established and are credited, not passed as novel. The distinct supported claim is the evaluated all-set polynomial and the associated exhaustive basis and forcing classification. The inspected comparisons do not state that result or mechanically imply it from exact enumerator or basis data for the same product.

## value

PASS

Clique–cycle products are natural finite metric graphs. The full cardinality distribution gives information the known optimum and minimal-solution algorithms do not. The parity-dependent component/trace evaluation exposes the role of singleton colors and the exceptional tie at the smallest product; the basis census and exact witness sizes determine when a basis can be specified from a small subset. This is a useful exact invariant and classified boundary, not merely a recalculation of strong metric dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
