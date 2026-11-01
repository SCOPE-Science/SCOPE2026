# Universal one-third correlation in the joint Hilbert-distance fluctuations of random simplex points

## Finding

Fix an integer \(k\ge 2\). For each integer \(N\ge 2\), let \(S_N\) be any nondegenerate Euclidean \((N-1)\)-simplex, and sample \(k\) points \(X^{(1)},\ldots,X^{(k)}\) independently and uniformly by Euclidean volume from its interior. Write \(D_{ab}^{(N)}\) for the Hilbert projective distance between points \(a\) and \(b\), normalized as the **full logarithm** of the four-point cross ratio, not half of that logarithm. Then the entire \(\binom{k}{2}\)-dimensional vector of centered distances

\[
\bigl(D_{ab}^{(N)}-2\log N\bigr)_{1\le a<b\le k}
\]

converges jointly in law, as \(N\to\infty\), to the explicitly specified array \((L_{ab})_{a<b}\) below. The convergence also holds for all joint moments of any fixed finite order.

For each ordered pair \(a\ne b\), define positive random variables \(Z_{ab}\). The collections of variables having different **second subscripts** \(b\) are mutually independent. Within a fixed second subscript \(b\), for every collection of positive thresholds \((x_{ab})_{a\ne b}\), their complete joint distribution is

\[
\Pr\bigl(Z_{ab}\le x_{ab}\ \text{for every }a\ne b\bigr)
=\exp\!\left[-\sum_{\varnothing\ne J\subseteq\{1,\ldots,k\}\setminus\{b\}}
\frac{(-1)^{|J|+1}}{\sum_{a\in J}x_{ab}}\right].
\tag{1}
\]

Equivalently, the exponent in (1) is \(\mathbb E\max_{a\ne b}(E_a/x_{ab})\) for independent mean-one exponential random variables \(E_a\). The joint distance limit is

\[
L_{ab}=\log Z_{ab}+\log Z_{ba},\qquad a<b.\tag{2}
\]

Each \(L_{ab}\) has the distribution of the sum of two independent standard Gumbel variables. For all distinct unordered edges \(e,f\) on \(\{1,\ldots,k\}\),

\[
\mathbb E L_e=2\gamma,\qquad
\operatorname{Cov}(L_e,L_f)=
\begin{cases}
\pi^2/3,&e=f,\\
\pi^2/9,&|e\cap f|=1,\\
0,&e\cap f=\varnothing.
\end{cases}\tag{3}
\]

In particular, two distinct incident distances have limiting Pearson correlation **exactly \(1/3\)**, while distances with disjoint endpoints are independent. The exact mean and covariance convergence also gives these as limits of the covariances and correlations of the original centered distances. Here \(\gamma\) is Euler's constant.

## Assumptions and scope

The sample size \(k\) is fixed as \(N\to\infty\). The parent simplex may vary arbitrarily with \(N\); an affine map preserves both its uniform-volume measure and Hilbert cross ratios, so its shape has no effect. Barycentric coordinates are indexed \(1,\ldots,N\), strictly positive almost surely, and sum to one. The metric convention matters: a definition using half the logarithm instead would divide all centered distances and their means by two and all covariances by four, leaving the correlations unchanged. All limits are in fixed finite dimensions, not uniform in growing \(k\).

For probability calculations, choose an independent array of standard exponential variables \((E_{ai})\), \(1\le a\le k,1\le i\le N\), and let

\[
X_i^{(a)}=\frac{E_{ai}}{\sum_{j=1}^N E_{aj}}.
\]

This is the Dirichlet \((1,\ldots,1)\) law, exactly the barycentric distribution of a volume-uniform point in an \((N-1)\)-simplex. The Hilbert distance is the variation of the logarithmic coordinate ratios:

\[
D_{ab}^{(N)}=\max_i\log\frac{X_i^{(a)}}{X_i^{(b)}}-
\min_i\log\frac{X_i^{(a)}}{X_i^{(b)}}.
\tag{4}
\]

## Proof

**Step 1: An exact directed-maxima representation.** Normalizing the exponential coordinates shifts all logarithmic coordinate ratios in (4) by the same constant and cancels in their range. For ordered distinct indices set

\[
M_{ab}^{(N)}=\max_{1\le i\le N}\frac{E_{ai}}{E_{bi}},\qquad
Z_{ab}^{(N)}=\frac{M_{ab}^{(N)}}{N}.
\]

Because the minimum of the ratios is the reciprocal of the maximum with the indices reversed, the following identity holds for every \(N\), without approximation:

\[
D_{ab}^{(N)}=\log M_{ab}^{(N)}+\log M_{ba}^{(N)}
=2\log N+\log Z_{ab}^{(N)}+\log Z_{ba}^{(N)}.
\tag{5}
\]

