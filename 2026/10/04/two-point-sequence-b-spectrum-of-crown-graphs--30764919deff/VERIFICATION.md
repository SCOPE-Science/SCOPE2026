---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Every independent set in the crown graph is either contained in one bipartition class or is a single deleted-matching pair \(\{a_i,b_i\}\). In a proper coloring satisfying the requirement of at least two color-dominating vertices in every color class, a pure class and a paired class cannot coexist: one endpoint of the paired class sees no vertex of the pure class, leaving at most one color-dominating vertex in that pair. If there are no paired classes, there can be at most one pure class on each side, forcing the two-color bipartition coloring. If any paired class occurs, all classes are paired, so covering all vertices forces the \(n\) deleted-matching pairs. Both constructions meet the two-color-dominating-vertex condition, so the spectrum is exactly \(\{2,n\}\), with the two realizing partitions unique up to color-name permutation. The package's exhaustive set-partition check for \(3\le n\le5\) corroborates the structural proof but is not used to infer the universal theorem.

## originality

PASS

Jakovac and Lang introduce sequence \(b\)-colorings, define the \(S\)-spectrum, and explicitly ask which sets can occur as spectra. The complete current paper contains no crown or complete-multipartite treatment. The classical \(b\)-spectrum literature uses only one color-dominating vertex per color class and therefore does not imply the two-vertex condition here. Resultary searches found the assigned theorem as the exact sequence-\(b\) crown result and unrelated crown-coloring invariants, but no prior spectrum \(\{2,n\}\) theorem.

## value

PASS

The source explicitly asks about possible spectrum shapes. The crown family supplies an infinite, connected, regular bipartite example whose spectrum consists only of its minimum and maximum color counts, so the internal gap grows arbitrarily large. This is a natural structural answer to the new spectrum question rather than a small isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
