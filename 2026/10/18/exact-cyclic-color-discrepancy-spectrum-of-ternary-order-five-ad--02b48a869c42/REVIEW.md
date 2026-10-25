# Independent mathematical audit

## correctness

PASS

The assigned RESULT defines a length-48 cyclic word whose 48 proper ternary length-five factors each occur once, modulo rotation only. The 24-vertex/48-edge Eulerian model is bijective; the factor 01010 occurs exactly once and fixes a unique root. For each color pair, the range of the prefix-balance path equals the maximum circular interval imbalance because total balance is zero. The inspected verify_dfs.cpp exhausts edge-simple rooted walks; verify_pairings.cpp enumerates all 2^24 local incoming/outgoing bijections and accepts exactly the single 48-edge orbit; verify_witnesses.py checks every factor and circular interval of three witnesses. The two independent histograms agree at 23,700, 420,924, and 341,808, summing to the known 786,432 total. These are exhaustive finite proofs under the stated bijections, not samples.

## originality

PASS

The claim is the exact discrepancy-class histogram of ternary order-five adjacency-hopping/Kautz cycles, not the known total number of cycles. The full Chen–Liang–Wu PDF was inspected at its definition and Theorem 3: it defines the same restricted object and gives the total 786,432, but no discrepancy classes. The full Chen–Sima–Milenkovic PDF was inspected at the Kautz definitions and Section VI: it studies orthogonality of collections, not within-cycle color imbalance. Resultary returned unrelated nearest hits for the exact-histogram query. The unrestricted discrepancy literature is a meaningful related family but its factor universe includes adjacent repetitions and its lengths differ. Best-of-knowledge novelty passes; unindexed equivalent tables remain possible.

## value

PASS

Color-count discrepancy is a natural optimization/quality statistic for non-repetitive cyclic coding. Order five is the first order in this family where cycle-level discrepancy varies; the complete distribution separates optimal, intermediate, and worst classes rather than restating the known total. The result is a precise, self-contained finite design census with practical selection value and explicit scope boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
