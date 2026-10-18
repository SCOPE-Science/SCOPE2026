---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed from actual RESULT.md: stable-set polytope is coordinatewise downward-closed by thinning random independent sets. With q=(1+r)c, containment −(P−c)⊂r(P−c) means q−x∈rP for all x∈P; x=0 and x=e_i force q∈rP and q_i≥1, and downward closure proves converse. Fractional coloring gives minimum r=χ_f and q=1 feasible. Compact dual D=nonnegative weights with independent-set sums ≤1; antiblocker representation λP={z≥0:y·z≤λ ∀y∈D}. At optimum y, y·q≤λ=∑y with q≥1 forces pinned q_i=1 on optimal support. For vertices outside T, every dual vertex with y_i>0 has strict objective gap; finitely many vertices allow a small positive box in those directions, giving affine dimension n−|T|. Perfect-graph specialization uses clique polytope description; automorphism averaging gives transitive uniqueness. Independent LP finite cases and provided exact-rational verifier support examples only.

## originality

PASS

The direct relation s(STAB(G))=χ_f(G) and dimension of its entire center space is a meaningful synthesis of known antiblocking and fractional-coloring facts. Resultary search finds parallel polymatroid/poset center descriptions but no universal simple graph stable-set result dominating this. Rezaei convex corner/entropy references could already encode the optimal-support formula; full primary chapter could not be read, so O PASS is qualified and not an absolute uniqueness claim.

## value

PASS

This converts fractional coloring into a full affine-geometric asymmetry invariant across all finite graphs, including noninteger values, and classifies the entire center locus. The pinned/free coordinate interpretation and perfect/transitive specializations form a natural structural classification rather than a single tabulated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
