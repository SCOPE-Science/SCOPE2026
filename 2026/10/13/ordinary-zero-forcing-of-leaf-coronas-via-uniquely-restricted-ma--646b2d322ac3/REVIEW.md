# Scientific review of leaf-corona zero forcing

## Correctness (PASS)

The reduction preserves every original vertex's blue/white status after the initial private-leaf forces. A nondonor root cannot force an originally empty root while its own private leaf remains white, and may force its own leaf only after all its original neighbors have become blue. Thus every originally empty root must be reached by a distinct private-leaf donor. Such donor forces are ordered by a directed acyclic dependence relation, equivalent to a uniquely restricted matching saturating all empty-pair vertices. The reverse direction is a legal chronology. The generating formula assigns independent weight \(x(1+x)\) to each leaf-donor pair and \(x\) to a root-only pair; the complete-clique formula follows from the impossibility of starting when at least two pairs are empty. The inclusion-minimal classification follows by checking removal of every possible selected vertex. A separate direct simulator checked 500,260 initial sets, including all simple base graphs of order at most four. The proof handles all finite graph orders, including isolated vertices; computational checks alone would not.

## Originality (PASS, subject to residual risks)

The full 2018 founding zero-forcing-polynomial preprint covers general coefficient theory and several basic graph families, but not this leaf-corona cut formula. Brimkov--Carlson (2022) discuss exponentially many minimal zero forcing sets for whiskered cliques but do not give the full polynomial or complete classification; moreover, their exhibited mixed sets include sets that are not inclusion-minimal, as the explicit four-clique counterexample demonstrates. Javaid et al. (2016) treat larger attached corona factors and principally the scalar minimum. Earlier constrained-matching theory is acknowledged and could shorten the general structural argument, so the work does not assert novelty of uniquely restricted matchings themselves. Searches for weighted zero forcing polynomials of one-leaf coronas did not locate an equivalent theorem. The 2014 constrained-matching paper was not available in complete text during comparison, leaving a nonzero risk of antecedent structural coverage.

## Value (PASS)

The structural equivalence supplies a universally exact weighted enumerator of zero forcing sets in an operation—adjoining private leaves—that changes the forcing constraints in a nontrivial way. The clique specialization computes all coefficients and, beyond minimum size, separates one inclusion-minimal family of size \(n\) from exponentially many minimum sets of size \(n-1\). It also furnishes an explicit counterexample to the inclusion-minimal claim of a closely relevant published construction. These are natural invariants and a motivated boundary correction rather than an arbitrary single numerical table. This is an exact enumerative result, not a polynomial-time solution to arbitrary graph zero forcing.

## Closest literature and limitations

The principal comparisons are Boyer et al. (2018, arXiv:1801.08910), Brimkov and Carlson (2022, arXiv:2204.01810, Proposition 1), Javaid et al. (2016, arXiv:1607.04071), and Tréfois and Delvenne (2014, arXiv:1405.6222). General constrained-matching reductions and unindexed equivalent formulas are residual originality risks; the 2014 full text was unavailable. The exact cut sum need not have polynomial running time. Finite exhaustive computations are supporting checks only.

Self-review: passed. Independent audit: not yet performed.
