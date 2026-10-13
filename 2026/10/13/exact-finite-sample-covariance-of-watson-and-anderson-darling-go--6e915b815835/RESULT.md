# Exact finite-sample covariance of Watson and Anderson–Darling goodness-of-fit statistics

## Finding

Under an iid **fully specified, continuous** null model, Watson's centered empirical-distribution statistic and the Anderson–Darling weighted statistic have the exact covariance
\[
\boxed{\operatorname{Cov}(U_n^2,A_n^2)=\frac{n-1}{36n}},\qquad n\in\{1,2,\ldots\}.
\]
The covariance vanishes at one observation and is positive for every \(n\ge2\). More specifically, with \(a=\pi^2/3-3\), \(b=4-\pi^2/3\),
\[
\boxed{\operatorname{Corr}(U_n^2,A_n^2)=\frac{\sqrt{10}}6\sqrt{\frac{n-1}{2(n-1)a+b}}},\qquad n\ge2.
\]
This correlation is strictly increasing in sample size and tends to
\[
\boxed{\frac{\sqrt{15}}{6\sqrt{\pi^2-9}}}=0.6922\ldots.
\]

## Assumptions and scope

Let \(n\ge1\) be an integer. Under the null, \(X_1,\dots,X_n\) are independent draws from a known continuous cumulative distribution function \(F_0\). The probability-integral-transformed observations \(V_i=F_0(X_i)\) are iid uniform on \((0,1)\); let \(G_n\) denote their empirical distribution. Put \(e_n(t)=G_n(t)-t\). The usual one-sample, unmodified Watson and Anderson–Darling statistics in the present normalization are
\[
U_n^2=n\int_0^1\left(e_n(t)-\int_0^1e_n(r)\,dr\right)^2dt,
\qquad A_n^2=n\int_0^1\frac{e_n(t)^2}{t(1-t)}\,dt.
\]
All integrals are Lebesgue integrals; the weighted one is finite almost surely because no transformed observation equals either boundary almost surely. There are **no fitted or estimated nuisance parameters**, no two-sample version, and no finite-sample adjustment to either statistic. The covariance is distribution-free within this null class.

## Proof

For \(x\in(0,1)\), define \(Y_x(t)={\bf1}\{x\le t\}-t\) and the Brownian-bridge covariance kernel
\[
K(s,t)=\mathbb E[Y_V(s)Y_V(t)]=\min(s,t)-st,\quad V\sim\operatorname{Unif}(0,1).
\]
Set
\[
h(x,y)=\int_0^1Y_x(t)Y_y(t)\,dt
-\left(\int_0^1Y_x(t)\,dt\right)\left(\int_0^1Y_y(t)\,dt\right),
\]
\[
a(x,y)=\int_0^1\frac{Y_x(t)Y_y(t)}{t(1-t)}\,dt.
\]
Both kernels are canonical: fixing either argument and averaging the other against a uniform draw yields zero. Expanding the empirical process as a sum of \(Y_{V_i}\) gives
\[
U_n^2=\frac1n\sum_{i,j=1}^nh(V_i,V_j),\qquad
A_n^2=\frac1n\sum_{i,j=1}^na(V_i,V_j).
\]
Direct integration, with \(\delta=|x-y|\), gives
\[
h(x,y)=\frac1{12}-\frac{\delta}{2}+\frac{\delta^2}{2},\qquad h(x,x)=\frac1{12}.
\]
Hence Watson's diagonal sum is deterministic. In the mixed covariance, two off-diagonal ordered pairs are orthogonal unless they have the same unordered pair of indices: canonicality kills terms sharing at most one index, and Watson's constant diagonal kills terms involving diagonal indices. Therefore, also for \(n=1\),
\[
\operatorname{Cov}(U_n^2,A_n^2)
=\frac{2(n-1)}{n}\,\mathbb E[h(V_1,V_2)a(V_1,V_2)]
\]
(where the right side is read as zero at \(n=1\)).

To evaluate the remaining cross moment, put \(\kappa(s)=\int_0^1K(s,t)\,dt=s(1-s)/2\). Independence of \(V_1,V_2\) and Fubini's theorem imply
\[
\mathbb E[ha]=\int_0^1\frac1{s(1-s)}\int_0^1
\bigl(K(s,t)-\kappa(s)\bigr)^2\,dt\,ds.
\]
For \(0\le t\le s\), the centered kernel is \((1-s)t-s(1-s)/2\). For \(s\le t\le1\), it is \(s(1-t)-s(1-s)/2\). Squaring and integrating the two linear polynomials proves the identity
\[
\int_0^1\bigl(K(s,t)-\kappa(s)\bigr)^2dt
=\frac{s^2(1-s)^2}{12}.
\]
Thus
\[
\mathbb E[ha]=\frac1{12}\int_0^1s(1-s)\,ds=\frac1{72},
\]
and multiplying by \(2(n-1)/n\) proves the covariance formula.

