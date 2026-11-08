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

The flats are subsets of size <=r-1 plus top. A three-round EF game is determined after two selected flats by possible equality/inclusion relation triples with a third flat. Four Venn cells reduce these to 81 empty/full/nontrivial choices, and rank availability is encoded by capped sizes. The proof gives explicit outside-capacity, t>=3 and s>=6 pumping identities, with finite exceptional patterns, yielding pointed two-round types indexed by (min(s,3),min(t,2)). Rank-three distinguishing sentences combine L1,L2,L3 and U1,U2, true at exactly r>=3,4,5,6. Independently enumerated direct three-round types for all 2<=r<n<=7 and checked a separate four-cell capped transfer for r through 14, n=r+1,r+2,r+4. The universal conclusion depends on the explicit finite-state pumping derivation, not extrapolation from these checks.

## originality

PASS

General Ehrenfeucht–Fraisse theory and structural descriptions of uniform-matroid flat lattices are classical. The precise collapse at rank six for pure-inclusion 3-round equivalence is not implied by a comparable published Boolean-algebra threshold: that result uses Boolean operations and untruncated Boolean lattices, both absent here. Inspected matroid papers target representation and cyclic flats, not this parameter-uniform EF classification. Priority risk remains for specialist model theory of truncated Boolean posets.

## value

PASS

This is a complete five-class quantifier-depth classification across an infinite natural matroid family, with an exact sharp finite representative cutoff. It quantifies information lost when rank and cardinality symbols are omitted and supplies useful test structures for finite-model-theoretic equivalence; not merely a small computed table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
