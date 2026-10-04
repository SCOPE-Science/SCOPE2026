# A finite-sample tail obstruction for Gaussian linear cross-HSIC
## Finding
Consider the studentized cross-HSIC statistic introduced by Shekhar, Kim and Ramdas, specialized to scalar linear kernels. The data consist of \(2n\) iid pairs, split into two halves of size \(n\), and the null model here is that the two coordinates are independent nondegenerate Gaussian variables. Write \(T_n\) for the published studentized statistic.

The finite-sample null law has a sharp qualitative change at the first admissible half-sample sizes. If \(n=3\), then \(T_3\) is exactly arcsine distributed on \((-1,1)\):
\[
\Pr(T_3\in dt)=\frac{dt}{\pi\sqrt{1-t^2}},\qquad -1<t<1.
\]
If \(n\ge4\), then \(T_n\) has unbounded support. More quantitatively, for each fixed \(n\ge4\) there are constants \(c_n,t_n>0\) for which
\[
\Pr(|T_n|>t)\ge c_n t^{-(n-1)}\qquad(t\ge t_n).
\]
Therefore
\[
\mathbb E|T_n|^p=\infty\qquad\text{for every }p\ge n-1.
\]
In particular, the Gaussian-null statistic with half-sample size \(n=4\) has no finite third absolute moment, even though the source theorem establishes a standard-normal limit as \(n\to\infty\).

