# Exact second-order dependence of Wald–Wolfowitz runs and Mann–Whitney rank sum
## Finding
Take two independent samples of sizes \(m,n\ge1\) from a common continuous distribution, and put \(N=m+n\). After sorting all \(N\) observations, encode each first-sample observation by \(1\) and each second-sample observation by \(0\). Under the null hypothesis of a common distribution, every binary word with exactly \(m\) ones and \(n\) zeros is equally likely.

Let
\[
R=1+\sum_{i=1}^{N-1}\mathbf{1}\{B_i\ne B_{i+1}\}
\]
be the Wald–Wolfowitz number of runs. Let
\[
U=\sum_{1\le i<j\le N} B_i(1-B_j)
\]
be the number of first-sample symbols preceding second-sample symbols. This is one orientation of the Mann–Whitney statistic; replacing \(U\) by \(mn-U\) leaves all squared-centered formulas below unchanged.

Then
\[
\mathbb E U=\frac{mn}2,\qquad \operatorname{Cov}(R,U)=0,
\]
while
\[
\boxed{\operatorname{Cov}\!\left(R,(U-mn/2)^2\right)
=-\frac{mn(mn-1)}{3N}}.
\]
Writing
\[
Z=\frac{U-mn/2}{\sqrt{mn(N+1)/12}},
\]
one obtains the particularly simple standardized identity
\[
\boxed{\operatorname{Cov}(R,Z^2)
=-\frac{4(mn-1)}{N(N+1)}}.
\]
Hence the covariance with two-sided rank-sum evidence is strictly negative whenever \(mn>1\).

The exact marginal variances needed for a correlation statement are
\[
\operatorname{Var}(R)
=\frac{2mn(2mn-N)}{N^2(N-1)}
\]
and
\[
\operatorname{Var}\!\left((U-mn/2)^2\right)
=\frac{mn(N+1)\,[5mnN+8mn-3N(N+1)]}{360}.
\]
Thus, for \(mn>1\),
\[
\boxed{
\operatorname{Corr}\!\left(R,Z^2\right)^2
=
\frac{20(mn-1)^2(N-1)}
{(N+1)(2mn-N)\,[5mnN+8mn-3N(N+1)]}
},
\]
with the correlation itself negative. If \(m/N\to\lambda\in(0,1)\), then
\[
\operatorname{Cov}(R,Z^2)\to-4\lambda(1-\lambda),
\qquad
\operatorname{Corr}(R,Z^2)\sim-\sqrt{\frac2N}.
\]

## Assumptions and scope
The two samples are independent and their common null distribution is continuous, so pooled ranks have no ties and the induced binary label word is uniform over all \(\binom{N}{m}\) words with the prescribed symbol counts. The statement is finite-sample and distribution-free under this null.

The orientation of the Mann–Whitney statistic is immaterial for the squared-centered result. If a convention uses the complementary count \(mn-U\), its centered value is the negative of the one used here.

No claim is made for ties, unequal null distributions, random sample sizes, or the joint law under fixed alternatives.

## Proof
Put
\[
Q=U-\frac{mn}2.
\]
Reversing a binary word leaves \(R\) unchanged and sends \(U\) to \(mn-U\). Since reversal is a measure-preserving involution on the null sample space,
\[
\operatorname{Cov}(R,U)=0.
\]

For the even cross-moment, let
\[
a_j=j-\frac{N+1}2.
\]
If \(W=\sum_{j=1}^N jB_j\) is the first-sample rank sum, then the usual complementary Mann–Whitney count is \(W-m(m+1)/2\). Therefore
\[
Q^2=\left(\sum_{j=1}^N a_jB_j\right)^2.
\]
Write
\[
T_i=\mathbf{1}\{B_i\ne B_{i+1}\},
\qquad
R=1+\sum_{i=1}^{N-1}T_i.
\]
Under uniform sampling with fixed symbol counts,
\[
\mathbb P(T_i=1)=\frac{2mn}{N(N-1)}
\]
for every \(i\).

Assume first \(N\ge4\). Conditional on \(T_i=1\), exactly one of positions \(i,i+1\) is selected for the first sample, equally likely, and the remaining \(m-1\) selected positions form a uniform subset of size \(m-1\) from the other \(N-2\) positions. Put
\[
s_i=a_i+a_{i+1}=2i-N,
\qquad
A_2=\sum_{j=1}^N a_j^2=\frac{N(N^2-1)}{12}.
\]
Let \(B\) denote the coefficient contributed by the selected member of the adjacent pair and let \(Y\) be the sum of the coefficients selected outside that pair. Then
\[
\mathbb EB=\frac{s_i}2,
\qquad
\mathbb EB^2=\frac{s_i^2+1}4.
\]
For the remaining coefficient population, the sum is \(-s_i\), the sum of squares is
\[
A_2-\frac{s_i^2+1}2,
\]
the population size is \(M=N-2\), and the sample size is \(r=m-1\). For a uniform subset sum \(Y\) from a finite population with total \(S\) and square-sum \(H\),
\[
\mathbb EY=\frac rM S,
\]
and the inclusion-probability identity gives
\[
\mathbb EY^2
=
\frac rM H
+
\frac{r(r-1)}{M(M-1)}(S^2-H).
\]
Because the choice inside the adjacent pair is independent of the remaining subset,
\[
\mathbb E[Q^2\mid T_i=1]
=
\mathbb EB^2+2\mathbb EB\,\mathbb EY+\mathbb EY^2.
\]
Substituting the displayed values and summing over \(i\) uses only
\[
\sum_{i=1}^{N-1}s_i^2
=
\frac{N(N-1)(N-2)}3
\]
and yields
\[
\sum_{i=1}^{N-1}
\left(
\mathbb E[Q^2\mid T_i=1]-\mathbb EQ^2
\right)
=
-\frac{(N-1)(mn-1)}6.
\]
Since \(\mathbb EQ^2=mn(N+1)/12\),
\[
\begin{aligned}
\operatorname{Cov}(R,Q^2)
&=
\sum_{i=1}^{N-1}
\operatorname{Cov}(T_i,Q^2)\\
&=
\frac{2mn}{N(N-1)}
\sum_{i=1}^{N-1}
\left(
\mathbb E[Q^2\mid T_i=1]-\mathbb EQ^2
\right)\\
&=
-\frac{mn(mn-1)}{3N}.
\end{aligned}
\]
The cases \(N=2\) and \(N=3\) follow directly from their finite label spaces and agree with the same formula.

