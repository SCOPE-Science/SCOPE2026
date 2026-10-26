# Exact quenched gap amplitude and Gaussian fluctuations in a balanced-disorder Ising chain

## Finding
For the bounded independent-coupling, exactly balanced open chain defined below, the lowest positive fermionic excitation has an almost-sure *nonrandom* critical amplitude and a nontrivial Gaussian sample-to-sample correction:
\[
N\varepsilon_N\xrightarrow{\mathrm{a.s.}}\frac{\pi}{2\sqrt m},\qquad
\sqrt N\left(N\varepsilon_N-\frac{\pi}{2\sqrt m}\right)
\xRightarrow{\mathrm d}\mathcal N\!\left(0,\frac{3\pi^2s^2}{32m^3}\right).
\]
Here \(m=\mathbb E[J_1^{-2}]\) and \(s^2=\operatorname{Var}(J_1^{-2})\). The second limiting law is a point mass at zero when \(s^2=0\). This specifies the gap prefactor and its asymptotic fluctuations, not merely its dynamical exponent.

## Assumptions and scope
Fix \(0<a<b<\infty\). For each integer \(N\ge2\), use the same infinite independent identically distributed sequence \((J_i)_{i\ge1}\) of strictly positive couplings with \(a\le J_i\le b\) almost surely. Consider the open spin Hamiltonian
\[
H_N=-\frac12\sum_{i=1}^{N-1}J_i\sigma_i^x\sigma_{i+1}^x
-\frac12\sum_{i=1}^{N}h_i\sigma_i^z,
\qquad h_i=J_i\ (1\le i<N),\quad h_N=1.
\]
The boundary value \(h_N=1\) is part of the model, corresponding to the \(s=0\) balance of Eq. (34) of Juhász [1]; it is not replaced with a bulk mean. Let \(\varepsilon_N\) be the **least singular value** of the \(N\)-by-\(N\) lower-bidiagonal matrix whose diagonal entries are \(h_i\) and whose subdiagonal entries are \(J_i\). Under the given Hamiltonian normalization, these are precisely the positive Bogoliubov excitation energies [1, Eq. (7)]. The result is not asserted for couplings approaching zero, long-range-correlated couplings, other balance exponents, or the lowest excitation restricted to conserved fermion parity.

## Proof
**1. Exact random-string reduction.** Write \(M_N\) for that bidiagonal matrix, \(D_N=\operatorname{diag}(h_1,\dots,h_N)\), and \(S_N\) for the strict lower shift. Because \(J_i=h_i\) for \(i<N\), we have \(M_N=(I+S_N)D_N\). Given a real vector \(v\), set \(z_i=(-1)^i h_i v_i\), with \(z_0=0\). Then \((M_Nv)_i=(-1)^i(z_i-z_{i-1})\), so the smallest squared singular value has the *exact* variational form
\[
\varepsilon_N^2
=\min_{z\ne0}\frac{\sum_{i=1}^N(z_i-z_{i-1})^2}{\sum_{i=1}^Nw_i z_i^2},
\quad w_i=J_i^{-2}\ (i<N),\quad w_N=1.
\]
Let \(K_N\) be the positive stiffness matrix of the numerator: its diagonal is \(2\), except that the last element is \(1\), and both neighboring diagonals equal \(-1\). A direct difference-equation calculation gives \((K_N^{-1})_{ij}=\min(i,j)\). Thus \((N\varepsilon_N)^{-2}\) equals the spectral radius \(\rho_N\) of the positive \(N\)-by-\(N\) matrix with elements \(\min(i,j)w_j/N^2\).

**2. A fixed-space compact-operator limit.** Introduce the atomic measure
\[
\mu_N=\frac1N\sum_{j=1}^{N}w_j\delta_{j/N}
\]
and, on the Banach space \(\operatorname{Lip}([0,1])\) with its usual supremum-plus-Lipschitz norm, the finite-rank operator
\[
(A_N f)(x)=\int_0^1\min(x,y)f(y)\,\mu_N(dy).
\]
The nonzero eigenvalues of \(A_N\) equal those of the displayed matrix. Set \(\mu_0(dy)=m\,dy\) and \((A_0f)(x)=m\int_0^1\min(x,y)f(y)\,dy\). For the cumulative discrepancy
\[
\delta_N=\sup_{0\le t\le1}|\mu_N([0,t])-mt|,
\]
Stieltjes integration by parts applied to \(y\mapsto \min(x,y)f(y)\), and to its almost-everywhere \(x\)-derivative \(y\mapsto \mathbf1_{(x,1]}(y)f(y)\), gives a deterministic bound
\[
\|A_N-A_0\|_{\operatorname{Lip}\to\operatorname{Lip}}
\le C\delta_N.
\]
The constant depends only on the fixed norm convention. Indeed, the total variation of either test integrand is bounded by a multiple of \(\|f\|_\infty+\operatorname{Lip}(f)\). For the empirical weights, \(\delta_N\) is bounded by the maximum centered partial sum \(\max_{j<N}|\sum_{i\le j}(J_i^{-2}-m)|/N\), plus \(O(N^{-1})\), including the distinguished endpoint \(w_N=1\). The strong law and its maximal-partial-sum consequence yield \(\delta_N\to0\) almost surely; Kolmogorov's maximal inequality yields \(\delta_N=O_{\mathbb P}(N^{-1/2})\).

