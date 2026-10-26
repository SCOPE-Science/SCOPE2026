# Scientific review: longest-unbordered-factor law for two-marker binary words

## Correctness — PASS

The proof exhausts contiguous factors by the number of ones. Its only nontrivial structural step proves that the two-one factor \(0^i1\,0^b1\) is unbordered exactly for \(i>b\), with the reversed criterion on the other side. This yields the complete piecewise formula for every nonnegative gap triple, including the sharp equality boundary. Disjoint gap summations prove the rational bivariate generating function; exact differentiation proves the first-moment series. The uniform-lattice-to-simplex limit and explicit polygon-area calculation establish the CDF and mean. The standalone checker verified direct border testing on 2024 words, all bidegrees to 48 of the generating function, the first-moment coefficients and large-length numerical asymptotic checks. These finite tests corroborate, but do not replace, the symbolic arguments.

## Originality — PASS, with residual priority uncertainty

The closest historical paper is Kucherov–Loptev–Starikovskaya (2015, arXiv:1504.07406), which proves general-alphabet expected-length bounds and an algorithm. The close later study by Sekizaki–Mieno (2025/2026, arXiv:2507.16285) proves a useful RLE-boundary lemma and algorithms; the RLE lemma is consistent with the structural proof here but does not state the closed gap formula or the bivariate and limiting distributions. Searches for longest/maximal unbordered factors, two-marker or weight-two binary words, exact distributions and generating functions did not locate an equivalent statement. Earlier work could contain an unindexed equivalent specialization; a search is not proof of global priority.

## Value — PASS

The longest-unbordered-factor statistic is a standard measure of avoidance of prefix-suffix repetition, connected with periodicity and string algorithms. For a natural fixed-composition source class, the theorem gives a sharp structural phase boundary, every finite-length coefficient via a rational bivariate generating function, and a nontrivial limiting CDF with exact mean \(20/27\). The asymptotic contrasts with known near-full-length behavior for unrestricted random strings. These are standalone structural and statistical facts, not merely an optimized implementation or one more numerical example.

## Scientific limitations

The results concern linear binary words with exactly two ones, not all words or all sparse alphabets. No independent mathematical verification has been carried out. The most substantive residual risk is prior publication under terminology not captured by the searches; none of the inspected sources was shown to imply the exact distribution without new analysis.

Self-review: passed. Independent audit: not yet performed.
