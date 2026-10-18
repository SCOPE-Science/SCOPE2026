# A quadratic conditioning penalty from Frobenius-optimal diagonal congruence on positive-definite stars

## Finding
For each integer \(d\ge 2\) and each \(0<\rho<1\), the unique positive diagonal congruence minimizing the squared Frobenius error to the identity on the symmetric positive-definite star
\[
A_{d,\rho}=\begin{pmatrix}1&(\rho/\sqrt d)\mathbf 1_d^{\mathsf T}\\(\rho/\sqrt d)\mathbf1_d&I_d\end{pmatrix}
\]
**strictly worsens** the spectral condition number, even though a scalar diagonal is globally condition-number optimal among *all* positive diagonal congruences. In the singular limit the Frobenius-optimal condition number grows quadratically in the original condition number, with the exact constant
\[
\lim_{\rho\uparrow1}\frac{\kappa_2(G_F A_{d,\rho} G_F)}{\kappa_2(A_{d,\rho})^2}=\frac{d-1}{16d}.
\]
Here \(G_F\) is the uniquely minimizing positive diagonal factor. In dimension two (the omitted case \(d=1\)), Frobenius minimization instead produces a scalar factor and no condition-number penalty. Thus dimension three is the smallest dimension of this particular effect.

## Assumptions and scope
Work in real exact arithmetic. Fix an integer \(d\ge1\), \(0<\rho<1\), \(\mathbf1_d=(1,\ldots,1)^\mathsf T\), and the above \((d+1)\)-square matrix. Let \(G=\operatorname{diag}(g_0,g_1,\ldots,g_d)\) have strictly positive entries and define
\[
\mathcal F(G)=\|G A_{d,\rho}G-I\|_F^2,\qquad
\kappa_2(B)=\lambda_{\max}(B)/\lambda_{\min}(B)
\]
for symmetric positive-definite \(B\). The star's eigenvalues are \(1-\rho\), \(1+\rho\), and \(1\) with multiplicity \(d-1\); consequently \(\kappa_2(A_{d,\rho})=(1+\rho)/(1-\rho)\).

Write
\[
a=\frac{1-\rho^2}{1-\rho^4/d},\qquad
b=\frac{1-\rho^2/d}{1-\rho^4/d},\qquad
G_F=\operatorname{diag}(\sqrt a,\sqrt b,\ldots,\sqrt b).
\]
Then \(G_F\) is the unique positive diagonal minimizer of \(\mathcal F\), for every \(d\ge1\). For \(d\ge2\), \(a<b\), and
\[
\kappa_2(G_F A_{d,\rho}G_F)>\kappa_2(A_{d,\rho})
=\min_{G>0\text{ diagonal}}\kappa_2(GA_{d,\rho}G),
\]
where equality in the condition-number minimization occurs **only** when \(G\) is scalar. The Frobenius loss itself strictly improves relative to \(G=I\): \(\mathcal F(G_F)<\mathcal F(I)=2\rho^2\).

## Proof
**(1) Exact Frobenius minimization.** Set \(x=g_0^2\), \(y_i=g_i^2\). A direct entrywise calculation gives
\[
\mathcal F(G)=(x-1)^2+\sum_{i=1}^d(y_i-1)^2+\frac{2\rho^2}{d}x\sum_{i=1}^d y_i.
\]
Its Hessian in these variables is twice the block matrix
\[
H=\begin{pmatrix}1&(\rho^2/d)\mathbf1_d^\mathsf T\\(\rho^2/d)\mathbf1_d&I_d\end{pmatrix}.
\]
The Schur complement of \(I_d\) is \(1-\rho^4/d>0\), so \(H\) is positive definite. The stationarity equations are \(x=1-(\rho^2/d)\sum_i y_i\), \(y_i=1-(\rho^2/d)x\). They have the unique solution \(x=a\) and \(y_i=b\). Both are positive for the stated parameters, hence the unconstrained global minimizer lies inside the admissible positive orthant; it is the unique positive diagonal minimizer. Moreover
\[
b-a=\frac{\rho^2(1-1/d)}{1-\rho^4/d},
\]
positive exactly when \(d>1\). Since \(I\) is not stationary for \(\rho>0\), strict convexity gives \(\mathcal F(G_F)<\mathcal F(I)\).

**(2) Condition-number lower bound and equality characterization.** Let \(v=\mathbf1_d/\sqrt d\) and \(w_\pm=(1,\pm v)^\mathsf T/\sqrt2\). Then \(A_{d,\rho}w_\pm=(1\pm\rho)w_\pm\). For any positive diagonal \(G\), the Rayleigh quotient of \(B=G A_{d,\rho}G\) on \(G^{-1}w_\pm\) is
\[
\frac{(G^{-1}w_\pm)^\mathsf T B(G^{-1}w_\pm)}{\|G^{-1}w_\pm\|_2^2}
=\frac{1\pm\rho}{z},\qquad
z=w_+^\mathsf T G^{-2}w_+=w_-^\mathsf T G^{-2}w_->0.
\]
Thus \(\lambda_{\max}(B)\ge(1+\rho)/z\), \(\lambda_{\min}(B)\le(1-\rho)/z\), giving \(\kappa_2(B)\ge(1+\rho)/(1-\rho)\). If equality holds, both test vectors must attain the corresponding extremal Rayleigh values, hence each \(G^{-1}w_\pm\) is an eigenvector. The eigenvector equations imply \(G^2w_\pm\) is a scalar multiple of \(w_\pm\). Every coordinate of \(w_+\) is nonzero, so diagonal \(G^2\) must be scalar. Conversely every positive scalar \(G\) attains equality. Since \(G_F\) is nonscalar when \(d>1\), its inequality is strict.

