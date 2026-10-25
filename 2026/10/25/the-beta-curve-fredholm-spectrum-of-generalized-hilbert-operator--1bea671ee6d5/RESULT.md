# The beta-curve Fredholm spectrum of generalized Hilbert operators on \(H^2\)

## Finding
For each real \(b>0\), define the generalized Hilbert operator on the classical complex Hardy space \(H^2(\mathbb D)\) by
\[
(\mathcal H_b f)(z)=\int_0^1\frac{f(t)(1-t)^b}{(1-tz)^{b+1}}\,dt,
\qquad |z|<1.
\]
The operator is bounded. Its **Fredholm essential spectrum**, meaning the set of complex \(\lambda\) for which \(\mathcal H_b-\lambda I\) is not Fredholm, is exactly
\[
\boxed{\displaystyle
\sigma_{\mathrm F}(\mathcal H_b)
=\left\{\frac{\Gamma(\tfrac12+i\tau)\Gamma(b+\tfrac12-i\tau)}{\Gamma(b+1)}:\tau\in\mathbb R\right\}\cup\{0\}.}
\]
This is the image of a continuous curve completed at its vanishing ends. It is **not contained in the real axis for any \(b>0\)**. In the concrete first deformation \(b=1\), the curve is
\[
\sigma_{\mathrm F}(\mathcal H_1)
=\left\{\frac{\pi(\tfrac12-i\tau)}{\cosh(\pi\tau)}:\tau\in\mathbb R\right\}\cup\{0\}.
\]

## Assumptions and scope
We work over the complex field with \(b\) a fixed **real number strictly greater than zero**. The Hardy-space norm is the coefficient norm \(\|f\|_{H^2}^2=\sum_{n\ge0}|\widehat f(n)|^2\). The integral defines the operator first on polynomials and then continuously on the whole space. Fredholm means finite-dimensional kernel and cokernel and closed range. This result determines the Fredholm essential spectrum, **not** the complete spectrum, eigenvalue multiplicities or Fredholm indices. Complex powers and gamma functions use their standard analytic branches on the gamma arguments of positive real part occurring here.

## Proof
**1. Exact matrix and a compact homogeneous model.** Taylor expansion, the Euler beta integral, and the normalization of the monomial Hardy basis yield the matrix
\[
h^{(b)}_{nm}=\frac{\Gamma(n+b+1)}{\Gamma(n+1)}\,
\frac{\Gamma(n+m+1)}{\Gamma(n+m+b+2)},\qquad n,m\ge0.
\]
For \(n,m\ge1\), the gamma-ratio estimates, with constants depending only on the fixed \(b\), give
\[
h^{(b)}_{nm}=\frac{n^b}{(n+m)^{b+1}}+e_{nm},\qquad
|e_{nm}|\le C_b\left[\frac{n^{b-1}}{(n+m)^{b+1}}+
\frac{n^b}{(n+m)^{b+2}}\right].
\]
In fact both displayed error terms have square-summable arrays because, for \(a>1\),
\[
\sum_{m\ge1}(n+m)^{-a}=O_a(n^{1-a}),
\quad
\sum_{n,m\ge1}\frac{n^{2b-2}}{(n+m)^{2b+2}}=O_b\!\left(\sum_{n\ge1}n^{-3}\right)<\infty,
\]
and likewise for the second term. The row \(n=0\) is square-summable (it decays as \((m+1)^{-b-1}\)), and the column \(m=0\) is square-summable (it decays as \((n+1)^{-1}\)); together they form a finite-rank operator. Thus \(\mathcal H_b\) is Hilbert--Schmidt equivalent, after removing one row and column, to the discrete homogeneous kernel
\[
K_b(n,m)=\frac{n^b}{(n+m)^{b+1}},\qquad n,m\ge1.
\]

