# Scientific review: sharp positivity frontier on Markov cycles

## Correctness — PASS

The proof fixes the column-generator convention, proves invertibility of the Padé denominator from its right-half-plane roots, and uses exact rational formulas for every coefficient of the two-, three- and four-state cyclic matrices. All denominators are positive on the claimed range. The only sign-changing four-state coefficient is proportional to the negative of a polynomial with exactly one positive root (Descartes' rule plus its endpoint signs). The group-inverse coefficients are verified algebraically from the cyclic shift relation and establish the large-step expansion in each fixed dimension via finite Fourier diagonalization. The asserted limits apply at fixed dimension; no infinite-dimensional uniform bound is claimed. The packaged verifier checks 118 finite exact identities and rational cases, but the general quantifiers are supported by the written proof rather than by finite experimentation.

## Originality — PASS with residual publication-priority risk

The most relevant 2024 source by Blanes, Kopylov and Seydaoğlu provides Padé/scaling-and-squaring algorithms and structure preservation, not an entrywise Markov positivity classification. Zappavigna et al. (2012) already demonstrate failure of positivity for a diagonal Padé map, especially an eight-dimensional nilpotent shift; they do not supply an exact four-cycle horizon or the large-step group-inverse sign profile. The inspected previously published eight-state pure-birth Markov result resolves a complementary *small-step* obstruction, not this *large-step* directed-cycle result. General absolute-monotonicity statements alone also do not imply the exact four-cycle formula. A 2026 Fokker–Planck rational-positivity paper is relevant but only its abstract was accessible; its stated criteria treat large-step limits strictly below one or negative, whereas the present map has limit one. Specialized prior treatments of cyclic rational Markov approximants remain possible.

## Value — PASS

Directed cycles are elementary conservative irreducible Markov models, and the two-stage fourth-order Gauss–Legendre step is a standard rational exponential approximation. The result resolves an exact and natural question: which smallest cycle loses positivity under large steps, and at what unique four-state threshold? The root-defined cutoff of about 6.13572 and the universal first-neighbor group-inverse sign law distinguish mass preservation, true-semigroup positivity, and numerical map positivity. The classification is more informative than merely computing one negative matrix entry, and gives a sufficient positivity check for four-cycle scaling-and-squaring. It is restricted to this precise method and generator family.

## Evidence and remaining limits

The four-state factorization and all-dimension group inverse are rederived in `RESULT.md` and reproduced in `artifacts/verify_cycle_pade.py`; `VERIFICATION.md` specifies exactly which finite checks ran. Primary material inspected: Blanes et al., arXiv:2404.12789v1 (HTML sections on Padé, scaling-and-squaring and preserved structure); Zappavigna et al. (2012), full PDF section on positivity counterexamples; previously published eight-state pure-birth published-finding corpus `RESULT.md` (complete theorem/proof). Itkin and Kazbek, arXiv:2608.22703, was compared at the accessible abstract level only; full-text fetch was unsuccessful, so this is explicitly not a whole-document noncoverage finding.

The theorem does not assert that a fixed numerical implementation remains nonnegative under floating point, that all larger directed cycles have a single positivity interval, or that internal Gauss–Legendre stages preserve positivity. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
