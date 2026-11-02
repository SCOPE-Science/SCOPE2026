# Mathematical review: cyclic/impartial Condorcet contamination

## Correctness — PASS

The exact law conditions on zero, one, two or three independently contaminated ballots. With zero impartial ballots, the cyclic-winner event is exactly a collision of at least two rotations, of probability \((3n-2)/n^2\). With exactly one impartial ballot, any pair of distinct cyclic rotations partitions the alternatives into two ordered blocks; only their two first alternatives can win, with disjoint probabilities \(1/(j+1)\) and \(1/(n-j+1)\). This gives the exact harmonic coefficient \((2H_n-1)/n\). With two impartial ballots, relabeling invariance makes the third ballot irrelevant, so the event probability is exactly the impartial-culture probability \(Q_n\). The independent finite formula for \(Q_n\) is the count of three pairwise-disjoint upper preference sets. These facts prove the mixture formula for all \(n\ge3\) and all \(\varepsilon\in[0,1]\); no finite enumeration is used as an all-size proof. The asymptotic cutoff follows from the cited, established \(Q_n\sim\pi^{3/2}/(2\sqrt n)\), plus \(B_n=O(\log n/n)\).

The standalone exact-rational checker independently enumerates the three stratum probabilities through six alternatives, directly enumerates all weighted triple-ballot profiles through four alternatives at four contamination weights, checks the independent combinatorial formula for \(Q_n\), and checks strict initial slope for the first 98 nondegenerate sizes. It passed. Risk: the source theorem supplying the \(Q_n\) asymptotic is relied on rather than independently reproved; that dependence is explicit.

## Originality — PASS, qualified

Lisa Sauermann's *On the probability of a Condorcet winner among a large number of alternatives* (arXiv:2203.13713, 2022), Theorems 1–2 and Proposition 9, already proves the full impartial-culture asymptotic and the exact cyclic extremizer. Those endpoint facts are not claimed as new. Its relevant full-text statements and proof were compared: it does not give the mixed two-cyclic/one-impartial probability, its harmonic coefficient, or the critical \(n^{-1/4}\) perturbation scale. The new formula is not obtained by substituting a parameter into the endpoint equations, because those equations leave the mixed-ballot stratum undetermined.

Pittel's *On likelihood of a Condorcet winner for uniformly random and independent voter preferences* (arXiv:2506.20613, 2025) was also examined; it studies impartial culture with a growing, very large electorate, not a fixed three-voter mixture. May (1971) supplies the earlier three-voter impartial-culture asymptotic, while Garman and Kamien (1968) discuss arbitrary cultures and general finite enumeration; these are appropriately credited. A broad finite-probability summation applicable to arbitrary cultures does not by itself state or imply the exact harmonic simplification and sharp variable-\(n\) contamination limit without further analysis. Published finite-size majority-tournament tables can reproduce isolated values of \(Q_n\) without implying this law for all \(n\).

Residual risk: full publisher texts of the older 1968 and 1971 articles were not available for complete comparison, and literature searches cannot establish absolute novelty. No independent historical-priority certification is claimed.

## Value — PASS

The motivating extremizer achieves a rare Condorcet winner with probability of order \(1/n\) despite the standard impartial-culture \(n^{-1/2}\) rate. The exact intermediate harmonic probability exposes a structurally unexpected disparity: one independently impartial ballot has a logarithmic correction but does not change the leading scale, whereas two impartial ballots control the sharp fourth-root crossover. This determines the susceptibility of a specific natural extremal culture to whole-ranking contamination, including full-support perturbations, rather than merely evaluating an arbitrary finite probability. The result is narrow but motivated and self-contained when combined with the explicitly cited benchmark asymptotic.

## Limitations and closest literature

All statements require exactly three iid voters, strict rankings, cyclic-rotation baseline culture, and whole-ranking impartial contamination. The theorem neither classifies near-minimizing cultures nor addresses more voters or other perturbations. It is not a universal stability theorem. Principal literature: Sauermann (2022), May (1971), Pittel (2025), and Garman–Kamien (1968), with identifiers in RESULT.md. Independent validation is not performed.

Self-review: passed. Independent audit: not yet performed.
