# Review: explicit 2-adic obstructions for all twice-odd powers of the Thue–Morse series

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The proof is an exact \(2\)-adic argument with no asymptotic or numerical step.

The main congruence is reduced to the known exact valuation theorem for \(T(x)^{2^A}\), the elementary \(m=2\) recurrence, and binomial congruences below the dyadic boundary \(2^A\). The key coefficient lemma for \(T(x)^{2^Av}\) is stable under an odd power because the linear term has valuation \(A-\nu_2(i)\), while every product of two or more positive-degree terms has at least one additional factor of \(2\). This prevents hidden cancellation at the leading \(2\)-adic order.

The comparison between \(t_{2+2^Av}(k)\) and \(t_2(k)\) was checked at the exact endpoint needed by the odd-index recurrence. Below \(2^{A-1}-1\), every replacement error has two spare powers of \(2\); at the endpoint \(2^{A-1}-1\), every convolution summand has exactly order \(A\), and there are an odd number of them. This yields the nonzero correction \(2^{A+1}\) modulo \(2^{A+2}\) in the final boundary coefficient.

The remaining normalized coefficient sum is paired under \(k\leftrightarrow 2^A-k\). The only unpaired indices are \(0\) and \(2^{A-1}\). The mod-\(4\) binomial normalization has exactly one exceptional product factor, at \(j=2^{A-1}\), on the upper half; the \(m=2\) even coefficients satisfy \(t_2(2h)\equiv(-1)^h\pmod4\). These facts make every noncentral pair cancel modulo \(4\), leaving the claimed boundary congruence.

The comparator valuation
\[
\nu_2\binom{2^A(v+1)}{2^A-1}=A+\nu_2(v+1)
\]
follows directly from the binary digit-sum formula. The two odd classes modulo \(4\) force opposite inequalities, so equality cannot occur.

An exact-integer verification independently recomputed the relevant coefficients for 112 \((A,v)\) pairs with \(2\le A\le8\), \(1\le v\le31\) odd, and for all 127 odd \(u\) from \(3\) through \(255\). All checks passed. This computation is corroborative only; the proof is complete without it.

## Originality

**PASS, to the best of our knowledge.** Shen's arXiv:2609.16966v1 was inspected through the statements and proofs surrounding the power-of-two family, the \(m=6\) formula, and Conjecture 6.2. It explicitly leaves the general necessary-and-sufficient criterion open. For \(r=1\), the conjectural criterion reduces to the assertion that only \(u=1\) can have the exact binomial valuation at every index. The source proves the first excluded case \(u=3\) through its special \(m=6\) formula, but it does not give the arbitrary-\(u\) obstruction or the congruence at \(n=2^{\nu_2(u-1)+1}-1\).

The 2018 Gawron--Miska--Ulas paper was inspected in its section on positive integer powers and the exact power-of-two valuation theorem. It establishes the \(2^r\) family and related recurrences but does not state the twice-odd classification proved here. Ulas's 2019 paper was checked through its bibliographic record and available abstract; it concerns a general method for \(2\)-adic valuations of powers of integer-coefficient series and does not advertise this Thue--Morse boundary congruence.

Searches covered the exact and synonymous formulations “Thue--Morse \(t_{2u}\)”, “twice odd exponent”, “\(m=2u\)”, “exact binomial valuation”, the boundary index \(2^A-1\), and recent follow-up work on arXiv:2609.16966. No theorem implying the stated all-\(r=1\) obstruction was located.

No inaccessible source was identified whose title or available metadata specifically suggests the same result. The main residual risk is unindexed contemporaneous work because the motivating preprint was submitted in September 2026.

## Value

**PASS.** The result settles an entire infinite layer of a newly stated necessary-and-sufficient conjecture rather than checking additional isolated exponents. Every excluded exponent with exactly one factor of \(2\) receives a closed-form witness index, and the stronger congruence explains why the obstruction flips according to the odd parameter modulo \(4\). The proof also supplies a reusable dyadic-boundary method: an odd perturbation of a power-of-two exponent is controlled sharply enough to compare an entire convolution against the \(m=2\) base case.

The theorem is strictly stronger than the previously known \(m=6\) failure in this layer and is not a mechanically larger finite computation. It gives a uniform exact statement for infinitely many exponents.

## Limitations

The theorem settles only the \(r=1\) slice of Conjecture 6.2. It does not prove the sufficiency or necessity directions for general \(r\ge2\), and it does not address Conjecture 6.1 on automatic odd parts. For \(v\equiv1\pmod4\), the congruence yields the lower bound \(\nu_2(t_m(2^A-1))\ge A+2\), not a complete formula for that valuation. Originality remains to the best of our knowledge, with elevated residual uncertainty from the recency of the motivating preprint. No independent validation or formal proof-assistant verification has been performed.