**(3) Full spectrum at the Frobenius optimum.** Decompose leaf space into the unit vector \(v\) and its orthogonal complement. In the center-plus-\(v\) plane, \(G_F A_{d,\rho}G_F\) has the \(2\times2\) block
\[
B_F=\begin{pmatrix}a&\rho\sqrt{ab}\\\rho\sqrt{ab}&b\end{pmatrix};
\]
all other eigenvalues are \(b\), with multiplicity \(d-1\). Put
\[
\lambda_\pm=\frac{a+b\pm\sqrt{(a-b)^2+4\rho^2 ab}}2.
\]
Since \(0<\rho<1\) gives \(\lambda_-<b<\lambda_+\), the condition number is
\[
\kappa_F=\frac{\lambda_+}{\lambda_-}=
\frac{\lambda_+^2}{ab(1-\rho^2)},
\]
using \(\det B_F=ab(1-\rho^2)\).

**(4) Exact quadratic penalty.** With \(\epsilon=1-\rho^2\downarrow0\) and fixed integer \(d\ge2\),
\[
a\sim\frac{d}{d-1}\epsilon,\quad b\to1,\quad \lambda_+\to1,\quad
ab(1-\rho^2)\sim\frac{d}{d-1}\epsilon^2.
\]
Hence \(\kappa_F\sim(d-1)/(d\epsilon^2)\). Meanwhile \(\kappa_2(A_{d,\rho})=(1+\rho)^2/\epsilon\sim4/\epsilon\), so the claimed squared-condition-number limit equals \((d-1)/(16d)\). Also \(\mathcal F(G_F)\to1\) and \(\mathcal F(I)=2\rho^2\to2\). For \(d=1\), the formulas give \(a=b=1/(1+\rho^2)\), so \(G_F\) is scalar and its condition number equals that of \(A\), proving the boundary claim.

## Verification
The accompanying `verify_star.py` (Python 3, NumPy, SymPy) checks exact stationary equations, the Hessian determinant and Schur positivity, the block trace/determinant, strict objective improvement, and the \(d=1\) boundary for rational parameters. It also independently calculates eigenvalues and tests randomly chosen positive diagonal factors, plus checks the leading asymptotic coefficients numerically. All 6,440 finite checks passed in a local run. These calculations are diagnostics, **not** a proof over all dimensions and correlations; the universal theorem follows from the preceding exact arguments.

## Relationship to prior work
Brarda, Xu, Kalantzis, Li, and Xi (2026) introduce spectral value optimization for prescribed-support factored approximate inverses and explicitly compare with the Frobenius congruence residual \(\|I-G^\mathsf TAG\|_F\). Their full study motivates the baseline and documents spectrum/residual mismatch, but it does not present the present globally solved star-family objective, uniqueness, exact dimension boundary, or asymptotic square-law. Qu, Gao, Hinder, Ye, and Zhou (2022) study general optimal diagonal conditioning, so diagonal condition-number optimization itself is prior art. Vandebril, Golub, and Van Barel (2005) already describe optimal unit-diagonal scaling for SPD tridiagonal matrices; in particular, the three-dimensional unscaled star being condition-optimal is not claimed as new in isolation. Xu, Tang, Remis, and Leus (2012) exhibit deterioration under an algebraic one-sided diagonal-preconditioning criterion; the general qualitative warning is likewise not claimed as new. The contribution assessed here is the **joint, exact global comparison** and its sharp quadratic singular-limit law for the diagonal **congruence** Frobenius objective on positive-definite stars.

## Limitations
The result is specific to positive diagonal congruences, an exactly normalized SPD star, and the squared Frobenius residual \(\|GAG-I\|_F^2\), not the one-sided SPAI or Cholesky-factor FSAI construction. The matrix family becomes singular only in a limit; each asserted inequality holds for \(0<\rho<1\). No Krylov iteration count, computational runtime, or objective guarantee for arbitrary matrices is claimed. Earlier equivalent specialized scaling results cannot be ruled out by literature searches alone.

## References
- F. Brarda, T. Xu, V. Kalantzis, R. P. Li, and Y. Xi, *Factored Sparse Approximate Inverse Preconditioning via Spectral Optimization*, arXiv:2606.22742, first publicly submitted 2026-06-22. https://arxiv.org/abs/2606.22742
- Z. Qu, W. Gao, O. Hinder, Y. Ye, and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809, first posted 2022-09-02. https://arxiv.org/abs/2209.00809
- R. Vandebril, G. Golub, and M. Van Barel, *A small note on the scaling of symmetric positive definite semiseparable matrices*, 2005. https://people.cs.kuleuven.be/~raf.vandebril/homepage/publications/papers_html/condss/
- T. Xu, Z. Tang, R. Remis, and G. Leus, *Iterative equalization for OFDM systems over wideband Multi-Scale Multi-Lag channels*, EURASIP Journal on Wireless Communications and Networking 2012:280, 2012. https://link.springer.com/article/10.1186/1687-1499-2012-280
