# Strict likelihood-ratio decay of singleton abundance at nonuniform coupon coverage

## Finding

Let \(m\ge2\), and take arbitrary positive coupon probabilities \(p_1,\ldots,p_m\) with \(\sum_i p_i=1\). Run independent Poisson processes \(N_i\) at these respective rates. Let \(T\) be the first instant at which all types have appeared, and \(S=\#\{i:N_i(T)=1\}\) the singleton-type count at completion. For every \(t>0\), set
\[
q_i(t)=\frac{p_i t}{e^{p_i t}-1},\qquad Q(t)=\sum_{i=1}^m q_i(t),\qquad F_t(z)=\prod_{i=1}^m(1-q_i(t)+q_i(t)z).
\]
For the continuous regular conditional distribution at \(T=t\), the **complete law** is
\[
\boxed{\Pr(S=s\mid T=t)=\frac{s[z^s]F_t(z)}{Q(t)},\quad 1\le s\le m.}
\]
Equivalently, \(S\mid T=t\) is the size-biased distribution of the sum of independent Bernoulli variables with parameters \(q_i(t)\); its probability-generating function is \(zF'_t(z)/Q(t)\). The resulting mean is
\[
\mathbb E[S\mid T=t]=1+Q(t)-\frac{\sum_iq_i(t)^2}{Q(t)}.
\]

The conditional family is **strictly decreasing in monotone likelihood-ratio order**: for every \(0<t<u<\infty\),
\[
\boxed{S\mid T=u\ <_{\mathrm{lr}}\ S\mid T=t.}
\]
Here \(<_{\mathrm{lr}}\) means that the ratio of the mass function at \(t\) to that at \(u\) is nondecreasing with singleton count, and is not constant. Hence all upper-tail probabilities are nonincreasing, with a strict inequality for at least one nontrivial threshold. In particular, for every pair of real, strictly increasing functions \(f,g\), with \(\mathbb E|f(T)|<\infty\),
\[
\boxed{\operatorname{Cov}(f(T),g(S))<0.}
\]

## Assumptions and scope

The number of types is a finite integer \(m\ge2\); all \(p_i>0\) and their sum equals one. A rate-one merged Poisson process marks the iid coupon sequence with probabilities \(p_i\); \(T\) is its *continuous elapsed time*, not its integer number of coupon draws. Since \(T\) has a strictly positive continuous density on \((0,\infty)\), conditioning on \(T=t\) means the density-defined regular conditional law. No assertion about stochastic ordering conditional on an integer draw-count completion time is made. For \(m=1\), the singleton count is identically one and the strict ordering does not hold.

## Proof

**1. Conditional winner decomposition.** Write \(X_i=\inf\{t:N_i(t)>0\}\). The independent variables \(X_i\) have exponential densities \(p_i e^{-p_it}\), and \(T=\max_i X_i\). The probability density that the last previously missing type is \(i\), with completion at \(t\), is
\[
 h_i(t)=p_i e^{-p_it}\prod_{j\ne i}(1-e^{-p_jt}).
\]
Summing yields a strictly positive density
\[
 h(t)=\prod_i(1-e^{-p_it})\sum_i\frac{p_i}{e^{p_it}-1}.
\]
Consequently, the conditional probability that type \(i\) completes the collection is
\[
 w_i(t)=\frac{h_i(t)}{h(t)}=\frac{q_i(t)}{Q(t)}.
\]
Given \(T=t\) and that \(i\) completes the collection, type \(i\) has exactly one arrival, and the other type counts are independent Poisson variables conditioned to be positive. For each \(j\ne i\), the probability of exactly one count is \(p_jt/(e^{p_jt}-1)=q_j(t)\). Thus
\[
 S\mid(T=t,I=i)\ \overset d=\ 1+\sum_{j\ne i}\operatorname{Bernoulli}(q_j(t)),
\]
with independent summands. If \(Y_t=\sum_i\operatorname{Bernoulli}(q_i(t))\) has independent summands, then
\[
 \Pr(S=s\mid T=t)=\sum_i\frac{q_i(t)}{Q(t)}\Pr(Y_t-B_i=s-1)
 =\frac{s\Pr(Y_t=s)}{Q(t)}.
\]
The last equality is the expansion of \(s\Pr(Y_t=s)=\sum_i\Pr(B_i=1,Y_t=s)\). This proves the law, generating function, and mean.

**2. A likelihood-ratio lemma for size-biased Bernoulli sums.** Let \(B_1,\ldots,B_m\) be independent Bernoulli variables with strictly interior parameters. Let \(Y^\star\) be the positive size-biased sum, \(\Pr(Y^\star=s)=s\Pr(\sum B_i=s)/\mathbb E\sum B_i\). This law is nondecreasing in each Bernoulli parameter in likelihood-ratio order, and the order is strict when the parameter increases, for \(m\ge2\).

For proof, vary one coordinate \(q\) and write \(W\) for the sum of the others, with \(a_s=\Pr(W=s)\), \(\mu=\mathbb EW>0\), and \(a_{-1}=a_m=0\). The changed size-biased pmf is
\[
 b_q(s)=\frac{s[(1-q)a_s+qa_{s-1}]}{\mu+q},\qquad 1\le s\le m.
\]
The distribution \((a_s)\) is log-concave with positive mass at each integer from zero through \(m-1\): it is the convolution of \(m-1\) positive Bernoulli mass sequences, and convolution preserves such log-concavity. Therefore the ratios \(a_{s-1}/a_s\) are nondecreasing in \(s\), taking the final ratio as \(+\infty\). For \(0<q<q'<1\),
\[
 \frac{b_{q'}(s)}{b_q(s)}
 =\frac{\mu+q}{\mu+q'}\frac{1-q'+q' a_{s-1}/a_s}{1-q+q a_{s-1}/a_s}
\]
is nondecreasing in \(s\): the displayed fractional-linear function is strictly increasing in the ratio because \(q'>q\). It is not constant, since its argument has a finite first value and infinite final value. This is strict likelihood-ratio ordering. The case of a single remaining Bernoulli is included, with the final ratio interpreted by continuity. Changing several coordinates one by one preserves the likelihood-ratio order by transitivity.

**3. Apply the lemma and obtain covariance.** For each fixed rate \(p_i>0\), \(q_i(t)=(\int_0^1e^{up_it}\,du)^{-1}\) is strictly decreasing on \((0,\infty)\). Therefore for \(t<u\), every Bernoulli parameter at \(t\) is greater than at \(u\). Applying the lemma one coordinate at a time proves the strict likelihood-ratio ordering claimed.

The likelihood-ratio order implies stochastic order, and strictness implies that \(g_t=\mathbb E[g(S)\mid T=t]\) is strictly decreasing in \(t\) for any strictly increasing \(g\), as the support is the finite set \(\{1,\ldots,m\}\). The density \(h\) is positive everywhere on \((0,\infty)\), so \(T\) is nondegenerate. For an independent copy \(T'\),
\[
 2\operatorname{Cov}(f(T),g(S))
 =\mathbb E[(f(T)-f(T'))(g_T-g_{T'})]<0,
\]
where integrability of \(f(T)\) ensures the expectation exists. This proves the final assertion.

## Verification

The accompanying standalone `coupon_singletons_check.py` performs 16,538 assertions. For random nonuniform probability vectors of sizes two through eight, it compares the size-biased probability formula with an independently assembled mixture over last-arriving coupon types, checks normalization, checks every adjacent likelihood-ratio inequality, and checks all relevant upper-tail inequalities. Independently, it computes exact rational singleton distributions from a finite-state recursion on zero/one/at-least-two occupancy states for four rational probability vectors; numerical integration of the Poissonized joint density agrees with every rational probability to within \(4\times10^{-9}\).

Run `python coupon_singletons_check.py` with Python 3 and SciPy installed. These finite checks support implementation accuracy; the all-size statement is proved by the independent analytic argument above, not by finite enumeration.

## Relationship to prior work

Myers and Wilf [1, Section 4, equations (44)–(47)] already derive the full joint discrete completion-draw-count and singleton distribution for **equal** coupon probabilities, and the harmonic mean singleton count. Adler, Oren and Ross [2, Section 3] use independent Poissonized streams for **unequal** probabilities and derive expectations and bounds for later albums; their displayed calculations do not specify the conditional singleton law given continuous completion time or its likelihood-ratio ordering. Long [3, Sections 2 and 6] gives further nonuniform expectation identities and a different monotonicity statement comparing album statistics as the number of types changes, rather than conditioning singleton abundance on completion time. The standard log-concavity of Poisson-binomial probabilities is an input here, not claimed as new.

The novelty assessed here is the combination of **arbitrary nonuniform probabilities**, the exact regular conditional distribution at each continuous cover time, and the strict, all-time monotone likelihood-ratio ordering (hence increasing-transform covariance). A known result that implied this exact joint statement, even with different notation, would subsume the claim; searches and inspections do not constitute a proof of absolute historical priority.

## Limitations

The conditional variable is continuous Poissonized collection time. No discrete count-conditioned likelihood-ratio assertion is established. The theorem requires fixed finite support with all positive probabilities; zero-probability coupon types cannot be collected. The proof does not give a quantitative uniform lower bound on covariance magnitude as probabilities vary. A comprehensive independent literature audit has not been performed, and an implicit specialization of more general older occupancy-process results remains possible.

## References

[1] A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1 (public 16 April 2003), https://arxiv.org/pdf/math/0304229, especially Section 4.

[2] I. Adler, S. Oren and S. M. Ross, *The Coupon-Collector's Problem Revisited*, Journal of Applied Probability **40** (2003), 513–518, https://oren.ieor.berkeley.edu/pubs/coupon.pdf, especially Section 3.

[3] C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635 (2026), https://arxiv.org/abs/2606.29635, especially Sections 2 and 6.
