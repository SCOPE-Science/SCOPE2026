# Scientific review: first-regime zero-run-free cyclic covers

## Correctness: PASS

The graph's exact deficits and their exceptional overlap at \(k=2h\) have been recomputed. Every required added flow must connect each surplus source to some deficient target. For \(h\le k\le2h\), a shorter bridge would force overlapping or touching copies of \(0^{h-1}\), creating forbidden \(0^h\), except for a source simultaneously beginning and ending with the shorter run, which has already been excluded as balanced. Universal bridges of length \(k-h\) exist, balance the graph, and yield real Eulerian covers. The finite verifier separately validates literal cyclic covers, graph distances, and exact minimum-cost assignments. This verifies the all-parameter reasoning without treating finite enumeration as its proof.

## Originality: PASS with residual risk

The closest same-object source, Chee et al. (2024), maximizes distinct-window run-limited cycles rather than minimizing cyclic covers with necessary repeated windows. Bernardini et al. (2022) provide general Eulerian-walk algorithms without an explicit all-parameter formula in this restricted family. An earlier private binary no-adjacent-equal-symbol covering result subsumes the \(q=2,h=2\) slice but not the higher-alphabet and higher-forbidden-run theorem. Moreno's 2005 restricted-language thesis was inspected only by abstract because its PDF was unavailable; equivalent treatment there remains a real literature risk. The four detailed implication checks and source-reading limitations are retained in `AUDIT.json`.

## Value: PASS

The minimum cycle is a natural optimal universal readout/test word for a channel that prohibits long zero runs. An exact closed first-regime formula, full path-level classification of optimal augmentations, and a parameter boundary at \(k=2h\) go beyond isolated computational examples. The correction measures precisely the minimum cost of restoring flow balance while respecting the same physical run constraint. The theorem makes no unwarranted claim about broader windows or the number of distinct cyclic optima.

Self-review: passed. Independent audit: not yet performed.
