# Self-review

## Correctness — PASS

The total-domination predicate on the crown graph is equivalently \(a(D),b(D)\ge2\), including selected vertices; the proof checks both directions. With deficit \(s=2n-|\mathcal P|\le4\), at most \(2s\) vertices are in nonsingleton classes. If a bipartition side lacks a singleton, a singleton on the other side forces a \((r,1)\) partner; an additional pure block and its partner saturate the deficit and leave at most four vertices on the supposedly singleton-free side. Hence both sides contain singletons. Their necessarily distinct nonsingleton partners each cost at least two deficit units, yielding the exact two opposing triples. Counting them has no quotient by block exchange because profiles differ. The construction meets every required partnership, and its only partnership edges form a double star. A standalone adjacency checker and exhaustive small-instance enumeration corroborate the proof, not replace it.

## Originality — PASS, with explicitly bounded risk

The scalar \(TC(K_{n,n}-M)=2n-4\) is **already covered**: the total-coalition feasibility condition coincides with total \(2\)-coalition in \(K_{n,n}\). Golmohammadi–Alikhani–Bakhshesh, Proposition 3.3 (2024 public manuscript), and Brešar–Henning–Samadi, Theorem 5.3 (arXiv:2507.18306), obtain exactly that scalar and show an instance of the two-triple construction. Those original proofs and source text were inspected; neither establishes the enumeration, proves all extremizers have this shape, or establishes their unique coalition graph. Barát–Blázsik's sharp-upper-bound coalition graph uniqueness theorem assumes equality in a far larger maximum-degree bound, absent here. Searches for the crown and complete-bipartite aliases, double-total/total-2 terminology, exact extremizer counts, and equivalent double-star assertions did not reveal the classification. Possible unindexed literature is a residual risk; no absent search hit is offered as proof of originality.

## Value — PASS

This is an exact, all-extremizer classification for a natural family arising from deletion of a perfect matching, together with a labeled partition count and a unique associated total-coalition graph. The structural rigidity is not recoverable merely from the pre-existing scalar optimum or one exhibited construction. Exact maximum-partition and partnership-graph information is a distinct natural invariant motivated by the original papers' focus on total-coalition graphs, with polynomially many distinct optimizers despite a unique graph type. It is not a marginal numerical bound or arbitrary small-order slice.

## Limits and closest literature

The argument requires \(n\ge5\) and open-neighborhood total domination. It does not claim novelty for the scalar, the transfer of that scalar, or an example optimal construction. Relevant complete primary text includes arXiv:2211.11590v2, arXiv:2301.09979v3, the 2024-12-24 publicly supplied double-total-coalition manuscript, arXiv:2502.07310v3, and arXiv:2507.18306v1. Computer tests are bounded. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