For the correlation, canonicality yields the variance identity for any symmetric canonical kernel \(q\):
\[
\operatorname{Var}\left(\frac1n\sum_{i,j}q(V_i,V_j)\right)
=\frac1n\operatorname{Var}(q(V,V))
+\frac{2(n-1)}n\mathbb E[q(V_1,V_2)^2].
\]
The density of \(|V_1-V_2|\) is \(2(1-z)\), and direct polynomial integration gives
\[
\mathbb E[h(V_1,V_2)^2]
=2\int_0^1(1-z)\left(\frac1{12}-\frac z2+\frac{z^2}2\right)^2dz
=\frac1{720}.
\]
The constant Watson diagonal therefore gives
\[
\operatorname{Var}(U_n^2)=\frac{n-1}{360n}.
\]
For the weighted kernel, \(a(x,x)=-1-\log[x(1-x)]\); the beta-logarithm integrals \(\mathbb E\log V=-1\), \(\mathbb E\log^2V=2\), and \(\mathbb E[\log V\log(1-V)]=2-\pi^2/6\) yield
\[
\operatorname{Var}(a(V,V))=4-\frac{\pi^2}{3}=b.
\]
Moreover,
\[
\mathbb E[a(V_1,V_2)^2]
=2\int_0^1\frac{1-t}{t}\int_0^t\frac{s}{1-s}\,ds\,dt
=\frac{\pi^2}{3}-3=a.
\]
Consequently
\[
\operatorname{Var}(A_n^2)=\frac{b+2(n-1)a}{n}.
\]
Combining the three formulas yields the displayed correlation. Both \(a>0\) and \(b>0\), because \(9<\pi^2<12\); the function \(r\mapsto r/(2ar+b)\) has positive derivative \(b/(2ar+b)^2\) for \(r>0\). Strict monotonicity and the limit follow. At \(n=1\), Watson's statistic equals \(1/12\) almost surely, so its correlation is undefined (though covariance is zero).

## Verification

Run `python3 verify.py` with Python's standard library. It checks the exact centered-kernel polynomial identity **coefficient by coefficient**, the mixed bridge integral \(1/72\), the Watson quadratic-kernel moment \(1/720\), and positive strictly increasing correlations for \(2\le n\le200\). Independent seeded finite-sample Monte Carlo computes both statistics directly from sorted uniform samples at sizes \(1,2,4,9,20\), with \(40{,}000\)–\(60{,}000\) replicates per size and compares covariance against the exact formula. The finite simulations are diagnostic only; all-size claims follow from the displayed analytic identities.

## Relationship to prior work

Watson's centered quadratic empirical-distribution statistic and Anderson–Darling's tail-weighted statistic are classical; Stephens (1974) decomposes both into components and compares asymptotic power and separate moment behavior, not this finite-sample mixed covariance. Puig and Stephens (2000) compare goodness-of-fit tests for the Laplace distribution, without stating the cross moment in the inspected sections. Lemeshko, Lemeshko, and Postovalov (2010) study distributions of several omnibus statistics under fitted parameters, a materially different composite-null setting. The later complete treatment by Hwang and Kuriki (2024) derives separate generalized statistics and their own process covariance kernels; the finite-sample cross covariance of the two different statistics is not among the inspected stated results. Durbin and Knott (1972) discuss components of related statistics; their full article could not be verified here and remains a residual risk.

Separate marginal variances or cross covariances of either statistic with Cramér–von Mises do not algebraically determine the Watson–Anderson–Darling cross covariance. The constant diagonal and the exact mixed-kernel inner product are the needed additional structure.

## Limitations

The result is exclusively for a **simple continuous null distribution**. Parameter fitting generally alters the empirical-process covariance, so neither the finite-sample covariance nor the correlation formula is asserted for composite nulls. A covariance and a correlation do not determine the joint distribution, joint tail probabilities, or the validity of a combined test. The cited search and literature inspection cannot establish absolute historical novelty; a past cross-statistic component calculation or unindexed generating function could express the same value.

## References

1. M. A. Stephens (1974), *Components of goodness-of-fit statistics*, Annales de l'Institut Henri Poincaré, Section B, 10(1), 37–54. https://www.numdam.org/article/AIHPB_1974__10_1_37_0.pdf
2. J. Durbin and M. Knott (1972), *Components of Cramér–von Mises statistics I*, Journal of the Royal Statistical Society B 34(2), 290–307. https://academic.oup.com/jrsssb/article/34/2/290/7027179
3. P. Puig and M. A. Stephens (2000), *Tests of fit for the Laplace distribution, with applications*, Technometrics 42(4), 417–424. https://doi.org/10.1080/00401706.2000.10485715
4. B. Yu. Lemeshko, S. B. Lemeshko, and S. N. Postovalov (2010), *Statistic distribution models for some nonparametric goodness-of-fit tests in testing composite hypotheses*, Communications in Statistics – Theory and Methods 39(3), 460–471, published online 2010-01-06. Primary MSC 62G10. https://doi.org/10.1080/03610920903140148
5. H.-K. Hwang and S. Kuriki (2024), *Integrated empirical measures and generalizations of classical goodness-of-fit statistics*, arXiv:2404.06040, first submitted 2024-04-09. https://arxiv.org/abs/2404.06040
