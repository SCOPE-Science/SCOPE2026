# Conditioning removes a leading variance term from multinomial histogram roughness

## Finding
Fix a positive real occupancy load \(\lambda\). For every \(n\ge2\), let \(N=N(n)\) be an integer such that \(N/n\to\lambda\), and let \((X_1,\ldots,X_n)\sim\operatorname{Mult}(N;1/n,\ldots,1/n)\). Define the noncyclic discrete histogram total variation
\[
D_{n,N}=\sum_{i=1}^{n-1}|X_{i+1}-X_i|.
\]
For independent \(A,B,C\sim\operatorname{Pois}(\lambda)\), put
\[
m=\mathbb E|A-B|,\quad h=\mathbb E(|A-B|\,|B-C|),\quad
c=\operatorname{Cov}(|A-B|,A+B).
\]
Then the **finite-load variance law** is
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Var}(D_{n,N})}{n}
=V(\lambda):=2\lambda+2h-3m^2-\frac{c^2}{\lambda}>0.}
\]
The correction \(-c^2/\lambda\) is essential: independent Poissonization gives the wrong coefficient for a fixed-sample multinomial histogram. The strictly positive coefficient has two distinct endpoint scales:
\[
\boxed{V(\lambda)=4\lambda^2-12\lambda^3+O(\lambda^4)
\quad (\lambda\downarrow0),}
\]
\[
\boxed{\frac{V(\lambda)}{\lambda}\longrightarrow
\frac83+\frac{4\sqrt3-12}{\pi}=1.052263614148\ldots
\quad(\lambda\to\infty).}
\]
In particular, the apparent order-\(\lambda\) Poisson fluctuations cancel in the sparse-load fixed-sample variance; adjacent occupied bins govern the leading quadratic order instead.

## Assumptions and scope
The counts have a **fixed total** \(N\), uniform multinomial cell probabilities, and a path of \(n\) ordered cells with \(n-1\) adjacent differences. Both \(n\) and \(N\) tend to infinity, with the positive finite ratio \(N/n\to\lambda\). The formula concerns a variance limit, not a distributional central limit theorem. Definitions of \(m,h,c\) use three independent Poisson random variables of the same mean; all moments are finite. No monotonicity of \(V\) is claimed. Limits in \(\lambda\) are limits of the already identified coefficient \(V(\lambda)\), not statements uniform in changing load sequences.

## Proof
**1. Local Poisson approximation through the first conditioning correction.** Set \(\lambda_n=N/n\). For any fixed \(k\in\{2,3,4\}\) and nonnegative integers \((x_1,\ldots,x_k)\), with \(s=\sum_jx_j\), the exact multinomial marginal is
\[
\frac{(N)_s}{n^s\prod_jx_j!}\left(1-\frac{k}{n}\right)^{N-s}.
\]
Relative to the joint mass of \(k\) independent \(\operatorname{Pois}(\lambda_n)\) variables this has expansion
\[
1+\frac{A_k(s;\lambda_n)}n+o(n^{-1}),\qquad
A_k(s;\lambda)=-\frac{s(s-1)}{2\lambda}+ks-\frac{k^2\lambda}{2}.
\]
The remainder can be summed against any fixed-degree polynomially bounded function of the \(k\) coordinates, uniformly for \(\lambda_n\) in compact subsets of \((0,\infty)\). One rigorous truncation uses \(s\le L\log n\), Taylor remainder \(O((1+s)^4/n^2)\), and exponentially small Poisson and multinomial tails outside the truncation (taking \(L\) sufficiently large). Consequently marginal moments have the displayed first-order expansion.

**2. Diagonal and neighboring edges.** Let \(F_i=|X_{i+1}-X_i|\). The expansion with two and three coordinates gives
\[
\operatorname{Var}(F_i)\longrightarrow 2\lambda-m^2,
\qquad
\operatorname{Cov}(F_i,F_{i+1})\longrightarrow h-m^2.
\]
The first identity uses \(\mathbb E(A-B)^2=2\lambda\). There are \(n-1\) diagonal terms and \(n-2\) unordered neighboring pairs in the variance sum.

