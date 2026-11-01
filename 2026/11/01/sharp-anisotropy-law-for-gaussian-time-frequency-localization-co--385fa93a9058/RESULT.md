# Sharp anisotropy law for Gaussian time-frequency localization commutators

## Finding
Fix two Gaussian time-frequency masks, one radial and one with variable eccentricity. The squared Hilbert–Schmidt norm of the commutator of their localization operators has an exact two-radical expression, increases strictly with anisotropy, and is maximized at the stripe boundary where the second localization operator is not compact. In particular, the radial mask commutes with the anisotropic family only in the rotationally symmetric case.

Precisely, set \(u=(1+a)^{-1}\), \(B=1+b\), \(Q=B^2-c^2-u^2\), and \(\mathcal C=[T_{f_a},T_{g_{b,c,\theta}}]\). Then
\[
\boxed{\|\mathcal C\|_{\mathcal S_2}^2=2u^2\left[\frac1{\sqrt{Q^2-c^2(1+u^2)^2}}-\frac1{\sqrt{Q^2-4c^2u^2}}\right].}
\]
For every fixed \(a,b>0\), this expression is independent of \(\theta\), is strictly increasing with \(c\in[0,b]\), and vanishes only at \(c=0\). Its unique maximum occurs at \(c=b\), including the noncompact stripe endpoint. Its small-anisotropy expansion is
\[
\|\mathcal C\|_{\mathcal S_2}^2=\frac{u^2(1-u^2)^2}{(B^2-u^2)^3}c^2+O_{a,b}(c^4).
\]

## Assumptions and scope
The normalized analytic Bargmann–Fock space is
\[
\mathcal F^2=\{F:\mathbb C\to\mathbb C\text{ entire}:\|F\|^2=\pi^{-1}\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z)<\infty\}.
\]
Its orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\). If \(P\) is orthogonal projection onto \(\mathcal F^2\), a bounded mask \(h\) defines \(T_h=PM_h|_{\mathcal F^2}\). Via the Gaussian Bargmann transform these are Gaussian-window time-frequency localization (anti-Wick) operators, with a fixed normalization of phase-space coordinates.

Fix arbitrary real \(a>0\), \(b>0\), \(\theta\in\mathbb R\), and \(0\le c\le b\). Define
\[
f_a(z)=\exp(-a|z|^2),\qquad g_{b,c,\theta}(z)=\exp[-b|z|^2+c\operatorname{Re}(e^{-2i\theta}z^2)].
\]
These masks are positive and bounded by one. For \(c<b\), the second mask is integrable and elliptical; at \(c=b\) it is constant in one real direction and gives a Gaussian stripe. All quantifiers include this endpoint; the angle is arbitrary. We use \(\mathcal S_2\) for the Hilbert–Schmidt class.

## Proof
**1. Radial spectrum and matrix reduction.** Gaussian radial integration gives
\[
T_{f_a}e_n=u^{n+1}e_n,\qquad u=(1+a)^{-1}\in(0,1).
\]
Since \(\sum_{n\ge0}u^{n+1}<\infty\), this operator is trace class. Rotation covariance removes \(\theta\) without changing any Schatten norm. Write \(G_{mn}=\langle T_{g_{b,c,0}}e_n,e_m\rangle\) and, for the arguments used below, define the nonnegative matrix generating series
\[
F(x,y)=\sum_{m,n\ge0}|G_{mn}|^2x^my^n.
\]
The squared commutator norm, calculated in the monomial basis, is
\[
\|\mathcal C\|_{\mathcal S_2}^2=\sum_{m,n\ge0}(u^{m+1}-u^{n+1})^2|G_{mn}|^2
=2u^2\bigl(F(u^2,1)-F(u,u)\bigr).
\]
The equality follows from the symmetry \(|G_{mn}|=|G_{nm}|\). Because \(T_{f_a}\) is trace class and \(T_g\) is bounded, all indicated series converge even at \(c=b\).

**2. Gaussian generating function.** Expanding the exponential series and applying Fubini gives
\[
F(x,y)=\frac1{\pi^2}\int_{\mathbb C^2}
\exp\bigl[-B(|z|^2+|w|^2)+c\operatorname{Re}(z^2+w^2)+x\overline z w+y z\overline w\bigr]dA(z)dA(w),\quad B=1+b.
\]
For \((x,y)\in\{(u^2,1),(u,u)\}\) this integral is absolutely convergent: the real part of the exponent is at most \(-(B-c)(|z|^2+|w|^2)+(x+y)|z||w|\), and \(B-c\ge1>(x+y)/2\). With real coordinates \((\operatorname{Re}z,\operatorname{Re}w,\operatorname{Im}z,\operatorname{Im}w)\), the quadratic-form matrix equals
\[
M=\begin{pmatrix}
B-c&-(x+y)/2&0&-i(x-y)/2\\
-(x+y)/2&B-c&i(x-y)/2&0\\
0&i(x-y)/2&B+c&-(x+y)/2\\
-i(x-y)/2&0&-(x+y)/2&B+c
\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\det M=(B^2-c^2-xy)^2-c^2(x+y)^2.
\]
The complex Gaussian integral, obtained first by continuity near \(x=y=0\) and then on the convergence domain, yields the positive real value
\[
F(x,y)=\left[(B^2-c^2-xy)^2-c^2(x+y)^2\right]^{-1/2}.
\]
Substitute \((x,y)=(u^2,1)\) and \((u,u)\) in step 1 to obtain the boxed formula. The radicands are positive: write \(C=B^2-u^2\), \(z=c^2\), and \(s\in[4u^2,(1+u^2)^2]\). Then
\[
D(z,s)=(C-z)^2-zs>0.
\]
Indeed, at the worst endpoint \(c=b\) and \(s=(1+u^2)^2\), this factors as
\[
(1+b)(1-u^2)\big[(1-u^2)+b(3+u^2)\big]>0.
\]
All smaller \(z,s\) only increase \(D\).

