# Scientific review

## Correctness — PASS

For selected-edge bit \(v=1\), the perfect edge-domination condition is vacuous; when \(v=0\), exactly one neighboring edge must be selected. The four-state matrix implements precisely that rule on every degree-two edge. The root constraints in the lollipop transfer sum correctly include the three neighbors of each root-incident cycle edge and of the initial pendant edge. The identities \(M^4=M^3+M\) and \(M^3h=M^2h+h\) give independent recurrences in cycle and tail lengths. The nine initial counts and positive cycle-count differences are explicitly verified, so two inductions prove the strict comparison for all allowed parameters. Exact stand-alone brute enumeration checks all cases with at most 15 vertices, alongside independent recurrences on a 28-by-30 parameter grid. Finite checks do not replace the symbolic argument.

## Originality — PASS, with historical-priority risk

Grippo–Lin–Moyano–Vera (arXiv:2607.03894v1) already prove the cycle recurrence, provide a generic generalized-series-parallel counting algorithm, and explicitly state their connected-cycle extremal Conjecture 5.1. The inspected sections containing these results did not give a lollipop-specific two-parameter rational series or the strict inequality for every cycle-plus-one-path graph. The 2025 predecessor concerns algorithms in \(P_6\)-free graphs, not the unlimited-cycle family. Targeted literature queries, equivalence checks, and related-result searches found no result whose statement implies the new theorem; these searches do not certify priority. See the structured literature comparisons for inspected portions and residual risks.

## Value — PASS

The established connected-graph inequality is a live extremal conjecture. This proof verifies it strictly for a natural two-parameter infinite connected-unicyclic class, while simultaneously giving the complete counting generating function and a transparent positive-difference certificate. It is a motivated graph-family theorem, not a bounded computation or a cosmetic restatement of the generic algorithm.

## Limitations

No assertion is made for arbitrary unicyclic or connected graphs, nor of the earliest historical appearance of all equivalences. The code checks only finite instances.

Self-review: passed. Independent audit: not yet performed.
