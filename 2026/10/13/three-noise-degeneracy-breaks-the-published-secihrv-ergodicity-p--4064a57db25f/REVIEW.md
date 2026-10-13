# Self-review

## Correctness
PASS. System (4) has only three diffusion columns, and the fifth and sixth coordinates have zero diffusion in every column. Thus the covariance has exact kernel vectors \(e_5,e_6\), making the paper's stated uniform-ellipticity condition impossible. Eqs. (40)–(42) omit \(x_5\), so the claimed Lyapunov function is zero on the nontrivial ray \(x^*+t e_5\); Eq. (50) additionally omits \(x_3\) and \(x_5\), making its nonempty level set unbounded. These are direct algebraic consequences of the displayed formulas and are replayed by the bundled exact checker.

## Originality
PASS. Exact-title, DOI, theorem-number, uniform-ellipticity, rank-deficiency, and Lyapunov-coercivity searches found no published correction or source-specific diagnosis. General degenerate-diffusion epidemic papers explain that uniform ellipticity fails and use different Markov-semigroup methods, but they do not imply the source-specific covariance kernel, noncoercive Lyapunov function, or unbounded Eq. (50) level set.

## Value
PASS. Theorem 4.2 is the article's principal persistence/ergodicity statement. The identified obstructions occur exactly at the step intended to justify a unique stationary distribution, and they distinguish a nondegenerate theorem template from a genuinely degenerate seven-dimensional model. This is mathematically substantive because a valid repair would require new structural hypotheses or a different ergodic method, not a cosmetic notation change.

## Closest literature and limitations
Cao et al. (2019), DOI 10.1038/s41598-019-47131-6, is the closest methodological comparator: it explicitly recognizes that a degenerate epidemic diffusion does not satisfy uniform ellipticity and switches to Markov-semigroup theory. Dieu et al. (2016), DOI 10.1137/15M1043315, similarly establishes ergodicity for a degenerate stochastic SIR model with a dedicated analysis. Neither covers the 2026 SECIHRV formulas. The present result does not claim that Theorem 4.2 is false, only that its printed proof does not establish the conclusion.

Self-review: passed. Independent audit: not yet performed.
