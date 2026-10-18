# Strict dispersive ordering of logarithmic exponential maxima

## Finding

**Theorem (strict quantile-spread contraction).** For each real parameter \(a>0\), let \(Y_a\) have cumulative distribution function
\[
 F_a(y)=(1-\exp(-\exp y))^a,\qquad y\in\mathbb R.
\]
For every \(0<a<b\) and every \(0<u<v<1\), the quantiles satisfy the *strict dispersive ordering*
\[
 Q_b(v)-Q_b(u)<Q_a(v)-Q_a(u),\qquad
 Q_a(u)=\log[-\log(1-u^{1/a})].
\]
In particular, for every integer \(n\ge1\), \(Y_n\) has the law of the logarithm of the maximum of \(n\) independent standard exponential variables. Thus the entire family of interquantile widths, not only its variance, decreases strictly with sample size. For independent copies \(Y_a'\) and \(Y_a''\), the spread variables are strictly ordered under a uniform coupling:
\[
 |Y_b'-Y_b''|<|Y_a'-Y_a''|\quad\text{almost surely}.
\]
Consequently \(\operatorname{Var}(Y_b)<\operatorname{Var}(Y_a)\) for every \(0<a<b\). The last variance inequality for *integer* parameters is known from Giam's 2026 paper; the claim here is the stronger, continuous-parameter dispersive ordering and its pairwise-distance implication.

## Assumptions and scope

The scale-one exponential distribution has \(\Pr(E\le t)=1-e^{-t}\) for \(t\ge0\). For integer \(n\ge1\), take \(E_1,\ldots,E_n\) independent and set \(Y_n=\log\max_i E_i\). Its CDF equals \(F_n\) above. The expression \(F_a\) also defines a continuous, strictly increasing CDF on \(\mathbb R\) for any real \(a>0\). All assertions concern fixed, strictly positive real parameters and probabilities strictly between zero and one; no endpoint derivative at \(u=0\) or \(u=1\) is asserted. The word *strict* means a strictly positive gap whenever \(u<v\) and \(a<b\).

## Proof

1. For \(a>0\), inversion of \(F_a\) gives
\[
 Q_a(u)=\log[-\log(1-u^{1/a})],\qquad 0<u<1.
\]
Differentiating with respect to \(u\), put \(z=u^{1/a}\), \(L_0=-\log z>0\), and \(L_1=-\log(1-z)>0\). Since \(aL_0=-\log u\),
\[
 Q_a'(u)=\frac{z}{a u(1-z)L_1}=
 \frac{h(z)}{u(-\log u)},\qquad
 h(z)=\frac{z(-\log z)}{(1-z)(-\log(1-z))}.
\]
2. The positive function \(h\) is strictly decreasing on \((0,1)\). Indeed, direct logarithmic differentiation gives
\[
 \frac{h'(z)}{h(z)}=
 \frac{1-(1-z)/(-\log z)-z/(-\log(1-z))}{z(1-z)}.
\]
For every \(x>0\), \(\log x<x-1\) unless \(x=1\). Applying this strict inequality to \(x=1/z\) and \(x=1/(1-z)\) yields respectively
\[
 \frac{1-z}{-\log z}>z,
 \qquad \frac{z}{-\log(1-z)}>1-z.
\]
The two positive fractions therefore sum to more than one, proving \(h'(z)<0\).
3. Fix \(0<u<1\). As \(a\) increases, \(u^{1/a}\) increases strictly, while the factor \(1/[u(-\log u)]\) is independent of \(a\). Hence, for \(0<a<b\), \(Q_b'(u)<Q_a'(u)\) for every \(u\in(0,1)\). Integrating over any \([u,v]\) with \(0<u<v<1\) proves the displayed strict quantile-spread inequality.
4. Let \(U,V\) be independent uniforms on \((0,1)\). For each parameter \(a\), \(Q_a(U)\) and \(Q_a(V)\) are independent observations with law \(F_a\). Since \(U\ne V\) almost surely and quantile differences are ordered strictly for any two distinct probabilities, the pairwise-distance coupling follows. The left tail of \(Y_a\) is exponentially small and its right tail is double-exponentially small, so its second moment is finite. The identity
\[
 2\operatorname{Var}(Y_a)=\mathbb E[(Y_a'-Y_a'')^2]
\]
then gives strict variance ordering. More generally, every nonconstant increasing function of the pairwise absolute distance, whenever integrable, obeys the corresponding stochastic comparison.

## Verification

The standalone standard-library program `verify.py` recomputes the CDF/quantile identity, checks direct derivative against finite differences, and tests strict interquantile contraction over specified grids of integer and noninteger parameters. These are numerical consistency tests, not replacements for the universally quantified proof. The proof relies only on the displayed elementary derivative and the strict logarithmic inequality.

## Relationship to prior work

Doumas, *An inequality involving alternating binomial sums* (arXiv:2603.11129, publicly submitted 2026-03-11), identifies \(\operatorname{Var}(\log\max_i E_i)\) with the positive coupon-collector coefficient \(\pi^2/6+n w_n-n^2c_n^2\) and remarks on a then-open monotonicity conjecture. Giam, *Decreasing nature of a sequence related to the Coupon Collector's problem* (Statistics & Probability Letters 236 (2026), 110790, DOI 10.1016/j.spl.2026.110790), subsequently **proved strict decrease of that variance sequence**; this already-known claim is not asserted as novel here. The additional statement proved above orders *all* quantile gaps and is valid for every positive real exponent parameter, not just integers.

Classical dispersive-order theory establishes its definition and variance implications. The full texts of Kochar (1996) and Khaledi–Kochar (2000) were compared. Their comparisons of order statistics under a decreasing-failure-rate (DFR) parent distribution do not yield this assertion: the parent \(\log E\) has increasing failure rate \(r(y)=e^y\), not DFR. The 2025 work of Das and collaborators on dependent Kumaraswamy-generated extremes compares different models/parameters and uses hypotheses not supplying this fixed-baseline, variable-exponent quantile conclusion. Searches did not identify the stronger exact claim in published records, but absence of a search hit is not a uniqueness certificate.

## Limitations

The proof is specific to the CDF family \(F_a\), not to arbitrary exponential, log-concave, IFR, or random-sample models. The statement gives no numerical optimal bound for individual quantile gaps, and no uniform convergence rate in \(a\). No priority or independent validation is certified. Giam's 2026 article was available through its published abstract and metadata, not full text, so it remains possible that an auxiliary theorem therein states or implies this stronger ordering. Likewise, earlier general transform-order theorems may cover this example. These are residual originality risks requiring independent checking. The comparison with the 1996/2000 DFR theorems is based on their inspected full texts.

## References

1. A. V. Doumas, *An inequality involving alternating binomial sums* (2026), arXiv:2603.11129v1, https://arxiv.org/html/2603.11129v1 .
2. K. K. Giam, *Decreasing nature of a sequence related to the Coupon Collector's problem*, Statistics & Probability Letters **236** (2026), 110790, https://doi.org/10.1016/j.spl.2026.110790 .
3. S. C. Kochar, *Dispersive ordering of order statistics*, Statistics & Probability Letters **27** (1996), 271–274, https://web.pdx.edu/~kochar/Papers/d_papers/SPL1996.pdf .
4. B.-E. Khaledi and S. Kochar, *On dispersive ordering between order statistics in one-sample and two-sample problems*, Statistics & Probability Letters **46** (2000), 257–261, https://web.pdx.edu/~kochar/Papers/d_papers/SPL2000.pdf .
5. J. Jeon, S. Kochar, and C. G. Park, *Dispersive ordering—some applications and examples*, Statistical Papers **47** (2006), 227–247, https://doi.org/10.1007/s00362-005-0285-4 .
6. S. Das et al., *Ordering results for random maxima and minima from two dependent Kumaraswamy generalized distributed samples* (2025), arXiv:2508.14855, https://arxiv.org/html/2508.14855 .
