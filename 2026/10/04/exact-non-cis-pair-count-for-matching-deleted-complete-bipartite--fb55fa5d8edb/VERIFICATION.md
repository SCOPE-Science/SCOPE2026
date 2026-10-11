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

In this bipartite graph every non-isolated maximal clique is a surviving cross edge, while every mixed maximal stable set is exactly one deleted matching pair. Side stable sets meet every surviving edge, and any isolated singleton clique lies in every maximal stable set, so they create no non-CIS pair. For each deleted pair, exactly (a−1)(b−1)−(t−1) surviving edges avoid its endpoints. Summing over t pairs gives the formula, and the zero/one classifications follow arithmetically. Fresh brute-force enumeration independently generated all maximal cliques and maximal stable sets for all 46 legal triples with 1≤a,b≤4 and matched the formula in every case.

## originality

PASS

The 2009 theorem directly covers the defect-one notion and therefore the P4 corollary, while broader CIS structure can recover portions of the zero/nonzero boundary. Neither inspected accessible source gives the exact count t((a−1)(b−1)−t+1) throughout the three-parameter matching-deleted biclique family. Resultary returned no matching exact formula. The recent general recognition preprint remained full-text inaccessible, so possible overlap there is retained as a residual risk rather than converted into noncoverage.

## value

PASS

Deleting a matching is a canonical controlled perturbation of the basic complete-bipartite CIS family. The exact certificate count quantifies how CIS fails throughout the whole perturbation family and gives a natural crown-graph specialization; that is more informative than recognition alone and fits the current complexity-motivated study of tractable CIS subclasses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