**2. Passage to a continuous half-line kernel.** Embed \(\ell^2(\mathbb N)\) isometrically in \(L^2([1,\infty),dx)\) as step functions constant on \([n,n+1)\), with the orthogonal complement kept separate. Let
\[
(B_bf)(x)=\int_1^\infty\frac{x^b}{(x+y)^{b+1}}f(y)\,dy.
\]
On cells \([n,n+1)\times[m,m+1)\), elementary differentiation of the continuous kernel gives
\[
\left|\frac{x^b}{(x+y)^{b+1}}-\frac{n^b}{(n+m)^{b+1}}\right|
\le C_b\left[\frac{n^{b-1}}{(n+m)^{b+1}}+\frac{n^b}{(n+m)^{b+2}}\right].
\]
The identical square-summability estimate shows that the continuous operator differs by Hilbert--Schmidt perturbation from the operator \(K_b\) on the step-function subspace, extended by zero to its orthogonal complement. For every \(\lambda\ne0\), Fredholmness of the extended discrete model minus \(\lambda I\) is equivalent to that of \(K_b-\lambda I\): on the complement the operator equals \(-\lambda I\). As compact perturbations preserve Fredholmness, we have reduced all nonzero spectral values to \(B_b\).

**3. Mellin-to-Fourier conjugation.** Define a unitary map from \(L^2([1,\infty),dx)\) to \(L^2([0,\infty),ds)\) by
\[
(Vf)(s)=e^{s/2}f(e^s).
\]
Substituting \(x=e^s\), \(y=e^t\), and multiplying by the unitary Jacobian yields
\[
(VB_bV^{-1}g)(s)
=\int_0^\infty q_b(t-s)g(t)\,dt,
\qquad
q_b(u)=\frac{e^{u/2}}{(1+e^u)^{b+1}}.
\]
The kernel \(q_b\) and its first weighted square moment belong to \(L^1(\mathbb R)\) and \(L^2(\mathbb R)\), respectively, because it decays exponentially as \(u\to\pm\infty\). Thus the resulting Wiener--Hopf operator \(W_b\) is bounded. On the full line the convolution with \(q_b(t-s)\) is diagonalized by the Fourier exponentials \(e^{i\tau s}\) with multiplier
\[
m_b(\tau)=\int_{\mathbb R}q_b(u)e^{i\tau u}\,du
=\int_0^\infty\frac{v^{-1/2+i\tau}}{(1+v)^{b+1}}\,dv
=B\left(\tfrac12+i\tau,b+\tfrac12-i\tau\right).
\]
This Euler beta integral is absolutely convergent for all real \(\tau\). In particular \(m_b\) is continuous and tends to zero as \(|\tau|\to\infty\) by the Riemann--Lebesgue lemma.

**4. Fredholmness outside the beta curve.** Let \(P\) be restriction/projection from \(L^2(\mathbb R)\) onto \(L^2([0,\infty))\) and \(Q=I-P\). Write \(C_b\) for full-line convolution. For \(\lambda\ne0\) outside the completed multiplier curve, \(C_b-\lambda I\) has a bounded full-line inverse \(R_\lambda\) because its Fourier multiplier \(m_b(\tau)-\lambda\) is uniformly separated from zero. Both cross-boundary operators \(PC_bQ\) and \(QC_bP\) are Hilbert--Schmidt: their squared kernel integrals are bounded by
\[
\int_{\mathbb R}|u|\,|q_b(u)|^2\,du<\infty.
\]
It follows that \(PR_\lambda P\) is a two-sided parametrix for \(PC_bP-\lambda I\) modulo compact operators, as the remainders factor through one of those cross-boundary Hilbert--Schmidt operators. Hence \(W_b-\lambda I\), and therefore \(\mathcal H_b-\lambda I\), is Fredholm.

