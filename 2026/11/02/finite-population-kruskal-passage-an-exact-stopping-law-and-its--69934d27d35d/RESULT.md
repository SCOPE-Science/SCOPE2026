# Finite-population Kruskal passage: an exact stopping law and its first-order bias

## Finding

Let \(m,n\ge1\), and shuffle uniformly all distinct arrangements of a deck containing exactly \(m\) copies of each integer label \(1,\ldots,n\). Define \(L=mn\), the starting position \(P_0=1\), and, whenever \(P_{r-1}\le L\), put
\[
P_r=P_{r-1}+C_{P_{r-1}}.
\]
Here \(C_p\) is the label at position \(p\). Define \(T_{m,n}=\min\{r\ge1:P_r>L\}\). For every integer \(0\le t\le L\),
\[
\boxed{\Pr(T_{m,n}>t)=\frac{\sum_{s=0}^{L-1}[x^tq^s]\prod_{j=1}^{n}(1+xq^j)^m}{\binom Lt}.}\tag{1}
\]
The full probability mass function is the difference of consecutive tails in (1). All coefficient extractions are from ordinary polynomials, so (1) is an exact finite formula.

For fixed \(m\), the law and mean converge as \(n\to\infty\) to the known continuous-uniform renewal crossing time \(N_m=\inf\{t\ge1:\sum_{i=1}^{t}U_i\ge m\}\), where the \(U_i\) are i.i.d. \(\mathrm{Unif}(0,1)\). Its tails are
\[
\Pr(N_m>t)=\frac1{t!}\sum_{j=0}^{\min\{t,m\}}(-1)^j\binom tj(m-j)_+^t\quad(t\ge1),\tag{2}
\]
with a zero-valued endpoint term understood by continuity; \(\Pr(N_m>0)=1\). Formula (2) is classical, not an originality claim.

For \(m=1\), each fixed positive integer \(t\) satisfies the sharper finite-deck expansion
\[
\boxed{\Pr(T_{1,n}>t)=\frac1{t!}-\frac{t(t^2-t+4)}{4t!\,n}+O_t(n^{-2}).}\tag{3}
\]
Moreover,
\[
\boxed{\mathbb ET_{1,n}=e-\frac{7e}{4n}+o(n^{-1}).}\tag{4}
\]
The correction \(7e/4\) separates the leading integer-threshold and no-replacement collision effects.

## Assumptions and scope

All positions are labelled and all distinct value sequences with the specified multiplicities have the same probability. The process reads the first surviving card, removes its labelled number of consecutive cards (or all remaining cards when fewer remain), and repeats. A removal is counted even when it exhausts the deck. The convention in (1) counts a tail after \(t\) removals. For \(t=0\), the tail is one; for \(t=L\), it is zero. The standard notation \([x^tq^s]\) extracts the coefficient of a monomial; \(a_+=\max\{a,0\}\). Formula (3) has \(t\) fixed as \(n\to\infty\), not uniform in growing \(t\).

## Proof

**1. Adaptive-deck exposure.** Suppose the labels already inspected along the jump path are \(v_1,\ldots,v_r\). The next visited position, if it exists, is a deterministic function of these labels and has never previously been inspected because all labels are positive and positions increase. Conditional on the inspected labels, the uninspected positions contain a uniformly random permutation of the remaining physical cards. Hence the next visited label is distributed as one draw without replacement from the remaining multiset. Inductively, the visited labels have the law of the successive draws \(V_1,V_2,\ldots\) in a uniform random ordering of all physical cards. The process terminates at the first \(t\) for which \(\sum_{i=1}^t V_i\ge L\).

**2. Exact finite distribution.** Conditional on a sample of length \(t\), its unordered collection of physical cards is a uniform \(t\)-subset of the \(L\) distinguishable cards. The subset has total value below \(L\) if and only if the process lasts longer than \(t\) removals. Taking \(k\) cards of label \(j\) contributes \(\binom{m}{k}x^kq^{jk}\); multiplication over all labels gives exactly the numerator in (1), and the denominator counts all \(t\)-subsets. This proves (1) and its probability-mass corollary.

**3. Uniform-renewal limit.** For each fixed \(t\), the joint law of \((V_1/n,\ldots,V_t/n)\) approaches that of independent \(\mathrm{Unif}(0,1)\) random variables, since the population has \(mn\) physical cards, draws are without replacement, and the empirical label distribution converges to uniform. The boundary \(\sum U_i=m\) has zero probability, so (1) tends to (2). To justify mean convergence, call labels at most \(n/2\) **low**. On the event \(\sum_{i=1}^t V_i<mn\), fewer than \(2m\) of the first \(t\) draws can exceed \(n/2\). Thus for \(t\ge2m\), at least \(t-2m\) draws are low. Any specified collection of \(r\) draws is low with probability at most \(2^{-r}\), by sampling without replacement from a population with at most half low cards. Therefore
\[
\Pr(T_{m,n}>t)\le\binom{t}{2m}2^{-(t-2m)},\qquad t\ge2m.\tag{5}
\]
The right-hand side is summable over \(t\), uniformly in \(n\) when \(m\) is fixed. Dominated convergence for \(\mathbb ET_{m,n}=\sum_{t\ge0}\Pr(T_{m,n}>t)\) proves the mean assertion. The Irwin--Hall inclusion-exclusion formula for the continuous sum supplies (2).

