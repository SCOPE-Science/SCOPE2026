# Gaussian area fluctuations under Bernoulli thinning of regular polygons

## Finding
For every fixed retention probability \(p\in(0,1)\), put \(q=1-p\). Independently retain each of the \(n\ge3\) unit-circumradius regular-polygon vertices with probability \(p\), and let \(A_n\) be the area of their convex hull, taking area zero for fewer than three retained vertices. The following *exact finite-size mean* holds, with \(\vartheta_n=2\pi/n\):
\[
\mathbb E A_n=\frac{np^2\sin\vartheta_n(1-q^n)}{2[p^2+2q(1-\cos\vartheta_n)]}.
\]
Write \(A_n^{\mathrm{reg}}=n\sin\vartheta_n/2\) for the full regular-polygon area and \(D_n=A_n^{\mathrm{reg}}-A_n\) for its missed area. Then
\[
\mathbb E D_n=\frac{4\pi^3q}{p^2n^2}-\frac{4\pi^5q(1+q)^2}{p^4n^4}+O(n^{-6}),
\]
\[
\lim_{n\to\infty}n^5\operatorname{Var}(A_n)=V_p,
\qquad V_p=\frac{16\pi^6q(1+q)(1+5q+q^2)}{p^5}>0,
\]
and
\[
 n^{5/2}(A_n-\mathbb E A_n)\;\xrightarrow{\mathrm d}\;N(0,V_p).
\]
All asymptotic implicit constants may depend on the fixed probability \(p\). The fixed-\(p\) regime is essential: no uniformity as \(p\) tends to zero or one is claimed.

## Assumptions and scope
The polygon is the unit-circumradius regular \(n\)-gon, its vertices are fixed before sampling, and their retention indicators are i.i.d. Bernoulli with constant \(p\in(0,1)\). The probability is fixed while \(n\to\infty\). This is not the random-point model with continuous angular coordinates or an interior Poisson cloud.

## Proof
**1. Cyclic area gaps, including degenerate samples.** Let \(\vartheta=2\pi/n\). If at least one vertex survives, enumerate retained indices cyclically and write their successive positive integer gaps as \(K_1,\ldots,K_s\) with \(\sum_i K_i=n\). The shoelace formula yields
\[
 A_n=\frac12\sum_{i=1}^s\sin(K_i\vartheta),\qquad
 D_n=\sum_{i=1}^s f_n(K_i),\quad
 f_n(k)=\frac12[k\sin\vartheta-\sin(k\vartheta)].
\]
Both formulas remain valid for one or two survivors (the oriented sine sum vanishes); for zero survivors, \(D_n=A_n^{\mathrm{reg}}\). Each gap score \(f_n(k)\) is nonnegative by the elementary inequality \(\sin(k\vartheta)\le k\sin\vartheta\) for integer \(k\ge1\) and \(0<\vartheta<\pi\); in particular, no assumption that every \(\sin(k\vartheta)\) is positive is made.

**2. Exact expectation.** An oriented chord advancing \(k<n\) index steps is a boundary edge exactly when both endpoints survive and the \(k-1\) intermediate vertices do not; this has probability \(p^2q^{k-1}\). Consequently
\[
 \mathbb E A_n=\frac{np^2}{2}\sum_{k=1}^{n-1}q^{k-1}\sin(k\vartheta).
\]
The finite geometric sum evaluates to
\[
 \sum_{k=1}^{n-1}q^{k-1}\sin(k\vartheta)
 =\frac{(1-q^n)\sin\vartheta}{1-2q\cos\vartheta+q^2},
\]
which proves the stated mean. Its expansion using \(1-2q\cos\vartheta+q^2=p^2+2q(1-\cos\vartheta)\) gives the two indicated mean-deficit terms; the exponentially small term \(q^n\) is absorbed.

**3. Reduction to a cubic geometric-gap reward.** The Taylor remainder for sine gives, for \(1\le k\le n\),
\[
 \left|f_n(k)-\frac{\vartheta^3}{12}(k^3-k)\right|
 \le C\vartheta^5(k^5+k),
\]
with an absolute \(C\). Put \(g(k)=k^3-k\) and \(S_n=\sum_i g(K_i)\) for nonempty retained sets, zero for the empty set. The Bernoulli gaps have geometric tails uniformly in \(n\): for each possible cyclic starting index, the probability of a forward gap \(k<n\) is \(p^2q^{k-1}\), and the unique-singleton event contributes at most \(npq^{n-1}\). For fixed \(p\), Minkowski's inequality and these tails show
\[
 \left\|D_n-\frac{\vartheta^3}{12}S_n\right\|_{L^2}=O(n^{-4}),
\]
including the empty-sample event (its contribution is exponentially small).

