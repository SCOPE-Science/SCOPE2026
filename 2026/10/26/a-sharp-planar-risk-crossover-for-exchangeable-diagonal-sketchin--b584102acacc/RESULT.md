# A sharp planar risk crossover for exchangeable diagonal sketching

## Finding

The exchangeable XDiag diagonal estimator of Epperly, Tropp, and Webber and the classical Bekas–Kokiopoulou–Saad (BKS) Rademacher diagonal estimator admit a **complete, exact, equal-matvec risk comparison** on every real symmetric positive-definite two-dimensional matrix. Neither method dominates in general. For equal diagonal entries the classical estimator is strictly better; for unequal entries there is precisely one correlation-strength threshold above which XDiag is strictly better.

Let
\[
 A=\begin{pmatrix}a&c\\c&b\end{pmatrix},\qquad a,b>0,\quad c^2<ab.
\]
Set \(q=ab\), \(P=a^2+b^2\), and \(u=c^2\). The squared Euclidean risks, using four matrix-vector products for each algorithm, are exactly
\[
 \boxed{\mathcal R_{\mathrm X}(A)=\frac{(q-u)^2(P+u)}{P^2-8qu+4u^2}},\qquad
 \boxed{\mathcal R_{\mathrm BKS}(A)=\frac{u}{2}}.
\]
For \(a=b\), \(\mathcal R_{\mathrm X}>\mathcal R_{\mathrm BKS}\) for every admissible \(c\). When \(a\ne b\), put \(\sigma=P/q>2\) and \(z=u/q\in[0,1)\). There is a **unique** \(z_*(\sigma)\in(0,1)\) satisfying
\[
 \boxed{2\sigma-(\sigma^2+4\sigma-2)z+(2\sigma+4)z^2-2z^3=0}.
\]
XDiag has greater risk for \(0\le z<z_*(\sigma)\), equal risk at the threshold, and lower risk for \(z_*(\sigma)<z<1\). In the strongly anisotropic limit, \(z_*(\sigma)=2/\sigma-8/\sigma^2+O(\sigma^{-3})\).

This risk reversal survives in arbitrarily high dimensions: for every \(n\ge5\) there are positive-definite \(n\)-dimensional inputs on which either estimator has arbitrarily larger squared risk than the other. These last assertions are about risks, not universal performance or the relative quality of practical implementations.

## Assumptions and scope

All computations use real exact arithmetic. The matrix \(A\) is symmetric positive definite. Each probe has independent, equally likely Rademacher entries \(\pm1\); probes are independent. For any vector \(w\), write \(P(w)\) for the orthogonal projector onto \(\operatorname{span}\{Aw\}\), which is well-defined because \(A\) is invertible. XDiag uses two independent probes \(w_1,w_2\) and the **conceptual leave-one-out definition**
\[
 \widehat d_{\mathrm X}=\frac12\sum_{i=1}^{2}
 \left[\operatorname{diag}(P(w_{3-i})A)
 +w_i\odot((I-P(w_{3-i}))Aw_i)\right].
\]
For symmetric \(A\), its two forward and two adjoint matrix-vector products constitute a nominal four-matvec budget. This definition is meaningful even if the two probes happen to coincide; an implementation based on inverting a rank-deficient QR factor need not be.

The comparator, at the same four-matvec budget, is
\[
 \widehat d_{\mathrm BKS}=\frac14\sum_{j=1}^{4}v_j\odot(Av_j),
\]
for four independent Rademacher probes \(v_j\). The risk is \(\mathcal R=\mathbb E\|\widehat d-\operatorname{diag}A\|_2^2\), with independent sampling between methods if jointly simulated. The result is not a comparison against direct coordinate probing, which would recover the diagonal in two matvecs in dimension two.

## Proof

**1. Classical comparator.** For a two-dimensional Rademacher probe \(v\), put \(s=v_1v_2\), a fair random sign. Then \(v\odot Av=(a+cs,b+cs)^{\mathsf T}\). Averaging four independent signs gives \(\mathbb E\|\widehat d_{\mathrm BKS}-(a,b)^{\mathsf T}\|_2^2=2c^2/4=u/2\).

