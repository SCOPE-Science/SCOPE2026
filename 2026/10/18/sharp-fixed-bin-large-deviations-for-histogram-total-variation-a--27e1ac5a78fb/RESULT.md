# Sharp fixed-bin large deviations for histogram total variation and alternating comb minimizers

## Finding

Let \(n\ge3\) be fixed, let \(X=(X_1,\ldots,X_n)\sim\operatorname{Mult}(N;1/n,\ldots,1/n)\), and define the ordered-histogram statistic \(D_N=\sum_{i=1}^{n-1}|X_{i+1}-X_i|\). For \(\theta\ge0\), set \(\Lambda_n(\theta)=\log(Z_n(\theta)/n)\), where

\[
Z_n(\theta)=\begin{cases}
2\cosh\theta+(n-2)\cosh(2\theta),&n\text{ even},\\
2e^{-\theta}+\frac{n-1}{2}e^{2\theta}+\frac{n-3}{2}e^{-2\theta},&n\text{ odd}.
\end{cases}
\]

For each fixed \(0<t<2\), there is a unique \(\theta_t>0\) satisfying \(\Lambda_n'(\theta_t)=t\). Put \(I_n(t)=\theta_t t-\Lambda_n(\theta_t)\), \(v_n(t)=\Lambda_n''(\theta_t)>0\), \(K_n=2\) for even \(n\) and \(K_n=1\) for odd \(n\), and \(h_n=3\) for \(n=3\), \(h_n=1\) for \(n\ge4\). Define \(a_3=-1\) and \(a_n=-2\) for \(n\ge4\); let \(k_N\) be the smallest element of \(a_nN+h_n\mathbb Z\) at least \(Nt\), and \(\delta_N=k_N-Nt\in[0,h_n)\). Then the **sharp lattice-sensitive upper-tail asymptotic** is

\[
\boxed{\mathbb P(D_N\ge Nt)=
\frac{K_n h_n e^{-\theta_t\delta_N}}{(1-e^{-h_n\theta_t})\sqrt{2\pi N v_n(t)}}
 e^{-NI_n(t)}(1+o(1)),\qquad N\to\infty.}
\]

The entropy-minimizing empirical histograms behind this rare event have an **alternating comb** profile. Write \(\sigma_i^*=(-1)^{i+1}\) for \(1\le i<n\) and let \(w=(-1,2,-2,2,\ldots,(-1)^n)\), with its interior entries alternating between \(2\) and \(-2\). Then the minimizing probability vector is \(p_i^*=e^{\theta_t w_i}/Z_n(\theta_t)\). For odd \(n\) it is unique; for even \(n\) the complete minimizing set is \(\{p^*,p^-\}\), where \(p_i^-=e^{-\theta_t w_i}/Z_n(\theta_t)\). In particular, conditioned on \(D_N\ge Nt\), \(X/N\) concentrates on that finite set.

At the maximum threshold, let \(k=\lfloor(n-1)/2\rfloor\). Then \(\mathbb P(D_N=2N)\sim C_n(k/n)^N\), where \(C_n=1\) if \(n\) is odd and \(C_n=n/2\) if \(n\) is even. Thus \(I_n(2)=\log(n/k)\). Moreover \(I_n(t)=t^2/[2(4-6/n)]+O_n(t^3)\) as \(t\downarrow0\). For fixed \(0<t<2\), \(I_n(t)\) tends as \(n\to\infty\) to \(\frac{1+t/2}{2}\log(1+t/2)+\frac{1-t/2}{2}\log(1-t/2)\).

## Assumptions and scope

The bin count \(n\) is held fixed while sample size \(N\) tends to infinity, with independent uniform bin draws. The formula with \(N^{-1/2}\) prefactor is for fixed \(t\in(0,2)\), not for a threshold approaching either endpoint with \(N\). The large-bin limit is iterated after the fixed-bin large-deviation limit. This is *ordered-bin discrete total variation*, not total-variation distance between probability measures.

## Proof

**1. Linearization and the extremal sign pattern.** For each sign word \(\sigma=(\sigma_1,\ldots,\sigma_{n-1})\in\{-1,1\}^{n-1}\), define \(w_1(\sigma)=-\sigma_1\), \(w_i(\sigma)=\sigma_{i-1}-\sigma_i\) for \(2\le i\le n-1\), and \(w_n(\sigma)=\sigma_{n-1}\). The identity \(|u|=\max_{\sigma=\pm1}\sigma u\) gives

\[
D_N=\max_{\sigma}\sum_{i=1}^n w_i(\sigma)X_i.
\]

Let \(z=e^\theta>1\), and define \(S(\sigma)=\sum_i z^{w_i(\sigma)}\). Internal transitions of the sign word contribute \(z^2\) at a change \(+\to-\), \(z^{-2}\) at \(-\to+\), and \(1\) at no change; endpoints contribute \(z^{-\sigma_1}+z^{\sigma_{n-1}}\). At fixed endpoints, replacing two nonchanges by a pair of opposite changes increases the sum by \(z^2+z^{-2}-2>0\). Consequently the maximizing sign word has as many changes as parity allows.

If \(n\) is even, full alternation has equal initial and final signs and score \(Z_n(\theta)=(n-2)\cosh(2\theta)+2\cosh\theta\). There are exactly two such words, which are negatives of one another. The strongest opposite-endpoint competitor has a score smaller by \((z-1)(1-z^{-2})>0\); all other competitors lose at least one further positive pair-of-changes increment. If \(n\) is odd, full alternation has opposite endpoint signs. Its better orientation starts with \(+\) and ends with \(-\), giving the displayed odd-\(n\) value of \(Z_n\). Reversing that orientation decreases the score by \((z-z^{-1})(z+z^{-1}-2)>0\); the strongest equal-endpoint competitor is smaller by \((z-1)(z-z^{-1})>0\). Thus the stated maximizer set is complete, with strict inequality for every other sign word and every \(\theta>0\).

**2. Exponential rate and most likely profiles.** For a fixed sign word, \(Y_{N,\sigma}=\sum_i w_i(\sigma)X_i\) is the sum of \(N\) independent variables taking the values \(w_i(\sigma)\) with uniform probabilities. Its log moment-generating function is \(\Lambda_\sigma(\theta)=\log(S(\sigma)/n)\). Every such variable has mean zero because \(\sum_iw_i=0\). By Step 1, \(\Lambda_\sigma(\theta)\le\Lambda_n(\theta)\), with equality for \(\theta>0\) precisely for the alternating words. The optimizing alternating variable has positive variance, mean zero, and maximum \(2\); hence \(\Lambda_n'\) increases strictly from \(0\) to \(2\), proving existence and uniqueness of \(\theta_t\).

For a probability vector \(p\), let \(H(p)=\sum_i p_i\log(np_i)\) (with \(0\log0=0\)). The entropy variational inequality gives, for every word \(\sigma\),

\[
H(p)\ge\theta\sum_iw_i(\sigma)p_i-\Lambda_\sigma(\theta),
\]

with equality exactly at \(p_i\propto e^{\theta w_i(\sigma)}\). If \(\sum|p_{i+1}-p_i|\ge t\), choose a maximizing sign word and put \(\theta=\theta_t\); the inequality gives \(H(p)\ge I_n(t)\). The alternating tilted vectors attain equality, since their signed contrast equals \(\Lambda_n'(\theta_t)=t\) and the absolute variation is at least that contrast. Strictness in Step 1 and in the entropy inequality proves the complete optimizer classification. Standard finite-alphabet type bounds (equivalently, Sanov's theorem) then give the logarithmic upper-tail rate and exponential conditional concentration on this finite optimizer set.

**3. Sharp prefactor, including the lattice.** For the canonical alternating word, the score sum \(Y_N\) has one-step support of maximal lattice span \(h_3=3\) with offset \(-1\) when \(n=3\), and span \(h_n=1\) with offset \(-2\) otherwise. Its tilted one-step law \(q_i=e^{\theta_t w_i}/Z_n(\theta_t)\) has mean \(t\) and variance \(v_n(t)\). Exponential tilting yields

\[
\mathbb P(Y_N\ge Nt)=e^{-NI_n(t)}\sum_{j\ge0}
 e^{-\theta_t(\delta_N+h_nj)}
 \mathbb P_{\theta_t}(Y_N=k_N+h_nj).
\]

For every fixed \(j\), the maximal-span lattice local central limit theorem gives \(\mathbb P_{\theta_t}(Y_N=k_N+h_nj)\sim h_n/\sqrt{2\pi N v_n(t)}\). Fourier inversion for a bounded, nondegenerate lattice variable also bounds all its tilted point masses by \(O(N^{-1/2})\); dominated convergence against the geometric weights gives the single-word prefactor in the displayed theorem. Each nonalternating word has \(\Lambda_\sigma(\theta_t)<\Lambda_n(\theta_t)\), so Chernoff's bound makes its tail exponentially smaller than \(e^{-NI_n(t)}\). In even dimension, the two maximizing sign words are negatives of each other, and their positive-threshold events are disjoint; they contribute a factor of exactly two to leading order. In odd dimension there is one maximizing word. This proves the full upper-tail expansion.

**4. Maximal threshold and limiting laws.** For any probability vector \(p\),

\[
\sum_{i=1}^{n-1}|p_{i+1}-p_i|=2-p_1-p_n-2\sum_{i=1}^{n-1}\min(p_i,p_{i+1}).
\]

Equality with \(2\) holds exactly when both endpoint masses vanish and no two adjacent bin masses are simultaneously positive. Therefore the observed bins must lie in an independent subset of the path on its \(n-2\) interior vertices. Its largest independent sets have size \(k=\lfloor(n-1)/2\rfloor\), with precisely one such set for odd \(n\) and \(n/2\) such sets for even \(n\). Taking the union of the events that all \(N\) observations lie in a given independent set, intersections of distinct maximal sets contribute only \(O(((k-1)/n)^N)\) for fixed \(n\). This proves the endpoint asymptotic. Finally, \(\Lambda_n''(0)=(4n-6)/n\), which gives the small-\(t\) expansion by Legendre inversion; and \(\Lambda_n(\theta)\to\log\cosh(2\theta)\) as \(n\to\infty\), which gives the stated iterated large-bin limit by strict convexity.

## Verification

A standalone Python checker enumerates every sign word for \(3\le n\le11\) and verifies the unique maximizing pattern(s) at four exact rational exponential weights, checking all scores with rational arithmetic. It also exhaustively checks the maximal-variation characterization across integer histograms for \(3\le n\le8\) and \(1\le N\le10\). Finally it compares the lattice prefactor with exact binomial-tail probabilities for twelve three-bin cases. These are finite consistency tests: the infinite asymptotics are proved by the sign-pattern argument, entropy variational principle, and lattice local central limit theorem.

To reproduce, run `python3 verification/check.py` in an environment with SciPy installed. The finite test script is ancillary; no computation of infinitely many instances is asserted.

## Relationship to prior work

Banić and Elezović (2026, arXiv:2610.13366v1) obtain exact and asymptotic first moments of this uniform-multinomial ordered total variation, and explicitly distinguish their expectation calculation from the variance and distributional questions. Banić and Elezović's *Comb Test* (arXiv:2606.01465v1) describes a dynamic-programming computation of the exact null distribution and empirical calibration; that approach does not itself furnish the closed fixed-bin large-deviation rate, identification of the entropy-minimizing comb, or lattice-sensitive asymptotic coefficient given here. The abstract of the latter paper was available, but its complete text was not available for this comparison, so implicit coverage there remains a residual risk. Earlier work on large deviations of separable multinomial statistics or unordered divergences does not directly state a result for sums of *adjacent* absolute count differences.

## Limitations

The findings are confined to fixed \(n\), uniform independent sampling, and ordered linear rather than cyclic total variation. The strong asymptotic is not uniform as \(t\to0\), \(t\to2\), or \(n\to\infty\), and no simultaneous growing-bin/sample theorem or exact finite-sample tail formula is claimed. The elementary Chernoff/entropy and lattice-theory ingredients are classical; the new assertion is their sharp all-bin alternating-pattern optimization and the resulting fully explicit calibrated tail formula. A full-text check of the original *Comb Test* article was unavailable, so priority assessment retains that risk.

## References

1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1, first submitted 2026-10-09. Full HTML text at https://arxiv.org/html/2610.13366.
2. N. Banić and N. Elezović, *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation*, arXiv:2606.01465v1, first submitted 2026-05-31. Abstract at https://arxiv.org/abs/2606.01465.
3. N. Banić and N. Elezović, *TVOR: Finding Discrete Total Variation Outliers among Histograms*, arXiv:2012.11574, first submitted 2020-12-21.
4. S. M. Mirakhmedov, *The probabilities of large deviations for a certain class of statistics associated with multinomial distribution*, ESAIM: Probability and Statistics 24 (2020), 581–606, DOI:10.1051/ps/2020020 (separable-bin statistic framework).
5. Standard finite-alphabet Sanov/type bounds and the classical maximal-span lattice local central limit theorem are used as stated within the proof.
