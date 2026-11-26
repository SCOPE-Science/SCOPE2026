---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both in the ordinary game and with only f declared, every finishing selection set contains b and d because a and e are undeclared leaves. Also b and d are undeclared and nonadjacent, so any finishing set of size at most three must add their only common neighbor c. With no declaration, indicating f,a,e successively forces c,b,d. With f declared, selecting b,d via a,e leaves only b,d possibly undominated and at most two moves. If an initial indication is one of b,c,d, Staller can choose an outsider a,f,e, respectively. Otherwise b or d is forced, immediately covering c. Neither c nor f can then be indicated, and any later legal indication of b or d can be answered by a leaf (a or e has no other neighbor through which it could already have been selected). Thus Staller can avoid c and rule out any three-move finish. An independent census used all simple (n−1)-edge subsets filtered by connectivity, and a descending covered-set DP, not Prüfer sequences or the packaged selected-set recursion. For a legal indication no neighbor has previously been selected, hence the DP depends only on the covered set. Across 1, 3, 16, 125, 1296 labelled trees the violating counts are 0, 0, 0, 0, 360 respectively, testing all inclusions. Every offending labelled tree has a degree-three center with arms of lengths 1,2,2 (the single isomorphism class of T₀); each had 13 violating nested pairs. The all-r classification of the displayed game values follows from strategies, not the finite replay.

## originality

PASS

Henning–Rall already show that general-graph continuation fails, but their cyclic eight-vertex witness with two declarations gives neither an acyclic one-declaration obstruction nor the sharp tree cutoff and uniqueness. The comparison supports those specific distinctions; it does not establish exhaustive priority.

## value

PASS

The result locates exactly where a familiar monotonicity principle first fails within trees, identifies the unique first obstruction even allowing arbitrary nested declarations, and uses one already-dominated leaf to force failure at every larger order. This is stronger and structurally different from finding another cyclic example or computing an arbitrary tree invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