**2. One leave-one-out residual.** Let \(\Delta=ab-c^2>0\). A probe \(w\) with \(s=w_1w_2\) has \(Aw\) proportional to \((a+sc,\,s(b+sc))^{\mathsf T}\). Define
\[
 D_s=(a+sc)^2+(b+sc)^2>0,\qquad
 f_s=-\frac{s\Delta}{D_s}\begin{pmatrix}b+sc\\a+sc\end{pmatrix}.
\]
Direct two-by-two multiplication gives
\[
 ((I-P(w))A)_{12}=(f_s)_1,\qquad
 ((I-P(w))A)_{21}=(f_s)_2.
\]
Because the diagonal of \(P(w)A\) plus the diagonal of \((I-P(w))A\) equals \(\operatorname{diag}A\), the error of a basic leave-one-out estimate with held-out sign \(t\) is exactly \(t f_s\). This holds for all sign realizations, not just in expectation.

**3. Exact XDiag risk.** The independent signs \(s_1,s_2\) yield total error
\[
 e_{\mathrm X}=\frac12(s_1f_{s_2}+s_2f_{s_1}).
\]
Its four equally likely values are \(f_+\), \(-f_-\), and twice \((f_- -f_+)/2\). Thus
\[
 \mathcal R_{\mathrm X}=\frac18\left(3\|f_+\|_2^2+3\|f_-\|_2^2-2f_+^{\mathsf T}f_-\right).
\]
The identities
\[
 \|f_s\|_2^2=\frac{\Delta^2}{D_s},\quad
 f_+^{\mathsf T}f_-=-\frac{\Delta^2(P-2u)}{D_+D_-},\quad
 D_+D_-=P^2-8qu+4u^2
\]
reduce this to the displayed exact rational risk. All denominators are strictly positive under the stated hypotheses, since each \(D_s\) is a sum of squares of a nonzero vector.

