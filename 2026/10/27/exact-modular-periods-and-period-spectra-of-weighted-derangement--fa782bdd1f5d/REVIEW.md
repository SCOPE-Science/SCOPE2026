# Mathematical review: modular periods of derangement polynomials

## Correctness — PASS
The factorial-expansion definition yields the recurrence \(R_n(u)=nR_{n-1}(u)+u^n\). Direct divisibility of all but the final term in \(R_m(u)\) and induction give \(R_{n+m}(u)\equiv u^mR_n(u)\pmod m\). Every period \(P\) forces two low-index recurrence relations; eliminating \(P\) shows \(u(1-u^P)\equiv0\pmod m\), so unitness forces both \(\operatorname{ord}_m(u)\mid P\) and \(m\mid P\). The constructed upper period meets this sharp lower bound. Finite abelian group structure supplies precisely all divisor orders of the Carmichael exponent. This is a complete universal proof, not extrapolation from the verifier. The verifier independently tests 773 coprime parameter/modulus pairs, 49 period spectra, and 56 permutation sums.

## Originality — PASS, subject to residual literature risk
Sun--Wu--Zhuang (2010, arXiv:1009.2929v1) gives the same polynomial recurrence and a prime-modulus congruence for ordinary derangements (Corollary 3.2); neither is claimed as new. OEIS A000166 explicitly contains a 2017 comment giving an upper period for ordinary derangements. Those results do not state the sharp least-period law for all unit-weight evaluations over arbitrary composite moduli or the spectrum of possible least periods. Targeted exact-form, alias, and broader published-index and literature searches did not locate a theorem implying both statements. This is not a claim of exhaustive novelty: the same conclusion may exist as an unrecorded easy corollary or in a general theorem on factorial-polynomial sequences.

## Mathematical value — PASS
The invariant is the *least* period of a classical enumerative sequence reduced modulo arbitrary composite integers, not merely a known period. The theorem classifies all unit weights and all moduli at once and then completely describes which distinct periods are realizable at each fixed modulus, with extrema and a divisor-counting formula. It sharpens the known derangement upper-period observation and connects permutation fixed-point statistics to multiplicative orders and the Carmichael exponent. It requires neither arbitrary numerical cutoffs nor selected parameters; it resolves a natural complete two-parameter classification. Its elementary proof and possible folklore status are explicit limitations, not a substitute for a mathematical motive.

## Closest literature and residual risk
The closest explicit same-object results are the 2010 arXiv article's polynomial recurrence and prime congruences, and the 2017 OEIS upper-period observation. The remaining risk is that a more general statement about factorial polynomials or polynomial recurrences already implies the classification. Nonunit weights are unclassified and are excluded from the assertion.

Self-review: passed. Independent audit: not yet performed.
