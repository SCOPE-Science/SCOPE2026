# One-switch and zero-plateau law for multiscale circular coverage gaps

## Finding

Let \(n\ge3\) and sample \(n\) independent uniform points on a unit circle. Let \(S_1,\ldots,S_n\) be the clockwise circular spacings, and for \(0<t<1\) write
\[
G_n(t)=\sum_{i=1}^n\mathbf 1\{S_i>t\}.
\]
This counts uncovered connected gaps after placing a clockwise arc of length \(t\) at every sampled point. (When the circle is covered, the count is zero.) Nested coverage yields \(G_n(b)\le G_n(a)\) for \(a\le b\), but **the covariance of these nested counts may be strictly negative**.

**Theorem (complete two-threshold sign law).** For every integer \(n\ge3\) and every \(0<a\le b<1\),
\[
\operatorname{Cov}(G_n(a),G_n(b))=
 n\bigl[(1-b)^{n-1}+(n-1)(1-a-b)_+^{n-1}
       -n(1-a)^{n-1}(1-b)^{n-1}\bigr], \tag{1}
\]
where \(z_+=\max\{z,0\}\). Define the critical smaller radius
\[
\alpha_n=1-n^{-1/(n-1)}\in(1/n,1/2). \tag{2}
\]
Then the covariance signs on the entire triangle \(0<a\le b<1\) are as follows.

1. If \(0<a<\alpha_n\), set
\[
 b_n(a)=1-\frac{a}{1-\left(\frac{n(1-a)^{n-1}-1}{n-1}\right)^{1/(n-1)}}. \tag{3}
\]
One has \(a<b_n(a)<1-a\), and the covariance is positive for \(a\le b<b_n(a)\), zero only at \(b=b_n(a)\), and negative for \(b_n(a)<b<1\).
2. If \(a=\alpha_n\), the covariance is positive for \(a\le b<1-a\) and **exactly zero on the whole interval** \(1-a\le b<1\). These zero-covariance random variables are not independent.
3. If \(a>\alpha_n\), the covariance is positive for every \(a\le b<1\).

**Corollary (the classical spacing scale).** For fixed real \(0<x\le y\),
\[
 \lim_{n\to\infty}\frac{1}{n}\operatorname{Cov}
 \bigl(G_n(x/n),G_n(y/n)\bigr)
 = e^{-y}-(1+xy)e^{-(x+y)}. \tag{4}
\]
For fixed \(x>0\), the single finite sign-change point has the sharp limit
\[
\lim_{n\to\infty} n b_n(x/n)=\frac{e^x-1}{x}>x. \tag{5}
\]
Also \(\alpha_n\sim(\log n)/n\), which is the natural maximum-spacing scale. The asymptotic covariance kernel is included as a consistency check with earlier spacing-limit theory, not as an independently asserted novelty.

## Assumptions and scope

The points are iid continuous uniform locations on the circle. The count uses **strict** exceedance; equalities of spacings and prescribed thresholds have probability zero. Thresholds are deterministic, may be unequal, and lie in \((0,1)\). The theorem concerns a fixed finite sample of size \(n\ge3\), and the corollary the stated deterministic triangular array. Neither the count at one threshold nor its covariance at two thresholds is claimed to determine a joint distribution or independence.

## Proof

**1. Simplex-volume identity.** Rotating the sample so that one sampled point is at the origin, the other ordered locations have constant order-statistic density. Hence \((S_1,\ldots,S_n)\) is uniform on the simplex \(\{s_i>0:\sum_i s_i=1\}\), equivalently \(\operatorname{Dirichlet}(1,\ldots,1)\). For distinct indices \(i_1,\ldots,i_k\) and nonnegative numbers \(t_1,\ldots,t_k\), translating these \(k\) coordinates by their required lower bounds scales the simplex volume by the \((n-1)\)-st power of the remaining total length. Thus
\[
 \Pr\{S_{i_j}>t_j\ \text{for all }j\}
 =\left(1-\sum_{j=1}^{k}t_j\right)_+^{n-1}. \tag{6}
\]
In particular, \(\mathbb E G_n(a)=n(1-a)^{n-1}\). For \(a\le b\), a *single* spacing exceeds both thresholds with probability \((1-b)^{n-1}\), whereas *two distinct* spacings exceed their respective thresholds with probability \((1-a-b)_+^{n-1}\). Summing the \(n\) diagonal and \(n(n-1)\) off-diagonal contributions to \(\mathbb E[G_n(a)G_n(b)]\), then subtracting the product of means, proves (1).

**2. Sign reduction.** The positive factor \(n(1-b)^{n-1}\) can be extracted from (1), giving
\[
 \frac{\operatorname{Cov}(G_n(a),G_n(b))}{n(1-b)^{n-1}}
 = 1-n(1-a)^{n-1}
 +(n-1)\left(\frac{(1-a-b)_+}{1-b}\right)^{n-1}. \tag{7}
\]
For \(b<1-a\), the last ratio equals \(1-a/(1-b)\); it is strictly decreasing in \(b\). For \(b\ge1-a\), it is zero. The sign at the endpoint of the decreasing interval is the sign of \(1-n(1-a)^{n-1}\), which is negative, zero, or positive precisely as \(a\) is below, at, or above \(\alpha_n\).