Dividing by
\[
\operatorname{Var}(U)=\mathbb EQ^2=\frac{mn(N+1)}{12}
\]
gives
\[
\operatorname{Cov}(R,Z^2)
=-\frac{4(mn-1)}{N(N+1)}.
\]

For completeness, the variance of \(Q^2\) follows from the classical Gaussian-binomial probability generating function for the two-letter inversion statistic. Its centered cumulant generating function is
\[
K(t)=
\sum_{j=1}^m
\left[
\log\!\left(
\frac{\sinh((n+j)t/2)}{(n+j)t/2}
\right)
-
\log\!\left(
\frac{\sinh(jt/2)}{jt/2}
\right)
\right].
\]
Using
\[
\log\!\left(\frac{\sinh(x/2)}{x/2}\right)
=
\frac{x^2}{24}-\frac{x^4}{2880}+O(x^6)
\]
gives
\[
\kappa_2=\frac{mn(N+1)}{12},
\]
and
\[
\kappa_4
=
-\frac{mn(N+1)(m^2+mn+m+n^2+n)}{120}.
\]
Since
\[
\operatorname{Var}(Q^2)=\kappa_4+2\kappa_2^2,
\]
the displayed exact variance of \(Q^2\) follows. Combining it with the classical exact variance of \(R\) gives the stated correlation formula. The proportional-sample asymptotics then follow by direct expansion.

## Verification
The accompanying `checker.py` exhaustively enumerates every binary label word for every pair \((m,n)\) with \(2\le m+n\le14\). It uses exact rational arithmetic and independently checks the exact mean and variance of \(R\), the exact mean and variance of \(U\), the zero covariance \(\operatorname{Cov}(R,U)\), the new covariance \(\operatorname{Cov}(R,Q^2)\), the exact variance of \(Q^2\), the standardized covariance, and the exact squared correlation whenever it is defined.

The recorded run completes 818 exact formula comparisons. These finite checks test the algebra and boundary cases; the all-sample-size theorem rests on the analytic argument above.

## Relationship to prior work
Wilcoxon's 1945 paper introduced ranking comparisons that underlie the two-sample rank-sum statistic. Baringhaus and Henze's full 2016 treatment revisits the Wald–Wolfowitz two-sample runs statistic, gives its exact null mean and variance, derives mean and variance under fixed alternatives, and identifies the subject as MSC \(62G10\) and \(62G20\). That article does not state a joint moment with the Mann–Whitney statistic.

Biswas, Mukhopadhyay, and Ghosh explicitly place the Wilcoxon–Mann–Whitney rank test and Wald–Wolfowitz run test side by side as classical distribution-free univariate two-sample procedures, and reproduce the exact null distribution and first two moments of the run statistic while developing a multivariate generalization. Their inspected text does not derive a cross-moment between the two classical statistics.

Canfield, Janson, and Zeilberger give the Gaussian-binomial generating function, exact mean and variance, and higher-moment machinery for inversion counts on words. In the two-letter case this supplies the marginal Mann–Whitney distribution used for the fourth-moment calculation, but it contains no run-count variable and therefore does not imply the cross-covariance.

A 2009 statistical-process-control paper with the superficially close title “Nonparametric control charts based on runs and Wilcoxon-type rank-sum statistics” was also checked at abstract and later-literature level. The later literature describes that work as adding runs-type signaling rules to a Mann–Whitney chart, rather than coupling the Wald–Wolfowitz pooled-label run count with the Mann–Whitney statistic. Full text of that 2009 paper was not successfully obtained, so it remains a specifically recorded residual literature risk.

## Limitations
The result concerns the common continuous-distribution null. Ties destroy the uniform fixed-composition word model unless a tie-breaking or conditional convention is imposed. Under alternatives, the binary rank-label word is no longer uniformly distributed and the formulas need not hold.

The originality comparison cannot exclude every unindexed historical identity. In particular, a joint generating function for inversion number and symbol-run count in fixed-composition binary words would dominate the new moment if it already contained this derivative as a stated consequence. Searches under both statistical and binary-word aliases did not locate such a source, but failed search is not a proof of absence.

## References
1. F. Wilcoxon, “Individual Comparisons by Ranking Methods,” *Biometrics Bulletin* 1(6) (1945), 80–83. DOI: 10.2307/3001968.
2. L. Baringhaus and N. Henze, “Revisiting the two-sample runs test,” *TEST* 25 (2016), 432–448. DOI: 10.1007/s11749-015-0463-1.
3. M. Biswas, M. Mukhopadhyay, and A. K. Ghosh, “A distribution-free two-sample run test applicable to high-dimensional data,” *Biometrika* 101(4) (2014), 913–926. DOI: 10.1093/biomet/asu045.
4. E. R. Canfield, S. Janson, and D. Zeilberger, “The Mahonian probability distribution on words is asymptotically normal,” arXiv:0908.2089 (2009).
