---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Writing \(x=|S\cap A|\) and \(y=|S\cap B|\), the switched graph has the explicit bipartition \((S\cap A)\cup(B\setminus S)\) and \((S\cap B)\cup(A\setminus S)\), hence is \(K_{b+x-y,a-x+y}\). Equality of unordered part sizes with \(\{a,b\}\) gives exactly \(x-y=0\) or \(a-b\). Vandermonde counts each selector family, with coincidence exactly in the balanced case. In \(K_{2,3}\), a singleton in the larger part and an edge containing it are both identity switches, while their symmetric difference is a singleton in the smaller part and is not. The frozen verifier independently exhausts all selectors in 33 small parameter cases.

## originality

PASS

The defining 2026 preprint was inspected at its identity-switch definition, the complete-bipartite examples and the subgroup claim. It states the opposite universal closure conclusion. Its own examples are compatible with the \(K_{2,3}\) counterexample but do not classify all selectors. Classical switching-class results identify complete bipartite graphs as one switching class, yet do not determine which selectors return a fixed biclique or count them. Resultary search found no prior exact selector classification or correction.

## value

PASS

The result directly corrects a central algebraic claim of the source paper and replaces an isolated counterexample with a complete transparent classification on the canonical biclique family. This changes the premise of the proposed subgroup program and supplies reusable exact structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
