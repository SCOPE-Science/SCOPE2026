# Gaussian-sketch nonreal Ritz pairs: sharp coalescence and oversampling laws

## Finding

A real symmetric positive-definite matrix can yield a nonreal conjugate pair under Gaussian sketched Rayleigh–Ritz extraction. For the concrete three-state family defined below and every integer sketch size \(s\geq2\), the exact probability depends only on the normalized compressed eigenvalue gap \(t=\delta/(\sqrt2 g)\):
\[
\mathcal P_s(t)=\frac{s-1}{2\pi}\int_{-\infty}^{\infty}\int_{(t^2+y^2)/(2t)}^{\infty}(1+x^2+y^2)^{-(s+1)/2}\,dx\,dy.
\]
Its two sharp endpoints are
\[
\mathcal P_s(t)\sim C_s\sqrt t\quad(t\downarrow0),\qquad
\mathcal P_s(t)\sim K_s t^{1-s}\quad(t\to\infty),
\]
where
\[
C_s=\frac{s-1}{\sqrt2\pi}\operatorname B\!\left(\frac34,\frac{2s-1}{4}\right)
\]
and
\[
K_s=\frac1{2\pi}\int_{-\pi/4}^{\pi/4}
\left[\left(\cos\theta+\sqrt{\cos2\theta}\right)^{s-1}
-\left(\cos\theta-\sqrt{\cos2\theta}\right)^{s-1}\right]d\theta.
\]
These constants are finite and strictly positive. In particular,
\[
C_2=K_2=\frac{\sqrt2\,\Gamma(3/4)^2}{\pi^{3/2}},\qquad
C_3=\frac12,\quad K_3=\frac1{\sqrt2}.
\]
The coalescence exponent \(1/2\) is independent of oversampling. The large-gap power is \(1-s\), becoming more strongly suppressed when additional Gaussian rows are used. The probability is strictly positive for every finite \(t>0\), despite positive definiteness of the underlying matrix; at the exactly repeated compressed eigenvalue \(\delta=0\) it is zero.

## Assumptions and scope

Fix \(a>0\), \(g>0\), \(\delta\ge0\), and \(d>g^2(1/a+1/(a+\delta))\). Let
\[
A=\begin{pmatrix}a&0&g\\0&a+\delta&g\\g&g&d\end{pmatrix},\qquad
Q=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}.
\]
The stated Schur-complement condition makes \(A\) positive definite. Independently draw the entries of \(S\in\mathbb R^{s\times3}\) from the real standard Gaussian distribution, for any integer \(s\ge2\). Almost surely \(SQ\) has rank two. Compute the exact-arithmetic, unmodified sketched Rayleigh–Ritz matrix \(M=(SQ)^\dagger SAQ\). Whitening \(Q\) through a nonsingular basis transformation changes \(M\) by similarity and therefore does not change its eigenvalues. The event studied is that the two eigenvalues of \(M\) are a nonreal conjugate pair, with probability taken only over \(S\). Multiplication of the entire sketch by a common positive scalar does not change \(M\).

## Proof

**1. Reduction to one discriminant.** Write \(G=SQ\in\mathbb R^{s\times2}\) and \(h=Se_3\in\mathbb R^s\). The three Gaussian columns are independent. Put \(p=(p_1,p_2)^\top=G^\dagger h\). Because \(AQ=Q\operatorname{diag}(a,a+\delta)+e_3(g,g)\),
\[
M=\begin{pmatrix}a&0\\0&a+\delta\end{pmatrix}+p(g,g).
\]
The discriminant of its characteristic polynomial is
\[
\operatorname{disc}(M)=\delta^2-2\delta g(p_1-p_2)+g^2(p_1+p_2)^2.
\]
Introduce \(X=(p_1-p_2)/\sqrt2\), \(Y=(p_1+p_2)/\sqrt2\), and \(t=\delta/(\sqrt2 g)\). For \(\delta>0\), the discriminant is negative precisely when
\[
X>\frac{t^2+Y^2}{2t}. \tag{1}
\]
For \(\delta=0\), it is \(g^2(p_1+p_2)^2\ge0\), hence no nonreal pair occurs.

**2. Exact Gaussian-sketch law.** Conditional on \(G\), \(p\) is centered normal with covariance \((G^\top G)^{-1}\). The Gram matrix \(W=G^\top G\) has the real Wishart distribution with \(s\) degrees of freedom and dimension two. Integrating the conditional normal density against its Wishart density multiplies the integrand in \(W\) by \(\det(W)^{1/2}\) and replaces the matrix exponent by \(\exp[-\operatorname{tr}(W(I+pp^\top))/2]\). The Wishart matrix-gamma integral is proportional to \(\det(I+pp^\top)^{-(s+1)/2}=(1+\|p\|_2^2)^{-(s+1)/2}\). The radial integral
\[
\int_{\mathbb R^2}(1+\|p\|_2^2)^{-(s+1)/2}\,dp=\frac{2\pi}{s-1}
\]
fixes the normalizing constant. Thus the joint density of the orthogonal rotation \((X,Y)\) is exactly
\[
f_s(x,y)=\frac{s-1}{2\pi}(1+x^2+y^2)^{-(s+1)/2}. \tag{2}
\]
For \(s=2\), the same identity holds by the square-Gaussian inverse construction or by the limiting Wishart integral. Integrating (2) over (1) proves the displayed exact probability formula. Both the event and its complement have positive measure for every \(t>0\).

