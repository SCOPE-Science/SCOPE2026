# A half-density phase transition for Haar mean widths of partial permutohedra

## Finding
For integers \(m\ge2\) and \(n\ge1\), let the partial permutohedron \(P(m,n)\) be the convex hull in \(\mathbb R^m\) of all vectors with entries from \(\{0,1,\ldots,n\}\) whose nonzero entries are pairwise distinct. Let \(w_{m,n}\) denote its Euclidean mean width, averaging the distance between opposite supporting hyperplanes over Haar-uniform unit directions. Let \(G_{(1)}\ge\cdots\ge G_{(m)}\) be descending order statistics of independent standard normal random variables, and let \(\mu_m=\sqrt2\,\Gamma((m+1)/2)/\Gamma(m/2)\). Then the exact finite-dimensional formula is

\[
w_{m,n}=\frac{2}{\mu_m}\sum_{j=1}^{\min(m,n)}(n-j+1)\,\mathbb E\bigl[(G_{(j)})_+\bigr].
\]

Each expectation is a one-dimensional integral:

\[
\mathbb E[(G_{(j)})_+]=\frac{m!}{(j-1)!(m-j)!}\int_0^\infty x\,\varphi(x)\,\Phi(x)^{m-j}\bigl(1-\Phi(x)\bigr)^{j-1}\,dx,
\]

where \(\varphi\) and \(\Phi\) are the standard normal density and distribution function. In particular this formula is valid throughout the sparse and dense ranges, including \(n>m\).

If \(n_m/m\to\alpha\in(0,\infty)\), the sharp normalized mean-width limit is

\[
\lim_{m\to\infty}\frac{w_{m,n_m}}{m^{3/2}}=F(\alpha)
=2\int_0^{\min\{\alpha,1/2\}}(\alpha-t)\Phi^{-1}(1-t)\,dt.
\]

For \(\alpha\ge1/2\) it becomes the elementary affine function

\[
F(\alpha)=\frac{2\alpha-1}{\sqrt{2\pi}}+\frac1{2\sqrt\pi}.
\]

The function \(F\) is strictly convex on \((0,1/2)\), is affine on \([1/2,\infty)\), is twice continuously differentiable at \(1/2\), and has the exact third-derivative jump

\[
F'''(1/2+)-F'''(1/2-)=2\sqrt{2\pi}.
\]

## Assumptions and scope
The coordinates use the ordinary Euclidean norm on \(\mathbb R^m\); no centering or rescaling of the defining vertices is imposed. The mean width is
\[
w_{m,n}=\int_{S^{m-1}}\bigl(h_{P(m,n)}(u)+h_{P(m,n)}(-u)\bigr)\,d\sigma(u),
\]
with normalized rotationally invariant spherical measure \(\sigma\) and support function \(h_K(u)=\sup_{x\in K}\langle u,x\rangle\). The finite formula holds for every pair of integers \(m\ge2,n\ge1\). The asymptotic holds for every integer sequence \(n_m\ge1\) satisfying \(n_m/m\to\alpha\) with fixed finite \(\alpha>0\); the derivatives concern the deterministic limiting function, not a derivative of the integer-indexed mean width.

## Proof
**Support-function reduction.** Let \(g\in\mathbb R^m\) have ordered coordinates \(g_{(1)}\ge\cdots\ge g_{(m)}\). To maximize \(\langle g,x\rangle\) over the defining vertices, place the largest available positive label \(n\) on the largest positive coordinate, the next label \(n-1\) on the next positive coordinate, and so forth. Negative coordinates receive zero. Rearrangement and the option to leave entries zero prove, including ties by continuity,
\[
h_{P(m,n)}(g)=\sum_{j=1}^{\min(m,n)}(n-j+1)(g_{(j)})_+.
\]

**Exact mean width.** Let \(G\) be a standard Gaussian vector and write \(G=RU\), where \(R=\|G\|_2\) is independent of Haar-uniform \(U\in S^{m-1}\). Positive homogeneity gives \(\mathbb E h_P(G)=\mathbb E R\,\mathbb E h_P(U)\). Since \(U\) and \(-U\) have the same law, \(w_{m,n}=2\mathbb E h_P(G)/\mu_m\), with \(\mu_m=\mathbb E R\) as stated. Substitution of the support function gives the sum. The standard density for the \(j\)-th largest Gaussian order statistic gives the displayed integral; all terms are finite and nonnegative.

