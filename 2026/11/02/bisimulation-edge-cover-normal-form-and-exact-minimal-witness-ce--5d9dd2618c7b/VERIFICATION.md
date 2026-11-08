---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For a finite one-agent S5 model, successors of a world are its complete equivalence class. An active cross-model class pair must have identical atomic profile support and, for each profile, the chosen relation pairs form a spanning bipartite edge cover. Conversely any selection of compatible class pairs and independent internal profile covers satisfies atomic harmony, forth and back. This is a genuine bijection (even if a class participates in multiple pairs). Inclusion-exclusion gives U(a,b) spanning covers. Any inclusion-minimal cover has every edge incident to a degree-one endpoint; its connected components are precisely stars, yielding H(a,b) from exp(xy+x(e^y-1-y)+y(e^x-1-x)). Thus nonempty, minimal nonempty, global, and minimal global relations are counted respectively by product_{ij}(1+beta_ij)-1; sum eta_ij; a weighted spanning edge-cover sum on compatibility graph; and a weighted minimal edge-cover sum. These formulas cover empty compatibility graphs, isolated class vertices, zero propositional vocabulary, all nonempty finite labelled models and distinguish inclusion-minimality from minimum size.

## originality

PASS

Ordinary bisimulation axioms, global/total bisimulation terminology, and complete-bipartite edge-cover counts are classical. The independent two-stage weighted enumeration across arbitrary finite labelled one-agent S5 model pairs, with all four inclusion-minimal/global census formulas, is a nontrivial combined classification not stated in the inspected logical-definability sources. Best-of-knowledge PASS qualified against obscure enumeration results or alternate presentations of bisimulation witnesses.

## value

PASS

A universal exact census for four natural classes of witnesses between arbitrary fixed finite epistemic models is a useful structural classification, not just another example or arbitrary small enumeration. The layered normal form allows researchers to compute minimal/global witness abundance and understand effects of accessibility partitions and valuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
