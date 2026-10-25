---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For every unselected edge uv, perfect edge domination is exactly deg_F(u)+deg_F(v)=1. The F-zero-degree vertex set U must be independent; every edge with both ends outside U is in F, so F=E(G[V\U]). For K_{m,n} minus t distinct matched edges, any independent U is confined to a single side or one missing pair, and the deg_F=1 condition allows only stars centered on unmatched vertices, except K3,3 minus its whole matching, which is C6 with three 2-edge and six 4-edge choices. Hence for 3<=m<=n,0<=t<=m the polynomial is (n-t)z^m+(m-t)z^n+z^(mn-t), except (3,3,3) with 3z²+6z⁴+z⁶. Independently enumerated 2,228,672 exact edge subsets for 22 parameter triples, confirming every polynomial; for n>=4 deleting the last matching edge changes two n-edge minima into a unique n(n-1)-edge minimum.

## originality

PASS

The P6-free graph class includes matched-deletion bicliques (an induced P6 would require four missing cross edges among three vertices per side, while a matching can provide at most three), so the published general PED counting algorithm is applicable. Its existence does NOT state or mathematically imply without new specialized analysis the closed three-term polynomial, exception and sharp one-edge instability; 2026 follow-up tree/chordal/GSP claims also do not state this family in accessible material. A plausible later primary paper could not be read in full; qualification preserved.

## value

PASS

A dense classical graph family suffers a sharp one-edge jump in minimum perfect-edge domination by an unbounded factor; the exact polynomial gives every valid set and isolates a unique exceptional six-cycle. This is a structural phase transition for a natural domination invariant rather than just another table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