**Proportional-rank limit.** Write \(\alpha_m=n_m/m\), and let \(Q_m(t)=G_{(\lceil mt\rceil)}\) for \(0<t\le1\), using descending order statistics. The preceding support formula can be written *exactly* as
\[
\frac{h_{P(m,n_m)}(G)}{m^2}=\int_0^1\left(\alpha_m-\frac{\lceil mt\rceil-1}{m}\right)_+\bigl(Q_m(t)\bigr)_+\,dt.
\]
For every fixed \(0<t<1\), the empirical-quantile law implies almost surely \(Q_m(t)\to q(t)=\Phi^{-1}(1-t)\). The empirical first moments have uniformly vanishing Gaussian tails: for every threshold \(M\), their contribution above \(M\) converges by the strong law to \(\mathbb E[|G_1|\mathbf1_{|G_1|>M}]\), which tends to zero as \(M\to\infty\). Truncating the quantiles, applying bounded convergence, and then removing the truncation yields almost sure convergence of the last integral to \(\int_0^1(\alpha-t)_+q(t)_+\,dt\). In addition,
\[
0\le\frac{h_P(G)}{m^2}\le C\frac1m\sum_{i=1}^m|G_i|
\]
for a uniform constant \(C\) once \(\alpha_m\) is bounded. The right side has bounded second moments, so the family is uniformly integrable and the expectations converge. Since \(\mu_m/\sqrt m\to1\), the normalized width converges to twice that integral. The normal quantile is positive exactly for \(0<t<1/2\), proving the stated \(F\).

**Affine branch and transition.** Set \(q(t)=\Phi^{-1}(1-t)\). Direct substitution \(t=1-\Phi(x)\) and integration by parts give
\[
\int_0^{1/2}q(t)\,dt=\frac1{\sqrt{2\pi}},\qquad
\int_0^{1/2}tq(t)\,dt=\frac1{2\sqrt{2\pi}}-\frac1{4\sqrt\pi}.
\]
These yield the affine formula for \(\alpha\ge1/2\). For \(0<\alpha<1/2\), differentiation under the integral gives \(F'(\alpha)=2\int_0^\alpha q(t)\,dt\), \(F''(\alpha)=2q(\alpha)>0\), and \(F'''(\alpha)=-2/\varphi(q(\alpha))\). At the boundary, \(q(1/2)=0\) and \(\varphi(0)=1/\sqrt{2\pi}\). Thus \(F\), \(F'\), and \(F''\) match their affine right-hand limits, whereas the left third derivative is \(-2\sqrt{2\pi}\) and the right one zero. This proves the sharp jump.

## Verification
The accompanying `check_width.py` uses exhaustive vertex enumeration for small parameters to verify the rearrangement formula, independent Gaussian numerical integration for the finite mean width, and seeded Gaussian sampling for several proportional-rank limits. Run after installing dependencies from `requirements.txt` with `python check_width.py`. The completed run printed `PARTIAL_PERMUTOHEDRON_GAUSSIAN_WIDTH_CHECKS_PASSED`. These tests corroborate but do not replace the proof for all integers and asymptotic sequences.

## Relationship to prior work
Heuer and Striker (arXiv:2012.09901, Definition 5.4, Proposition 5.7 and Theorem 5.10) introduced partial permutohedra and established their vertices and inequalities. Behrend and collaborators (arXiv:2207.14253, particularly Section 5 and Corollary 5.8) characterized faces and obtained volume and Ehrhart results, including a description by anti-blocking permutohedra. Those results support the underlying finite geometric object and the rearrangement step but do not state its Haar mean width or a proportional-rank limiting width profile. General Gaussian order-statistic and quantile laws are classical ingredients; the evaluated one-dimensional formula and the half-density differentiability transition are the distinct conclusions here. Jochemko and Ravichandran's study of symmetric Minkowski-linear functionals on generalized permutahedra concerns a broader structural class but does not give the specific limiting profile for this family.

## Limitations
The probabilistic expectation is over viewing directions only, not random vertices. The asymptotic assumes a positive finite limiting ratio \(n_m/m\); it does not claim a uniform error bound, rates of convergence, or an asymptotic for \(n_m/m\to0\) or infinity. The finite integral expression is exact but not generally elementary. Historical priority is provisional, especially regarding unindexed calculations of mean widths for anti-blocking permutahedra; no independent mathematical audit has been performed.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first public version 2020-12-17), Sections 5.1–5.4, https://arxiv.org/abs/2012.09901.
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253 (first public version 2022-07-28), Sections 3–6, https://arxiv.org/abs/2207.14253.
3. K. Jochemko and M. Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, Mathematika 68 (2022), 217–236, DOI:10.1112/mtk.12122.
