---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed the stipulated signed-burning update semantics (spread before one manually ignited vertex, no recolouring), a,b>=3, one negative edge u0v0. First ignition spreads to the whole opposite part in the second spreading phase; at most one further opposite-colour ignition is made and by the third spread every remaining vertex has strict majority because each part size >=3. This directly yields green codewords empty, all, each singleton and complement, each of n-2 edges incident to exactly one endpoint of the frustrated edge and complement: size 4n-2 and claimed six-term weight enumerator. Switching is a pointwise sign conjugation of influences, so every signed plurality is n minus Hamming distance to the code. The auxiliary eligible-pair graph is two disjoint stars; its balanced-cut colour-class sizes are 2,a,b,n-2, giving radius floor(n/2)-1 odd or balanced, n/2-2 even unbalanced, with only A/B deepest balanced words. An independently written brute signed-dynamics BFS for (3,3),(3,4),(3,5),(4,4),(4,5),(5,5) reproduced full green codes and covering radii; these are bounded checks, whereas the three-round argument and two-star analysis prove all a,b>=3. K2,3 excluded and known to violate code claim.

## originality

PASS

Best-of-knowledge originality of the precise final claim, with prior partial/general coverage credited. The primary signed-burning paper already establishes switching-conjugacy of reachable terminal colours and their coding covering-radius interpretation for ALL signed graphs. Those are credited general tools; its exact worked graph-family results concern paths, not the complete bipartite with one frustrated edge. General radius definition alone cannot deduce the biclique’s 4n-2 code, every-switching formula, or the part-balance phase transition. Search failure alone is not proof of novelty, and explicit residual risks remain.

## value

PASS

Exact code plus every-switching plurality supplies a full dynamical classification of a natural one-frustrated biclique family, not an arbitrary tiny graph calculation. Balanced K4,4 versus K3,5 share n and weight enumerator but have covering radii 3 versus 2: this identifies a genuine structural quantity undetected by weight distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
