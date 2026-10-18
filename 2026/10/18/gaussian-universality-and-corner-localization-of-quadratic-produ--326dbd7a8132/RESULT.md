# Gaussian universality and corner localization of quadratic product-polynomial projectors

## Finding
Let \(\mu\) be a symmetric Borel probability measure on \([-1,1]\) with both endpoints in its topological support. Put
\[
s=\int_{-1}^1 t^2\,d\mu(t)>0,\qquad
h=\int_{-1}^1t^4\,d\mu(t)-s^2>0.
\]
Write \(S=\operatorname{supp}\mu\) and \(\mu_d=\mu^{\otimes d}\). Let \(P_d:L^2(\mu_d)\to L^2(\mu_d)\) be the orthogonal projection onto restrictions of polynomials of **total degree at most two**. It acts as a bounded map from \(L^\infty(\mu_d)\) to itself. Its reproducing kernel is \(K_d\), with Lebesgue function
\[
\Lambda_d(x)=\int_{S^d}|K_d(x,y)|\,d\mu_d(y),\qquad x\in S^d.
\]
For \(q_d(x)=d^{-1}\sum_{i=1}^d x_i^2\), the following **uniform spatial profile** holds:
\[
\boxed{\lim_{d\to\infty}\sup_{x\in S^d}
\left|\frac{\Lambda_d(x)}d-\frac{2q_d(x)}{s\sqrt{2\pi e}}\right|=0.}
\]
Therefore
\[
\boxed{\lim_{d\to\infty}\frac{\|P_d\|_{L^\infty\to L^\infty}}d
=\frac{2}{s\sqrt{2\pi e}}.}
\]
Moreover, every sequence \(x^{(d)}\in S^d\) obeys
\[
\frac{\Lambda_d(x^{(d)})}{\|P_d\|_{L^\infty\to L^\infty}}\longrightarrow1
\quad\Longleftrightarrow\quad
\frac1d\sum_{i=1}^d\bigl(1-(x_i^{(d)})^2\bigr)\longrightarrow0.
\]
In other words, asymptotic extremizers concentrate their empirical squared coordinates at the endpoint value; there is no assertion that a corner is an exact finite-dimensional maximizer.

Two central cases are normalized volume on the cube, with \(s=1/3\), and the product arcsine law, with \(s=1/2\):
\[
\lim_{d\to\infty}\frac{\|P_d^{\mathrm{Legendre}}\|_\infty}{d}
=\frac6{\sqrt{2\pi e}},\qquad
\lim_{d\to\infty}\frac{\|P_d^{\mathrm{Chebyshev}}\|_\infty}{d}
=\frac4{\sqrt{2\pi e}}.
\]
As a non-Jacobi example, the marginal that gives half its mass to the uniform law and half to symmetric atoms at the endpoints has \(s=2/3\) and coefficient \(3/\sqrt{2\pi e}\). More generally the Jacobi marginal density proportional to \((1-t^2)^\alpha\), \(\alpha>-1\), has \(s=(2\alpha+3)^{-1}\), and hence the coefficient \(2(2\alpha+3)/\sqrt{2\pi e}\).

## Assumptions and scope
The ground field may be real or complex. The marginal law is fixed as the dimension \(d\to\infty\); it is symmetric, supported in \([-1,1]\), has endpoints in its support, and has \(s,h>0\). No smoothness or density assumption is imposed. The result concerns the **continuous orthogonal projector**, not discrete hyperinterpolation or the full tensor-degree-two projector. All limits are in dimension, with polynomial total degree fixed at two.

## Proof
**1. Exact kernel.** The first three normalized univariate orthogonal polynomials are
\[
p_0(t)=1,\quad p_1(t)=\frac{t}{\sqrt{s}},\quad
p_2(t)=\frac{t^2-s}{\sqrt h}.
\]
Independence and symmetry give the complete orthonormal basis for total degree at most two: \(1\), the \(p_1(x_i)\), the \(p_2(x_i)\), and the \(p_1(x_i)p_1(x_j)\) with \(i<j\). Consequently
\[
K_d(x,y)=1+\frac1s\sum_i x_iy_i+
\frac1h\sum_i(x_i^2-s)(y_i^2-s)
+\frac1{s^2}\sum_{i<j}x_ix_jy_iy_j.
\tag{1}
\]
The endpoint norm of the integral operator equals \(\sup_{x\in S^d}\Lambda_d(x)\): the upper bound is immediate, and the lower bound follows for any fixed \(x\) by choosing the bounded measurable sign of \(K_d(x,\cdot)\); the resulting projection is continuous, so its supremum on the support equals its essential supremum.

**2. The lower-order terms vanish uniformly after division by dimension.** Let \(Y=(Y_1,\ldots,Y_d)\sim\mu_d\). Denote by \(R_d(x,Y)\) the first three terms of (1). Orthonormality yields, exactly,
\[
\mathbb E|R_d(x,Y)|^2=1+\frac1s\sum_i x_i^2+
\frac1h\sum_i(x_i^2-s)^2\le C_\mu d.
\]
Here \(C_\mu\) does not depend on \(d,x\). Thus \(\sup_x\mathbb E|R_d(x,Y)|/d\to0\).

