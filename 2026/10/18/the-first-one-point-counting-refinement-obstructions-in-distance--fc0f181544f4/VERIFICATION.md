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

The exact finite domain is connected distance-hereditary graphs with at most eight vertices, each choice of one distinguished root. Bandelt–Mulder pendant/true-twin/false-twin characterization implies every such graph arises inductively from a singleton, and exhaustive graph-isomorphism deduplication gives layer cardinalities 1,1,2,6,18,73,308,1484. Two supplied independent strategies (constructive recursive generation and complete unlabeled graph atlas filtered by reverse removable vertices) use exact isomorphism and rooted orbit decisions; both give zero failures through n=7 and two unrooted types at n=8 each with a single bad root. Independently regenerated 1,484 eight-vertex types from 308 seven-vertex types and tested pointed colours vs pointed graph-isomorphism; exactly those two obstructions found. Explicit graphs K1 join (K3 ⊔ C4) and K1 join complement(K3 ⊔ C4) have unique dominating root, all seven other points identical 1-WL signatures, but root-stabilizer orbits of sizes 3 and 4: cell sizes 1,7 vs orbits 1,3,4, with 14 and 21 edges. Finite enumeration is exhaustive up to size8, not extrapolated above.

## originality

PASS

Well-known distance-hereditary structure and counts, graph colour refinement and 2-dimensional WL identification do not state the exact first one-marked 1-WL-versus-rooted-orbits failure at n=8 and classify its two unique witnesses. The unrooted counts and decomposition are used as prior inputs, not rebranded novelty.

## value

PASS

A sharp first failure size for individualised 1-WL to identify rooted automorphism orbits in distance-hereditary graphs is a natural informative boundary between symmetry and coarse local counting. The complete two-model classification (and unique roots) exhibits a structural regular-module mechanism and can serve as small counterexample basis; this finite complete and motivated classification is valuable without extending to n>=9.

The dated certificate retains the supplied scientific assessment, sources and limitations.
