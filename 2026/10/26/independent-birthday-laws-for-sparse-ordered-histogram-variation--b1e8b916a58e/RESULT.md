# Independent birthday laws for sparse ordered-histogram variation

## Finding

The null variation of a sparsely populated ordered histogram is governed jointly with the ordinary occupancy-collision count by two asymptotically **independent** birthday laws. The assertion is quantitative, and also gives exact finite formulas for the probability of maximal variation.

For integers \(n\ge2\) and \(N\ge2\), take independent uniform labels \(U_1,\ldots,U_N\in\{1,\ldots,n\}\), let \(X_j=\#\{a:U_a=j\}\), and define
\[
T=\sum_{j=1}^{n-1}|X_{j+1}-X_j|,\qquad
C=\sum_{1\le a<b\le N}\mathbf1\{U_a=U_b\}.
\]
Set
\[
\lambda_0=\frac{\binom N2}{n},\qquad
\lambda_1=\frac{2(n-1)\binom N2}{n^2},\quad
q_n=\frac{3n-2}{n^2},\quad s_n=\frac{9n-10}{n^3},
\]
and the explicit nonnegative error bound
\[
\mathcal B_{n,N}=\frac{2N}{n}+
\frac{2(n-1)N(N-1)(N-2)}{n^3}+
2\binom N2\left[(2N-3)q_n^2+2(N-2)s_n\right].
\]
For independent \(P_0\sim\operatorname{Pois}(\lambda_0)\) and \(P_1\sim\operatorname{Pois}(\lambda_1)\),
\[
\boxed{
 d_{\mathrm{TV}}\!\left(\mathcal L(C,2N-T),\mathcal L(P_0,2P_1)\right)
 \le\min\{1,\mathcal B_{n,N}\}.}
\]
Here \(d_{\mathrm{TV}}\) is the supremum of the absolute probability difference over measurable events; the second Poisson variable is multiplied by two. In particular, the bound tends to zero whenever \(n\to\infty\) and \(N=o(n^{2/3})\).

The resulting simultaneous phase classification, for sequences of integer sample sizes \(N=N_n\ge2\), is:

* If \(N/\sqrt n\to0\), then \((C,2N-T)\to(0,0)\) in probability.
* If \(N/\sqrt n\to c\in(0,\infty)\), then \((C,2N-T)\) converges in total variation to \((P,2Q)\), with **independent** \(P\sim\operatorname{Pois}(c^2/2)\) and \(Q\sim\operatorname{Pois}(c^2)\). Thus, for fixed nonnegative integers \(j,k\),
\[
\Pr\{C=j,\ T=2N-2k\}\longrightarrow
 e^{-3c^2/2}\frac{(c^2/2)^j}{j!}\frac{(c^2)^k}{k!}.
\]
* If \(\sqrt n\ll N\ll n^{2/3}\), then
\[
\left(\frac{C-\lambda_0}{\sqrt{\lambda_0}},\ 
\frac{(2N-T)/2-\lambda_1}{\sqrt{\lambda_1}}\right)
\Longrightarrow (G_0,G_1),
\]
where \(G_0,G_1\) are **independent** standard normal variables.

There are also exact formulas, valid without asymptotic assumptions:
\[
\boxed{\Pr\{T=2N\}=\frac1{n^N}
\sum_{k=1}^{\min\{N,\lfloor(n-1)/2\rfloor\}}
\binom{n-k-1}{k}\,k!\,\left\{\begin{matrix}N\\k\end{matrix}\right\},}
\]
where the braces are Stirling numbers of the second kind, and
\[
\boxed{\Pr\{C=0,\ T=2N\}=\begin{cases}
 (n-N-1)_{\underline N}/n^N,&n\ge2N+1,\\
 0,&n<2N+1,
\end{cases}}
\]
with \((a)_{\underline N}=a(a-1)\cdots(a-N+1)\).

## Assumptions and scope

The bin ordering is linear, not cyclic. Every sample label is independent and uniform; no independence is assumed between the statistics \(C\) and \(T\) before taking the limit. The finite bound applies to all integers \(n,N\ge2\), including parameter values at which it exceeds one (when only the trivial upper bound is informative). The asymptotic conclusions concern the explicitly stated simultaneous limits and make no assertion when \(N\) is of order \(n^{2/3}\) or larger.

## Proof

**1. A deterministic variation-defect identity.** Define \(Z=\sum_{j=1}^{n-1}\min(X_j,X_{j+1})\). Using \(|a-b|=a+b-2\min(a,b)\) and summing over adjacent cells gives the exact pathwise identity
\[
2N-T=X_1+X_n+2Z.
\]
Also put
\[
W=\sum_{j=1}^{n-1}X_jX_{j+1}
=\sum_{1\le a<b\le N}\mathbf1\{|U_a-U_b|=1\}.
\]
For nonnegative integers \(a,b\), \(ab-\min(a,b)\le a(a-1)b+ab(b-1)\). Therefore \(W\ge Z\) and
\[
0\le\mathbb E(W-Z)
\le\sum_{j=1}^{n-1}\mathbb E[(X_j)_2X_{j+1}+X_j(X_{j+1})_2]
=\frac{2(n-1)(N)_3}{n^3},
\]
where \((N)_3=N(N-1)(N-2)\). Moreover \(\Pr\{X_1+X_n>0\}\le2N/n\). Consequently, under the original sampling coupling,
\[
\Pr\{(C,2N-T)\ne(C,2W)\}
\le\frac{2N}{n}+\frac{2(n-1)(N)_3}{n^3}.
\]

**2. A two-color rare-pair process.** Index all unordered pairs of sample positions \(e=\{a,b\}\), with a color \(t=0\) for equal labels and \(t=1\) for labels one bin apart. The Bernoulli indicators are
\[
I_{e,0}=\mathbf1\{U_a=U_b\},\qquad
I_{e,1}=\mathbf1\{|U_a-U_b|=1\}.
\]
Their color-specific means are \(1/n\) and \(2(n-1)/n^2\); their aggregates are exactly \(C\) and \(W\). Use the dependency neighborhood of \((e,t)\) consisting of all colored pairs whose underlying sample-position pair intersects \(e\). Outside this neighborhood the indicator is independent of the entire outside family, so the conditional-dependence term of Arratia--Goldstein--Gordon is zero. Summing both colors,
\[
\Pr\{|U_a-U_b|\le1\}=q_n=\frac{3n-2}{n^2},
\]
and for distinct \(a,b,c\),
\[
\Pr\{|U_a-U_b|\le1,\ |U_a-U_c|\le1\}
=s_n=\frac{9n-10}{n^3}.
\]
(The two boundary labels have two permitted neighbors including themselves; the \(n-2\) interior labels have three.) The first AGG dependency sum is
\[
b_1=\binom N2(2N-3)q_n^2.
\]
For the second sum, two different colors on the same sample pair cannot occur together; each sample pair has exactly \(2(N-2)\) other pairs sharing one sample position. Thus
\[
b_2=\binom N2\,2(N-2)s_n.
\]
The multivariate Poisson-process approximation in Arratia, Goldstein and Gordon (1989, Theorem 2) bounds the standard total-variation distance between the colored indicator process and independent Poisson coordinates by \(2(b_1+b_2)\). Summing the coordinates by color is a measurable map and cannot increase total variation. It follows that
\[
d_{\mathrm{TV}}\!\left(\mathcal L(C,W),\operatorname{Pois}(\lambda_0)\otimes\operatorname{Pois}(\lambda_1)\right)
\le 2(b_1+b_2).
\]
Combine this with the preceding coupling and apply the triangle inequality to obtain the displayed finite \(\mathcal B_{n,N}\) bound. No independence between overlapping pairs has been assumed.

**3. The birthday, Gaussian and extreme-value consequences.** As \(n\to\infty\), the bound is \(O(N/n+N^3/n^2)\); both terms vanish for \(N=o(n^{2/3})\). The Poisson parameters are \(\lambda_0\sim N^2/(2n)\) and \(\lambda_1\sim N^2/n\) whenever \(N\to\infty\). Their subcritical and critical limits yield the first two regimes; when both means diverge, the elementary standardized Poisson central limit theorem plus total-variation contraction and weak convergence yields the two independent Gaussians.

Finally, \(T=2N\) if and only if the two endpoint bins are empty and no two adjacent bins are both occupied. If exactly \(k\) interior bins are occupied, their locations form a size-\(k\) independent set in the path on \(n-2\) vertices, of which there are \(\binom{n-k-1}{k}\). Assigning \(N\) labeled observations onto those \(k\) bins gives \(k!\left\{\begin{smallmatrix}N\\k\end{smallmatrix}\right\}\) possibilities. Summation proves the first exact formula. Adding \(C=0\) forces all \(N\) labels to be distinct: the locations must be an independent set of size \(N\) among the interior bins, and there are \(N!\binom{n-N-1}{N}=(n-N-1)_{\underline N}\) assignments. This proves the second formula.

## Verification

Run `python3 verify.py` using the provided standard-library-only script. It performs exact enumerations of all ordered samples for bin counts from two through six and sample sizes from two through five, checks both rare-event kernels, the pathwise variation and collision identities, the two coupling bounds, the finite bivariate total-variation inequality, and both exact maximum-event counts. It also reports separately labeled seeded simulation diagnostics. The recorded run passed 75,160 finite assertions and produced 60,000 simulated histograms. Finite checks supplement, rather than prove, the asymptotic argument.

## Relationship to prior work

Banić and Elezović introduce and calibrate the same discrete variation statistic in their 2026 Comb Test paper, whose finite-sample dynamic program computes its exact null law. Their subsequent Part 1 (October 9, 2026) treats means, and Part 2 (October 12, 2026) develops finite formulas and large-sample fixed-bin variance asymptotics. The present claim is instead a uniform, **simultaneously growing** sparse-regime distributional law with an explicit two-color total-variation error and independence from the usual pair-collision statistic. Exact finite computation does not itself state this simultaneous asymptotic. The classic birthday and near-birthday Poisson techniques, notably Arratia--Goldstein--Gordon's theorem, are indispensable known inputs; their general approximation result is not claimed as new.

## Limitations

The conclusion does not establish optimality of the \(N=o(n^{2/3})\) range, a nonsparse limit, an asymptotic power theorem for a statistical test, or a cyclic version. The same authors mention prospective separate analyses of sparse and null-distribution regimes, and a previously unlocated treatment might imply all or part of the result. The new contribution asserted here is the displayed model-specific variation/collision theorem and its exact extremal counts, not the original Chen--Stein machinery. Independent mathematical validation has not been performed.

## References

1. N. Banić and N. Elezović, *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation*, arXiv:2606.01465, first submitted 2026-05-31. https://arxiv.org/abs/2606.01465
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1, 2026-10-09. https://arxiv.org/abs/2610.13366
3. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 2: variance under the uniform null*, arXiv:2610.17046v1, 2026-10-12. https://arxiv.org/html/2610.17046v1
4. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen--Stein Method*, Annals of Probability 17 (1989), 9--25, Theorems 1--2. https://doi.org/10.1214/aop/1176991491
