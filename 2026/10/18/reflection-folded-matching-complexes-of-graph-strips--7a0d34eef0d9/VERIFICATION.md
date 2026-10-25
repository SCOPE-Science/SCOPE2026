---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

A fixed point of a finite simplicial involution has a stable support and orbit-constant barycentric coordinates, giving exactly the simplicial orbit complex of qualifying vertex orbits. For a matching complex, an edge orbit qualifies iff its edges are vertex-disjoint. Odd height: all crossing-central-edge pairs share the center vertex and are inadmissible; lower k-layer orbits correspond to edges of H_k, while central G edges are singleton disjoint-orbit vertices, so fixed space is |M(H_k)*M(G)|. Even height: center-seam edges are singleton orbits and conflict exactly with edges incident to the terminal half-strip layer, realizing |M(boundary-whiskered H_k)|. Both identifications are canonical under Aut(G). For G=P_n, M(P_n)=Ind(P_(n−1)) and the standard 3-step path suspension recurrence gives contractibility iff n≡2 mod3, otherwise the floor(n/3)-fold suspension of M(P_n□P_k). Independently reconstructed all orbit-conflict equivalences for G=P_3, k=2 and 3, both parities; qualifying vertices respectively 10,9 and 15,14. Finite tests do not establish universal PL topology.

## originality

PASS

The fully read published 3×n reflection Lefschetz result gives alternating homological traces and counts of invariant matching edge orbits for height three (k=1). Such traces cannot determine geometric fixed spaces in general; the new PL identification extends to any graph G and all k≥2 and distinguishes odd joins from even boundary whiskers. Other published 3×n symmetry-character results are more specialized. The closest new 2026 nonequivariant 3×n manuscript remained inaccessible full text; it might contain an incidental folding lemma, explicitly recorded as priority risk.

## value

PASS

The exact, natural PL reduction of every deeper reflected matching complex from a full strip to a half strip is a nontrivial equivariant structural fact, valid for arbitrary base graphs. The odd join/even whisker parity gives a computable recursive model; the n≡2 mod3 all-odd-height contractibility yields an infinite uniform family without requiring the unknown nonequivariant large-grid type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