For \(0<a<\alpha_n\), one has \(a<1/2\). At \(b=a\), the covariance is the strictly positive variance of \(G_n(a)\). To see the variance is positive, if \(a<1/n\) then the simplex contains positive-volume neighborhoods having all spacings above \(a\) and others with one below \(a\). For \(1/n\le a<1/2\), there are positive-volume neighborhoods with exactly one and with exactly two spacings exceeding \(a\). (Take one or two large coordinates and distribute the remaining positive mass among sufficiently small coordinates.) Therefore the strictly decreasing expression (7) crosses zero exactly once before \(b=1-a\). Solving (7) for its unique zero yields (3), and also proves \(a<b_n(a)<1-a\). All asserted signs for \(a<\alpha_n\) follow. At \(a=\alpha_n\), equation (7) is positive while \(b<1-a\) and zero thereafter. Above that critical value it is positive everywhere. Finally, Bernoulli's strict inequality \((1-1/n)^{n-1}>1/n\) and \(n<2^{n-1}\) establish the inclusions claimed in (2).

**3. Zero covariance need not mean independence.** Set \(a=\alpha_n\) and \(b\ge1-a\). Since \(a+b\ge1\), any spacing larger than \(b\) forces every other spacing below \(a\). Consequently \(G_n(b)=1\) implies \(G_n(a)=1\), and \(G_n(a)G_n(b)=G_n(b)\) almost surely. Since \(\mathbb E G_n(a)=1\), the covariance is zero. But \(a>1/n\) ensures \(\Pr\{G_n(a)=0\}>0\) (near equal spacings), and \(\Pr\{G_n(b)=1\}>0\) (one spacing close to one). Thus the two variables cannot be independent: the first cannot be zero when the second is one, despite both events having positive marginal probability.

**4. Asymptotic consequence.** With \(a=x/n\) and \(b=y/n\), expand the three powers in (1) using \(\log(1-z/n)=-z/n-z^2/(2n^2)+O(n^{-3})\) for fixed \(z\). The order-\(n\) terms cancel, leaving (4). Equivalently, (7) tends uniformly for bounded \(y\) to \(1-e^{-x}(1+xy)\), so its unique zero tends to \(y=(e^x-1)/x\), giving (5) by bracketing on either side. The strict inequality \(e^x>1+x^2\) for \(x>0\) shows the limit exceeds \(x\). Finally (2) gives \(\alpha_n=1-\exp[-(\log n)/(n-1)]\sim(\log n)/n\).

## Verification

The accompanying standard-library script `verify.py` checks equation (7) in exact rational arithmetic on 7,000+ threshold/sample-size cases, checks convergence of an independent positive-integer-composition discretization to the continuous simplex prediction, verifies critical zero bands and strict one-switch samples, and compares (4) and (5) numerically at increasing sample sizes. It also samples normalized independent exponential variables, which realize the Dirichlet spacings. Run `python verify.py`; the expected terminal output begins with `PASS`. These finite calculations corroborate, but do not replace, the exact volume and monotonicity proof above. All boundaries, including \(b=1-a\), use exact theoretical identities, not a floating-point sign test.

## Relationship to prior work

The Dirichlet spacing law, the exact one-threshold distribution of uncovered gaps, and ordinary spacing asymptotics are classical and are not claimed as new. Huillet (2003), especially Proposition 4 and formula (5), calculates the **one-radius** gap-count distribution and limit regimes in the same circle-covering model. Mirakhmedov (2024), Proposition 2.2 and the subsequent corollaries, gives general **asymptotic** variance and normal-limit formulas for sums of spacing scores. These broader techniques may imply the asymptotic covariance kernel (4) by polarization; the novelty assessed here is the entire **finite** two-threshold sign diagram, explicit moving transition (3), and nonindependent zero-covariance plateau at (2). Holst and Hüsler (1984) discuss joint limiting distributions of gap count with other coverage observables **at a single radius**; its complete article was not available for material-level comparison and is a residual priority risk.

## Limitations

This theorem is restricted to independent uniform circle points and deterministic clockwise arc lengths. It establishes covariance signs, not positive/negative association or independence, nor a multivariate central limit theorem. The explicit threshold is for the uniform-simplex distribution and need not apply to nonuniform points or random arc lengths. The historical-priority search is incomplete: an implicit derivation from older general spacing-moment theory or inaccessible same-object literature remains possible. Independent verification has not been performed.

## References

1. S. M. Mirakhmedov, *The central limit theorem for sum-functions of m-tuples of spacings*, arXiv:2404.09581, first publicly posted 2024-04-15. https://arxiv.org/abs/2404.09581
2. T. Huillet, *Random covering of the circle: the size of the connected components*, Advances in Applied Probability **35** (2003), 563–582, doi:10.1239/aap/1059486818. https://doi.org/10.1239/aap/1059486818
3. L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability **21** (1984), 558–566, doi:10.2307/3213617. https://doi.org/10.2307/3213617
4. H. Solomon, *Geometric Probability*, chapter 4, historical one-threshold coverage formulas. https://doi.org/10.1137/1.9781611970418.ch4
