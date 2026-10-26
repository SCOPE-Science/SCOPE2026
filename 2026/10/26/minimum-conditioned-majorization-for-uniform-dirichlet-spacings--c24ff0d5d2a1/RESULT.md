# Minimum-conditioned majorization for uniform Dirichlet spacings

## Finding
For \(n\ge2\) uniform simplex spacings, conditioning on a larger minimum makes the **entire spacing vector less dispersed in majorization order**, not merely its largest coordinate smaller on average. More precisely, the minimum, its index, and the normalized residual simplex point factor independently; the coupling below realizes pointwise majorization simultaneously for all Schur-convex functionals. A quantitative consequence is
\[
\operatorname{Cov}(m,M)=\frac{1-H_n}{n^3(n+1)}<0,
\qquad H_n=\sum_{j=1}^n\frac1j.
\]
The structural statement and covariance formula are one finding: an exact conditional law that determines global concentration-versus-minimum dependence.

## Assumptions and scope
Fix an integer \(n\ge2\). Let \(X=(X_1,\ldots,X_n)\) be uniformly distributed on the standard probability simplex \(\Delta_{n-1}=\{x_i\ge0,\sum_ix_i=1\}\); equivalently \(X\sim\operatorname{Dirichlet}(1,\ldots,1)\), the random spacings produced by \(n-1\) independent uniform cuts in an interval. Write \(m=\min_iX_i\), \(M=\max_iX_i\), and \(I\) for the unique (almost surely) minimizing index. Define \(Z=(X-m\mathbf1)/(1-nm)\). It has one zero coordinate \(Z_I\) and its remaining coordinates sum to one. At \(n=2\), a one-component \(\operatorname{Dirichlet}(1)\) means the constant one. Define \(H_r=\sum_{j=1}^r1/j\) and \(H_r^{(2)}=\sum_{j=1}^r1/j^2\).

A vector \(x\) *majorizes* \(y\), written \(x\succeq y\), when the sums of its \(k\) largest components are at least those of \(y\) for all \(1\le k<n\), with equal total sums. A symmetric real-valued functional \(F\) on the simplex is Schur-convex when \(x\succeq y\) implies \(F(x)\ge F(y)\). Integrability here is with respect to the uniform Dirichlet law and the conditional laws for almost every \(t\); strictness is asserted only for strictly Schur-convex functions and a nondegenerate minimum distribution.

## Proof
**1. Minimum/residual disintegration.** Uniformity gives, for \(0\le t<1/n\),
\[
\Pr(m\ge t)=(1-nt)^{n-1},\quad f_m(t)=n(n-1)(1-nt)^{n-2}.
\]
For each fixed index \(i\), the region on which \(I=i\) and \(m\) lies between \(t\) and \(t+dt\) is parametrized by \(x_i=t\) and \(x_j=t+(1-nt)z_j\), \(j\ne i\), with \(z_j\ge0\) and \(\sum_{j\ne i}z_j=1\). The Euclidean simplex volume factor from the latter variables is proportional to \((1-nt)^{n-2}\), independent of \(z\). Its same constant applies to every \(i\). Dividing by the normalizer yields \(\Pr(I=i)=1/n\), \(m\) independent of \(I\), and a uniform \(\Delta_{n-2}\) residual point independent of both. In particular \(nm\sim\operatorname{Beta}(1,n-1)\). The \(n=2\) assertion follows directly from the two symmetric halves of the unit interval.

**2. Simultaneous majorization.** Let \(Z\) have that residual distribution, with an independently uniform zero index. For each \(0\le t<1/n\), set \(X_t=t\mathbf1+(1-nt)Z\); this has the regular conditional law of \(X\) given \(m=t\). For \(0\le s<t<1/n\) write
\[
X_t=\lambda X_s+(1-\lambda)\mathbf u,\quad
\lambda=\frac{1-nt}{1-ns}\in(0,1),\quad\mathbf u=(1/n,\ldots,1/n).
\]
Since \(\mathbf u\) is majorized by every probability vector and convex mixing with \(\mathbf u\) preserves component order and decreases each proper top-\(k\) sum, \(X_s\succeq X_t\) **for every realized \(Z\)**. Thus \(g_F(t)=\mathbb E[F(X)\mid m=t]\) is nonincreasing for every integrable Schur-convex \(F\). If \(F\) is strictly Schur-convex, then \(g_F(s)>g_F(t)\): \(X_s\ne X_t\), because the shared \(Z\) has at least one zero coordinate and cannot equal \(\mathbf u\). For an independent copy \(m'\) of \(m\),
\[
2\operatorname{Cov}(m,F(X))
=\mathbb E[(m-m')(g_F(m)-g_F(m'))]\le0.
\]
Strictness follows when appropriate. Replace \(F\) by \(-F\) for the Schur-concave case. Examples include the maximum, sum of squares, and negative Shannon entropy.

