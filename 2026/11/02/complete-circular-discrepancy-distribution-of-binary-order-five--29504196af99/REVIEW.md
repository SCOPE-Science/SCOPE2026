# Scientific review: circular discrepancy of binary order-five de Bruijn cycles

## Correctness — PASS

The claimed population has an exhaustive shift-register parametrization by all \(2^{16}\) possible bijective feedback truth tables; a full orbit from the unique all-zero block corresponds bijectively to a cycle modulo rotation. Independently, Euler circuits of the four-bit de Bruijn graph enumerate the same objects. Both complete enumerations return exactly \(2048\) identical canonical words, and the independently implemented prefix-range and direct cyclic-substring discrepancy calculations agree on every word. The four class sizes add to \(2048\). The embedded standard-library checker reproduces the exact certificate and is not used to extrapolate beyond order five.

## Originality — PASS (qualified)

Cooper–Heitsch's 2009 preprint examines the lex-least cycle, not the population's cyclic-discrepancy distribution. Gabric–Sawada's 2020/2021 work examines several constructions and explicitly names the all-cycle discrepancy distribution as future research (Section 7, item 6). The 2024 Álvarez–Becher–Mereb–Pajor–Soto theorem already gives the general binary minimum \(n\); no novelty is claimed for that bound. The full multiplicity vector \((224,688,912,224)\) is a strictly more specific population statement than those results. Comparisons of the actual statements and searches for equivalent feedback-register, Eulerian and cyclic-discrepancy tables found no covering source, but unindexed historical enumerations remain a residual risk.

## Value — PASS

The invariant is the concrete local-balance property studied for pseudorandom and constructed de Bruijn sequences, and its full distribution was expressly proposed in prior research. The order-five case classifies the first \(2048\)-cycle population at a manageable yet substantive size, quantifies the prevalence of all balance classes, and verifies the proposed maximum at that order without claiming the all-order conjecture. This is not merely a single extremal witness or a recomputation of an established table.

## Limitations and closest literature

This is a finite order-five classification, not a general distribution theorem. The minimum value is known in all binary orders. The special-case maximum does not settle the Gabric–Sawada conjecture. References: Cooper–Heitsch (2009), https://arxiv.org/abs/0903.3753; Gabric–Sawada (2020), https://arxiv.org/abs/2005.01638, Section 7; Álvarez et al. (2024), https://arxiv.org/abs/2407.17367. The earliest publicly verified source underlying the discrepancy direction is the 2009 Cooper–Heitsch preprint, while later sources are scientific comparisons.

Self-review: passed. Independent audit: not yet performed.
