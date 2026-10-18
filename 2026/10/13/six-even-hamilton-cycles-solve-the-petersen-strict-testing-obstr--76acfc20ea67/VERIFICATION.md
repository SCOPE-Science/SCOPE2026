---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Model Petersen vertices as edges of K5 and its 15 candidate edges as disjoint unordered K5 edge pairs. The six even-permutation Hamilton pentagons of K5 are distinct modulo dihedral action and form six pools; for every candidate pair {e,f} and any outsider w, at least one even pentagon contains w but omits e,f. Independently enumerated all 15×8=120 witness obligations. Strict testing criterion thus proves six pools suffice. Outcomes of 15 candidate pairs under any strict design form an antichain, since each directed pair must have outsider separating pool; Sperner bound binom(5,2)=10<15 forces ≥6. For m>=5 first-stage all 3-subsets of [m] plus six zero-incidence items, positive index set Y has sizes 0,3,4,5,6 (otherwise >2 defectives). The specified 6/4/6/5 adaptive second-stage pools resolve all potential ≤2 candidate sets and reject strict supersets. Independent exhaustive m5 16-item check over 65536 defective subsets verified strict detection; general m proof is by complete case analysis, not extrapolation. Thus t(n,2,2)≤m+6 when n≤binom(m,3)+6; local Petersen six-test optimum is exact while global two-stage bound only upper.

## originality

PASS

Damaschke--Sheikh Muhammad--Wiener 2014 full primary paper sets out exact strict candidate-hypergraph criterion and their Lemma17 uses 7 pools for the same Petersen graph; Proposition16 gives m+7 with seven zero-incidence items. Six even Hamilton cycles supply a new more efficient local design and tight Sperner lower bound, and replacing seven zeros by six propagates a sharper construction bound. Nothing in inspected 2014 criterion or seven-pool witness implies six pool feasibility; an unindexed other six-pool design remains risk.

## value

PASS

The exact minimum solves the specific small-graph bottleneck identified in a foundational strict two-stage group testing construction. Explicit symmetric six-pool design improves a nontrivial infinite-family upper bound by one test and gives a matching local lower bound rather than a marginal unrelated finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