**Step 2: All simultaneous directed extremes.** Choose arbitrary positive \(x_{ab}\) for the finitely many ordered pairs. In a single exponential-coordinate column \(i\), let \(A_b\) denote the event that at least one ratio with denominator index \(b\) violates its \(Nx_{ab}\) threshold. With \(T_b=\max_{a\ne b} E_{ai}/x_{ab}\), conditioning on all numerator variables gives

\[
\Pr(A_b)=\mathbb E(1-e^{-T_b/N})
=\frac{\mathbb ET_b}{N}+O_{k,x}(N^{-2}).
\tag{6}
\]

The error bound follows from \(\mathbb E T_b^2<\infty\). For two distinct denominator indices \(b,c\), put \(\delta=\min_{u\ne v}x_{uv}>0\) and \(R=\max_jE_{ji}\). On \(A_b\cap A_c\) one has \(E_{bi}<R/(N\delta)\) and \(E_{ci}<R/(N\delta)\). For \(N\delta>1\), neither \(b\) nor \(c\) can attain \(R\). Thus \(R=\max_{j\notin\{b,c\}}E_{ji}\), which is independent of \(E_{bi},E_{ci}\). If \(k\ge3\), conditional integration gives

\[
\Pr(A_b\cap A_c)
\le\frac{\mathbb E\left[(\max_{j\notin\{b,c\}}E_{ji})^2\right]}{N^2\delta^2}
=O_{k,x}(N^{-2}).\tag{7}
\]

For \(k=2\) the intersection is empty once \(N\delta>1\). Finite inclusion–exclusion, (6), and (7) show that the probability of no threshold violation in one coordinate column equals

\[
1-\frac{1}{N}\sum_{b=1}^k\mathbb ET_b+O_{k,x}(N^{-2}).
\]

Coordinate columns are independent, so the probability of **all** \(N\) columns satisfying **all** thresholds converges to \(\exp(-\sum_b\mathbb ET_b)\). This exponent separates additively by \(b\); therefore the limiting directed-maxima blocks indexed by different denominators are independent. The continuous joint law is the one in (1). Direct exponential integration yields the inclusion–exclusion formula

\[
\mathbb ET_b
=\int_0^\infty\left(1-\prod_{a\ne b}(1-e^{-t x_{ab}})\right)dt
=\sum_{\varnothing\ne J\subseteq\{1,\ldots,k\}\setminus\{b\}}
\frac{(-1)^{|J|+1}}{\sum_{a\in J}x_{ab}}.
\]

Continuous mapping through (5) establishes the asserted joint distance-array convergence.

**Step 3: Moment convergence.** The one-dimensional ratio of independent standard exponentials satisfies

\[
\Pr(E_{ai}/E_{bi}\le r)=\frac{r}{1+r},\qquad r>0.
\]

Thus, for \(V_{ab}^{(N)}=\log Z_{ab}^{(N)}\),

\[
\Pr(V_{ab}^{(N)}\le u)=(1+e^{-u}/N)^{-N},\qquad u\in\mathbb R.
\tag{8}
\]

For every \(t\ge0\) and all \(N\ge1\), Bernoulli's inequality and a union bound give

\[
\Pr(V_{ab}^{(N)}<-t)\le e^{-t},\qquad
\Pr(V_{ab}^{(N)}>t)\le e^{-t}.
\tag{9}
\]

All absolute moments of every fixed order are uniformly bounded. By Hölder's inequality, so are moments of finite products of the centered distances (5). Uniform integrability, together with joint weak convergence, proves convergence of all fixed joint moments. Formula (8) also shows that \(\log Z_{ab}\) is standard Gumbel, with mean \(\gamma\) and variance \(\pi^2/6\). As distinct denominator blocks are independent, this gives the mean and diagonal variance in (3).

**Step 4: The exact off-diagonal coefficient.** For distinct numerator indices \(a,c\) sharing denominator \(b\), inclusion–exclusion in (1) gives

\[
\Pr(Z_{ab}\le x,Z_{cb}\le y)
=\exp\left(-\frac1x-\frac1y+\frac1{x+y}\right),\qquad x,y>0.\tag{10}
\]

This is a familiar bivariate extreme-value law (the parameter-one Galambos copula), **not** claimed here as a new distribution. Let \(U=\log Z_{ab}\) and \(V=\log Z_{cb}\). Hoeffding's covariance identity (justified by the exponential tails (9)) yields

\[
\begin{aligned}
\operatorname{Cov}(U,V)
&=\int_{\mathbb R^2}e^{-e^{-u}-e^{-v}}
\left(e^{1/(e^u+e^v)}-1\right)du\,dv\\
&=\int_0^1\frac{-\log(1-w+w^2)}{w(1-w)}\,dw\\
&=-2\int_0^1\frac{\log(1-w+w^2)}w\,dw
=4\operatorname{Re}\operatorname{Li}_2(e^{i\pi/3})=\frac{\pi^2}{9}.
\end{aligned}\tag{11}
\]

