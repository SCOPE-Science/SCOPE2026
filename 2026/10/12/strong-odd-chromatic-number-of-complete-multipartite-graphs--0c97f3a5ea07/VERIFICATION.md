---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Properness keeps each color within one independent part. Every vertex outside that part sees every vertex of its color class, forcing the class size odd. Conversely all visible color classes are viewed in full and therefore satisfy every neighborhood parity rule when globally odd. An odd part takes one odd class, and an even part needs two positive odd summands, attainable as 1+(n_i-1). The proof includes size-one parts and r=2, and excludes r=1 where the vertex-neighborhood condition is vacuous. Independent partition enumeration of 23 multipartite profiles totaling <=6 vertices found the exact minima over 2414 canonical colorings.

## originality

PASS

Best-of-knowledge distinct exact all-multipartite strong-odd invariant formula. Earlier odd-color-class observation for cycle/empty-graph joins suggests the mechanism but is not an all-independent-part join theorem; Kwon–Park state a four-color biclique upper bound, not the parity classification. A close ordinary-odd-coloring result uses an existential rather than all-visible-colors requirement. Elementary nature leaves elevated folklore/implicit-generalization risk.

## value

PASS

The class is a canonical test of the strong odd chromatic number, and the result gives both a global coloring characterization and exact minimum for any number/size of parts, sharpening the published biclique 4-color bound. This exact natural family-wide parity classification is useful as a benchmark; its very short proof and close relation to the definition are openly flagged as a significance limitation, not an unsupported general extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
