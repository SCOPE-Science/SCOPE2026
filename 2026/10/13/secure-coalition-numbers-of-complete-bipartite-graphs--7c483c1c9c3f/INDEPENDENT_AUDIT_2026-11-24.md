# Independent mathematical audit

## correctness

PASS

The frozen numerical classification is correct. The defender-swap test follows by checking whether the defender's removal leaves another outside vertex on the attacker's shore without a selected neighbor. In the relevant low-excess cases (E≤2 at s=5, E≤3 at s≥6), when both shores have singleton blocks their partners must contain at least (1,2) and (2,1); the near-full-shore alternatives are too large. They cannot be the same block because a block with both requirements is secure dominating. With excess at most three and no singleton on a six-vertex shore, equality against half its size forces three pure two-vertex blocks (even counts and equality in |C|−1≥q_C/2); opposite-shore singletons cannot partner with them. The hub constructions and small-shore cases give the frozen values. In the repaired finding, containing the whole two-vertex shore makes a block already secure. Thus exactly two blocks meet that shore. If at least three larger-shore-only blocks existed, the union of two would still miss a larger-shore vertex with no neighbor in the union. The union of one with an A-containing block would leave at least two larger-shore vertices outside and only one possible defender. The four-block construction works, including the all-singleton K_{2,2} boundary. Rechecked the repaired contextual reduction as well: a union of two blocks has size at most E+2, where E is total excess; for size <s both predicates reduce to x,y≥2. The direct adjacency/occupancy-multiset replay /workspace/branches/audit_coalition.py verified the maxima for all 1≤s≤t≤9, including the first stabilized cases. It is finite corroboration, not the proof.

## originality

PASS

Frozen originality FAIL as framed: the frozen record specifically presents the stabilized large-shore branch as new structural content, but both the bound and the optimal construction in that regime follow from Henning–Mojdeh's Theorem 6 via agreement of the two predicates on small block unions. This is actual implication and shared construction, not merely numeric coincidence or unresolved access. Repaired originality PASS for the narrowed finding SEC(K_{2,t})=4 for all t≥2, whose upper bound does not transfer from double coalitions or the general SEC bounds. The complete classification remains contextual and the overlapping parts are explicitly credited.

## value

PASS

The repair resolves the entire first nonstar complete-bipartite family rather than isolating a few small cases. It shows that the general minimum-degree-based lower bound stays exact as the larger shore grows without bound, despite the distinct and growing double-coalition number. The mechanism is the incompatibility of placing the entire two-vertex shore in one block and of having a third pure block on the larger shore. The previously covered stabilization is no longer counted toward the repaired finding's value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
