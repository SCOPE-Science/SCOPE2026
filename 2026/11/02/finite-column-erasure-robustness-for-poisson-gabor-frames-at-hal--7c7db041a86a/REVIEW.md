# Independent mathematical audit

## correctness

PASS

For g_w=1/(x²+w²), w>0, k integer except finite F and modulation e^{pi imx}, Fourier Parseval on [0,2] reduces L2 frame estimates to two convolution channels on ell²(Z). Poisson summation yields symbols A_t(theta) and A_(t−1)(theta) with coefficient determinant −2rz(1−r²)/((1−rz)(1+rz)(z−r)(z+r)), r=e^{−pi w}, |z|=1, nonzero; therefore complete two-channel convolution is uniformly bounded below on compact t,theta. For fixed t the channel ratio includes e^{i theta/2}(a+b e^{w theta})/(a_prime+b_prime e^{w theta}); if rational in e^{i theta}, analytic continuation forces 2pi-periodicity, whose polynomial constant term gives impossible −aa_prime=aa_prime. If finitely many channel output coefficients are erased, any kernel input would produce two finite Laurent polynomials with rational channel ratio, impossible; finite-rank perturbation of positive invertible complete frame operator is Fredholm index zero, hence bounded invertible; norm-continuity on t compact gives uniform positive lower bound. For one-sided k<=0, f_R=indicator[R,R+1] has unit norm and analysis energy <=2 sum_{n>=R} n^-4=O(R^-3), so no lower frame bound. Source CHECK.py independently read: exact fractional determinant identity, 12001-term Poisson Fourier comparisons and halfline energy tests are consistency checks, not the all-w/F proof.

## originality

PASS

PASS best-of-knowledge: Belov--Semenov October 21, 2026 Theorem 1 solves Poisson Gabor with an irregular set in MODULATION and regular translations; the authors explicitly say their criterion does not solve the REVERSE arrangement. Deleting finitely many translation columns is precisely a reverse-orientation special case and is not a direct corollary by interchanging axes, because Fourier transform changes the Poisson window. Existing lattice-density/frame criteria and generic excess theorems do not prove robustness after infinitely many atoms (an entire modulation column) removed. Historical alternative transfer-function results remain possible.

## value

PASS

In an oversampled Gabor frame, deleting a finite number of entire integer translation columns removes infinitely many atoms per deletion; this is not implied by finite-atom excess. The exact preservation theorem for arbitrary finite F and sharp contrasting one-sided infinite deletion clarify a motivated nonuniform-sampling stability boundary for a canonical Poisson window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
