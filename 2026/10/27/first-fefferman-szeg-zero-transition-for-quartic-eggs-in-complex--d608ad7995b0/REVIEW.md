# Mathematical review: quartic-egg Fefferman–Szegő kernel zeros

## Correctness — PASS

The precise setting is the Fefferman boundary measure on \(E_n=\{\|z\|^2+|w|^4<1\}\) in the complete integer range \(2\le n\le11\). The actual monomial norm is reconstructed using the coarea and beta-integral formula, and agrees with Pendyala's full text (Proposition 2.1 and Lemma 3.1). Every open-disk auxiliary argument occurs for two interior points, with all remaining kernel factors nonvanishing. The degree \(n-1\) polynomial follows by finite differences, and its Cayley transform maps exactly to a half-plane root count. For all ten integers, exact rational Hurwitz determinants and an independently computed fraction-based Routh array give zero roots for \(2\le n\le10\) and exactly two for \(n=11\). Alternating coefficients and the positive generating series exclude real critical roots, yielding a simple conjugate pair. The attached standard-library checker replays these calculations. No infinite-dimensional conclusion rests on decimal root approximations.

## Originality — PASS, subject to historical-priority limits

The closest source is Pendyala, arXiv:2607.04100v1 (2026-07-05), full-text inspected in Sections 2–4 and 6–7. Its main new computation is exactly the general Fefferman–Szegő rational kernel that this theorem starts from; its proved rigidity and boundary results do not state the new first-dimension zero-count classification. Earlier Bhatnagar–Fan work treats a two-dimensional metric. Kamimoto (1998) treats egg-domain Bergman and a different-surface-measure Szegő kernel, and Zhang–Yin (2009) treats ellipsoid Bergman zeros. Those conclusions do not imply the statement about Fefferman–Szegő zeros. Targeted kernel-identity, Lu Qi-Keng, Hurwitz, quartic-egg, and published-record searches found no matching or dominating result. The inaccessible full Bhatnagar–Fan article and earlier unindexed literature remain priority risks; search absence is not proof of worldwide novelty.

## Value — PASS

The first dimension in which an important naturally normalized Szegő kernel acquires off-diagonal zeros is a structural invariant, not a generic coefficient evaluation. For the simplest quartic egg family the threshold is surprisingly delayed until dimension \(11\), and the exact root count gives distinct geometric zero fibers. This establishes a meaningful finite all-dimensions-up-to-onset classification and complements, rather than repeats, known diagonal-metric rigidity. It does not classify dimensions \(n\ge12\) or other egg exponents.

## Limits of the assessment

The rational-generating-function formula is already published; only the dimension threshold, exact zero count, and nonreal conjugate nature are under originality consideration. General historical priority and correctness have not been independently verified.

Self-review: passed. Independent audit: not yet performed.
