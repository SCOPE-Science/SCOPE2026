# Self-review

## Correctness — PASS

The claimed formula is reconstructed from the exact three-step local criterion: a nonfixed period-three trajectory on a connected graph forces all vertices to advance, equivalent to each phase having a successor-phase neighbor. Directing these successor edges proves that any chosen arrow must eventually reach a simple cycle divisible by three. On a cactus with a unique such cycle, outgoing support cannot lie in a child block because it would create a second resonant directed cycle. This forces the six core phases, unique bridge phases, and independent rooted cycle extensions. The latter count is proved from exactly two admissible families of edge-increment words and explicit modulo-three closure conditions. Ten exact graph enumerations and an independently derived edge-increment transfer agree with the theorem, but the proof does not depend on finite experimental extrapolation.

## Originality — PASS with residual risk

The closely relevant 2016 paper of Gravner, Lyu, and Sivakoff (arXiv:1610.07320v1, Theorem 3 and Section 4) treats long-run synchronization and activity through winding integrals, not the count of configurations satisfying the immediate successor-neighbor condition on singly resonant cactus block trees. Durrett and Griffeath (1993, arXiv:patt-sol/9303002) treat excitable automata and large-lattice periodic patterns, not this block-product enumeration. Additional targeted literature searches and semantic records searches found no dominating or equivalent result. Accessible local historical claims include a general cactus *asymptotic-rate* distribution and a triangular cactus *chain* census; the former concerns a different invariant, while the latter assumes multiple resonant triangle blocks (except its single-triangle base case). No equivalence implication was identified. Search incompleteness and possible independently known cyclic-neighbor-coloring formulas remain priority risks.

## Mathematical value — PASS

The problem concerns a natural, completely specified recurrent-point invariant for the classical Greenberg–Hastings model. The answer works for every finite cactus with one resonant cycle, not merely a bounded family or arbitrary parameter slice. It gives the surprising independence of the positions of bridges, nesting of nonresonant cycles, and the size of the unique resonant cycle, while the other lengths contribute explicit staircase factors. It sharply separates activity produced by a cycle from time-zero periodicity and gives exact numbers of temporally distinct orbits. This structural factorization is relevant to enumerating recurrent configurations on sparse excitable networks; no downstream theorem beyond this classification is assumed.

## Closest literature and scientific limits

The finite-graph winding theorem in arXiv:1610.07320v1 is the strongest directly inspected primary antecedent. It does not enumerate initial period-three states, although its methods motivate studying cycle blocks. The 1993 lattice study supplies the underlying excitable-media model, not the count. The product theorem does not classify more than one resonant cycle or other temporal periods. All verification programs use the exact declared update rule, and the documented finite tests are secondary to the proof. The result is new relative to the cited and accessible indexed material to the best of the present comparison; no independent historical priority judgment is asserted.

Self-review: passed. Independent audit: not yet performed.
