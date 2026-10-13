# The upper boundary gap has exact positive Cramér–von Mises covariance
## Finding
Let \(U_1,\ldots,U_n\) be independent \(\operatorname{Unif}(0,1)\) variables, let
\[
M_n=U_{(n)},\qquad B_n=1-M_n,
\]
and define the one-sample Cramér–von Mises statistic
\[
W_n^2=\frac1{12n}+\sum_{i=1}^n\left(U_{(i)}-\frac{2i-1}{2n}\right)^2.
\]
For every integer \(n\ge2\) and \(0\le b\le1\),
\[
\boxed{
\mathbb E[W_n^2\mid B_n=b]
=
\frac{2n(n+2)b^2-(5n+1)b+n+1}{6n}
}.
\]
The regression is strictly convex and is minimized at
\[
\boxed{b_n^\star=\frac{5n+1}{4n(n+2)}}.
\]
The exact covariance is
\[
\boxed{
\operatorname{Cov}(B_n,W_n^2)
=
\frac{n-1}{2(n+1)(n+2)(n+3)}>0
}.
\]
Equivalently,
\[
\operatorname{Cov}(M_n,W_n^2)
=-\frac{n-1}{2(n+1)(n+2)(n+3)}.
\]
Since
\[
\operatorname{Var}(B_n)=\frac{n}{(n+1)^2(n+2)}
\]
and
\[
\operatorname{Var}(W_n^2)=\frac{4n-3}{180n},
\]
the exact correlation is
\[
\boxed{
\operatorname{Corr}(B_n,W_n^2)
=
\frac{3\sqrt5\,(n-1)}{(n+3)\sqrt{(n+2)(4n-3)}}
}.
\]
Consequently,
\[
\operatorname{Corr}(B_n,W_n^2)\sim\frac{3\sqrt5}{2n}.
\]

## Assumptions and scope
The result is for the fully specified continuous-uniform null. By the probability integral transform, the Cramér–von Mises statistic itself is distribution-free for any fully specified continuous null, but the boundary-gap variable here is specifically the upper gap on the transformed \([0,1]\) scale. The quantity \(B_n\) measures the empty upper-tail interval left by the sample, whereas \(W_n^2\) integrates squared empirical-CDF discrepancy over the whole support.

The conditional formula is stronger than the covariance alone. It shows that the expected integrated discrepancy is not monotone in the boundary gap: it has a unique finite-sample optimum at \(b_n^\star\), while the overall linear covariance with \(B_n\) is positive.

## Proof
Condition on \(M_n=m\). Given this event, the lower \(n-1\) order statistics have the same law as \(m\) times the order statistics from \(n-1\) independent uniform variables. Therefore, for \(1\le i<n\),
\[
\mathbb E[U_{(i)}\mid M_n=m]=\frac{im}n,
\]
and, using the unordered sample for the quadratic sum,
\[
\mathbb E\left[\sum_{i=1}^nU_{(i)}^2\mid M_n=m\right]
=m^2+\frac{n-1}3m^2
=\frac{n+2}3m^2.
\]
Expanding the defining order-statistic formula for \(W_n^2\) gives
\[
W_n^2
=
\sum_{i=1}^nU_{(i)}^2
-\frac1n\sum_{i=1}^n(2i-1)U_{(i)}
+\frac n3.
\]
The conditional expectation of the weighted linear term is
\[
\mathbb E\left[\sum_{i=1}^n(2i-1)U_{(i)}\mid M_n=m\right]
=
\frac{(n+1)(4n-1)}6m.
\]
Hence
\[
\mathbb E[W_n^2\mid M_n=m]
=
\frac{n+2}3m^2
-
\frac{(n+1)(4n-1)}{6n}m
+
\frac n3.
\]
Substituting \(m=1-b\) yields the claimed regression in \(B_n\). Differentiating that quadratic gives the unique minimizer \(b_n^\star\).

The maximum has beta moments
\[
\mathbb E[M_n^k]=\frac n{n+k},\qquad k>0.
\]
Combining the first three such moments with the conditional quadratic and \(\mathbb E[W_n^2]=1/6\) gives
\[
\operatorname{Cov}(M_n,W_n^2)
=-\frac{n-1}{2(n+1)(n+2)(n+3)}.
\]
Since \(B_n=1-M_n\), the covariance for the boundary gap has the opposite sign.