**3. Exact extreme covariance.** The residual maximum is the largest of \(n-1\) uniform simplex components, with mean \(H_{n-1}/(n-1)\). This can be derived by the standard inclusion-exclusion identity
\[
\Pr\left(\max_{1\le i\le r}U_i\le x\right)
=\sum_{j=0}^r(-1)^j\binom rj(1-jx)_+^{r-1},\quad r\ge2,
\]
followed by integration, giving \(\mathbb E\max_iU_i=H_r/r\). When \(r=1\) the maximum equals one. Consequently,
\[
\mathbb E[M\mid m=t]=t+(1-nt)\frac{H_{n-1}}{n-1}.
\]
From the beta law, \(\mathbb Em=1/n^2\) and \(\operatorname{Var}(m)=(n-1)/(n^4(n+1))\). Taking covariance against this affine conditional expectation gives
\[
\operatorname{Cov}(m,M)
=\left(1-\frac{nH_{n-1}}{n-1}\right)\frac{n-1}{n^4(n+1)}
=\frac{1-H_n}{n^3(n+1)}.
\]
Since \(H_n>1\) for \(n\ge2\), this is strictly negative. No large-\(n\) approximation is used.

**4. Conditional extreme distribution and independent moment check.** For \(n\ge3\), letting \(r=n-1\) and \(x=(b-t)/(1-nt)\), the inclusion-exclusion formula above gives
\[
\Pr(M\le b\mid m=t)
=\sum_{j=0}^r(-1)^j\binom rj(1-jx)_+^{r-1},\qquad b\ge t.
\]
For \(n=2\), \(M=1-m\) deterministically. Independently, represent \(X\) by \(n\) independent unit-rate exponentials divided by their sum \(S\). The total \(S\sim\operatorname{Gamma}(n,1)\) is independent of the normalized vector; exponential order-statistic increments yield
\[
\mathbb E[E_{(1)}E_{(n)}]=\frac2{n^2}+\frac{H_{n-1}}n,
\quad \mathbb E[S^2]=n(n+1),
\]
so \(\mathbb E[mM]=(2+nH_{n-1})/(n^3(n+1))\), independently confirming the covariance result after subtracting \((1/n^2)(H_n/n)\).

## Verification
The self-contained `verify.py` executes exact rational calculations for \(2\le n\le29\), independently compares the conditional-covariance and exponential-order-statistic formulas, and checks 71 rational conditional-maximum CDF values against derivatives of a separate inclusion-exclusion volume formula for \(3\le n\le8\). All checks completed successfully. These finite tests corroborate the identities; the arbitrary-dimensional conclusion is established by the analytic proof above. Run with `python3 verify.py` from a directory containing the two files.

## Relationship to prior work
Barthe–Gamboa–Lozada-Chang–Rouault (2010), §2.1–§2.2, give Dirichlet simplex laws, gamma normalization, and stick-breaking/partial-sum independence; they do not state an independence decomposition after subtracting the **global smallest component**, nor a coupling ordered by conditional majorization. Monti–Mateu-Figueras–Pawlowsky-Glahn–Egozcue (2011) examine shifted-scaled compositional laws using Aitchison perturbation, distinct from the additive global-minimum disintegration here. Lin (2016), Ch. 2, reviews moments and standard Dirichlet representations but not this conditional majorization. Reznik–Efimov–Soloviev–Torgov (2014) study bounded-length scanning occupancy of random cuts, not the conditional whole-vector dispersion order. Classical spacing studies (Mauldon 1951; Weiss 1959; Pyke 1965) may contain equivalent conditional identities; full comparison with their complete texts remains a priority risk. The novelty claimed is the **simultaneous conditional majorization/dependence principle**, not the marginal law of the maximum or the usual gamma normalization, which are standard.

## Limitations
The result assumes the **uniform** Dirichlet law; the proof's constant-density disintegration fails in general for unequal/other concentration parameters. It concerns symmetric Schur-convex or Schur-concave functionals, not arbitrary functions of the unsorted vector, and uses regular conditional laws at \(0\le t<1/n\). The covariance formula is for a simplex normalized to total length one. It is not a characterization of all dependence or a theorem for nonuniform random cuts. Historical priority remains uncertain because the full text of several classical spacing papers was inaccessible; no independent audit has been performed.

## References
1. F. Barthe, F. Gamboa, L.-V. Lozada-Chang, A. Rouault, *Generalized Dirichlet distributions on the ball and moments*, arXiv:1002.1544, first public 2010-02-08, §2.1–§2.2. https://arxiv.org/abs/1002.1544
2. G. S. Monti, G. Mateu-Figueras, V. Pawlowsky-Glahn, J. J. Egozcue, *The shifted-scaled Dirichlet distribution in the simplex*, CoDaWork 2011. https://congress2.cimne.com/codawork11/Admin/Files/FilePaper/p20.pdf
3. J. Lin, *On the Dirichlet Distribution*, Queen's University, September 2016, Ch. 2. https://mast.queensu.ca/~communications/Papers/msc-jiayu-lin.pdf
4. A. Reznik, V. Efimov, A. Soloviev, A. Torgov, *The Solving of the Problems with Random Division of an Interval with Use of Computer Analytic Programs*, arXiv:1411.6580 (2014). https://arxiv.org/abs/1411.6580
5. J. G. Mauldon, *Random division of an interval*, 1951; L. Weiss, *The Limiting Joint Distribution of the Largest and Smallest Sample Spacings*, 1959; R. Pyke, *Spacings*, 1965. Historical comparisons are limited by inaccessible full texts.