**3. Disjoint edges and the global constraint.** Write \(g(a,b)=|a-b|\), \(U=A+B\), and take an independent copy \((g',U')\). Substituting \(A_4(U+U')\) and \(A_2(U)\) in the first-order expansion yields
\[
\lim_{n\to\infty} n\operatorname{Cov}(F_i,F_j)
=\mathbb E[gg'A_4(U+U')]-2m\mathbb E[gA_2(U)]
=-\frac{(\mathbb E[gU]-2\lambda m)^2}{\lambda}
=-\frac{c^2}{\lambda}
\]
whenever the edges are disjoint (\(|i-j|>1\)). The calculation is independent of their separation because the multinomial occupancy vector is exchangeable. There are \((n-2)(n-3)/2\) unordered disjoint pairs. Dividing the full variance by \(n\), the preceding three contributions give
\[
(2\lambda-m^2)+2(h-m^2)-c^2/\lambda=V(\lambda).
\]
Continuity of Poisson moments in \(\lambda\) also covers sequences with \(N/n\to\lambda\) without any specified rate.

**4. Strict positivity.** Let \(Y_1,Y_2\) be independent Poisson variables, and perform the symmetric Hoeffding decomposition
\[
g(Y_1,Y_2)=m+H(Y_1)+H(Y_2)+K(Y_1,Y_2),
\]
where \(H(x)=\mathbb E[g(x,Y_2)]-m\), and \(\mathbb E[K(x,Y_2)]=0\) for every \(x\). For an independent Poisson chain, degeneracy removes covariances between distinct adjacent \(K\)-terms and between any \(K\)-term and any one-site term. Thus
\[
V(\lambda)=\mathbb E[K(Y_1,Y_2)^2]
+4\left(\operatorname{Var}(H(Y_1))-
\frac{\operatorname{Cov}(H(Y_1),Y_1)^2}{\lambda}\right).
\]
The bracket is nonnegative by Cauchy–Schwarz. The kernel variance is **strictly** positive: if \(K\) vanished, \(g\) would be additively separable, contradicting
\(g(0,0)+g(1,1)-g(0,1)-g(1,0)=-2\).
All four configurations have positive Poisson probability.

**5. Endpoint scales.** The Poisson series truncated through cubic order gives
\[
m=2\lambda-2\lambda^2+2\lambda^3+O(\lambda^4),\quad
h=\lambda+2\lambda^3+O(\lambda^4),\quad
c=2\lambda-4\lambda^2+6\lambda^3+O(\lambda^4).
\]
Substitution into \(V\), keeping the necessary fourth-order terms when evaluating \(c^2/\lambda\), gives \(4\lambda^2-12\lambda^3+O(\lambda^4)\); these expansions follow by enumerating total Poisson counts up to four, with the remaining mass bounded by \(O(\lambda^5)\). For large \(\lambda\), the normalized two adjacent differences converge jointly to centered Gaussians with unit variances and correlation \(-1/2\). Their absolute Gaussian covariance, from
\[
\mathbb E|Z_1Z_2|=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right),
\]
is \(\frac16+(\sqrt3-2)/\pi\) at \(\rho=-1/2\). Gaussian second-moment convergence gives the leading two edge terms. The Skellam mean formula \(m=2\lambda e^{-2\lambda}[I_0(2\lambda)+I_1(2\lambda)]\) and the Poisson score identity \(c=\lambda m'(\lambda)\) imply \(c^2/\lambda=O(1)\). The displayed large-load constant follows.

## Verification
The accompanying self-contained program `verify.py` checks the exact multinomial first- and second-moment identities by exhaustive small-size enumeration, evaluates the Poisson coefficient by independent truncated sums, checks the disjoint-edge first-order correction numerically, and compares with seeded multinomial simulation at fixed load. It also checks the small- and large-load coefficient scales. These finite calculations are consistency checks; the infinite statements use the preceding analytic proof.

## Relationship to prior work
Banić and Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null* (arXiv:2610.13366, first submitted October 9, 2026), derive an exact **expectation** and related expansions in other regimes. Their earlier *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation* (arXiv:2606.01465, May 31, 2026) computes finite null distributions by dynamic programming and uses a simulated gamma approximation. These finite-law methods permit computation of finite moments, but the new result isolates the analytic proportional-load variance coefficient and the nonvanishing sample-size-conditioning correction, including its sparse- and dense-load scalings. Prior fixed-category large-deviation results for the same statistic concern a different regime. Primary manuscripts could not all be reviewed in full; the originality conclusion is therefore qualified by a residual risk of an implicit equivalent in material not accessible during this investigation.

## Limitations
The theorem gives a second-moment limit, not a central limit theorem or a finite-sample confidence interval. The limit assumes equal bin probabilities and a path adjacency pattern; nonuniform histograms or arbitrary graphs require additional analysis. Computation of finite null distributions was previously available, and no claim is made to have invented the statistic or the underlying Poisson approximation. The main added information is the explicit analytic **fixed-sample** variance profile under a simultaneous increasing-bin and increasing-sample limit.

## References
1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366 (first publicly posted October 9, 2026).
2. N. Banić and N. Elezović, *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation*, arXiv:2606.01465 (first publicly posted May 31, 2026).
3. N. Banić and N. Elezović, *TVOR: Finding Discrete Total Variation Outliers among Histograms*, arXiv:2012.11574 (first publicly posted December 21, 2020).