For completeness, the exact variance of \(W_n^2\) can be reconstructed without a distribution table. Put
\[
Z_x(t)=\mathbf1\{x\le t\}-t
\]
and
\[
h(x,y)=\int_0^1Z_x(t)Z_y(t)\,dt
=\frac13+\frac{x^2+y^2}2-\max(x,y).
\]
Then
\[
W_n^2=\frac1n\sum_{i,j=1}^nh(U_i,U_j).
\]
For independent uniform \(U,V\), the kernel is degenerate off the diagonal:
\[
\mathbb E[h(U,V)\mid U]=0.
\]
Writing \(d(U)=h(U,U)\), direct polynomial integration gives
\[
\operatorname{Var}(d(U))=\frac1{180},
\qquad
\mathbb E[h(U,V)^2]=\frac1{90}.
\]
Only identical unordered off-diagonal pairs contribute to the variance, so
\[
\operatorname{Var}(W_n^2)
=
\frac1{n^2}
\left(
\frac n{180}+rac{2n(n-1)}{90}
\right)
=
\frac{4n-3}{180n}.
\]
Together with the beta variance of \(M_n\), this gives the displayed exact correlation and its \(n^-1\) asymptotic.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It checks the conditional regression at 1,501 finite \((n,m)\) pairs, reconstructs the covariance for every \(2\le n\le80\), independently integrates the empirical-process kernel to recover \(\operatorname{Var}(W_n^2)\), verifies the exact correlation formula, and checks \(\mathbb E[W_n^2]=1/6\) through \(n=200\). Successful replay prints:

`VERIFY_OK conditional=1501 covariance=79 kernel=79 mean=199`

The executable checks are corroborative. The proof above establishes the identities for every admissible sample size and boundary-gap value.

## Relationship to prior work
The Cramér–von Mises statistic is a classical integrated empirical-distribution goodness-of-fit criterion. Arnold and Emerson give a full modern account of Cramér–von Mises-type tests and emphasize that these criteria integrate discrepancy over the whole support. Knott studies the exact small-sample distribution of the classical statistic, and Csörgő and Faraway develop exact and asymptotic marginal distribution approximations. Those sources address the marginal law of the criterion rather than the joint dependence with the terminal order statistic or boundary gap.

Lemeshko, Lemeshko, and Postovalov study finite and modeled distributions of several nonparametric goodness-of-fit statistics and classify the work under primary MSC \(62G10\). Their article supplies the exact day-level public-date anchor used here. Published-record and semantic searches for combinations of Cramér–von Mises, sample maximum, maximum order statistic, boundary gap, covariance, and conditional regression did not locate the displayed formulas.

The closest prior findings in the checked local record concern exact Cramér–von Mises covariance with Watson and Anderson–Darling statistics. Those are integrated EDF functionals and do not determine a mixed moment with the endpoint order statistic. An exact variance formula for \(W_n^2\) appearing there is compatible with, but does not imply, the present boundary-gap regression or covariance.

## Limitations
The boundary variable is defined after transformation to the continuous-uniform null. No claim is made for a raw-scale endpoint gap under arbitrary parent distributions, for composite nulls with estimated parameters, or for censored samples. The exact correlation tends to zero, so the dependence is finite and structurally interpretable rather than asymptotically strong.

A residual originality risk remains in older exact-distribution literature for empirical-distribution statistics and order statistics. The highly plausible Knott and Csörgő–Faraway sources were inspected through their journal records, summaries, and available bibliographic material, but their complete article bodies were not available in the checked lawful access path; that access limitation is retained rather than converted into negative evidence.

## References
T. B. Arnold and J. W. Emerson, *Nonparametric Goodness-of-Fit Tests for Discrete Null Distributions*, The R Journal 3(2) (2011), 34–39, DOI: 10.32614/RJ-2011-016.

M. Knott, *The Distribution of the Cramér–Von Mises Statistic for Small Sample Sizes*, Journal of the Royal Statistical Society Series B 36 (1974), 430–438, DOI: 10.1111/j.2517-6161.1974.tb01017.x.

S. Csörgő and J. J. Faraway, *The Exact and Asymptotic Distributions of Cramér–Von Mises Statistics*, Journal of the Royal Statistical Society Series B 58 (1996), 221–234, DOI: 10.1111/j.2517-6161.1996.tb02077.x.

B. Yu. Lemeshko, S. B. Lemeshko, and S. N. Postovalov, *Statistic Distribution Models for Some Nonparametric Goodness-of-Fit Tests in Testing Composite Hypotheses*, Communications in Statistics—Theory and Methods 39 (2010), 460–471, DOI: 10.1080/03610920903140148; published online 2010-01-06.