**4. Unique crossover.** Subtraction yields
\[
 \mathcal R_{\mathrm X}-\mathcal R_{\mathrm BKS}=
 \frac{q^3 H_\sigma(z)}{2D_+D_-},
\]
where
\[
 H_\sigma(z)=2\sigma-(\sigma^2+4\sigma-2)z+(2\sigma+4)z^2-2z^3.
\]
For \(\sigma=2\), \(H_2(z)=2(1-z)^2(2-z)>0\) on \([0,1)\). For \(\sigma>2\), the derivative has
\[
 H_\sigma''(z)=4\sigma+8-12z>0,\qquad
 H_\sigma'(1)=4-\sigma^2<0.
\]
Therefore \(H_\sigma'\) is strictly negative throughout \([0,1]\). Since \(H_\sigma(0)=2\sigma>0\) and \(H_\sigma(1)=4-\sigma^2<0\), there is exactly one root in \((0,1)\) and the asserted strict inequalities follow. For the large-anisotropy expansion, write \(z=y/\sigma\) and \(\varepsilon=1/\sigma\). The equation \(\varepsilon H_{1/\varepsilon}(\varepsilon y)=0\) has at \(\varepsilon=0\) the simple root \(y=2\) with derivative \(-1\) in \(y\). The implicit-function theorem gives an analytic root; its first terms \(y=2-8\varepsilon+O(\varepsilon^2)\) prove the stated expansion.

**5. High-dimensional non-domination.** The same four-matvec estimators make sense for arbitrary \(n\). On \(A=I_n\), BKS is exact for every realization. But on the event \(w_1=w_2\) (positive probability), XDiag returns \(\operatorname{diag}(P(w_1))=(1/n,\ldots,1/n)\), so its risk is strictly positive.

Conversely, let \(v=(1,2,4,\ldots,2^{n-1})^{\mathsf T}\) and \(A_\varepsilon=vv^{\mathsf T}+\varepsilon I_n\) for \(\varepsilon>0\). Every Rademacher \(w\) has \(v^{\mathsf T}w\ne0\) (an odd integer); hence all leave-one-out projectors converge uniformly over the finite sign set to the projector onto \(v\). Consequently \(\mathcal R_{\mathrm X}(A_\varepsilon)\to0\) as \(\varepsilon\downarrow0\). In contrast,
\[
 \mathcal R_{\mathrm BKS}(A_\varepsilon)
 =\frac14\sum_{i\ne j}v_i^2v_j^2>0
\]
is independent of \(\varepsilon\). This follows because each coordinate of the four-probe BKS error has variance one quarter of the sum of the squares of the off-diagonal entries in its row. The resulting opposite ratios are unbounded. This establishes non-domination even with strictly positive-definite inputs in arbitrarily high dimensions.

## Verification

Run the standard-library program `verify_xdiag.py` with `python3 verify_xdiag.py`. It independently enumerates all Rademacher sign pairs for many rational positive-definite two-by-two matrices and evaluates the leave-one-out projector formula using exact rational arithmetic. It checks both closed risks, the cubic risk difference, and sample outcomes on both sides of the crossover. The program additionally checks derivative identities over rational test points and one high-dimensional diagonal witness. The analytic proof above, not finite testing, establishes the universal claims.

For example, \(a=1\), \(b=4\), and \(c=0\) give \(\mathcal R_{\mathrm X}=16/17\) and \(\mathcal R_{\mathrm BKS}=0\). For the same diagonal entries and \(c=3/2\), the risks reverse: \(\mathcal R_{\mathrm X}=3773/15184\) and \(\mathcal R_{\mathrm BKS}=9/8\). The unique threshold for this family is \(c\approx1.070980242858\) in absolute value.

## Relationship to prior work

Epperly, Tropp, and Webber introduced XDiag as an exchangeable leave-one-out, randomized-SVD-based diagonal estimator; their article gives the estimator and numerical comparisons. Epperly's subsequent dissertation (Chapter 16) provides a detailed derivation and qualitative experiments showing that BKS can beat deflation-based estimators for flat spectra, while deflation methods improve on spectrally decaying examples. Hallman, Ipsen, and Saibaba analyze Rademacher diagonal estimates and their dependence on off-diagonal mass; Baston and Nakatsukasa analyze stochastic diagonal estimators and Diag++.

The distinct assertion established here is the exact **finite-budget XDiag-versus-BKS squared-risk formula**, its unique correlation crossover on every two-dimensional symmetric positive-definite input, and dimension-independent non-domination via strictly positive-definite embeddings. The general leave-one-out construction, the baseline estimator, and previous empirical trends are not claimed as new.

## Limitations

The crossover formula assumes two independent Rademacher probes for conceptual XDiag, four for BKS, real symmetric two-dimensional positive-definite inputs, squared Euclidean error, and exact arithmetic. Actual implementations, especially QR-based code faced with rank-deficient sampled matrices, require separate handling. The result is not a broad finite-sample bound for arbitrary sketch sizes, a complexity improvement, nor a guarantee that either algorithm is globally preferable. The high-dimensional extension proves an existence/separation statement, not an exact risk classification in larger dimensions. The specialized two-dimensional risk comparison may have unlocated equivalents in matrix-estimation literature.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825, first posted 2023-01-19, especially Section 2.4 (XDiag) and Section 4.4. https://arxiv.org/abs/2301.07825
2. E. N. Epperly, *Make the Most of What You Have: Resource-Efficient Randomized Algorithms for Matrix Computations*, Caltech dissertation (2025), Chapter 16, DOI:10.7907/pef3-mg80. https://tropp.caltech.edu/dissertations/Epp25-Making-Most.pdf
3. E. Hallman, I. C. F. Ipsen, and A. K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, arXiv:2202.02887. https://arxiv.org/abs/2202.02887
4. R. A. Baston and Y. Nakatsukasa, *Stochastic diagonal estimation: probabilistic bounds and an improved algorithm*, arXiv:2201.10684. https://arxiv.org/abs/2201.10684
