# Scientific review

## Correctness — PASS

Each binary word of weight three corresponds bijectively to three nondecreasing zero-before-one counts \((a,b,c)\) bounded by \(n-3\). The entire length-at-most-three scattered profile is an explicit function of \(S=a+b+c\), \(Q=\sum\binom{d}{2}\), and \(T=2a+b\); these are themselves measured components. Solving for the second triple reduces to a quadratic whose nontrivial root interchanges the successive zero gaps subject to divisibility by three and boundary conditions. Counting the uniquely oriented pairs gives the exact doubleton sum and rational generating function. The fourth-order pole and \(\binom n3\) denominator establish the limiting proportion. The companion independent subsequence DP checked every triple at lengths 3–30 and coefficient identities through 1000. No finite search is treated as the infinite proof.

## Originality — PASS, with defined source-access risk

The 2015 introduction and testing algorithms for \(k\)-binomial equivalence do not classify this particular sparse fiber. The 2020 full paper on binomial classes focuses on general properties, including global class-growth bounds and \(2\)-binomial classes; its concluding discussion explicitly identifies structural analysis for \(k\ge3\) as an avenue for further work. OEIS A258585 already supplies global counts and the specific length-seven collision, which are acknowledged as previously known; neither directly implies the all-length three-one collision involution, the exact doubleton generating function, or one-quarter limiting ambiguity. The 2019/2023 general \(k\)-deck study lists unrestricted counts and bounds. Its full paper was not accessible through the paths attempted, so an unpublished or unadvertised specialization remains a residual risk. General asymptotic results for unrestricted decks in 2026 are not weight-conditioned fiber classifications. Relevant database searches returned broad neighboring topics but no equivalent or dominating sparse-layer theorem. Search failure is not proof of uniqueness.

## Mathematical value — PASS

A length-three scattered-deck channel is a natural low-observation reconstruction model. The weight-three layer is the first sparse regime with a genuine collision; the theorem determines *all* its collisions and proves a sharp two-element maximum class size. The exact rational generating function provides an all-length count and the asymptotic result shows a substantial (one-quarter) ambiguity probability, rather than an isolated curiosity or a finite census. This conditional slice is motivated by sparse-marker reconstruction, not arbitrary numerical truncation. No unrestricted reconstruction claim is made.

## Closest literature and limitations

Freydenberger et al., *Testing k-binomial equivalence* (arXiv:1509.00622, 2015); Lejeune–Rigo–Rosenfeld, *On the binomial equivalence classes of finite words* (arXiv:2001.11732, 2020); OEIS A258585 (2015); Chrisnata et al., *On the number of distinct k-decks* (2019 and 2023 versions); Nilforoushan–Parvaresh (arXiv:2609.23106, 2026). The all-length proof is for binary weight three only. The close 2019/2023 paper's full text remains incompletely inspected. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
