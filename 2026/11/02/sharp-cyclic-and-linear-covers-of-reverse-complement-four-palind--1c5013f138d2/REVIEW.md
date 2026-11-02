# Scientific review: reverse-complement four-palindrome covers

## Correctness — PASS

The theorem quantifies over every even alphabet size \(q\ge2\) and every fixed-point-free involution. The exact suffix-prefix calculation yields \(q(q-1)/2\) ordinary pairs with reciprocal overlap length two and \(q/2\) special pairs with reciprocal overlap length three; every transition leaving its pair has cost at least three. A circular target tour must leave all pairs, forcing the bound \((5q^2-q)/2\). A linear target path must leave all but its terminal pair, giving one more symbol. The constructive Euler multigraph is balanced and connected on its support, contains every paired target exactly once, and realizes all inter-pair overlaps in one symbol. This supplies a complete proof, independent of finite experiments. `verify.py` reproduces the explicit constructions through \(q=30\) and exact Hamiltonian minimization for \(q=2,4\). Boundary cases include \(q=2\), empty nonisolated complementary vertices, circular wraparound and the linear terminal factor.

## Originality — PASS, with residual literature risk

The 2018 Gabric–Sawada universal-cycle concatenation study develops exact-once constructions for other factor languages, but does not derive the all-even-alphabet reverse-complement-palindrome *shortest cover* cost. The 2019 Chen–Kitaev–Sun paper treats probabilities of exact-once universal cycles after deleting factors from a full language; its main theorems neither assert nor imply this complement-specific minimum. The 2026 Yamano–Shibuya work analyzes general reverse-complement superstring approximation, and does not state an exact optimal length for these \(q^2\) self-reverse-complementary factors. A separate ordinary-palindrome theorem concerns \(abba\), rather than \(ab\bar b\bar a\), and its numerical optimum is different. Searches for Watson–Crick palindrome coverings, involutive universal cycles, exact target-length superstrings and database near equivalents yielded no decisive covering claim. Originality is assessed relative to inspected and available sources, not claimed as uniqueness across all published mathematics.

## Mathematical value — PASS

The targets are precisely all possible length-four Watson–Crick palindromic DNA motifs at \(q=4\). The exact \(38\)-symbol cyclic and \(39\)-symbol linear minima, plus the all-even-\(q\) formulas, are natural optimal control lengths for full motif coverage. The partner-pair decomposition establishes why the exact bound exceeds the raw \(q^2\) factor count, and gives a reproducible quadratic-size constructive algorithm. This is a complete motivated family, not an arbitrary finite slice or a restatement of the classical de Bruijn word count.

## Closest sources, scope and remaining risks

- Gabric and Sawada, arXiv:1803.09009 (2018-03-23): general universal-cycle concatenations, but no complement-paired four-gram shortest-cover theorem in inspected sections.
- Chen, Kitaev and Sun, arXiv:1908.01116 (2019-08-03): exact-once u-cycle existence/probability, not minimum-length all-target coverage with non-target fillers.
- Yamano and Shibuya, DOI:10.4230/LIPIcs.CPM.2026.15 (2026): arbitrary-instance reverse-complement superstring approximation, not the present exact special-instance optimum.
- A preexisting ordinary-palindrome covering theorem has different required targets and the even-alphabet circular value \((5q^2+2q)/2\); it does not subsume the result here.

Residual risk: a mathematically equivalent treatment could appear under earlier involutive-string, anti-palindromic word, or directed rural-postman terminology. Other lengths and involutions with fixed points are not covered. Independent scientific checking, including searches outside currently indexed sources, is still warranted.

Self-review: passed. Independent audit: not yet performed.
