# Moment-exact diffusion with maximal stationary-law failure under common Poisson resetting

## Finding

Consider \(d\ge2\) coordinates obeying a linear relaxation/immigration equation between common Poisson reset times, with \(X_i\mapsto A X_i\) at every reset. Here all \(a_i,b_i,\rho\) are positive, the \(a_i\) are pairwise distinct, and \(A\) is an independent mark in \([0,1]\), not almost surely \(1\). Put
\[
\delta=\rho\mathbb E(1-A),\quad \kappa=\rho\mathbb E(1-A)^2,
\quad \zeta=\rho\mathbb E(1-A^2)=2\delta-\kappa,
\quad c_i=a_i+\delta.
\]
The scalar-common-noise Itô diffusion
\[
 dY_i=(b_i-c_iY_i)\,dt+\sqrt\kappa\,Y_i\,dW_t
\]
has exactly the same first and second joint moments as the reset process \(X\) at **every finite time**, whenever their initial first and second joint moments agree. Its stationary means are \(m_i=b_i/c_i\), and both stationary covariance matrices are the identical, strictly positive-definite matrix
\[
 C_{ij}=\frac{\kappa m_i m_j}{a_i+a_j+\zeta},\qquad
 \det C=\frac{\kappa^d\prod_i m_i^2\prod_{i<j}(a_j-a_i)^2}{\prod_{i,j}(a_i+a_j+\zeta)}>0.
\]
Nonetheless, when all reset marks equal zero, the unique stationary law of \(X\) is singular with respect to Lebesgue measure while the unique stationary law of \(Y\) has a Lebesgue density. Thus the two stationary probability measures have **total-variation distance exactly one**, despite identical full-rank covariance matrices and equal means. The generators agree on all polynomials of total degree at most two but, for \(f(x)=x_i^3\),
\[
 (\mathcal L_X-\mathcal L_Y)f(x)=-\rho\,\mathbb E(1-A)^3\,x_i^3,
\]
so the degree-two exactness cannot be extended to all cubic polynomials for a genuine resetting law.

## Assumptions and scope

Fix an integer \(d\ge2\), pairwise distinct \(a_1,\ldots,a_d>0\), \(b_1,\ldots,b_d>0\), and a rate \(\rho>0\). Let a rate-\(\rho\) Poisson process carry independent identically distributed marks \(A\in[0,1]\), independent of everything else, with \(\Pr(A<1)>0\). Between resets, \(\dot X_i=b_i-a_iX_i\); at a reset, all \(X_i\) are simultaneously multiplied by the **same** mark. Let \(W\) be one real Brownian motion and let \(Y\) solve the displayed Itô equation, with the same parameter values. Initial laws need finite second moments for finite-time moment equality. Stationary comparisons concern the unique invariant probability measures. The strongest singularity statement assumes \(\Pr(A=0)=1\) and is not asserted for arbitrary marks. Total variation is \(d_{\mathrm{TV}}(\mu,\nu)=\sup_B|\mu(B)-\nu(B)|\), with maximum \(1\).

## Proof

**1. Quadratic generator agreement.** For smooth polynomials the jump and diffusion generators are, respectively,
\[
\mathcal L_X f(x)=\sum_i(b_i-a_ix_i)\partial_i f(x)+\rho\mathbb E[f(Ax)-f(x)],
\]
\[
\mathcal L_Y f(x)=\sum_i(b_i-c_ix_i)\partial_i f(x)
 +\frac\kappa2\sum_{i,j}x_ix_j\partial_i\partial_jf(x).
\]
Their values on the basis \(1,x_i,x_ix_j\) agree by \(c_i-a_i=\rho\mathbb E(1-A)\) and \(\zeta=2\delta-\kappa\). Indeed for the quadratic monomial both give
\[
\mathcal L(x_ix_j)=b_ix_j+b_jx_i-(a_i+a_j+\zeta)x_ix_j,
\]
including \(i=j\), where the two linear terms both occur. Dynkin's formula or Itô's formula closes the same finite-dimensional linear moment system for \(X\) and \(Y\). The system is globally well posed and its unique solution gives equality of all means and raw second moments at every time from matched initial moments. For a cubic monomial the jump contribution has coefficient \(\rho(\mathbb EA^3-1)\), whereas diffusion adds the drift correction \(-3\delta\) and the Itô correction \(+3\kappa\); their difference simplifies to \(-\rho\mathbb E(1-A)^3\), which is nonzero for a genuine reset at nonzero \(x_i\).

