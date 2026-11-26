---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Strict matrix-unit multiplication is associative; a nonzero j-fold product is precisely a composable strict chain of j+1 vertices. Thus the nilpotency index at height h>=2 is h. At heights 0 and 1 the full powerset semiring is the two-element distributive lattice, with setwise product as meet. At height 2 the universal unary relation imposes no constraint, and at height 3 the nonzero-product digraph is homomorphically equivalent to a single arc since no vertex can be both source and target; the directed two-edge path (whose images need not be distinct in an input) is a finite obstruction. At h>=4 a four-point chain supplies the directed walk of length two. For each frozen alternating odd cycle, tracking the endpoint equalities v_i=u_j along the arcs yields v_0=u_1=v_2=...=v_{2m}=u_0, so the strict interval at vertex 0 is impossible. Every proper induced substructure splits into paths. If the unique two-walk survives, pin its values to 0,1,2 on the chain walk and extend alternately by 0,1 on the entering tail and 1,2 on the exiting tail; other components map to a single edge. A finite obstruction list would force a bound on the size of the induced support of an obstruction image, contradicting these unbounded minimal induced examples. Wang–Yin–Wang Theorem 1.1 applies in the stated full constant-free signature. For the precise encoding of the displayed absorption identity use empty R1 on the obstruction, rather than universal R1: this leaves all maps unchanged since R1 on the target is universal and gives exactly the binary sum. Direct evaluation proves validity (an empty variable kills the long word; otherwise it is {0} and some binary term must contain 0). Theorem 4.1 and its explicit post-theorem consequence establish precisely the nonderivability asserted at ℓ>(h−1)(k+2).

## originality

PASS

The supported increment is the all-finite-poset upper-height obstruction and exact height threshold, not the general duality criterion, the low-index positive case, or invention of the odd-cycle family. The strongest earlier indexed result uses the same oriented odd cycles but its negative theorem assumes index three and a bipartite product graph. The frozen obstruction argument is genuinely stronger for strict intervals, for which product graphs at height at least five need not be bipartite and higher nonzero-product relations are present.

## value

PASS

This is a natural uniform height threshold for a poset construction that is insensitive to width and branching yet sharply contrasts with flat addition on the same chain multiplication. The obstruction remains informative for nonbipartite high-index targets and gives explicit arbitrarily large minimal induced counterinstances and valid identities with unbounded variable complexity. A bounded small-semigroup census would not supply these conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