**3. Coalescing-gap asymptotic.** Reverse the integration order in (1): \(x\ge t/2\) and \(|y|<\sqrt{2tx-t^2}\). Substitute \(y=\sqrt t\,z\). Then
\[
\frac{\mathcal P_s(t)}{\sqrt t}
=\frac{s-1}{2\pi}\int_{t/2}^{\infty}\int_{-\sqrt{2x-t}}^{\sqrt{2x-t}}
(1+x^2+tz^2)^{-(s+1)/2}\,dz\,dx.
\]
As \(t\downarrow0\), dominated convergence applies with integrable majorant \(2\sqrt{2x}(1+x^2)^{-(s+1)/2}\), because \(s\ge2\). The limit equals
\[
\frac{(s-1)\sqrt2}{\pi}\int_0^\infty\frac{\sqrt x}{(1+x^2)^{(s+1)/2}}\,dx
=\frac{s-1}{\sqrt2\pi}\operatorname B\!\left(\frac34,\frac{2s-1}{4}\right).
\]
Here \(\operatorname B(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)\). No finite simulation is used to justify this limiting statement.

**4. Separated-gap asymptotic.** In (1) use \(x=tu\), \(y=tv\). The event becomes the fixed region \(\mathcal D=\{(u,v):2u>1+v^2\}\), and
\[
t^{s-1}\mathcal P_s(t)=\frac{s-1}{2\pi}\int_{\mathcal D}
\left(t^{-2}+u^2+v^2\right)^{-(s+1)/2}\,du\,dv.
\]
The domain lies in \(u>1/2\), so the limiting singularity at the origin is excluded and dominated convergence is valid. In polar coordinates \(u=r\cos\theta\), \(v=r\sin\theta\), the admissible angular range is \(|\theta|<\pi/4\) and the radial endpoints are
\[
r_{\mathrm{in}}=\frac1{\cos\theta+\sqrt{\cos2\theta}},\qquad
r_{\mathrm{out}}=\frac1{\cos\theta-\sqrt{\cos2\theta}}.
\]
At \(\theta=0\), the latter endpoint is interpreted as \(+\infty\). Integration of \(r^{-s}\) between the endpoints gives the displayed formula for \(K_s\). Positivity is immediate from the strictly positive radial interval on the interior angular range.

**5. Explicit constants.** Beta/gamma identities yield \(C_3=1/2\) and the stated \(C_2\). For \(s=3\), the integral for \(K_3\) simplifies to \((2/\pi)\int_{-\pi/4}^{\pi/4}\cos\theta\sqrt{\cos2\theta}\,d\theta=1/\sqrt2\). For \(s=2\), both constants reduce to the same beta integral, giving the stated common value.

## Verification

The accompanying reproducible `check.py` evaluates the discriminant identity symbolically, checks radial normalization and special constants, numerically integrates the exact probability, tests the small-gap law, compares independent Gaussian-sketch frequencies against their binomial uncertainties, and tests an explicit positive-definite example with nonreal sketched Ritz values. Use `python check.py` with NumPy, SciPy, and SymPy installed. The analytical proof above, rather than finite testing, establishes all integer sketch sizes and both asymptotic statements. Representative exact quadratures at \(t=1\) are \(\mathcal P_2(1)\approx0.178681159113\), \(\mathcal P_3(1)\approx0.170820393250\), and \(\mathcal P_5(1)\approx0.130131556175\).

## Relationship to prior work

Liu and Liu introduce real-Schur approaches for symmetric sketched eigensolvers and identify potentially nonreal sketched Ritz pairs. Nakatsukasa and Tropp likewise observe that a sketched Rayleigh–Ritz reduction need not retain real eigenvalues, and analyze deterministic projection quality and embedding conditions. Shao develops probabilistic conditioning estimates for a different complex-Gaussian randomized Rayleigh–Ritz procedure. These works motivate the exact model but do not, in the inspected material, supply the present real-Gaussian distributional law and its paired coalescence/oversampling exponents. The established fact that Gaussian least-squares coefficients follow a multivariate Student law is an ingredient, not presented here as new. Related deterministic three-state sketched Ritz counterexamples characterize particular coordinate-row sketches, not the random Gaussian event probability.

## Limitations

This statement is confined to a three-state symmetric positive-definite family with two-dimensional fixed trial space and independent dense real Gaussian sketch entries. It concerns unmodified exact-arithmetic sketched Rayleigh–Ritz extraction rather than real-Schur postprocessing, and counts a conjugate pair as nonreal only when the exact discriminant is strictly negative. The probability is not asserted for sparse-sign, subsampled orthogonal, or adaptively chosen sketches. The findings do not supply whole-eigensolver convergence guarantees. The high-gap regime changes the model parameter \(\delta/g\), not necessarily the condition number of a fixed matrix.

## References

- Jingyu Liu and Yuqi Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1, first public 2026-10-15. https://arxiv.org/html/2610.22261v1
- Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), section 6.8; preprint arXiv:2111.00113. https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf
- Nian Shao, *Stabilizing the Rayleigh–Ritz Procedure by Randomization*, arXiv:2604.01037v3 (2026). https://arxiv.org/html/2604.01037v3
