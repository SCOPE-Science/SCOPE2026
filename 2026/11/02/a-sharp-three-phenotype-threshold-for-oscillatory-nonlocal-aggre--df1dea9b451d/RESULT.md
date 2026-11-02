# A sharp three-phenotype threshold for oscillatory nonlocal aggregation with positive net attraction

## Finding

In the discrete-phenotype, response–signal separable nonlocal aggregation model described below, positive net interaction imposes a sharp restriction on linear spatial instabilities: **two phenotypes cannot have nonreal spatial Fourier growth rates, whereas three phenotypes can have a dominant, linearly unstable complex-conjugate pair even when all signal-production coefficients are strictly positive and the mean interaction matrix is normalized to one.** The three-phenotype witness below has precisely the Fourier modes \(n=\pm1\) unstable among the nonconstant spatial modes; their fastest-growing eigenvalues form a nonreal conjugate pair. This is a linear statement and does not assert existence of a nonlinear oscillatory attractor.

## Assumptions and scope

On a spatial torus consider \(N\ge1\) nonnegative phenotype densities governed formally near a homogeneous state by

\[
\partial_tu_i=\partial_{xx}u_i-\partial_x\left[u_i p(\overline u)\,\partial_x\left(\widetilde\mu B_i\sum_{j=1}^{N}C_j(K*u_j)\right)\right]+\widetilde\beta\sum_{j=1}^{N}(L_N)_{ij}u_j,
\]

where \(\overline u=N^{-1}\sum_j u_j\), \(\widetilde\mu>0\), \(\widetilde\beta>0\), and \(L_N\) is the nearest-neighbor, reflecting-endpoint discrete Laplacian in phenotype space. The convolution kernel is real, even, nonnegative, normalized to mass one and has nonnegative Fourier multipliers. We linearize around \(u_i\equiv U>0\) with \(p(U)>0\). The phenotype response vector \(B\) and signal vector \(C\) are real, with separable interaction coefficients \(A_{ij}=B_iC_j\). Positive net interaction means

\[
\left(\sum_{i=1}^{N}B_i\right)\left(\sum_{j=1}^{N}C_j\right)>0.
\]

For the impossibility statement, \(N=2\), any nonzero Fourier wavenumber and all parameters satisfying these conditions are allowed. For the sharp witness, \(N=3\), the torus has length \(2\pi\), \(p(s)=1-s\), \(U=1/2\), \(\widetilde\beta=1\), and \(\widetilde\mu=88/3\). The nonnegative heat kernel has Fourier multipliers \(\widehat K(n)=2^{-n^2}\), equivalently the heat kernel at positive time \(\log2\), which is smooth and strictly positive. Choose

\[
B=\frac3{11}(1,-13,15)^T,\qquad C=(7,2,2)^T.
\]

In particular, each signal coefficient is positive, \(B\) contains a genuinely repulsive phenotype, and \(9^{-1}\sum_{ij}A_{ij}=1\).

## Proof

**Fourier reduction.** A perturbation with wavenumber \(k\) has growth matrix

\[
M_N(k)=-k^2I+q(k)BC^T+\widetilde\beta L_N,\qquad
q(k)=k^2\widetilde\mu U p(U)\widehat K(k)\ge0.
\]

The derivative of \(p(\overline u)\) makes no linear contribution because the homogeneous base-state interaction potential has zero spatial gradient. The displayed matrix therefore follows directly by differentiating the differential equation and taking Fourier coefficients.

**Two phenotypes.** Write \(Q=qBC^T+\widetilde\beta L_2\), where

\[
L_2=\begin{pmatrix}-1&1\\1&-1\end{pmatrix}.
\]

The rank-one structure gives the exact determinant identity

\[
\det Q=-q\widetilde\beta(B_1+B_2)(C_1+C_2).
\]

If \(q>0\) and net interaction is positive, then \(\det Q<0\); a real two-by-two matrix with negative determinant has two real simple eigenvalues of opposite sign. If \(q=0\), the eigenvalues are \(0\) and \(-2\widetilde\beta\), also real. The scalar shift \(-k^2I\) does not alter reality. The single-phenotype case is scalar. Thus no linearly oscillatory Fourier growth rate occurs with one or two phenotypes under positive net interaction.

**Three-phenotype witness.** Put \(b=(1,-13,15)^T\), \(c=(7,2,2)^T\). The aggregate interaction is positive and correctly normalized because \(\sum b_i=3\), \(\sum c_i=11\), and \((1/9)(3/11)(3)(11)=1\). At \(k=1\),

\[
q(1)=\frac{88}{3}\frac14\frac12=\frac{11}{3},
\qquad q(1)BC^T=bc^T.
\]

Consequently \(M_3(1)=Q-I\), where

\[
Q=L_3+bc^T=
\begin{pmatrix}6&3&2\\-90&-28&-25\\105&31&29\end{pmatrix}
\]

and direct determinant expansion gives

\[
P(z)=\det(zI-Q)=z^3-7z^2+29z-33.
\]

