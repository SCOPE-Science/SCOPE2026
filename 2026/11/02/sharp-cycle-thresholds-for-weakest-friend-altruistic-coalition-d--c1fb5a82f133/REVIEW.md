# Scientific review

## Correctness — PASS

The definition uses the global minimum across every friend regardless of coalition membership, matching the published minimum-based equal-treatment model. The potential differences are proved by a pairwise-edge calculation. All four moves in the four-agent and arbitrary-order tree cycles have strictly positive utility changes, with explicitly displayed mover valuations. The finite enumeration is truly exhaustive for every simple labeled graph of order at most four and every coalition partition, with an independently implemented direct utility evaluation and a directed-cycle search. The included program was executed and passed all assertions. Its enumeration proves only the claimed finite cutoff; the all-order assertions have symbolic proofs.

## Originality — PASS, subject to priority risk

The principal source defines six altruistic coalition-formation models and establishes equilibrium existence and complexity, without asserting this improvement-dynamics boundary. The older minimum-based *hedonic* model computes friend minima inside the relevant coalition, not globally; the dynamic hedonic literature considered has changing utilities from historical interactions. The 2020 predecessor covers global summation, but not global minimization. Full-text comparisons, semantic research-record searches and prior accessible claim comparisons did not identify an equivalent sharp classification or a stronger theorem subsuming it. Search failure alone does not establish novelty; further specialist sources may exist.

## Mathematical value — PASS

The relevant problem is whether decentralized unilateral changes actually reach the Nash-stable partitions that existence theorems guarantee. The same model family has exact potentials under sum aggregation yet a strict improvement cycle under weakest-friend aggregation. The sharp four-agent classification and five-agent connected-tree threshold identify the first structural breakdown of convergence, and the all-order tree shows that cycles persist even for sparse connected networks. This is a motivated boundary of a natural dynamics question, not a mere renamed instance or routine numerical increment.

## Literature comparison and limits

Kerkmann–Cramer–Rothe (arXiv:2301.05674v1) is the most relevant direct baseline. Kerkmann–Rothe (IJCAI 2020) gives the earlier global-sum model. Wiechers–Rothe (2020) uses coalition-local minima, while Boehmer–Bullinger–Kerkmann (arXiv:2211.17169) uses history-dependent hedonic dynamics. No claim of priority certification is made. Arbitrary strict improvements, not best responses, are analyzed; the finite graph classification rests on a complete transparent enumerator, and no claim is made that a Nash-stable partition fails to exist.

Self-review: passed. Independent audit: not yet performed.
