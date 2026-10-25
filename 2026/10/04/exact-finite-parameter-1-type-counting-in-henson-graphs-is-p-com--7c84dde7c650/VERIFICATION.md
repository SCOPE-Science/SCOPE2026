---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Correct as stated for fixed r>=3 and finite induced A in the countable homogeneous K_r-free Henson graph. Proof reconstructs QE/homogeneity, the exact permitted S subset criterion, extension over A and infinite multiplicity of each outside type, giving Theta=C_{r-1} and total n+C(1). #P membership uses unique witness tags; joining arbitrary bipartite B with K_{r-3} is K_r-free and yields the exact offset for a polynomial-time metric reduction from exact bipartite #IS. Checked r=3, empty join, empty parameter set, and the five-point examples. Independent bounded enumeration tested 3,672 permissible parameter graphs and 112,580 one-point neighborhood masks, plus 3,445 bipartite-join identities across fixed r=3..7. Finite testing was not treated as an infinite proof.

## originality

PASS

Best-of-knowledge PASS for the combined fixed-r exact-complexity classification and uniform r>=3 reduction. The admissible-neighborhood bijection and its r=3 independence-set specialization are already explicit or immediate in the primary Katětov/extension literature; they are credited and NOT presented as novel standalone mathematical structure. The new claim is the complete counted 1-type invariant attached to these structures and the explicit uniform bipartite-#IS metric reduction for every fixed r. Although the reduction is concise and may be folklore, the inspected prior results do not themselves state the claimed graph-type #P-completeness theorem. An equivalent unindexed theorem remains possible and is recorded below. A failed search alone is not a novelty proof.

## value

PASS

Finite complete 1-type spaces are a canonical invariant of the Henson free-amalgamation theories, and the coefficient polynomial records all neighborhood sizes rather than only an isolated numerical count. The exact computational-complexity classification identifies a genuine tractability barrier for a natural model-theoretic counting problem, uniformly for every fixed clique prohibition r; the explicit bipartite join gadget is a reusable reduction despite its short proof. This is not intrinsically just a rebranding of the independence polynomial: the natural object to count is complete 1-types, and the r-dependent restriction and uniform hardness require an explicit bridge. The previously known r=3 admissibility rule by itself would not suffice to establish a new independent result, and this value assessment attaches to the full exact-complexity theorem. No downstream theorem or paper-sized contribution is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
