# Three square Gaussian Ritz sketches aggregated by medians match one-row oversampling in exact Frobenius risk

## Finding

Let \(A\in\mathbb C^{n\times n}\), \(W\in\mathbb C^{n\times m}\) have orthonormal columns, and \(1\le m<n\). Write \(T=W^*AW\) for the ordinary Rayleigh--Ritz compression and \(E=(I-WW^*)AW\) for its orthogonal residual. For three independent standard circular complex-Gaussian test matrices \(\Omega_t\in\mathbb C^{n\times m}\), form the square randomized Petrov--Galerkin compressions
\[
M_t=(\Omega_t^*W)^{-1}\Omega_t^*AW,\qquad t=1,2,3.
\]
Construct \(\widetilde M\) entrywise by taking the ordinary median separately across the three real parts and across the three imaginary parts. Independently, form the one-row-oversampled least-squares compression
\[
M_+=(\Omega_+^*W)^\dagger\Omega_+^*AW,\qquad
\Omega_+\in\mathbb C^{n\times(m+1)}
\]
with standard circular complex-Gaussian entries. The exact finite-dimensional identity is
\[
\boxed{\mathbb E\|\widetilde M-T\|_F^2
=\mathbb E\|M_+-T\|_F^2
=m\|E\|_F^2.}
\]
In contrast, if \(E\ne0\), then \(\mathbb E\|M_1-T\|_F^2=+\infty\); if \(E=0\), all compressions and their medians agree with \(T\) almost surely.

## Assumptions and scope

All matrices are deterministic except for the displayed independent Gaussian sketches; arithmetic is exact. Standard circular complex-Gaussian means real and imaginary parts independent, each with variance \(1/2\), so the complex variance is one. Every Gaussian square block is nonsingular with probability one, and the oversampled block has full column rank almost surely. No normality, diagonalizability, spectral-gap, or eigenvector assumption is imposed on \(A\). The medians are taken entrywise in the specified basis, and do not require any independence across different entries. The claim concerns expected squared Frobenius distance from the ordinary compressed matrix, not spectral error or computed Ritz values.

## Proof

**1. Orthogonal Gaussian decomposition.** Complete \(W\) to a unitary matrix \([W,U]\), and put \(F=U^*AW\). Then \(AW=WT+UF\) and \(\|F\|_F=\|E\|_F\). For a square test matrix, write \(G=\Omega^*W\), \(H=\Omega^*U\). These are independent matrices with standard circular complex-Gaussian entries, of sizes \(m\times m\) and \(m\times(n-m)\), respectively. Therefore
\[
M-T=G^{-1}HF.
\]
Fix an output entry \((i,j)\), and let \(f_j\) be column \(j\) of \(F\). If \(f_j=0\), the entry error is zero. Otherwise \(h=Hf_j\) is an independent centered complex-Gaussian vector with covariance \(\|f_j\|_2^2 I_m\).

**2. Universal complex ratio law.** Conditional on all columns of \(G\) except its \(i\)th, choose a unit vector \(\ell\) perpendicular to their span. Multiplying \(Gz=h\) by \(\ell^*\) gives
\[
(M-T)_{ij}=\frac{\ell^*h}{\ell^*g_i}
=\|f_j\|_2\frac{Z_1}{Z_2},
\]
where the numerator and denominator \(Z_1,Z_2\) are independent standard circular complex Gaussians, even conditional on the other columns. The ratio \(Z=Z_1/Z_2\) has planar density
\[
p_Z(z)=\frac1{\pi(1+|z|^2)^2},\qquad z\in\mathbb C,
\]
obtained directly by changing variables \((z,w)\mapsto(zw,w)\) in the joint Gaussian density, whose Jacobian is \(|w|^2\). Integrating out the imaginary coordinate, the real marginal \(X=\operatorname{Re}Z\) has density and distribution function
\[
p_X(x)=\frac1{2(1+x^2)^{3/2}},\qquad
F_X(x)=\frac12\left(1+\frac{x}{\sqrt{1+x^2}}\right).
\]
The imaginary marginal has the same law. In particular \(\mathbb E|Z|^2=+\infty\): in polar coordinates its tail-integral is a constant times \(\int_1^\infty r^3(1+r^2)^{-2}\,dr\), which diverges.

