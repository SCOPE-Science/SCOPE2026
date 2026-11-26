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

The pair description (U,F), F a subset of the edges induced by U, is equivalent to ideal closure. Omitted vertices are always minimal in the complement; an omitted edge is minimal there exactly when both endpoints are in U. Downward closing these generators is precisely the stated update. Independently, I encoded ideals by their maximal antichains, recursively enumerated antichains by deletion of comparable elements, and computed inverse rowmotion as A -> max(Q minus the upset of A). Indeed the preimage ideal has minimal complement A. Traversing the inverse permutation gives exactly the same orbit lengths as forward rowmotion. The replay checks closure, bijectivity and full orbit coverage, and matches all 39 multiplicities, 133,958 states, 6,207 cycles, maximum length 192 with multiplicity 30, and order 356800176532800 with the stated factorization. No fixed ideal is also immediate for a nonempty poset: a proper ideal lacks the minimal complement elements contained in its image, and the full ideal maps to the empty one.

## originality

PASS

The distinct result is the complete classical rowmotion cycle table and exact permutation order for the Petersen incidence poset, not rowmotion's generic bijectivity, toggle representation or lack of fixed points. Compared period formulas and neighboring exact censuses do not cover that poset.

## value

PASS

The vertex–edge incidence poset of the Petersen graph is a distinguished connected, highly symmetric height-two example outside the skeletal and fence formulas. The whole cycle census is a useful precise benchmark for proposed period bounds and structural descriptions of graph-incidence rowmotion: even with two ranks it exhibits 39 different lengths and an order divisible by eleven distinct primes. Merely computing one long orbit or counting ideals would not establish that behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
