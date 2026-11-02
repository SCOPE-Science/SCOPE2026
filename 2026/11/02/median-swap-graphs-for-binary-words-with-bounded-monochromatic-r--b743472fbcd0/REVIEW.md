# Scientific review: run-bounded binary-word swap graphs

## Correctness

PASS. The exact positional model proves that all and only run-avoiding words are feasible integer vectors satisfying bounds on adjacent and longer coordinate differences. Both meet and join preserve difference bounds. The genuinely nontrivial step is the acyclic dependency proof for a downward legal unit move: forward dependencies cross only maximal zero gaps, and tight backward dependencies can never cross one. Monotone paths to meets prove the exact adjacent-swap lower bound is attainable. The finite distributive-lattice structure and unique coordinatewise median follow. Symbol complementation covers the remaining nonexceptional parameters. Explicit boundary words show the exception is necessary. Exhaustive computational corroboration includes separate algorithms.

## Originality

PASS under the checked literature, with residual uncertainty. The following comparisons do not imply the new theorem: fixed-pattern binary-word generation (Bilotta–Pergola–Pinzani, 2011), sliding of independent sets on trees (Demaine et al., 2014), and structural token-sliding graphs (Avis–Hoang, 2022/23). Standard median/distributive-lattice statements alone do not establish that *physical adjacent swaps* implement the lattice covers of this simultaneously run-constrained system. Relevant older/current results and aliases were searched; unindexed or differently named bounded-gap lattice-path results may nevertheless exist.

## Value

PASS. The theorem resolves an all-parameter constrained sorting problem: for every pair of admissible fixed-composition words, the precise minimum number of legal swaps is given directly by the earth-mover formula. Its median/distributive structure supplies canonical three-way consensus configurations and makes constrained reconfiguration geodesically non-obstructive. The sharp two-two exception shows this is not a generic property of arbitrary forbidden runs. This is a structural characterization rather than a cosmetic enumeration or a finite table.

## Closest literature and limits

Relevant available primary-text sections listed in `RESULT.md` were inspected for objects, move rules and claimed consequences. The work does not solve the cyclic-word, larger-alphabet or arbitrary forbidden-language analogues. An equivalent general bounded-gap integer-height theorem or an unindexed application could subsume the result and remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
