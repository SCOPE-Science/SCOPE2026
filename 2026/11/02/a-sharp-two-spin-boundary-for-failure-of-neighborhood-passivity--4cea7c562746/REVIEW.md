# Scientific review: two-spin Glauber neighborhood passivity

## Correctness: PASS

For the four-state Ising Hamiltonian with energies \((0,A,A,B)\), direct Markov-kernel propagation gives the asserted exact formulas for the two relevant excited-state probabilities. The neighborhood-passivity sign reduces to the opposite sign of the scalar function \(H(B)\). Its left-endpoint value is strictly positive under any strict cooling, it is negative at the claimed right endpoint, it is strictly decreasing between them, and it stays negative thereafter. This proves existence, uniqueness, and the full sign classification rather than merely finding a negative numerical instance. The rational witness gives \(\mathcal P_{--}=-293719/163334085\), verified against direct four-state propagation. The single-spin minimality assertion follows because a heat-bath flip updates the two-state law exactly to its temperature-\(\beta_1\) Gibbs distribution. The standard-library checks confirm all central identities, plus 5,000 finite parameter diagnostics; numerical tests are not used as the proof of global uniqueness.

## Originality: PASS, with priority qualification

The closest primary work, Luo et al. (arXiv:2311.10424v1, Eqs. 39–41), introduces neighborhood passivity as an assumed sufficient criterion for the jump-activity conjecture and numerically observes its preservation on tested seven-spin systems. It neither states the present two-spin threshold nor a counterexample. The independent published description of conventional Glauber dynamics by Fukushima-Kimura et al. (arXiv:2007.11287, Eq. 1.4) uses the same single-spin transition rule, but studies mixing and a different parallel-update chain; it does not present an implication yielding this local sign classification. Searches for the paper, aliases, occupation inversion, and local passivity did not identify a covering mathematical record. Related general Markov-order theory could contain implicit coverage not uncovered by these checks, so publication priority is qualified. Exact match/semantic search absence alone is not considered proof of novelty.

## Mathematical value: PASS

This is a motivated boundary for a specific hypothesized mechanism in a published annealing-performance argument. It supplies a necessary-and-sufficient criterion throughout a complete two-spin parameter family, demonstrates failure on a nonempty open ferromagnetic set for *every* nonzero cooling increment, and establishes two spins as the minimal witness. Those structural facts identify precisely when a route to an activity bound is inapplicable, while not claiming to refute the activity bound itself. The result is not a bare numerical sign check or an unmotivated parameter slice: it tests the smallest Ising graph that admits a nontrivial interaction and matches the source's exact update/functional.

## Closest literature and limits

The source's Section IV.2 is the direct comparator. Broader finite-state time-inhomogeneous Markov and order-inversion theory was not exhausted; it could subsume some claims. The demonstrated failure concerns local neighborhood passivity after one temperature change and says nothing by itself about a violation of the separate \(\mathcal A^{\mathrm D}\le1/2\) conjecture. For the exact negative-passivity witness, direct arithmetic gives next-step activity \(2139045589/5553358890<1/2\).

Self-review: passed. Independent audit: not yet performed.