For clarity, the second identity first substitutes \(s=e^{-u}\), \(t=e^{-v}\), then \(r=s+t\), \(w=s/(s+t)\); integration in \(r\) is Frullani's logarithmic integral. The third identity uses symmetry under \(w\mapsto1-w\). The fourth follows by expanding \(\log(1-w+w^2)\) into its conjugate complex linear factors; the classical Fourier sum \(\sum_{n\ge1}\cos(n\theta)/n^2=\pi^2/6-\pi\theta/2+\theta^2/4\) at \(\theta=\pi/3\) yields the last equality. No conditional or merely numerical identity is needed.

Two distinct undirected edges share exactly one denominator block when they share one vertex; in that case (11) is their sole nonzero cross-covariance. If the edges are disjoint, they involve disjoint sets of entire denominator blocks and are independent (already for finite \(N\)). Dividing (11) by \(\pi^2/3\) gives the exact limiting correlation \(1/3\) and completes (3).

## Verification

The standalone `verify.py` checks the finite-\(N\) common-denominator bivariate distribution against (10), numerically evaluates the independent one-dimensional integral in (11), tests the uniform exponential tail bounds, and performs a seeded simulation of four uniform-simplex points using \(4{,}000\) barycentric coordinates over \(3{,}000\) repetitions. The simulation compares common-endpoint and disjoint-endpoint distance covariances and the individual fluctuation means and variances. All deterministic assertions passed. The simulation and numerical quadrature corroborate but **do not replace** the proof of the infinite-dimensional limit.

Run `python verify.py` with Python 3.9 or newer and NumPy installed. The code uses a fixed random seed. The source is included alongside this document.

## Relationship to prior work

The simplicial Hilbert-to-variation-norm identification is classical; Foertsch and Karlsson (2004), especially their discussion of earlier results of Nussbaum and de la Harpe, make clear that the deterministic isometry itself is prior knowledge. Lemmens (2011), Section 4, states the barycentric logarithmic coordinate expression explicitly. The stochastic exponential construction for uniform simplex points is likewise standard.

The dependence law in a *single* denominator block, particularly (10), falls within established Galambos extreme-value copula theory. Mai (2018), Sections 1–3, treats precisely the general expected-scaled-maximum construction and cites the established Galambos family; (10) and the underlying copula are not originality claims. The new mathematical target is instead the **joint coupling of all \(k(k-1)\) directed extremes from the shared point sample, their asymptotically independent denominator blocks, and the resulting complete Hilbert-distance covariance pattern** including its exact universal \(1/3\) incident-edge correlation. Neither that geometric coupling nor that full edge-array implication was found in the inspected sources. Nielsen and Sun (2023), Section 2.2, also use the same closed-form full-logarithm Hilbert simplex distance for graph embeddings; their random-data experiments do not establish the distance-array limit for independent volume-uniform simplex points. Cohen and Fausti (2023) analyze contractivity and the probability-simplex Hilbert metric, rather than distances among independent uniformly sampled points.

## Limitations

The result assumes fixed \(k\), independent Euclidean-volume-uniform points, and arbitrary full-dimensional simplices as \(N\to\infty\). It does not cover growing sample size, nonuniform Dirichlet parameters, general convex bodies, or arbitrary projectively invariant sampling laws. The individual copula (10), the deterministic metric identity, and the stochastic exponential normalization are pre-existing ingredients. The independent history search cannot establish universal first priority; multivariate extreme-value literature beyond the inspected primary works may offer other formulations of some of the dependence identities. No independent mathematical audit has been performed.

## References

1. Thomas Foertsch and Anders Karlsson, *Hilbert metrics and Minkowski norms*, arXiv:math/0407197, first publicly posted 2004-07-12, https://arxiv.org/abs/math/0407197 . Full text, introduction and Sections 1–3 inspected.
2. Bas Lemmens, *Nonexpansive mappings on Hilbert's metric spaces*, 2011, Section 4 (particularly the logarithmic variation-norm identification), https://www.kent.ac.uk/smsas/personal/bl81/v38n1-03.pdf . Full paper material inspected.
3. Jan-Frederik Mai, *Extreme-value copulas associated with the expected scaled maximum of independent random variables*, arXiv:1802.10330, 2018, https://arxiv.org/html/1802.10330v1 . Full text, Sections 1–3 and the Galambos example inspected.
4. Frank Nielsen and Ke Sun, *Non-linear Embeddings in Hilbert Simplex Geometry*, Proceedings of Machine Learning Research 221 (2023), Section 2.2, https://proceedings.mlr.press/v221/nielsen23a.html . Primary paper, Hilbert metric formula, experiments and conclusion inspected.
5. Samuel N. Cohen and Eliana Fausti, *Hyperbolic contractivity and the Hilbert metric on probability measures*, arXiv:2309.02413, first publicly posted 2023-09-05, https://arxiv.org/abs/2309.02413 . Accessible full-text introduction, results and relevant definitions inspected.
