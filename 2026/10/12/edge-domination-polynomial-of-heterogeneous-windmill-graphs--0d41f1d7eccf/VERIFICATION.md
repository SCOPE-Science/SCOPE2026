---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Reconstructed the zero-selected-degree lemma: F is edge dominating precisely when its incident-vertex complement is independent. Split disjointly into hub incident to a selected spoke (at most one rim isolated in each clique) versus no spoke (all rim vertices covered); exact-isolate inclusion-exclusion gives the three product terms with no double counting. Lower bound per blade uses at most two rim endpoints per internal selected edge; analyzed even local P perfect matchings/E one repeated internal endpoint/Q one spoke versus odd t matchings and one-extra-spoke types u, including singleton and size-two boundary. Direct independent edge-subset enumeration matched the inclusion-exclusion polynomial for nine small clique-bouquet choices; finite checks corroborate, while the combinatorial classification proves the unrestricted formula.

## originality

PASS

PASS best-of-knowledge: a complete heterogeneous-clique-bouquet edge domination enumerator and all parity-conditioned optimum multiplicities were not located in the primary edge-domination coefficient literature or Resultary results. Do not claim originality for general edge domination, line-graph equivalence, or the known friendship-graph scalar parameter. Full relevant 2016 article inaccessible and explicitly retained as risk.

## value

PASS

PASS: Edge domination is a standard graph optimization invariant. This all-size clique-bouquet family supports an explicit full coefficient enumerator and exact nonmatching optimum multiplicity, a substantive extension beyond scalar homogeneous friendship graph minima; parity dependence gives structurally meaningful extremal classification usable as benchmark for edge-domination counting on block graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
