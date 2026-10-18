---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read exact 18-output transversal T and verified directly that every one of 90 words has exactly one deletion in T, each output has five parents, yielding 18 disjoint cliques and the sharp independent-set upper bound. Reimplemented 18-partite exhaustive MRV recursion from deletion sets rather than trusting stored VERIFY_OK: visited 368 nodes, produced exactly eight maxima, 12-word common core and complete three-binary-block classification. Checked six-color descent syndrome for every confusable pair; common-core intersection proves five colors impossible because five color classes would each have 18 words. Independently enumerated networkx graph maximal cliques: 272 total, 96 size-five, none above five. Finite graph enumeration covers every labeled word in its 90-vertex domain, not an infinite inference.

## originality

PASS

The closest primary 2012 deletion-graph coloring analysis is explicitly binary and fixed-weight, whereas this concerns ternary fixed composition and complete equality structure. General q-ary deletion bounds do not imply the common-core or chromatic obstruction. A highly relevant 2014 Cullina thesis was located but could not be fully read; this is a genuine priority risk, not proof of coverage or automatic failure.

## value

PASS

The (2,2,2) layer is the natural twice-repeated smallest three-symbol composition, and a nontrivial clique/chromatic gap demonstrates failure of the binary optimal-coloring analogy. All eight extremizers, their common core and the exact obstruction are meaningful finite structural facts beyond a single number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