**5. Failure of Fredholmness on the beta curve.** For any fixed real \(\tau\), use the normalized packets
\[
g_L(s)=L^{-1/2}\mathbf1_{[L,2L]}(s)e^{i\tau s},\qquad L\to\infty.
\]
They satisfy \(\|g_L\|_2=1\) and \(g_L\rightharpoonup0\) weakly. Extending by zero to the full line and using Minkowski's integral inequality plus the elementary translation bound for intervals gives
\[
\|(C_b-m_b(\tau)I)g_L\|_2
\le\int_{\mathbb R}|q_b(u)|\min\left(2,\sqrt{2|u|/L}\right)\,du\longrightarrow0.
\]
The same convergence holds upon restriction to the positive half-line. A Fredholm operator cannot possess a weakly null sequence of unit vectors whose images converge to zero: the Fredholm parametrix would make the vectors norm-convergent to zero modulo a compact map. Thus each \(m_b(\tau)\) belongs to the Fredholm essential spectrum. Since this spectrum is closed and \(m_b(\tau)\to0\), zero also belongs. Steps 1--5 prove the claimed equality.

**6. The nonreal deformation.** Differentiate the beta quotient at \(\tau=0\):
\[
m_b'(0)=iB(\tfrac12,b+\tfrac12)
\left[\psi(\tfrac12)-\psi(b+\tfrac12)\right].
\]
The digamma function \(\psi\) is strictly increasing on \((0,\infty)\), so for every \(b>0\) this derivative is nonzero and purely imaginary. Hence the curve immediately leaves the real axis. For \(b=1\), gamma recurrence and \(|\Gamma(\tfrac12+i\tau)|^2=\pi/\cosh(\pi\tau)\) give the stated explicit curve.

## Verification
The argument is analytic for every real \(b>0\). The two compact-perturbation claims reduce to convergent double sums bounded by \(\sum_{n\ge1}n^{-3}\), and the Fredholm/non-Fredholm alternatives are proved by an explicit parametrix and explicit escaping approximate eigenvectors. Gamma-ratio asymptotics and the beta-integral identity can be independently checked directly. Numerical spot checks of the gamma-ratio matrix asymptotics and of the formula at \(b=1\) were consistent, but are not used as proof.

## Relationship to prior work
Li, Pan and Zhou (2026) introduce precisely this one-parameter generalized Hilbert operator and establish its exact Hardy-space norm; the Fredholm essential spectrum is a different invariant not supplied by their norm result. The classical Hilbert matrix has real essential spectrum \([0,\pi]\) (Silbermann 2021). Ferudun (2026) gives a Mellin/Wiener--Hopf treatment of the classical Hilbert matrix on power-weighted sequence spaces, producing a different cosine-quotient multiplier: a diagonally weighted kernel proportional to \(x^{\alpha/2}y^{-\alpha/2}/(x+y)\), rather than the present \(x^b/(x+y)^{b+1}\). The overlap is methodological, not a prior implication of the displayed beta-curve formula. Work on Hausdorff-matrix generalized Hilbert operators likewise concerns different matrix families and norm/compactness criteria. These comparisons do not establish exhaustive priority.

## Limitations
Only real \(b>0\), the unweighted Hardy Hilbert space, and the Fredholm essential spectrum are treated. The complete spectrum, point spectrum, residual spectrum, Fredholm index inside the curve, and extensions to other Hardy exponents are not classified. The exact beta-curve statement could conceivably follow from an unidentified general homogeneous-kernel spectral theorem; this is a residual priority risk rather than an established equivalent source. No independent audit or external certification is claimed here.

## References
1. S. Li, W. Pan, M. Zhou, *Norm of the generalized Hilbert operator on Hardy spaces*, arXiv:2608.19660 (first public 20 August 2026), https://arxiv.org/abs/2608.19660.
2. B. Silbermann, *On the Spectrum of Hilbert Matrix Operator* (2021), on the ordinary shifted Hilbert matrix and its essential spectrum.
3. A. Ferudun, *The Spectrum of the Hilbert Matrix on Power-Weighted \(\ell^2\) Spaces* (online 2 September 2026), DOI:10.5281/zenodo.22245611, https://www.eulersolve.org/papers/aim-analysis-0015/.
4. B. Bellavita, N. Chalmoukis, V. Daskalogiannis, G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, arXiv:2307.15334, https://arxiv.org/abs/2307.15334.