**3. Sharp monotonicity and rigidity.** The difference of square roots admits the exact integral representation
\[
\|\mathcal C\|_{\mathcal S_2}^2
=u^2 c^2\int_{4u^2}^{(1+u^2)^2}\big[(B^2-u^2-c^2)^2-c^2s\big]^{-3/2}\,ds.
\]
The interval has positive length \((1-u^2)^2\). For \(0\le z=c^2\le b^2\),
\[
\partial_z D(z,s)=-2(B^2-u^2-z)-s<0,
\]
since \(B^2-u^2-z\ge1+2b-u^2>0\). Therefore the integrand \(zD(z,s)^{-3/2}\) is strictly increasing with \(z\), giving strict increase for \(c\ge0\), vanishing only at \(c=0\), and the unique maximum at \(c=b\). Expanding the integral at \(z=0\), and using the integration range of length \((1-u^2)^2\), produces the asserted \(c^2\) coefficient and \(O(c^4)\) error.

**4. The endpoint operator is noncompact.** At \(c=b\), in the rotated coordinates the symbol is \(g_{b,b,0}(x+iy)=e^{-2by^2}\), independent of \(x\). The normalized coherent states \(k_t(z)=\exp(tz-t^2/2)\), for real \(t\to+\infty\), converge weakly to zero in \(\mathcal F^2\). But their diagonal expectation remains constant:
\[
\langle T_{g_{b,b,0}}k_t,k_t\rangle=(1+2b)^{-1/2}>0.
\]
Hence \(T_{g_{b,b,0}}\) is not compact. The commutator nevertheless has the stated finite Hilbert–Schmidt norm; its even stronger trace-class membership is immediate from step 1 and is not claimed as a separate discovery. This completes the proof.

## Verification
The self-contained program `check_gaussian_commutator.py` uses only the Python standard library. It compares a truncated complex-Gaussian monomial-moment recurrence with the closed Hilbert–Schmidt formula at six parameter triples, including \(c=b\). It also independently evaluates twenty-one complex \(4\times4\) determinants by permutation expansion, tests seventy-five adjacent strict-monotonicity comparisons, and checks nine small-anisotropy expansions. All tests passed with a 70-mode cutoff for the matrix comparisons. These checks are finite supplements and are not proofs of the full quantified statement. Run `python check_gaussian_commutator.py` in a Python 3 environment; no input data or third-party libraries are needed.

## Relationship to prior work
The Daubechies spectral theorem and its Gaussian-window extensions motivate weighted time-frequency localization. Testorf's treatment of discrete Gabor localization and Toeplitz operators on flat tori (arXiv:2410.15170, first available 2024-10-19) involves **discrete** finite-dimensional localization and eigenvalue counting, not the continuous-plane Schatten commutator of two weighted masks. Svela (arXiv:2410.18769, first available 2024-10-24), especially its Gaussian Cohen-class discussion in section 6.1, treats eigenfunctions/eigenvalues of individual localization operators and their symplectic transforms; the present invariant depends on two operators expressed in **different** diagonalizing bases. Huang–Zhang (arXiv:2405.11147, first available 2024-05-18) gives single-operator norm bounds for nonradial Fock Toeplitz symbols, not a bilinear commutator formula, and its integrability premise excludes the stripe endpoint. Kisil (arXiv:2108.13710, first available 2021-08-31) gives a broad Heisenberg-group cross-Toeplitz calculus but no identical sharp anisotropy envelope was identified in the inspected sections. The Gaussian integral machinery is classical and is not claimed as new. The new assertion is the *exact two-mask commutator norm together with its complete strict anisotropy optimization and noncompact optimizer*.

## Limitations
The result is for one complex dimension, a radial Gaussian mask and a centered positive anisotropic Gaussian mask with fixed average quadratic damping \(b\). The coefficient is not stated uniformly in \(a,b\). The result does not characterize all mask pairs or all Schatten norms; in particular, its trace-class membership at the endpoint is elementary. Historical priority remains provisional because a sufficiently general Gaussian operator product/covariance identity could imply the displayed formula indirectly. No independent mathematical audit or validation has been performed.

## References
- J. Testorf, *A Complex Geometric Approach to the Discrete Gabor Transform and Localization Operators on the Flat Torus*, arXiv:2410.15170 (first posted 2024-10-19), https://arxiv.org/abs/2410.15170.
- E. A. T. Svela, *Extensions of Daubechies' theorem: Reinhardt domains, Hagedorn wavepackets and mixed-state localization operators*, arXiv:2410.18769 (first posted 2024-10-24), https://arxiv.org/abs/2410.18769.
- H. Huang and X. Zhang, *Norm bounds for self-adjoint Toeplitz operators with non-radial symbols on the Fock space*, arXiv:2405.11147 (first posted 2024-05-18), https://arxiv.org/abs/2405.11147.
- V. V. Kisil, *Cross-Toeplitz Operators on the Fock–Segal–Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, arXiv:2108.13710 (first posted 2021-08-31), https://arxiv.org/abs/2108.13710.