**2. Invariant laws and moments.** On a common realization of reset events, distances between two solutions of the jump dynamics decay coordinatewise at least as \(e^{-a_it}\), since every reset mark is at most one; the positive forcing bounds stationary trajectories. Hence there is a unique stationary law with finite moments. The diffusion's linear stochastic flow contracts coordinatewise in mean square at rate \(2c_i-\kappa=2a_i+\zeta>0\). Its unique invariant solution can also be constructed as a convergent stochastic convolution. Stationarity of the shared first- and second-moment equations yields
\[
 m_i=\frac{b_i}{c_i},\qquad
 M_{ij}=\frac{b_im_j+b_jm_i}{c_i+c_j-\kappa},\qquad
 C_{ij}=M_{ij}-m_im_j=\frac{\kappa m_im_j}{a_i+a_j+\zeta}.
\]
The strict Cauchy-determinant identity
\[
 \det\left(\frac1{a_i+a_j+\zeta}\right)_{i,j=1}^d
 =\frac{\prod_{i<j}(a_j-a_i)^2}{\prod_{i,j}(a_i+a_j+\zeta)}
\]
proves the asserted positivity; every denominator is positive. The same Gram kernel can be written \(\int_0^\infty e^{-(a_i+\zeta/2)u}e^{-(a_j+\zeta/2)u}\,du\), proving strict positive definiteness directly from the independence of distinct exponentials.

**3. Reset law on a one-dimensional curve.** For \(A=0\) almost surely, the stationary system has an exponential time \(T\sim\operatorname{Exp}(\rho)\) since its last simultaneous reset, so
\[
 X_i\overset d=\frac{b_i}{a_i}(1-e^{-a_iT}),\qquad i=1,\ldots,d.
\]
The image of \([0,\infty)\) under this continuously differentiable curve is a countable union of compact Lipschitz images of intervals. It has \(d\)-dimensional Lebesgue measure zero for \(d\ge2\). Denote this support by \(\Gamma\); then \(\mathbb P(X\in\Gamma)=1\).

**4. The one-noise diffusion has a full-dimensional density.** For \(A=0\), \(\delta=\kappa=\rho>0\); the following also holds whenever \(\kappa>0\). Using a Brownian motion \(B\) on \([0,\infty)\), the stationary diffusion vector has the law
\[
 F_i=b_i\int_0^\infty\exp(-q_i u+\sqrt\kappa\,B_u)\,du,
 \qquad q_i=c_i+\kappa/2.
\]
The integrals converge almost surely by \(B_u/u\to0\), and in \(L^2\) because \(2c_i>\kappa\). Their first two moments solve exactly the stationary moment equations in step 2. More precisely, each \(F_i\) is Malliavin differentiable, with
\[
 D_sF_i=\sqrt\kappa\,b_i\int_s^\infty e^{-q_i u+\sqrt\kappa B_u}\,du,
\qquad
 \mathbb E\int_0^\infty(D_sF_i)^2\,ds
 =\frac{2\kappa b_i^2}{c_i(2c_i-\kappa)^2}<\infty.
\]
The formula follows first for truncated integrals, then by \(L^2\) convergence and closability of the Malliavin derivative. To show the Malliavin covariance \(\gamma_F=(\langle DF_i,DF_j\rangle_{L^2[0,\infty)})\) is nonsingular almost surely, fix any Brownian sample path for which these continuous tail functions and their derivatives exist. If \(z^\mathsf T\gamma_Fz=0\), then \(\sum_i z_iD_sF_i=0\) for almost every \(s\). The continuous sum therefore vanishes identically, and differentiation for almost every \(s\) yields
\[
 e^{\sqrt\kappa B_s}\sum_i z_i b_i e^{-q_is}=0.
\]
The rates \(q_i\) are pairwise distinct and all \(b_i\) are nonzero, so linear independence of the exponential functions forces every \(z_i=0\). This applies pathwise also to random null vectors. Consequently \(\det\gamma_F>0\) almost surely. The standard Bouleau–Hirsch absolute-continuity criterion for Malliavin-differentiable vectors gives a joint Lebesgue density for \(F\), hence for stationary \(Y\). Thus \(\mathbb P(Y\in\Gamma)=0\) while \(\mathbb P(X\in\Gamma)=1\), and the asserted total-variation distance is \(1\).