**4. Renewal fluctuation theorem and boundary control.** Extend the independent retention indicators to an infinite two-sided Bernoulli sequence. From each surviving position, the waiting time to the next survivor has geometric law
\[
 \Pr(K=k)=pq^{k-1},\qquad k=1,2,\ldots.
\]
The cyclic gap-reward sum \(S_n\) and the stationary infinite-line sum of rewards from surviving indices in an interval of \(n\) sites differ only in the terminal wrap-around reward, except on the exponentially rare empty event. The difference is bounded in \(L^2\) uniformly in \(n\): its two candidate gap lengths are sums of leading and trailing zero runs having uniformly bounded moments of every fixed order. Thus the standard renewal-reward proof applies without changing the normalized variance or distribution.

For completeness, let \(K_1,K_2,\dots\) now denote independent geometric waiting times, \(N(t)=\max\{j:\sum_{i=1}^jK_i\le t\}\), \(\mu_K=\mathbb E K=1/p\), and \(a=\mathbb E g(K)/\mu_K\). Decompose the stopped reward:
\[
 \sum_{i\le N(t)}g(K_i)-at
 =\sum_{i\le N(t)}[g(K_i)-aK_i]
 +a\left(\sum_{i\le N(t)}K_i-t\right).
\]
The overshoot/undershoot term is \(O_{L^2}(1)\) by geometric tails. By the law of large numbers \(N(t)/t\to p\); the i.i.d. central limit theorem and the maximal inequality for centered partial sums permit replacing the random index by \(\lfloor pt\rfloor\) on the \(\sqrt t\) scale. Therefore the first term, divided by \(\sqrt t\), tends to a centered Gaussian with variance \(p\mathbb E(g(K)-aK)^2\). Its variance also converges after division by \(t\), by uniform fourth-moment bounds for the stopped centered sum (the number of renewals never exceeds \(\lfloor t\rfloor\)) and the geometrically dominated boundary remainder. The initial delayed-renewal and final cyclic-edge corrections are bounded in \(L^2\), so the same conclusion holds for \(S_n\).

**5. Exact variance constant and transfer.** The geometric generating function \(\mathbb E z^K=pz/(1-qz)\) gives
\[
 \mathbb E g(K)=\frac{6q}{p^3},\qquad a=\frac{6q}{p^2},\qquad
 p\mathbb E[g(K)-aK]^2
 =\frac{36q(1+q)(1+5q+q^2)}{p^5}.
\]
In particular, \(\operatorname{Var}(S_n)/n\) tends to the last expression. Multiplying by \((2\pi)^6/144\) after the \(n^{-3}\) gap-score normalization yields
\[
 \lim n^5\operatorname{Var}(D_n)=\frac{16\pi^6q(1+q)(1+5q+q^2)}{p^5}=V_p.
\]
The \(L^2\) Taylor error is negligible on the \(n^{-5/2}\) fluctuation scale, so Slutsky's theorem gives the Gaussian law for \(D_n\). Negating the centered deficit gives the stated law for \(A_n\), whose variance equals that of the deficit.

## Verification
The accompanying \(\texttt{verify.py}\) uses only the Python standard library. It exhaustively checks the cyclic-gap identity and exact expected-area formula for \(3\le n\le12\) and retention probabilities \(1/4,1/2,3/4\); compares the two-term mean expansion at larger orders; and simulates the variance coefficient for three distinct probabilities using \(n=700\). The exact geometric-moment identities and renewal argument, not the numerical experiments, prove the theorem.

## Relationship to prior work
Pardon (2010/2011) established central limit theorems for convex hulls of Poisson or uniform interior samples in large convex bodies; the input points and scaling regime are different. Koroleva–Nikitin (2013) treated extremal areas/perimeters of fixed-order polygons from independent continuous points on a circumference. Pérez-Lantero (2014) studied complexity and approximation of area/perimeter distributions for independently present points from arbitrary finite input sets; those general algorithmic statements do not give the present exact regular-vertex finite-size mean, sharp area-variance coefficient, or Gaussian normalization. The distinct continuous circular-gap laws and randomly inscribed boundary approximation results provide conceptual comparison but not an implication for fixed Bernoulli thinning. This is a claim-relative comparison, not a guarantee of exhaustive priority.

## Limitations
The result does not describe the full finite-\(n\) area distribution, a uniform central limit theorem as \(p\to0\) or \(p\to1\), random locations off the fixed vertices, higher dimensions, or nonregular input polygons. The Gaussian limit and variance coefficient have only the stated fixed-probability scope. Definitive historical priority and external validation have not been established.

## References
- John Pardon, *Central limit theorems for random polygons in an arbitrary convex set*, arXiv:1003.4209 (first submitted 22 March 2010), Annals of Probability 39 (2011), 881–903; https://arxiv.org/abs/1003.4209.
- E. V. Koroleva and Ya. Yu. Nikitin, *U-max-statistics and limit theorems for perimeters and areas of random polygons*, arXiv:1301.1360 (first submitted 7 January 2013); https://arxiv.org/abs/1301.1360.
- Pablo Pérez-Lantero, *Area and Perimeter of the Convex Hull of Stochastic Points*, arXiv:1412.5153 (first submitted 16 December 2014); https://arxiv.org/abs/1412.5153.
