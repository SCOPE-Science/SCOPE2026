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

The quantifier-rank-two Ehrenfeucht–Fraisse game for a finite nonempty strict poset sees exactly which of the 3-bit pointed profiles (exists lower, exists upper, exists incomparable) occur; each profile is definable with at most two nested quantifiers and Duplicator matches any selected pointed profile. Incomparability-graph connected components are linearly ordered by the poset, so its ordinal-sum decomposition constrains signatures to 2 singleton/antichain cases, 4 nontrivial connected cases and 16 multi-component displays, with exactly two duplicated sets: 20 distinct rank-two theories. All 20 lower-bound witnesses are explicit downset tuples. The exceptional mask 232 requires two nontrivial endpoint components, a middle interior point, and an additional element for type 111, hence >=6; its six-element witness attains it. Independently generated naturally labelled posets by adjoining an ideal-supported maximal vertex, with per-size counts 1,2,7,40,357,4824 for n=1..6 and verified exact all-20 minimum masks, with mask 232 unique at size 6. Exhaustion through n=6 supports the table; global exclusion follows from ordinal-sum proof, not that census.

## originality

PASS

The two-round game and formula profile language are classical; the assessed contribution is the complete 20-type spectrum and optimal six-point bound for finite nonempty pure-order posets. Broader satisfiability algorithms for FO^2 with transitive relations and optimal representatives for colored linear orders do not supply this exact poset table as a formal consequence. No matching published exact finite-poset count was found in mathematical searches; unindexed prior enumeration remains a risk.

## value

PASS

The number and least sizes of bounded-quantifier-rank theories are canonical finite-model invariants for a classical family, not a freely chosen numerical slice. The 20-type complete census and single six-point obstruction give explicit finite representatives for every two-round observational class, of use in finite-model testing and logic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