## Verification

Run the standalone standard-library script `python3 check.py`. It performs 21,140 exact rational assertions for dimensions \(2\) through \(5\), heterogeneous damping and drift coefficients, deterministic full resets and two-point partial-reset marks. Assertions reproduce the quadratic moment equations, the Cauchy determinant, cubic generator mismatch, and the exponential-age stationary covariance in the full-reset case. Output: `PASS: 21140 exact rational assertions in affine common-reset systems`. These finite rational checks are diagnostic; generator identities, infinite-dimensional path regularity, positive definiteness for every finite \(d\), and absolute continuity are proved analytically above.

## Relationship to prior work

T. Galla, *A diffusion approximation for systems with frequent weak resetting* (arXiv:2602.21635v1, publicly submitted 25 February 2026) develops a diffusion approximation for **frequent, weak** resetting and associated multi-particle correlations. Its supplemental linear correlated example treats an unforced setting and does not derive exact degree-two equivalence for every reset strength together with a maximal total-variation obstruction for full resetting. We do **not** claim novelty for the second-order Taylor expansion itself, nor for general Malliavin absolute-continuity principles. P. C. Bressloff studies common resetting of interacting stochastic particles (arXiv:2401.03501), but its globally reset diffusion-density framework does not imply the stated scalar-driven deterministic-reset singularity/full-covariance contrast. K. S. Olsen studies stationary moments for **resets to a distribution** in a different model (arXiv:2310.04840v1); that renewal framework does not compare the complete common-multiplier jump system with a precisely moment-equivalent single-noise diffusion or prove the total-variation contrast. Earlier generic polynomial-process and diffusion-approximation theory covers parts of the method, not the compound conclusion. Priority may remain uncertain in less readily searchable multiplicative-catastrophe literature.

## Limitations

The full total-variation separation is proved for complete simultaneous resets \(A=0\), not arbitrary weak or partial reset laws. Coordinates require distinct positive relaxation rates and positive forcing; repeated rates make the Cauchy covariance singular. The matching statement concerns **one-time first and second joint moments**, not multi-time covariances, higher moments, path laws, or weak approximation in any metric. The stationary diffusion has an absolutely continuous law, but an explicit density, smoothness, and tail asymptotics are not claimed. This is a mathematical comparison, not an error assertion about the cited weak-resetting approximation outside its asymptotic domain.

## References

1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (25 February 2026), https://arxiv.org/html/2602.21635 .
2. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting*, arXiv:2401.03501 (2024), https://arxiv.org/pdf/2401.03501 .
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840v1 (2023); *Physical Review E* 108, 044120, https://arxiv.org/pdf/2310.04840 .
4. D. Nualart, *The Malliavin Calculus and Related Topics*, second edition, Springer (2006), absolute continuity criterion for nondegenerate Malliavin matrices.
