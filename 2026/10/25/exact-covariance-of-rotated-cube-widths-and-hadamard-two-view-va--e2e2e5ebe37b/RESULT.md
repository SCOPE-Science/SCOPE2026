# Exact covariance of rotated cube widths and Hadamard two-view variance reduction

## Finding
For every integer \(d\ge2\), let \(Q_d=[-1/2,1/2]^d\) and choose one Haar-uniform unit vector \(U\in\mathbb S^{d-1}\). For an arbitrary real orthogonal matrix \(R\), write \(W_0=w_{Q_d}(U)\) and \(W_R=w_{RQ_d}(U)\), where \(w_K(u)=\max_{x\in K}\langle x,u\rangle-\min_{x\in K}\langle x,u\rangle\). Thus both widths use the *same* random direction. Define
\[
\mu_d=\frac{d\,\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
 g(s)=\sqrt{1-s}+\sqrt{s}\arcsin\sqrt{s}\quad(0\le s\le1).
\]
The complete cross-orientation second-moment law is
\[
\boxed{\operatorname{Cov}(W_0,W_R)=\frac{2}{d\pi}\sum_{i,j=1}^d g(R_{ij}^2)-\mu_d^2.}
\]
It obeys the all-dimensional quantitative bound
\[
\boxed{\operatorname{Cov}(W_0,W_R)\ge C_d^\flat+\frac{1}{12\pi d}\sum_{i,j=1}^d\left(R_{ij}^2-\frac1d\right)^2,\qquad C_d^\flat=\frac{2d}{\pi}g(1/d)-\mu_d^2<0.}
\]
Equality in the *first* inequality occurs exactly when all \(|R_{ij}|=d^{-1/2}\), namely when \(\sqrt d\,R\) is a real Hadamard matrix. Therefore \(C_d^\flat\) is the attained minimum over rotations whenever a real Hadamard matrix of order \(d\) exists (including all powers of two). When no such matrix exists, the displayed lower bound is not claimed to be the attainable minimum. Furthermore
\[
 C_d^\flat=-\frac{1}{6\pi d}+O(d^{-2})\qquad(d\to\infty).
\]
An explicit non-Hadamard-dimensional negative-covariance example is \(d=3\) with \(R=I_3-\frac23\boldsymbol{1}\boldsymbol{1}^{\mathsf T}\), giving \(\operatorname{Cov}(W_0,W_R)\approx-0.0092446935\). For \(d=4\), the optimal covariance is
\[
 C_4^\flat=\frac{4\sqrt3}{\pi}+\frac23-\frac{256}{9\pi^2}\approx-0.01004253081.
\]
In each attainable order, the two identical marginal random widths thus form a negatively correlated pair, and their arithmetic mean is a lower-variance unbiased mean-width estimator than independent directional sampling.

## Assumptions and scope
All dimensions are integers \(d\ge2\); \(R\in O(d)\) and \(U\) is Haar-uniform on the unit sphere. Cube edges have length one. By symmetry of the cube, changing an orthogonal matrix determinant by a column sign does not change the width functional, so any flat-entry orthogonal frame can be represented by a proper rotation as well. The expectation is over a single, shared direction; drawing independent directions would give zero cross covariance irrespective of \(R\). The constant \(C_d^\flat\) is a universal lower bound in every dimension and a true global minimum *only* when a real Hadamard matrix of that order exists.

## Proof
**Width identity and normalization.** Since \(Q_d\) is the Minkowski sum of its \(d\) centered unit coordinate segments,
\[
 W_0=\sum_{i=1}^d|U_i|,\qquad W_R=\sum_{j=1}^d |(R^{\mathsf T}U)_j|.
\]
For \(U\) Haar-uniform, \(\mathbb E|U_i|=\Gamma(d/2)/(\sqrt\pi\Gamma((d+1)/2))\), so both means equal \(\mu_d\).

**Exact two-directional absolute moment.** Fix any unit vectors \(a,b\in\mathbb R^d\) with scalar product \(c\in[-1,1]\). Let \(G\) be a standard Gaussian vector and write \(G=T U\), where the radius \(T=\|G\|_2\) is independent of the Haar direction \(U\) and \(\mathbb E T^2=d\). The pair \((\langle G,a\rangle,\langle G,b\rangle)\) is standard bivariate Gaussian with correlation \(c\). Direct integration of its folded-normal density (or conditioning on one coordinate and integrating) gives
\[
 \mathbb E|\langle G,a\rangle\langle G,b\rangle|=\frac2\pi\bigl(\sqrt{1-c^2}+c\arcsin c\bigr).
\]
Dividing by \(\mathbb ET^2=d\) and using the evenness in \(c\) yields \(\mathbb E|\langle U,a\rangle\langle U,b\rangle|=2g(c^2)/(d\pi)\). Apply this identity to the standard coordinate basis and the columns of \(R\), sum over all \(d^2\) pairs, and subtract \(\mu_d^2\). This proves the boxed covariance formula, including \(d=2\) and zero or unit matrix entries.

**Global quantitative minimization.** The kernel has the integral representation
\[
 g'(s)=\frac12\int_0^1(1-st^2)^{-1/2}\,dt,\qquad
 g''(s)=\frac14\int_0^1t^2(1-st^2)^{-3/2}\,dt\ge\frac1{12},
\]
first on \(0\le s<1\), extending with the appropriate one-sided interpretation at \(1\). The lower bound in the second derivative implies
\[
 g(s)\ge g(1/d)+g'(1/d)(s-1/d)+\frac1{24}(s-1/d)^2.
\]
Because orthogonality gives \(\sum_{ij}R_{ij}^2=d\), the total linear contribution cancels. Multiplying by \(2/(d\pi)\) proves the explicit quadratic defect estimate. The inequality is strict for every non-flat frame, since the defect sum is positive. A frame with \(R_{ij}^2=1/d\) is equivalent to a normalized real Hadamard matrix. No existence assertion is made in non-Hadamard orders.

**Strict negativity and asymptotics.** Average \(\operatorname{Cov}(W_0,W_R)\) over a Haar-uniform \(R\), independent of \(U\). Conditional on \(U\), the rotated direction \(R^{\mathsf T}U\) is uniform, so the averaged covariance is exactly zero. The continuous function \(R\mapsto\operatorname{Cov}(W_0,W_R)\) is strictly positive at \(R=I\), because \(W_0\) is nonconstant. As all its values are at least \(C_d^\flat\), the Haar average zero forces \(C_d^\flat<0\). Finally Taylor expansion gives \(g(s)=1+s/2+s^2/24+O(s^3)\) at zero and the gamma-ratio expansion gives
\[
 \mu_d^2=\frac{2d}{\pi}+\frac1\pi+\frac{1}{4\pi d}+O(d^{-2});
\]
substitution yields \(C_d^\flat=-1/(6\pi d)+O(d^{-2})\).

**Variance-reduction interpretation.** The same absolute-moment identity gives
\[
 \operatorname{Var}(W_0)=v_d=1+\frac{2(d-1)}\pi-\mu_d^2>0.
\]
Therefore \(\operatorname{Var}[(W_0+W_R)/2]=(v_d+\operatorname{Cov}(W_0,W_R))/2\). At any Hadamard orientation it is strictly below \(v_d/2\), the variance of the average of two *independently directed* widths, and below \(v_d\), the single-view variance. For \(d=4\) the ratio of the Hadamard two-view variance to the one-view variance is approximately \(0.31960306245\).

## Verification
The standalone `check_width_covariance.py` uses direct cube-vertex projection checks in dimensions two through four, independent quasi-Monte Carlo directional sampling in dimensions two, three, four, and eight, hundreds of randomly sampled non-flat orthogonal frames to check the global inequality numerically, and high-precision large-dimension asymptotic diagnostics. The numerical tests corroborate the exact analytical proof; no finite test substitutes for its all-dimensional quantifiers. Run `python check_width_covariance.py` with NumPy, SciPy and mpmath available. The checker prints `ALL_ROTATED_HYPERCUBE_WIDTH_COVARIANCE_CHECKS_OK` upon passing.

## Relationship to prior work
The 2009 orthogonal-matrix work of Banica--Collins--Schlenker and Banica--Nechita's 2012 \(p\)-norm extension already show that flat-entry Hadamard frames extremize general entrywise matrix norms when they exist. **No originality is asserted for the abstract Hadamard matrix flattening principle or its equality criterion.** Finch (2011) computes one-body cube width moments, and Kabluchko--Litvak--Zaporozhets (2015) develop Gaussian representations and cube-width moments and limits. The distinct result here is the exact *mixed, same-direction* rotated-cube width covariance as a function of the complete relative orientation, its sign and quantitative orientation defect, and the resulting variance reduction of a paired geometric estimator. These are not provided by the cited one-body moments or the abstract matrix norm bounds alone, although the minimizer calculation uses familiar Jensen/convexity machinery. Priority may depend on other, as-yet-unlocated mixed-width literature.

## Limitations
The model is two congruent *Euclidean cubes* in a shared Haar viewing direction; no conclusion is claimed for arbitrary convex bodies, correlated non-Haar viewing directions, or a rotation-independent distribution of each pair. The universal lower bound is potentially unattainable in orders without real Hadamard matrices; no non-Hadamard-order global optimizer is classified. The proof is an analytical calculation and does not establish independent validation or definitive historical priority.

## References
1. T. Banica, B. Collins, J.-M. Schlenker, *On orthogonal matrices maximizing the 1-norm*, arXiv:0901.2923v1 (public 2009-01-19), https://arxiv.org/html/0901.2923v1.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1 (public 2011-10-04), https://arxiv.org/abs/1110.0671.
3. T. Banica, I. Nechita, *Almost Hadamard matrices: the case of arbitrary exponents*, arXiv:1211.2669v1 (public 2012-11-12), https://arxiv.org/html/1211.2669v1.
4. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1 (public 2015-11-26), https://arxiv.org/html/1511.08479v3.
