# Review: macroscopic dimer jamming on a blocked bipartite substrate

## Correctness

**PASS.** The finite process is reduced exactly to three edge types with respective transition weights \(AD\), \(BC\), and \(BD\). Equal-rate exponential edge clocks generate the same accepted-edge order as independent continuous priorities. The associated density-dependent Markov chain has a polynomial drift and bounded martingale noise; fixed-time convergence follows by Doob and Grönwall estimates. An explicit integration of the four ODEs gives a unique limiting vacuum state \((r,0,r,0)\). The deterministic tail bound, which charges every future deposition to a distinct currently vacant complementary-group vertex, upgrades fixed-time fluid convergence to final-jam convergence. All limits and the diagonal parameter case are stated explicitly. Exact-rational recurrences, a literal six-order check and finite simulations were reproduced from `verify.py`. Computations supplement rather than replace the proof.

## Originality

**PASS with bibliographic residual risk.** Literature comparisons distinguish fixed-graph random-edge adsorption from online vertex-arrival matching on random bipartite graphs, and from worst-case approximation results for general greedy matchings. Accessible full scientific text in Mastin–Jaillet (2013) analyzes a different \(G(n,n,p)\) input and Algorithm 2; Arnosti (2021) analyzes comparisons under a random edge-set distribution. The classic Pippenger (1989) and Dyer–Frieze (1991) works establish context but available abstracts do not establish this explicit blocked-rectangle law. Full text of the 1991 article was unavailable; an unrecognized related example is possible. The closest previous explicit random-dimer results concern dilute forbidden-edge families or different graph structures and do not imply a macroscopic residual fraction for a forbidden complete rectangle. The new mathematical statement is the closed-form value \(r(\alpha,\beta)\) and its positive Hall-feasible regime, not the general fluid-limit method.

## Mathematical value

**PASS.** Deleting all edges in one natural two-class forbidden rectangle is a minimal structured way to create incompatible adsorption opportunities on an otherwise complete bipartite substrate. Even with a perfect matching, the irreversible process wastes a positive fraction of vertices; e.g. equal blocked fractions \(2/5\) produce vacancy fraction \((2/5)e^{-3/2}\). The exact continuous two-parameter law quantifies this kinetic deficiency, distinguishes dynamical jamming from combinatorial feasibility, and gives a nonperturbatively small diagonal effect for small positive blocked fractions. The law is not merely a normalization check, finite lookup, or rephrasing of a standard matching bound.

## Closest literature and limitations

- N. Pippenger (1989), DOI 10.1137/0402034: general edge/vertex adsorption on graphs; original paper inaccessible for full inspection.
- M. Dyer and A. Frieze (1991), DOI 10.1002/rsa.3240020104: randomized greedy matching on fixed graphs, with particular focus on general guarantees and sparse families; complete text inaccessible, leaving the main residual overlap risk.
- A. Mastin and P. Jaillet (2013), arXiv:1307.2536v1: accessible full text, different online arrival rule and random graph input.
- N. Arnosti (2021), DOI 10.1287/stsy.2021.0082: accessible scientific text, compares greedy matching procedures in random graph ensembles rather than this fixed blocked rectangle's asymptotic count.

The theorem supplies a first-order thermodynamic vacancy law, not a convergence rate, fluctuations, or a result for a forbidden rectangle whose normalized width vanishes. The source comparison does not prove absolute bibliographic uniqueness.

Self-review: passed. Independent audit: not yet performed.
