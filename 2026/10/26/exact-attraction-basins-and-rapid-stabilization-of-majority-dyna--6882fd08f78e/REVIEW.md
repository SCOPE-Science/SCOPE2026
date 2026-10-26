# Scientific review

## Correctness — PASS

For every integer \(m\ge1\), the local update rules partition each peripheral pair relative to its initial hub into an agreeing pair, an opposing pair, and two orientations of a mixed pair. At the first update all mixed pairs align with the old hub; all other pairs remain monochromatic. Thereafter each pair has its matching partner as a neighbor and can never change. The hub's second majority comparison is therefore final. Direct disjoint counting by the initial hub color gives the precise basin sizes \(3^{m-j}+3^j\) for \(2j<m\) and \(3^j\) at \(2j=m\); the latter requires careful treatment of the hub's first-update tie. These counts prove the whole terminal polynomial and consensus law. Separately, an exact count of hub reversion configurations proves the two-update multiplicity and its limiting fraction. The independent graph-update implementation exhaustively checks all \(174{,}760\) inputs on sizes \(1\le m\le8\); the proof is uniform in \(m\) and does not extrapolate from the finite checks.

## Originality — PASS, with residual bibliographic risk

The closest primary source is Zehmakan's 2023 paper on the same synchronous majority-with-retention model, which establishes broad stabilization and cycle-specific results, not fixed-state attraction basins of friendship graphs. Out and Zehmakan (2021) investigate elite influence in the same model but do not furnish the exact friendship-graph basin law. Auletta, Ferraioli and Greco (2018) study consensus/coexistence on arbitrary graphs with asynchronous updates; their results do not determine these synchronous basin sizes. Published-results search and searches of weighted exact tables, graph aliases, full statements, and analogous Boolean-network descriptions found no direct implication or identical enumeration. Related cycle-specific majority calculations and friendship-graph *static* invariants likewise do not imply this theorem. A mathematically equivalent count in otherwise unindexed Boolean-network or majority-threshold literature cannot be ruled out; negative search alone is not asserted to prove uniqueness.

## Value — PASS

The result solves the full labelled attraction-basin problem on a natural graph family with a universal hub and many two-person cliques. It does not stop at a fixed-point census: each equilibrium's exact basin size is known, so every terminal opinion-count probability can be computed. The contrast between almost certain persistence of the initial universal hub and exponentially unlikely whole-network consensus is a structural consequence of local pair shielding. The sharp two-update convergence time and asymptotically one-half share requiring exactly two rounds quantify transients without simulation. These conclusions are natural network-opinion observables, not arbitrary finite parameters, and are not implied by general bounds on stabilization.

## Closest literature and limitations

Zehmakan (2023), arXiv:2302.06760v1; Out–Zehmakan (2021), DOI:10.24963/ijcai.2021/49; Auletta–Ferraioli–Greco (2018), DOI:10.24963/ijcai.2018/7. Claims are limited to deterministic synchronous updates, open neighborhoods, two opinions, and hub-joined triangles. Random tie-breaking, asynchronous update orders and other hub-clique sizes are not covered. Originality remains subject to independent bibliographic validation.

Self-review: passed. Independent audit: not yet performed.