**3. Quadratic chaos.** Put \(B_d=\sum_i x_iY_i\) and \(D_d=\sum_i x_i^2Y_i^2\). The remaining term is exactly
\[
M_d(x,Y)=\frac{B_d^2-D_d}{2s^2}.
\tag{2}
\]
Take an arbitrary triangular array of evaluation points \(x^{(d)}\in S^d\). By compactness, every subsequence of \(q_d=q_d(x^{(d)})\in[0,1]\) has a further subsequence with \(q_d\to q\in[0,1]\). Suppose first \(q>0\). As \(|x_iY_i|\le1\), the Lindeberg condition holds for the independent centered summands, whose total variance is \(sdq_d\). Consequently
\[
\frac{B_d}{\sqrt d}\ \Longrightarrow\ \sqrt{sq}\,Z,
\quad Z\sim N(0,1).
\]
By independence and boundedness, \(\mathbb ED_d/d=sq_d\) and
\[
\operatorname{Var}(D_d/d)
=\frac h{d^2}\sum_i x_i^4\le\frac hd,
\]
so \(D_d/d\to sq\) in \(L^2\). Continuous mapping and (2) give
\[
\frac{M_d(x^{(d)},Y)}d
\ \Longrightarrow\ \frac q{2s}(Z^2-1).
\tag{3}
\]
The family is uniformly integrable: by orthogonality of the mixed-coordinate basis,
\[
\mathbb E\left|\frac{M_d(x,Y)}d\right|^2
=\frac1{s^2d^2}\sum_{i<j}x_i^2x_j^2
\le\frac{q_d(x)^2}{2s^2}\le\frac1{2s^2}.
\tag{4}
\]
Therefore convergence of absolute first moments follows from (3). If \(q=0\), the right side of (4) tends to zero, yielding the same conclusion directly.

**4. Constant and uniformity.** Integration by parts against the standard normal density \(\varphi\) gives
\[
\mathbb E|Z^2-1|=4\varphi(1)=\frac4{\sqrt{2\pi e}}.
\]
Combining steps 2–3 for every convergent sequence \(q_d\) yields
\[
\frac{\Lambda_d(x^{(d)})}{d}\longrightarrow
\frac{2q}{s\sqrt{2\pi e}}.
\]
If the asserted uniform profile failed, a violating sequence of evaluation points would admit a subsequence with convergent \(q_d\), contradicting this sequential limit. This proves the uniform assertion.

**5. Sharp norm and extremizer localization.** Every \(x\in S^d\) satisfies \(q_d(x)\le1\); because the endpoints belong to \(S\), any corner \(x\in\{-1,1\}^d\) has \(q_d(x)=1\). The uniform profile gives the sharp norm limit. Dividing the profile by the positive norm limit proves the equivalence characterizing asymptotically maximizing point sequences. The Jacobi moment formula follows from elementary Beta integrals.

## Verification
The standalone script `checker.py` provides exact rational evaluations of the univariate moments, checks the two equivalent kernel representations, and verifies \(\mathbb E[K_d(x,Y)^2]=K_d(x,x)\) by direct polynomial integration for dimensions one through four. Deterministic Monte Carlo checks on uniform, arcsine and mixture product samples of dimensions eighty and three hundred twenty approach the two predicted constants. The script is a **finite consistency test**, not the proof of the central limit theorem or the uniform limit.

Run from the directory containing `checker.py` with `python checker.py`. Python 3.10+ and NumPy are required; no downloaded data are required.

## Relationship to prior work
Trefethen (2016) distinguishes total, Euclidean, and maximal degree for multivariate approximation in the hypercube and studies convergence of analytic polynomial approximants as degree increases. This provides the motivation for fixing the total-degree space, but does not supply the dimension-asymptotic endpoint norm of its degree-two orthogonal projection. Caliari, De Marchi, and Vianello (2008) analyze three-dimensional **discrete hyperinterpolation** under the product Chebyshev measure, primarily increasing polynomial degree. Their operator and asymptotic regime differ from this continuous projection in increasing dimension.

Published results on quadratic Walsh and Johnson spectral projectors concern finite association-scheme domains or homogeneous Fourier chaos, not continuous Jacobi product polynomial projections with separate diagonal-degree-two summands. Their Gaussian-looking constants alone do not imply the general variance-law or uniform corner-localization statement here. The formula should nevertheless be checked against broader polynomial-chaos and projection-constant literature before any external originality certification.

## Limitations
The theorem is an asymptotic law with fixed marginal \(\mu\) and polynomial degree exactly two. It gives neither an exact finite-dimensional norm nor a sharp convergence rate. The endpoint-support and quadratic nondegeneracy hypotheses are used to specify the corner geometry and orthogonal basis. The result makes no claim for changing marginals, nonsymmetric laws, or total degrees three and higher. The literature comparison is a bounded search rather than a proof of publication priority, and there is no independent audit.

## References
- L. N. Trefethen, *Multivariate polynomial approximation in the hypercube*, arXiv:1608.02216v1 (first publicly submitted 2016-08-07), https://arxiv.org/abs/1608.02216 .
- M. Caliari, S. De Marchi, and M. Vianello, *Hyperinterpolation in the cube*, Computers & Mathematics with Applications 55 (2008), 2490–2497, doi:10.1016/j.camwa.2007.10.003 ; author manuscript https://www.math.unipd.it/~demarchi/papers/CMA.pdf .
