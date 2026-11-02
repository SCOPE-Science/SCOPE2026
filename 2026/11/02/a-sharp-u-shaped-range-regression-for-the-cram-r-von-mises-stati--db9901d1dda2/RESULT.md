# A sharp U-shaped range regression for the Cramér–von Mises statistic

## Finding

Let \(U_1,\ldots,U_n\), for integer \(n\ge2\), be independent uniform observations on \([0,1]\). Write \(F_n\) for their empirical distribution function, \(R=\max_i U_i-\min_i U_i\) for their sample range, and
\[
W=n\int_0^1(F_n(t)-t)^2\,dt.
\]
For every \(0<r<1\), the conditional regression is the explicit strictly convex quadratic
\[
\boxed{\mathbb E[W\mid R=r]=\frac{n(1-r)^2+2r^2-r}{6}.}
\]
It decreases up to the unique point \(r_*=\frac{2n+1}{2(n+2)}\) and increases afterward. Its unique minimum is \(\frac{4n-1}{24(n+2)}=\frac16-\frac3{8(n+2)}\). Although the regression turns upward for near-spanning samples, its covariance with the range is always strictly negative:
\[
\boxed{\operatorname{Cov}(R,W)=-\frac{n-1}{(n+1)(n+2)(n+3)}<0.}
\]
More precisely, the conditional mean exceeds its unconditional value \(\mathbb EW=1/6\) exactly for \(0<r<(n-1)/(n+2)\), falls below it for \((n-1)/(n+2)<r<1\), and equals it at the interior crossing. The limiting value at \(r=1\) is also \(1/6\).

The Pearson correlation has a closed finite-sample form:
\[
\boxed{\operatorname{Corr}(R,W)=-\frac1{n+3}\sqrt{\frac{90n(n-1)}{(n+2)(4n-3)}}\sim-\frac{\sqrt{45/2}}n.}
\]
Thus a globally negative covariance coexists with a nonmonotone conditional expectation, and the correlation decays at the exact inverse-sample-size scale.

## Assumptions and scope

The parent distribution is the fully specified uniform law on the unit interval, not a location- or scale-fitted uniform family. The statistic \(W\) is the **one-sample** classical Cramér–von Mises statistic with factor \(n\), not its unscaled integral and not Watson's centered variant. Every integer \(n\ge2\) is covered. The range has a continuous beta law, so the regression is an almost-everywhere conditional expectation; the displayed polynomial is the natural continuous version for \(0<r<1\), while endpoint values are limits only. This result is not a conditional distribution or an independence claim.

## Proof

Put \(A=\min_i U_i\), \(B=\max_i U_i\), and \(r=B-A\). The standard order-statistic identity is
\[
W=\frac1{12n}+\sum_{i=1}^n\left(U_{(i)}-\frac{2i-1}{2n}\right)^2
=\frac n3+\sum_{i=1}^n U_i^2-\frac1n\sum_{i,j=1}^n\max(U_i,U_j).
\]
The joint density of the extrema on \(0<a<b<1\) is \(n(n-1)(b-a)^{n-2}\). Conditioned on \(A=a\), \(B=b=a+r\), the \(n-2\) unordered interior observations are independent uniform points on \((a,b)\). Their first two raw moments are \((a+b)/2\) and \((a^2+ab+b^2)/3\); the expected maximum of two independent interior observations is \((a+2b)/3\). Counting the diagonal, the extreme--extreme pair, the extreme--interior pairs, and the interior--interior pairs in the displayed identity gives
\[
\mathbb E[W\mid A=a,R=r]
=n\left(a^2+a(r-1)+\frac{(1-r)^2}{3}\right)+\frac{r^2}{3}-\frac r6.
\]
Equivalently, this is \(n[(a-(1-r)/2)^2+(1-r)^2/12]+r^2/3-r/6\). The conditional law of \(A\) given \(R=r\) is uniform on \((0,1-r)\); averaging its centered square, whose mean is \((1-r)^2/12\), proves the regression formula. Its derivative is \([2(n+2)r-(2n+1)]/6\), and its second derivative is \((n+2)/3>0\). Factoring
\[
\mathbb E[W\mid R=r]-\frac16
=\frac{(r-1)((n+2)r-(n-1))}{6}
\]
proves the level-crossing and strict sign assertions, including the unique minimizer.