**3. The isolated principal mode.** For a nonzero eigenpair \(A_0u=\rho u\), differentiation twice gives \(u''=-(m/\rho)u\), with \(u(0)=0\), \(u'(1)=0\). Put \(k=\pi/2\). The largest eigenvalue is simple, \(\rho_0=m/k^2\), with right eigenfunction \(u(x)=\sin(kx)\) and normalized left eigenfunctional \(\ell(f)=2\int_0^1u(x)f(x)\,dx\); it satisfies \(\ell(u)=1\). The remaining eigenvalues \(m/((j+\tfrac12)^2\pi^2)\), indexed by \(j\ge1\), lie strictly below \(\rho_0\). Both operators are compact on \(\operatorname{Lip}([0,1])\), so the isolated simple eigenvalue perturbation formula applies. Since \(\|A_N-A_0\|=O_{\mathbb P}(N^{-1/2})\),
\[
\rho_N=\rho_0+\ell((A_N-A_0)u)+O_{\mathbb P}(N^{-1}).
\]
This expansion is not an inference from numerical eigenvalues: it is the resolvent expansion for the spectral projection around the isolated principal eigenvalue. A positive-operator comparison and convergence of the compact operators ensure that the nearby eigenvalue is the top one for large \(N\).

**4. The exact first variation.** Since
\[
\int_0^1\min(x,y)u(x)\,dx=\frac{u(y)}{k^2},
\]
Fubini's theorem gives the exact identity
\[
\ell((A_N-A_0)u)=\frac2{k^2}
\left[\frac1N\sum_{j=1}^{N}w_j\sin^2(kj/N)
-m\int_0^1\sin^2(ky)\,dy\right].
\]
Replacing the last weight by \(m\) and comparing the smooth Riemann sum with its integral changes the bracket by \(O(N^{-1})\). Hence
\[
\rho_N=\frac m{k^2}+\frac2{k^2N}\sum_{j=1}^{N-1}
(J_j^{-2}-m)\sin^2(kj/N)+O_{\mathbb P}(N^{-1}).
\]
The weights of this triangular array are bounded; its limiting variance is obtained from \(\int_0^1\sin^4(\pi y/2)\,dy=3/8\). Lindeberg's central limit theorem therefore gives
\[
\sqrt N(\rho_N-\rho_0)\xRightarrow{\mathrm d}
\mathcal N\left(0,\frac{3s^2}{2k^4}\right).
\]
Finally, \(N\varepsilon_N=\rho_N^{-1/2}\) exactly. The continuous-mapping theorem gives the almost-sure amplitude, and the delta method with derivative \(-\tfrac12\rho_0^{-3/2}\) gives the claimed fluctuation variance \(3s^2k^2/(8m^3)=3\pi^2s^2/(32m^3)\).

## Verification
The identity \((K_N^{-1})_{ij}=\min(i,j)\) and the Rayleigh-quotient reduction can be checked independently on finite matrices. A standalone `verify_gap.py` forms the original bidiagonal singular-value problem as a symmetric tridiagonal eigenproblem and checks the limiting mean and variance empirically for a transparent test law, \(J\sim\operatorname{Unif}[1/2,1]\). For this law, \(m=2\), \(s^2=2/3\), hence the predicted amplitude is \(\pi/(2\sqrt2)\) and the predicted fluctuation variance is \(\pi^2/128\). Finite samples are consistency checks **only**; the proof of the infinite-size limit is Steps 1–4.

## Relationship to prior work
Juhász [1, Secs. II and V.2, especially Eqs. (7), (34), (36)–(40)] established the exact fermionic matrix and general random-walk bounds, giving the critical scaling exponent for this balanced model. Shirai and Tanaka [2, Secs. 2–3 and Appendix A] proved bounds on the dynamical exponent under coupling-field correlations. Juhász and Roósz [3, Sec. II and numerical sections] discussed this balance in annealing and quench problems. These works motivate the particular random spin chain but, in the inspected portions, do not determine the sample-independent amplitude \(\pi/(2\sqrt{\mathbb E[J^{-2}]})\) or the central limit fluctuation constant of its lowest fermionic gap. Bal [4, Sec. 4] established general Gaussian eigenvalue correctors in random-medium spectral perturbation problems; its operator family is not the discrete generalized random-mass string obtained in Step 1, and its stated hypotheses alone do not supply this chain-specific amplitude or variance without the reduction and first-variation calculation given here. Consequently the result is a model-specific refinement of the known exponent, rather than a claim of a new general spectral CLT method.

## Limitations
The theorem requires independent couplings uniformly bounded away from zero and infinity; heavy-tail cases may have different exponents and laws. It does not give the critical behavior for other field-coupling balance exponents. The excitation \(\varepsilon_N\) is the single-quasiparticle gap and should not be substituted for the parity-conserving two-quasiparticle gap relevant to some driving protocols. The convergence in distribution supplies a fixed-order fluctuation law, not a large-deviation estimate or a finite-size Berry–Esseen bound. General stochastic homogenization literature may contain abstract results from which related fluctuation principles can be obtained, and independent literature verification remains to be performed.

## References
[1] R. Juhász, *Exact bounds on the energy gap of transverse-field Ising chains by mapping to random walks*, arXiv:2206.11575 (first posted 2022-06-23), especially Eq. (7), Eq. (34), and Sec. V.2. https://arxiv.org/abs/2206.11575

[2] T. Shirai and S. Tanaka, *Exact bounds for dynamical critical exponents of transverse-field Ising chains with a correlated disorder*, arXiv:2007.07439 (first posted 2020-07-15). https://arxiv.org/abs/2007.07439

[3] R. Juhász and G. Roósz, *Reducing defect production in random transverse-field Ising chains by inhomogeneous driving fields*, arXiv:2309.12827 (first posted 2023-09-22). https://arxiv.org/abs/2309.12827

[4] G. Bal, *Central limits and homogenization in random media*, arXiv:0710.0363 (first posted 2007-10-01), especially Sec. 4. https://arxiv.org/abs/0710.0363