**3. Median-of-three cancellation.** For the median \(X_{(2)}\) of three independent copies of \(X\), the order-statistic density is \(6F_X(x)(1-F_X(x))p_X(x)=3/[4(1+x^2)^{5/2}]\). It is a probability density. With \(u=x/\sqrt{1+x^2}\in(-1,1)\), its measure becomes \(3(1-u^2)\,du/4\). Hence
\[
\mathbb E[X_{(2)}^2]
=\frac34\int_{-1}^1u^2\,du=\frac12.
\]
The imaginary median has the same marginal second moment; its dependence on the real median does not affect \(\mathbb E|Z_{\mathrm{med}}|^2\), which equals \(1\). Since multiplication by \(\|f_j\|_2\) is by a nonnegative real scale, the squared risk of entry \((i,j)\) in \(\widetilde M\) is exactly \(\|f_j\|_2^2\). Summing over all \(m\) rows and \(m\) columns yields
\[
\mathbb E\|\widetilde M-T\|_F^2
=\sum_{i=1}^m\sum_{j=1}^m\|f_j\|_2^2
=m\|F\|_F^2.
\]
The same ratio law makes the squared risk of a single square sketch infinite whenever any \(f_j\ne0\).

**4. The extra Gaussian row.** For the independent rectangular Gaussian test matrix let \(B=\Omega_+^*W\in\mathbb C^{(m+1)\times m}\) and \(J=\Omega_+^*U\), independent. Then \(M_+-T=B^\dagger JF\), and conditioning on \(B\) gives
\[
\mathbb E[\|M_+-T\|_F^2\mid B]
=\operatorname{tr}((B^*B)^{-1})\|F\|_F^2.
\]
Fix column \(i\) of \(B\). The Schur complement gives \(((B^*B)^{-1})_{ii}=\|(I-P_{B_{-i}})b_i\|_2^{-2}\). Conditional on the other \(m-1\) columns, their orthogonal complement in \(\mathbb C^{m+1}\) has dimension two, and the squared length of the independent standard complex-Gaussian projection is the sum of two independent unit-mean exponentials: a \(\operatorname{Gamma}(2,1)\) variable. Its reciprocal mean is \(\int_0^\infty e^{-t}\,dt=1\). Summing the \(m\) diagonal entries, \(\mathbb E\operatorname{tr}((B^*B)^{-1})=m\), and therefore \(\mathbb E\|M_+-T\|_F^2=m\|F\|_F^2\). This completes the proof.

## Verification

Run `python3 verify.py` with the Python standard library. It checks the transformed median law and its exact rational second-moment identity, then independently simulates the square-median and one-row-oversampled estimators for \(m=1\) and \(m=2\), using fixed pseudorandom seeds and stated finite tolerances. The script prints both empirical risks and their shared exact targets. Simulations are not used to establish any infinite-dimensional or all-parameter assertion; those follow from the preceding analytic calculation.

## Relationship to prior work

Shao's randomized Rayleigh--Ritz method (first public April 1, 2026) introduced the square complex-Gaussian Petrov--Galerkin compression and proves high-probability stability of extracted eigenpairs. Its reported medians summarize *errors of repeated independent runs*, not entrywise median aggregation of the compressed matrices. Its oversampling experiment uses a different rectangular-pencil total-least-squares formulation. Nakatsukasa and Tropp (2024) formulate the least-squares sketched Rayleigh--Ritz compression and establish general approximation theory with oversampling. The complex-Gaussian ratio density, order-statistic rule, and reciprocal-Gamma/Wishart calculations are classical ingredients and are not individually claimed as new. The point here is their exact finite-dimensional equality linking an entrywise robust aggregation of square Petrov--Galerkin compressions to the one-row least-squares oversampling benchmark, including the infinite-risk contrast for a lone square sketch.

## Limitations

This result concerns compression-matrix risk relative to \(W^*AW\), not individual Ritz eigenvalue/vector error, spectral separation, singularity probability in floating point, or dynamic subspace convergence. Entrywise medians need not be unitarily equivariant at the sample level or correspond to an ordinary Petrov--Galerkin compression; comparing their eigenvalues with single-sketch Ritz eigenvalues requires separate analysis. Three independent square sketches can require substantially more projection and solve work than one sketch with one additional row. The exact equalities assume independent isotropic *complex* Gaussian sketches, not real Gaussian, correlated sketches, or arbitrary embedding distributions.

## References

1. Nian Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization*, arXiv:2604.01037, first public 2026-04-01. https://arxiv.org/abs/2604.01037
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. 45 (2024), 1183–1214. DOI:10.1137/23M1565413. https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf
