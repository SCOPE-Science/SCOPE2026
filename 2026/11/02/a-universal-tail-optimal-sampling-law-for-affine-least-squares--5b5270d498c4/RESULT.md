# A universal tail-optimal sampling law for affine least squares

## Finding

Let \(m\ge2\) be an integer, let \(a<b\) be finite real numbers, and let \(B\in\mathbb R^{2\times2}\) be symmetric positive definite. Draw \(X_1,\ldots,X_m\) independently from a continuous, nonnegative probability density \(p\) on \([a,b]\). Form the unweighted two-column design and information matrix
\[
F=\begin{pmatrix}1&X_1\\\vdots&\vdots\\1&X_m\end{pmatrix},\qquad G=F^{\mathsf T}F,
\]
and measure its inverse-information amplification by \(R_B=\operatorname{tr}(BG^{-1})\). The matrix \(G\) is invertible almost surely. Set
\[
\rho=\frac{m-1}{2},\quad q_B(t)=(-t,1)B(-t,1)^{\mathsf T},\quad
v_{m-1}=\frac{\pi^\rho}{\Gamma(\rho+1)}.
\]
Then the following exact, positive tail constant exists:
\[
\boxed{\lim_{z\to\infty}z^\rho\Pr(R_B>z)
=\sqrt m\,v_{m-1}\int_a^b p(t)^m q_B(t)^\rho\,dt.}
\]
Consequently, for every \(s>0\), the moment \(\mathbb E[R_B^s]\) is finite if and only if \(s<\rho\); the boundary moment diverges.

**A universal optimal design.** Over all continuous nonnegative probability densities on \([a,b]\), the displayed tail constant has the unique minimizer
\[
\boxed{p_B^*(t)=\frac{q_B(t)^{-1/2}}{Z_B},\qquad
Z_B=\int_a^b q_B(u)^{-1/2}\,du.}
\]
The minimum constant is \(\sqrt m\,v_{m-1}Z_B^{1-m}\). Remarkably, \(p_B^*\) does not depend on the sample size \(m\), even though the failure-tail exponent and constant do.

For the Euclidean coefficient-loss metric \(B=I_2\), on \([-L,L]\) the unique optimal density is
\[
p^*(t)=\frac{1}{2\operatorname{arsinh}(L)\sqrt{1+t^2}}.
\]
For example, at \(L=10\) and \(m=4\), uniform independent input sampling has a leading failure-tail coefficient approximately \(6.943939037987\) times the optimum. This comparison concerns the \(z\to\infty\) tail, not every finite error threshold.

## Assumptions and scope

The input density \(p\) is continuous on the compact interval, nonnegative everywhere, and integrates to one. No strict lower bound for \(p\) is required. The matrix \(B\) is fixed independently of \(p\), and is strictly positive definite. The samples are identically distributed and independent, with no reweighting of the least-squares objective. In a well-specified affine regression with independent observation errors of conditional covariance \(\sigma^2 I_m\), the conditional quadratic parameter/prediction risk with loss matrix \(B\) is \(\sigma^2 R_B\). The mathematical distributional statement itself requires no observation-noise model.

## Proof

**1. Exact inverse-information identity.** With
\[
\overline X=\frac1m\sum_{i=1}^m X_i,\qquad
S=\sum_{i=1}^m(X_i-\overline X)^2,
\]
we have \(\det G=mS\), and \(S>0\) almost surely because the observations have a continuous common density. Direct inversion gives, with \(B=(b_{ij})\),
\[
G^{-1}=\frac1S\begin{pmatrix}\overline X^2&-\overline X\\-\overline X&1\end{pmatrix}
+\frac1m\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
\boxed{R_B=\frac{q_B(\overline X)}{S}+\frac{b_{11}}m.}
\]
This formula is exact for every nonconstant sample and all fixed \(B\succ0\).

**2. Sharp small-scatter volume.** Write the observation vector uniquely as \((X_1,\ldots,X_m)=t\mathbf1+u\), where \(t=\overline X\) and \(u\) belongs to the Euclidean hyperplane \(H=\{u\in\mathbb R^m:\sum_i u_i=0\}\). Its dimension is \(m-1\); \(S=\|u\|^2\), and the orthogonal-change-of-variables Jacobian is
\[
dX_1\cdots dX_m=\sqrt m\,dt\,d\operatorname{vol}_H(u).
\]
For \(z>b_{11}/m\), the event \(R_B>z\) is exactly the ball condition
\[
\|u\|^2<\frac{q_B(t)}{z-b_{11}/m}.
\]
Since \(B\succ0\), the function \(q_B\) is strictly positive and bounded on \([a,b]\). Substitute \(u=v/\sqrt{z-b_{11}/m}\). After multiplication by \(z^{(m-1)/2}\), the probability becomes an integral over \(t\in[a,b]\) and the uniformly bounded ball \(\|v\|^2<q_B(t)\) in \(H\). Its integrand is the product
\[
\prod_{i=1}^m p\left(t+\frac{v_i}{\sqrt{z-b_{11}/m}}\right)
\prod_{i=1}^m\mathbf1_{[a,b]}\left(t+\frac{v_i}{\sqrt{z-b_{11}/m}}\right),
\]
where values of \(p\) outside \([a,b]\) are immaterial because of the indicators. For almost every \(t\) strictly between the endpoints, this converges pointwise to \(p(t)^m\). Continuity makes \(p\) bounded and supplies an integrable dominating function on the bounded integration domain. Dominated convergence therefore yields
\[
\sqrt m\int_a^b p(t)^m\operatorname{vol}_{m-1}
\{v\in H:\|v\|^2<q_B(t)\}\,dt
=\sqrt m\,v_{m-1}\int_a^b p(t)^m q_B(t)^\rho\,dt.
\]
This proves the full asymptotic constant, including endpoint handling. The constant is strictly positive because any continuous probability density is positive on some interval and \(q_B>0\).

**3. Sharp moment threshold.** For each \(s>0\) and nonnegative random variable \(R_B\), the layer-cake formula reads
\[
\mathbb E[R_B^s]=s\int_0^\infty z^{s-1}\Pr(R_B>z)\,dz.
\]
The positive, finite tail constant makes the large-\(z\) integrand comparable to \(z^{s-1-\rho}\). Thus the integral converges precisely for \(s<\rho\), and diverges for \(s\ge\rho\). In particular, the unconditional conditional-risk expectation is infinite for \(m=2,3\) and finite for \(m\ge4\).

**4. Unique global density optimum.** Hölder's inequality, using \(\rho=(m-1)/2\), gives
\[
1=\int_a^b p(t)\,dt
\le\left(\int_a^b p(t)^m q_B(t)^\rho\,dt\right)^{1/m}
\left(\int_a^b q_B(t)^{-1/2}\,dt\right)^{(m-1)/m}.
\]
Hence \(\int p^m q_B^\rho\ge Z_B^{1-m}\). Equality in Hölder requires \(p(t)\) proportional to \(q_B(t)^{-1/2}\) almost everywhere. This positive continuous density is normalized by \(Z_B\) and achieves equality. Continuity upgrades almost-everywhere uniqueness to pointwise uniqueness, proving the asserted optimum for all \(m\ge2\).

## Verification

Run `python3 verify.py` with Python 3.10 or newer; only the standard library is used. The supplied verifier completed 1,528 checks. It includes 660 exact-rational sample configurations, separately checking positivity and the exact inverse-information identity; numerical quadrature of the Hölder equality, of strict perturbation gaps and of the actual two-observation rare-event probability; and comparisons of the analytic coefficient for different metrics, sample sizes and intervals. The independent direct tail integrations approach the predicted sharp coefficient. The analytic proof above, not numerical sampling or the finite checker, establishes the infinite-parameter theorem and uniqueness.

## Relationship to prior work

Chkifa and Dolbeault (2023) study randomized least-squares recovery with minimal oversampling, including conditioning of random information matrices and the advantage of dependent sampling. Their mathematical theorems concern alternative sampling algorithms, approximation-error criteria, and finite-sample spectral bounds rather than the exact iid affine inverse-information tail constant or its globally optimal continuous density. Mourtada (2019) treats lower tails and inverse moments of random sample covariance matrices at general dimension, but its lower-tail inequalities do not supply this two-column collision-volume coefficient or its minimizing density. Dereziński, Clarkson, Mahoney, and Warmuth (2019) study optimal experimental design and joint/importance sampling to control expected regression errors; their distributional design problem and performance criteria differ from optimizing this exact extreme-tail constant. A related planar unit-vector observability calculation has the same exponent but constant-norm observation rows, whereas the affine design rows \((1,t)\) have variable norm; the specific density optimum here is not a direct specialization of that unit-vector statement.

## Limitations

This is a fixed-sample, extreme-threshold asymptotic result for a two-parameter affine model with unweighted iid continuous inputs. The optimal density minimizes only the leading \(z\to\infty\) tail coefficient, not necessarily finite-threshold failure probabilities, mean risk, condition number, or classical A-optimal design criteria. The coefficient metric \(B\) must remain fixed when the sampling law changes. The theorem does not cover higher-degree regression, weighted least squares, dependent or adaptive input selection, or arbitrary input distributions with atoms. Its publication novelty requires assessment against any specialized earlier work on small-scatter geometry and extreme-tail experimental design not located in the checked sources.

## References

1. A. Chkifa and M. Dolbeault, *Randomized least-squares with minimal oversampling and interpolation in general spaces*, first publicly posted 12 June 2023, arXiv:2306.07435, https://arxiv.org/abs/2306.07435 .
2. J. Mourtada, *Exact minimax risk for linear least squares, and the lower tail of sample covariance matrices*, first publicly posted 23 December 2019, arXiv:1912.10754, https://arxiv.org/abs/1912.10754 .
3. M. Dereziński, K. L. Clarkson, M. W. Mahoney and M. K. Warmuth, *Minimax experimental design: Bridging the gap between statistical and worst-case approaches to least squares regression*, COLT/PMLR 99 (2019), pp. 1050–1069, https://proceedings.mlr.press/v99/derezinski19b.html .
