# Scientific assessment

## Correctness — PASS
For every \(k\ge1\) and \(n\ge k+4\), the threshold-one parallel update simply translates the initial four-grain support one site per round, truncated at the absorbing sink. The proof explicitly computes each new simplex's attaching intersection. All but one are connected contractible subcomplexes; the unique exceptional intersection at round \(k+1\) consists of two contractible components. The homotopy-pushout argument gives one permanent circle and every specified persistence inclusion. The finite standalone checker independently confirms the supports, intersections, and representative simplicial homology groups, but does not replace the symbolic proof. Assumptions on firing convention, boundary clipping and integer indices are essential.

## Originality — PASS, with residual risk
The closest primary paper is Riihimäki–Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786v1 (2026), whose directed-path Proposition 3.9 concerns three grains, rather than two adjacent pairs of four grains. Its persistence section introduces filtrations and illustrates cycle examples, not the present all-parameter two-block path barcode. The closest indexed avalanche finding concerns complementary congruence supports on directed cycles, where wraparound is central; it neither implies nor covers the present path filtration. Searches under two-block, four-grain, persistence, and shifted-support formulations and comparison against the accessible prior research ledger found no matching or stronger result. Unindexed equivalent work remains possible; search absence alone is not proof of novelty.

## Value — PASS
The two-block path support is a natural one-grain perturbation of a published three-grain example. The previously proved three-grain terminal first Betti number grows as \(n-k-2\), whereas the four-grain terminal first Betti number is always one: adding one grain can eliminate an arbitrarily large number of independent cycles. Identifying the exact birth time and every inclusion additionally gives the complete field-independent persistence barcode for an infinite family, not merely a computational example.

## Scope and limits
No claim is made for directed cycles, asynchronous chip-firing, more general grain configurations, or all sandpile filtrations. The available comparisons do not exhaust unpublished or unindexed work, and independent mathematical validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
