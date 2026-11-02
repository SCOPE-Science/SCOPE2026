# Scientific review: sharp online EFX probability

## Correctness

PASS. The proof uses a complete partition of the first two goods' two preference comparisons, including equalities resolved through a fixed total tie-break. In the opposite-preference case, complementary first-coin outcomes each certify one of two exhaustive third-good-top possibilities. In the same-preference cases, exact indicators or a two-way partition establish probability at least one-half. The last-stage completion is implementable after observing the final valuations, with no retrospectively changed assignments. Two indistinguishable-prefix inputs establish the converse upper bound for every randomized policy. Exact rational enumeration of 15,625 small profiles checks the algorithm separately; the proof, not enumeration, handles the continuum of real values.

## Originality

PASS under currently inspected literature, with publication-priority qualification. Cohen, Teh, and Wooldridge, arXiv:2609.28333v1, Section 5.3 and Theorem 5.4, provide an upper bound \(1/n!\) and a lower bound \(2/((n+1)n!)\); at two agents their stated constructive guarantee is \(1/3\), not the exact \(1/2\). Their fully inspected proof is compatible with, but does not imply, this adaptive two-agent policy. Neoh and Teh, arXiv:2504.03951v1, Proposition 3.6, count offline EFX allocations, not chronological irrevocable success probabilities. Other ex-post randomized EFX methods allow advance item knowledge or reallocation. Targeted mathematical record and literature searches found no identical sharp online probability; an unindexed equivalent remains a residual possibility.

## Value

PASS. The finding resolves the exact minimax randomized success probability at the first nontrivial online EFX horizon, rather than merely constructing another allocation. It gives a zero-gap calibration of the published broad upper bound for the smallest number of agents, proves the tightness of the information barrier, and supplies a constant-state, two-coin optimal online policy requiring no future values. The parameter restriction is intrinsic: three goods are the first possible nontrivial EFX online case for two agents.

## Boundaries

Nonnegative additive valuations; two agents; exactly three goods; current values visible, goods allocated immediately, no revisions. Does not settle larger horizons or agent counts, nonadditive valuations, or expected approximate-EFX ratio. This review does not assert independent external validation.

Self-review: passed. Independent audit: not yet performed.
