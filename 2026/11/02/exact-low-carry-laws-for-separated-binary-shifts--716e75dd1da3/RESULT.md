# Exact low-carry laws for separated binary shifts

## Finding
For every integer \(h\ge1\), choose nonnegative integers
\[0\le e_1<e_2<\cdots<e_h,\qquad e_{i+1}-e_i\ge h+1\quad(1\le i<h),\]
and put \(t=\sum_{i=1}^h2^{e_i}\). Let \(K_t(n)\) count all binary carry operations in the ordinary addition \(n+t\). For every integer \(j\) with \(0\le j\le h\), the natural density
\[d_{t,j}=\lim_{N\to\infty}\frac1N\#\{0\le n<N:K_t(n)=j\}\]
exists and is independent of the positions of the nonzero binary digits:
\[\boxed{d_{t,j}=\frac{\binom{h+j-1}{j}}{2^{h+j}}.}\]
Consequently, writing \(s_2(n)\) for the number of ones in the binary expansion,
\[\boxed{\lim_{N\to\infty}\frac1N\#\{0\le n<N:s_2(n+t)\ge s_2(n)\}
=\frac12+\frac12\frac{\binom{2h}{h}}{4^h}.}\]
The positive bias is asymptotic to \(1/(2\sqrt{\pi h})\) as \(h\to\infty\).

## Assumptions and scope
All binary additions are between nonnegative integers. A carry from position \(r\) to \(r+1\) counts as one operation, even if subsequently propagated farther. The weight \(h\) is fixed when the natural density in \(n\) is formed. Digit positions may depend on \(h\) and need not be equally spaced; the stated lower bound applies to every adjacent gap. The formula concerns the first \(h+1\) values of the carry-count distribution, not the whole distribution above \(h\).

## Proof
**(1) Carries and binary digit sums.** In any binary addition, each carry replaces two units in one column by one unit in the next, decreasing the total count of ones by one. Therefore
\[s_2(n+t)-s_2(n)=h-K_t(n).\]
It suffices to compute the probabilities \(\Pr(K_t(n)=j)\) for \(0\le j\le h\).

**(2) Passage to independent bits.** For every fixed \(t\) and finite number of positions, the corresponding lower bits of \(n\), as \(n\) ranges over nonnegative integers, have limiting joint law of independent fair bits. Let \(B_r\) denote these Bernoulli bits, and extend the model to all \(r\ge0\). Every addition with fixed \(t\) terminates its carries almost surely: beyond the highest nonzero digit of \(t\), continued carrying requires an infinite sequence of ones, an event of probability zero. For a fixed bound \(j\), the event of exactly \(j\) carries is determined by a finite prefix except on events of arbitrarily small probability; indeed after any sufficiently high fixed position, a surviving carry has probability at most a corresponding negative power of two. Thus its probability is the asserted natural density. Equivalently, this follows from cylinder-set approximation in the binary product measure.

**(3) Separate run lengths.** At each position \(e_i\) consider the independent hypothetical run length \(L_i\): the number of consecutive \(1\)-bits \(B_{e_i},B_{e_i+1},\ldots\) before the first \(0\)-bit. For \(0\le \ell\le h\), the event \(L_i=\ell\) requires \(\ell\) ones followed by one zero and has probability \(2^{-(\ell+1)}\). Because adjacent positions \(e_i\) are at least \(h+1\) apart, on every event in which each \(L_i\le h\), the bits queried for the events \(L_i=\ell_i\) are disjoint between different \(i\). Hence for any tuple \(\ell_1,\ldots,\ell_h\) of nonnegative integers with \(\sum_i\ell_i\le h\), its joint probability is
\[\prod_{i=1}^{h}2^{-(\ell_i+1)}=2^{-(h+\sum_i\ell_i)}.\]
On the same event, each carry chain stops before the next nonzero digit of \(t\), so the chains do not interact and \(K_t=\sum_i L_i\). Conversely, if \(K_t\le h\), no carry chain from a nonzero digit can reach the next such digit: reaching one at distance at least \(h+1\) requires at least \(h+1\) carry operations. Therefore \(K_t=j\le h\) is equivalent to the disjoint union of the events \(L_1=\ell_1,\ldots,L_h=\ell_h\) with sum \(j\).

**(4) Exact profile.** There are \(\binom{h+j-1}{j}\) weak compositions of \(j\) into \(h\) parts. Summing the equal probabilities from (3) gives
\[\Pr(K_t=j)=2^{-(h+j)}\binom{h+j-1}{j}\quad(0\le j\le h).\]
The carry identity in (1) shows that the desired digit-sum density is \(\Pr(K_t\le h)\). The negative-binomial/binomial-tail identity gives
\[\sum_{j=0}^{h}\binom{h+j-1}{j}2^{-(h+j)}
=2^{-2h}\sum_{r=h}^{2h}\binom{2h}{r}
=\frac12+\frac{\binom{2h}{h}}{2^{2h+1}}.\]
The middle expression describes the probability of at least \(h\) successes among \(2h\) independent fair coin flips, obtained by counting the time of the \(h\)-th success. Symmetry of the binomial distribution establishes the last equality. Finally \(\binom{2h}{h}\sim4^h/\sqrt{\pi h}\) by Stirling's formula, yielding the claimed asymptotic.

## Verification
Run \(`python3 verify.py`\) in a directory containing the supplied standalone verifier. It uses exact rational dynamic programming on the binary carry automaton, checks \(28\) separated-shift patterns with weights \(1\) through \(7\), checks all \(140\) low-carry probabilities, and independently compares small cases with direct dyadic enumeration. Its expected output begins `VERIFY_OK`. This finite check is corroboration; steps (1)–(4) give the infinite proof.

For a boundary check, the shifts \(t=5\) and \(t=9\) both have weight \(h=2\), but the former gap is only \(2\) and its digit-sum nondecrease density is \(5/8\), while the latter gap is \(3\) and its density is \(11/16\). Thus the spacing hypothesis is mathematically substantive.

## Relationship to prior work
Spiegelhofer and Wallner provide the general digit-sum-difference distribution recurrence and establish estimates in terms of the number of blocks of ones. Cheng's 2026 first-exit work establishes a universal positive bias, and Cheng's subsequent fixed-Hamming-weight work studies the asymptotic *minimum* bias over all shifts of given weight. The present claim concerns a distinct explicit *position-independent exact profile* for the first \(h+1\) carry values, with a different order of bias, \(h^{-1/2}\), in widely separated shifts. Its Kummer-theorem equivalent gives exact probabilities for low values of the \(2\)-adic valuation of \(\binom{n+t}{t}\).

The earlier general recurrence permits numerical calculation for any particular \(t\); the uniform sparse-shift formula and its spacing mechanism are the comparison target, not a claim that such general recurrences are new. An explicit identical special-family formula could exist in unindexed or uninspected portions of the recent preprints; independent priority assessment is therefore warranted.

## Limitations
No assertion is made for the carry probabilities above \(h\), for general patterns with smaller gaps, or that the displayed family minimizes or maximizes the bias at fixed weight. The bound on adjacent gaps is sufficient, not asserted necessary for every individual shift. The proof and verifier do not constitute an independent audit of priority or the scientific review.

## References
1. L. Spiegelhofer and M. Wallner, *The binary digits of n+t*, arXiv:2005.07167 (first publicly posted 2020-05-14), especially the introduction and distribution recurrences.
2. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398 (first publicly posted 2026-06-22).
3. K. Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899 (first publicly posted 2026-08-26).
4. E. E. Kummer, theorem relating prime-adic binomial valuation and carries (classical equivalence used only for context).