**4. First-order correction for one copy.** Fix \(t\ge2\). The number of ordered positive integer \(t\)-tuples with total at most \(n-1\), before requiring distinctness, is \(\binom{n-1}{t}\). For a prescribed pair of equal entries, the number is
\[
E_{n,t}=\sum_{a\ge1}\binom{n-2a-1}{t-2}=\frac{n^{t-1}}{2(t-1)!}+O_t(n^{t-2}),\tag{6}
\]
with binomial coefficients zero outside their natural range. Intersections of two *distinct* pair-equality conditions remove at least two independent degrees of freedom; they contribute at most \(O_t(n^{t-2})\) in total. Therefore the count of ordered, pairwise distinct positive tuples with sum below \(n\) is
\[
\binom{n-1}{t}-\binom t2 E_{n,t}+O_t(n^{t-2}).\tag{7}
\]
There are \((n)_t=n(n-1)\cdots(n-t+1)\) ordered distinct samples. Since
\[
\frac{\binom{n-1}{t}}{(n)_t}=\frac{n-t}{nt!}
\]
exactly, division of (7) by \((n)_t\) yields (3). For \(t=1\), the tail equals \((n-1)/n\), also agreeing with (3).

**5. Uniform interchange for the expectation correction.** Put \(d_{n,t}=1/t!-\Pr(T_{1,n}>t)\ge0\) for \(t\ge1\) (take the second probability as zero when \(t\ge n\)). For \(t<n\), the distinct-tuple count is at most \(\binom{n-1}{t}\), giving the displayed inequality. If \(n\ge2t^2\), the denominator satisfies \((n)_t\ge3n^t/4\) by the elementary product/union bound. With (6) bounded above by \(n^{t-1}/(2(t-1)!)\), a union bound over the \(\binom t2\) possible collisions yields
\[
nd_{n,t}\le\frac{t}{t!}+\frac{t^2(t-1)}{3t!}.
\]
If \(n<2t^2\), simply use \(0\le nd_{n,t}\le n/t!\le2t^2/t!\). Thus \(nd_{n,t}\) is dominated by a single summable sequence in \(t\), independently of \(n\). Termwise use of (3) is justified and gives
\[
\begin{aligned}
\lim_{n\to\infty}n\left(e-\mathbb ET_{1,n}\right)
&=\sum_{t\ge1}\frac{t(t^2-t+4)}{4t!}\\
&=\frac{(5-2+4)e}{4}=\frac{7e}{4}.
\end{aligned}
\]
This proves (4), with only the classical identity \(\sum_{t\ge0}1/t!=e\) used for the limiting mean.

## Verification

The accompanying standalone `verify.py` enumerates every distinct shuffled multiset deck in 16 small parameter cases, totalling 493231 decks, and directly executes each elimination path. It independently computes every tail from the coefficient polynomial, compares the distributions, checks their boundary and monotonicity conditions, and tests the finite-population mean bias at deck sizes 40, 80, and 160. Its successful output is `VERIFY_OK multiset_parameter_cases=16 direct_decks=493231 finite_n_bias_checked=40,80,160`. Exhaustive finite checks do not replace the general counting, limit, or asymptotic proofs.

## Relationship to prior work

Corregidor's 2026 analysis poses this same repeated-card deck process and identifies sharp extremal **worst-case** iteration bounds for arbitrary deck arrangements. Formula (1) instead treats a **uniform random arrangement**, giving its whole distribution. Lagarias, Rains, and Vanderbei studied collision/coupling probabilities for two Kruskal-count paths under independent card-label models; their text explicitly distinguishes uniform permutations of fixed decks from i.i.d. labels. Russell (1983) gives the continuous-i.i.d. uniform-summand first-passage distribution; Cohen (2024) places that classical law in broader first-passage context. Accordingly (2), and in particular the limit \(\mathbb EN_1=e\), are prior knowledge, while the precise finite-shuffle coefficient law and the correction \(7e/(4n)\) are the present comparisons' uncovered statements.

## Limitations

The result assumes uniform deck arrangement and multiplicities all exactly equal to \(m\). The asymptotic bias (3)--(4) is proved for \(m=1\) only; the general fixed-m convergence does not provide its rate. The coefficient law does not address two-path coupling probability or adversarial worst-case iteration counts. Published general theorems about sampling without replacement could imply some coefficient identities, and inaccessible historical combinatorial literature could contain an equivalent finite-population correction. Neither possibility is ruled out by a search alone. Independent review has not been performed.

## References

1. S. G. Corregidor, *On the Number of Iterations in a Kruskal-Type Process*, arXiv:2610.29015v1 (first available 2026-10-21), https://arxiv.org/abs/2610.29015.
2. J. C. Lagarias, E. M. Rains, and R. J. Vanderbei, *The Kruskal Count*, arXiv:math/0110143v1 (2001), https://arxiv.org/html/math/0110143v1.
3. K. G. Russell, *On the Number of Uniform Random Variables Which Must Be Added to Exceed a Given Level*, Journal of Applied Probability **20** (1983), 172–177, doi:10.2307/3213732.
4. J. E. Cohen, *First-Passage Times for Random Partial Sums: Yadrenko's Model for e and Beyond*, The American Statistician **78** (2024), 111–114, doi:10.1080/00031305.2023.2244542.