The range has density \(n(n-1)r^{n-2}(1-r)\), hence \(R\sim\operatorname{Beta}(n-1,2)\) and
\[
\mathbb ER^k=\frac{(n-1)(n)\cdots(n+k-2)}{(n+1)(n+2)\cdots(n+k)}\quad(k\ge1).
\]
The regression and these first three moments give \(\mathbb EW=1/6\) and the claimed exact covariance by direct rational simplification.

For the correlation, write \(\xi_i(t)=\mathbf1\{U_i\le t\}-t\), \(A_i=\int_0^1\xi_i(t)^2dt\) and \(B_{ij}=\int_0^1\xi_i(t)\xi_j(t)dt\). Then
\[
W=\frac1n\sum_i A_i+\frac2n\sum_{i<j}B_{ij}.
\]
Here \(\operatorname{Var}(A_i)=1/180\). Every \(B_{ij}\) is conditionally centered given either of its endpoints; consequently the distinct pair terms are pairwise uncorrelated and uncorrelated with all \(A_i\). The Brownian-bridge covariance kernel gives
\[
\mathbb EB_{ij}^2=\int_0^1\!\int_0^1(\min(s,t)-st)^2\,ds\,dt=\frac1{90}.
\]
Thus \(\operatorname{Var}(W)=(4n-3)/(180n)\). The beta variance is \(\operatorname{Var}(R)=2(n-1)/((n+1)^2(n+2))\); combining these identities yields the exact correlation and its asymptotic equivalent.

## Verification

The included `verify.py` uses only standard-library rational arithmetic. It independently integrates the polynomial in uniform Dirichlet spacings of ordered samples for every \(2\le n\le7\), verifying the exact means, mixed moment/covariance and variance. It additionally integrates the conditional ordered-interior spacings for four different rational pairs of extrema in every size, checking the unreduced conditional formula. Running `python3 verify.py` reports `PASS: 48 independent exact-rational identities`. These finite tests are cross-checks, not replacements for the analytic proof. The accompanying derivation covers all integer sizes \(n\ge2\).

## Relationship to prior work

The Cramér–von Mises one-sample statistic is classical. Laio (2004), in its full accessible Sections 2–4, reviews its integrated empirical-CDF form, case-zero moments and modifications for fitted-parameter goodness-of-fit tests; it does not give the sample-range conditional regression, its sign reversal, or this mixed covariance. Csörgő and Faraway (1996) study exact and asymptotic **marginal** laws of the Cramér–von Mises statistic, and Frey and Wang (2014) study EDF goodness-of-fit tests for ranked-set samples. None of the inspected accessible content directly states the present **joint** extremal-range/EDF-quadratic law. The 1996 full text was not fully available during this comparison, so historical equivalence remains possible. No originality claim follows solely from unsuccessful searches.

## Limitations

Only the uniform null with fully specified parameters and the ordinary quadratic EDF statistic are covered. The regression describes a conditional mean, not stochastic ordering, independence, or a conditional null distribution. Its U shape does not contradict the negative unconditional covariance. The available literature comparison cannot exclude a classical equivalent buried in older exact-distribution or order-statistics sources; this is a priority limitation, not an uncertainty about the analytic identity.

## References

- F. Laio (2004), *Cramer–von Mises and Anderson-Darling goodness of fit tests for extreme value distributions with unknown parameters*, *Water Resources Research* 40, doi:10.1029/2004WR003204. First available online September 28, 2004.
- S. Csörgő and J. J. Faraway (1996), *The Exact and Asymptotic Distributions of Cramér-Von Mises Statistics*, *Journal of the Royal Statistical Society, Series B* 58(1), 221–234, doi:10.1111/j.2517-6161.1996.tb02077.x.
- J. Frey and L. Wang (2014), *EDF-based goodness-of-fit tests for ranked-set sampling*, *Canadian Journal of Statistics* 42, 451–469, doi:10.1002/cjs.11224. First published online July 28, 2014.