The discriminant of \(P\) is \(-10444\). Furthermore, \(P'(z)=3z^2-14z+29>0\) on the real line, while \(P(1)=-10<0<P(2)=5\). Thus \(P\) has exactly one real root \(r\in(1,2)\); its remaining roots are a nonreal pair whose individual real parts are \((7-r)/2\), by the trace. Shifting by \(-I\) gives a real eigenvalue \(r-1\in(0,1)\) and a conjugate pair with real parts

\[
\operatorname{Re}\lambda_\pm(1)=\frac{5-r}{2}>\frac32>r-1.
\]

Hence the dominant eigenvalues at the first spatial harmonic are genuinely nonreal and unstable.

**All other spatial modes.** For each integer \(n\ge1\),

\[
M_3(n)=-n^2 I+L_3+a_nbc^T,\qquad a_n=2n^2\,2^{-n^2}.
\]

Exact characteristic polynomials at the two remaining small nonzero wavenumbers are

\[
\det(zI-M_3(2))=z^3+\frac{21}{2}z^2+52z+\frac{175}{2},
\]

\[
\det(zI-M_3(3))=z^3+\frac{7837}{256}z^2+\frac{19965}{64}z+\frac{135135}{128}.
\]

For the first polynomial, the cubic Routh–Hurwitz determinant is \(917/2>0\); for the second it is \(139168425/16384>0\). Their remaining coefficients are positive, so every eigenvalue has negative real part. For every \(|n|\ge4\), the symmetric matrix \(L_3\) is negative semidefinite and \(\|bc^T\|_2=\sqrt{395\cdot57}<151\). Thus any eigenvalue satisfies

\[
\operatorname{Re}\lambda\le -n^2+a_n\sqrt{395\cdot57}
<-n^2+\frac{302n^2}{2^{n^2}}<0.
\]

The spatially homogeneous mode has eigenvalues \(0,-1,-3\), consistent with mass conservation. Therefore the only unstable nonzero spatial Fourier modes are \(n=\pm1\), and each has a strictly dominant unstable conjugate pair. Simplicity and the spectral gaps make this property persist under sufficiently small changes in the finite coefficients and heat-kernel width.

## Verification

The standalone standard-library script `verify.py` independently reconstructs the normalized interaction coefficients, exact first-harmonic matrix, cubic polynomial and discriminant, both higher-harmonic Routh–Hurwitz polynomials, and the high-frequency operator-norm bound. It was executed successfully. The general two-phenotype determinant argument, the all-frequency estimate, and the implications of the Hurwitz inequalities are analytical proofs; no finite numerical experiment is treated as proof of an infinite statement.

## Relationship to prior work

Jewell, Krause, Maini and Gaffney (2026), especially Sections 2–3 and 6.2, introduce this precise discrete switching model and demonstrate a three-phenotype oscillatory example with signed interactions. Their displayed example has response sum \(-0.6\) and signal sum \(9.1\), hence a negative aggregate interaction; their Perron–Frobenius theorem instead excludes fastest-growing complex spectra when all off-diagonal interactions are attractive. The present theorem establishes a different, sharp positive-aggregate criterion at \(N=2\) and a normalized positive-aggregate \(N=3\) witness. The same authors' 2025 chirality work exhibits two-species oscillatory modes in a distinct model without the rank-one, positive-net, phenotype-switching restrictions; it does not contradict or imply this threshold. Giunta, Hillen, Lewis and Potts (2022) analyze symmetric nonlocal interaction matrices through an energy functional, whereas the constructed rank-one matrix is nonsymmetric and has a signed response coefficient.

## Limitations

This is a linearized Fourier-spectrum result, not a theorem that nonlinear solutions converge to traveling or oscillating patterns. The positive-net assumption is essential to the stated two-phenotype obstruction, and the nonnegative Fourier-transform assumption is part of the model. The example's signal production coefficients are positive, but one response coefficient is negative; fully attractive cross-interactions remain governed by the established Perron–Frobenius obstruction. The number three is minimal only within the stated separable and switching class, not among all multi-population advection-diffusion systems. Historical literature may contain a more general formulation; one related 2020 full text could not be examined. No independent certification has been performed.

## References

1. T. J. Jewell, A. L. Krause, P. K. Maini, E. A. Gaffney (2026), *Phenotype-structured nonlocal aggregation models I: signal production and response*, arXiv:2610.29884v1, first posted 2026-10-21, https://arxiv.org/html/2610.29884v1 (especially Sections 2–3 and 6.2).
2. T. J. Jewell, A. L. Krause, P. K. Maini, E. A. Gaffney (2025), *Chase-and-Run and Chirality in Nonlocal Models of Pattern Formation*, *Bulletin of Mathematical Biology* 87, 160; https://doi.org/10.1007/s11538-025-01539-6 (Sections 3–5).
3. V. Giunta, T. Hillen, M. A. Lewis, J. R. Potts (2022), *Detecting minimum energy states and multi-stability in nonlocal advection–diffusion models for interacting species*, *Journal of Mathematical Biology* 85, 56; https://doi.org/10.1007/s00285-022-01824-1 (Sections 2–3).
4. N. P. Taylor, H. Kim, A. L. Krause, R. A. Van Gorder (2020), *A Non-local Cross-Diffusion Model of Population Dynamics I: Emergent Spatial and Spatiotemporal Patterns*, *Bulletin of Mathematical Biology* 82, 112; https://doi.org/10.1007/s11538-020-00786-z (abstract/bibliographic comparison only; full text unavailable in this review).