## Assumptions and scope
The kernels are \(k(x,x')=xx'\) and \(\ell(y,y')=yy'\). The \(2n\) observed pairs are iid. Under the null, \(X\) and \(Y\) are independent Gaussian variables with arbitrary means and strictly positive variances. Translation and nonzero scale factors cancel from the studentized statistic, so the proof reduces to independent standard Gaussians.

No statement is made here about nonlinear kernels, non-Gaussian nulls, exact tail asymptotics for \(n\ge4\), or finiteness of \(\mathbb E|T_n|^p\) for \(p<n-1\). The denominator vanishes only on a null set under the stated Gaussian model, so assigning any value there leaves the distribution unchanged.

## Proof
For the first half, set
\[
a_i=X_i-\bar X,\qquad b_i=Y_i-\bar Y,\qquad z_i=a_i b_i,
\]
and define
\[
C=\sum_{i=1}^n z_i,\qquad Q=\sum_{i=1}^n\left(z_i-\frac Cn\right)^2.
\]
For linear kernels, the source definition has
\[
h_{ij}=\frac12(X_i-X_j)(Y_i-Y_j).
\]
The ordered-pair identity
\[
\sum_{i\ne j}h_{ij}=nC
\]
gives \(f_1=C/(n-1)\). If \(f_2\) is the analogous independent second-half factor, then the unstudentized cross-HSIC is \(f_1f_2\). For the jackknife term in the source definition,
\[
\frac1{n-1}\sum_{j\ne i} h_{ij}f_2
=\frac{f_2}{2(n-1)}(nz_i+C).
\]
Subtracting \(f_1f_2\), squaring, and inserting the published normalization yields
\[
s_n^2=\frac{f_2^2n^2}{(n-1)(n-2)^2}Q.
\]
Since \(f_2\ne0\) almost surely under a nondegenerate Gaussian null,
\[
T_n=\operatorname{sgn}(f_2)\frac{(n-2)C}{\sqrt{n(n-1)Q}}. \tag{1}
\]

Let \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and let \(P\) be orthogonal projection onto \(H\). Under the Gaussian null, the centered residual vectors can be written as independent radial parts times independent Haar-uniform directions \(u,v\) on the unit sphere of \(H\). The radial factors cancel in (1). Thus, with
\[
F(u,v)=P(u\circ v),
\]
where \(\circ\) denotes coordinatewise multiplication,
\[
|T_n|=\frac{n-2}{\sqrt{n(n-1)}}\frac{|u\cdot v|}{\|F(u,v)\|}. \tag{2}
\]

For \(n=3\), use the orthonormal basis
\[
e_1=\frac1{\sqrt2}(1,-1,0),\qquad e_2=\frac1{\sqrt6}(1,1,-2)
\]
of \(H\), and write \(u=\cos A\,e_1+\sin A\,e_2\) and \(v=\cos B\,e_1+\sin B\,e_2\), with \(A,B\) independent uniform angles. Direct expansion gives
\[
u\cdot v=\cos(A-B),\qquad \|F(u,v)\|^2=\frac16.
\]
Equation (2) therefore gives \(|T_3|=|\cos(A-B)|\); the independent sign from \(f_2\) preserves the symmetric arcsine law.

Now take \(n\ge4\). A nonzero denominator zero in (2) occurs whenever every coordinate is nonzero, \(\sum_i u_i=0\), \(\sum_i u_i^{-1}=0\), and \(v\) is proportional to \((u_i^{-1})_i\). Then \(u_iv_i\) is constant in \(i\), so \(F(u,v)=0\), while \(u\cdot v\ne0\).

For \(n=4\), one such point is obtained from the unnormalized vectors
\[
u_0=(1,-1,2,-2),\qquad v_0=(1,-1,1/2,-1/2).
\]
After normalization they lie on the two spheres in \(H\). Tangent bases may be chosen as
\[
(-3/2,1/2,1,0),\ (1/2,-3/2,0,1)
\]
for the \(u\)-sphere and
\[
(-3/4,-1/4,1,0),\ (-1/4,-3/4,0,1)
\]
for the \(v\)-sphere. In the first three coordinates of \(H\), three derivative columns of \(F\) have determinant \(-15/16\), up to the nonzero global normalization factors of \(u_0,v_0\). Hence \(DF\) has rank \(3=n-1\).

For every \(n\ge5\), choose a zero with at least five distinct nonzero coordinates in \(u\). For odd \(n\), start with
\[
1,\ 2,\ 3,\ -3+\frac{3\sqrt{77}}{11},\ -3-\frac{3\sqrt{77}}{11},
\]
whose sum and reciprocal sum are both zero, and append distinct pairs \((r,-r)\) as needed. For even \(n\ge6\), use distinct pairs \((r,-r)\), for example \((1,-1),(2,-2),(3,-3)\) and further distinct pairs. Normalize \(u\), and take \(v\) proportional to its coordinatewise reciprocal.

To verify regularity, suppose \(w\in H\) is orthogonal to the range of \(DF\) at such a zero. Orthogonality against the two tangent spaces implies
\[
w\circ v\in\operatorname{span}\{\mathbf1,u\},\qquad
w\circ u\in\operatorname{span}\{\mathbf1,v\}.
\]
Since \(v_i\) is proportional to \(u_i^{-1}\), every distinct coordinate \(u_i\) must be a root of one quartic polynomial
\[
A t^4+B t^3-Ct-D.
\]
Five distinct roots force all four coefficients to vanish, and then \(w=0\). Thus \(DF\) is surjective onto the \((n-1)\)-dimensional space \(H\).

At each displayed regular zero, \(|u\cdot v|\) is nonzero. The submersion theorem therefore supplies local coordinates \((y,z)\), with \(y\in\mathbb R^{n-1}\), in which \(F=y\), the Haar product density is smooth and bounded below, and the numerator in (2) stays bounded away from zero. A fixed neighborhood of the zero manifold consequently satisfies
\[
\Pr(|T_n|>t)\ge c_n t^{-(n-1)}
\]
for all sufficiently large \(t\). Integrating the tail identity for absolute moments gives divergence for every \(p\ge n-1\).

## Verification
The accompanying `verify.py` checks the exact linear-kernel reduction on deterministic rational data, verifies the rank-three \(n=4\) Jacobian certificate by exact rational elimination, checks the algebra behind the five-coordinate odd construction, and numerically stress-tests the \(n=3\) identity on several angles. These computations support the algebraic steps; the infinite tail and moment statements rely on the proved submersion argument, not on finite simulation.

## Relationship to prior work
Shekhar, Kim and Ramdas define the studentized cross-HSIC statistic and, for scalar linear kernels, derive its asymptotic standard-normal null behavior. Their paper explicitly presents the linear case as a warmup for the general theory and analyzes asymptotic validity, power, and moment conditions on the underlying kernel variables. The inspected definition, linear-kernel section, and appendix reduction do not state a finite-sample Gaussian tail lower bound, an infinite-moment result for the studentized statistic, or the \(n=3\) versus \(n\ge4\) geometric transition.

Kim and Ramdas develop the broader cross-U-statistic strategy of sample splitting and self-normalization and likewise focus on Gaussian limiting inference. Classical work on Studentized U-statistics supplies asymptotic approximations under moment assumptions. Targeted searches for cross-HSIC high moments, denominator singularities, and exact Gaussian finite-sample laws did not locate the statement above. The \(n=3\) arcsine marginal resembles classical correlation geometry and is not asserted as a stand-alone novelty claim; the finding is the combined finite-sample phase transition and polynomial-tail obstruction for the published cross-HSIC studentizer.

## Limitations
The lower bound \(t^{-(n-1)}\) is one-sided: no matching upper bound or exact tail constant is proved. The result does not establish whether moments of order below \(n-1\) are finite. It applies only to scalar linear kernels under an independent Gaussian null. Older general literature on ratios and Studentized U-statistics may contain abstract results that imply part of the moment-divergence mechanism under different notation; no such direct implication was found in the inspected searches.

## References
1. S. Shekhar, I. Kim, and A. Ramdas, “A Permutation-Free Kernel Independence Test,” arXiv:2212.09108v1, first posted 2022-12-18; Journal of Machine Learning Research 24(369), 2023, 1–68.
2. I. Kim and A. Ramdas, “Dimension-agnostic inference using cross U-statistics,” arXiv:2011.05068, first posted 2020-11-10; Bernoulli 30(1), 2024, 683–711.
3. M. M. Nasari, “Studentized Processes of U-statistics,” arXiv:0906.5101, 2009.
4. MSC 62H20, Measures of association (correlation and related dependence measures), MSC2020.
