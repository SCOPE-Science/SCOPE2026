# Sharp coherent-state splitting for two distant Gaussian localization disks

## Finding

Fix \(s>0\). Let \(\Omega_d\) be the union of two Euclidean disks of radius \(\sqrt{s}\), centered at \(a,b\in\mathbb C\) with separation \(d=|a-b|>2\sqrt{s}\). Let \(T_d\) be the indicator-symbol Toeplitz localization operator on the standard Bargmann–Fock space, and let \(\Lambda_1(d)\ge\Lambda_2(d)\) be its two largest eigenvalues, with multiplicity.

Set
\[
\lambda_0=1-e^{-s},\qquad \delta=se^{-s},\qquad
\varepsilon_d=e^{-d^2/2},\qquad
\eta_d=s\exp\!\left(-\frac{(d-2\sqrt{s})^2}{2}\right).
\]
For every \(d>2\sqrt{s}\) with \(\eta_d<\delta/4\), both inequalities below hold:
\[
0\le\Lambda_j(d)-\lambda_0\bigl(1+(-1)^{j+1}\varepsilon_d\bigr)
\le\frac{\eta_d^2}{\delta-2\eta_d},\qquad j=1,2.
\]
In particular, at every fixed \(s>0\),
\[
\Lambda_1(d)=\lambda_0+\lambda_0e^{-d^2/2}+O_s\!\left(e^{-(d-2\sqrt{s})^2}\right),
\]
\[
\Lambda_2(d)=\lambda_0-\lambda_0e^{-d^2/2}+O_s\!\left(e^{-(d-2\sqrt{s})^2}\right)
\]
as \(d\to\infty\). Hence the complete sharp first splitting law is
\[
\lim_{d\to\infty}e^{d^2/2}\bigl(\Lambda_1(d)-\lambda_0\bigr)
=\lim_{d\to\infty}e^{d^2/2}\bigl(\lambda_0-\Lambda_2(d)\bigr)=\lambda_0,
\]
and \(\Lambda_1(d)-\Lambda_2(d)\sim2\lambda_0 e^{-d^2/2}\).

## Assumptions and scope

The Bargmann–Fock Hilbert space is
\[
\mathcal F^2=\left\{F\text{ entire}:\|F\|^2
=\frac1\pi\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
Its reproducing kernel is \(K(z,w)=e^{z\overline w}\). For a bounded measurable set \(\Omega\), the positive compact localization operator \(T_\Omega\) is defined by the quadratic form
\[
\langle T_\Omega F,F\rangle
=\frac1\pi\int_\Omega|F(z)|^2e^{-|z|^2}\,dA(z).
\]
Disks are open; their boundaries have zero planar measure. The result concerns equal-radius, disjoint disks at fixed positive radius while their separation diverges. No relation between the centers' absolute positions and the origin is imposed.

## Proof

**1. The one-disk spectrum and its gap.** For a disk centered at the origin, the standard orthonormal monomials \(z^n/\sqrt{n!}\) diagonalize \(T_{D_{\sqrt{s}}(0)}\), with eigenvalues
\[
\lambda_n(s)=\frac1{n!}\int_0^s t^n e^{-t}\,dt
=1-e^{-s}\sum_{k=0}^n\frac{s^k}{k!},\qquad n=0,1,2,\ldots.
\]
They decrease strictly. The top eigenvalue is \(\lambda_0=1-e^{-s}\), and the gap to the rest is \(\lambda_0-\lambda_1=se^{-s}=\delta>0\). Weyl (magnetic translation) covariance gives the same spectrum for either translated disk. Its normalized top Fock eigenvector is the coherent state
\[
k_a(z)=\exp(\overline a z-|a|^2/2),\qquad \|k_a\|=1.
\]

**2. Restriction factorization and exact coherent coupling.** Put \(d\gamma(z)=\pi^{-1}e^{-|z|^2}dA(z)\). Define the bounded restriction operators \(B_a:\mathcal F^2\to L^2(D_{\sqrt{s}}(a),d\gamma)\) and \(B_b\) analogously, and write \(B=(B_a,B_b)\). Then
\[
B^*B=T_d,
\qquad
S:=BB^*=\begin{pmatrix}A_a&C\\C^*&A_b\end{pmatrix},
\quad A_a=B_aB_a^*,\quad C=B_aB_b^*.
\]
The nonzero eigenvalues, including multiplicity, of the compact positive operators \(T_d\) and \(S\) agree. The rank-one leading eigenvectors of \(A_a\) and \(A_b\) are
\[
u_a=\lambda_0^{-1/2}B_a k_a,\qquad u_b=\lambda_0^{-1/2}B_b k_b.
\]
Let \(P\) project onto the two-dimensional span of \((u_a,0)\) and \((0,u_b)\), and let \(Q=I-P\). Because \(T_{D_{\sqrt{s}}(a)}k_a=\lambda_0 k_a\),
\[
\langle u_a,C u_b\rangle
=\lambda_0^{-1}\langle T_{D_{\sqrt{s}}(a)}k_a,T_{D_{\sqrt{s}}(b)}k_b\rangle
=\lambda_0\langle k_a,k_b\rangle.
\]
The coherent overlap satisfies
\[
\langle k_a,k_b\rangle
=\exp\!\left(\overline a b-\frac{|a|^2+|b|^2}{2}\right),
\qquad |\langle k_a,k_b\rangle|=e^{-d^2/2}.
\]
Thus \(PSP\) has the **exact** two eigenvalues \(\mu_1=\lambda_0(1+\varepsilon_d)\) and \(\mu_2=\lambda_0(1-\varepsilon_d)\).

**3. Control of all remaining modes.** The off-diagonal integral operator \(C\) has kernel \(e^{z\overline w}\) relative to \(d\gamma\) on the two disks. Therefore
\[
\begin{aligned}
\|C\|^2&\le\|C\|_{\mathrm{HS}}^2
=\frac1{\pi^2}\int_{D_{\sqrt{s}}(a)}\int_{D_{\sqrt{s}}(b)}
 e^{-|z-w|^2}\,dA(w)\,dA(z)\\
&\le s^2 e^{-(d-2\sqrt{s})^2}=\eta_d^2.
\end{aligned}
\]
Writing \(S_0=\operatorname{diag}(A_a,A_b)\), the block matrix \(S-S_0\) has norm \(\|C\|\le\eta_d\), and the restriction of \(S_0\) to \(Q\) is bounded above by \(\lambda_1 I\). Hence
\[
QSQ\le(\lambda_1+\eta_d)I,
\qquad\|PSQ\|\le\eta_d.
\]
The min–max principle gives \(\Lambda_2(S)\ge\mu_2\ge\lambda_0-\eta_d\), because \(\lambda_0\varepsilon_d=|\langle u_a,C u_b\rangle|\le\eta_d\). Therefore both top eigenvalues lie at distance at least \(\delta-2\eta_d>0\) above the spectrum of \(QSQ\).

**4. Quantitative Schur-complement estimate.** For any such eigenvalue \(\Lambda\), eliminate the \(Q\)-component of its eigenvector. The associated effective operator on the two-dimensional space \(P\mathcal H\) is
\[
M(\Lambda)=PSP+PSQ(\Lambda-QSQ)^{-1}QSP.
\]
The correction is positive semidefinite, and its norm is at most
\[
\|PSQ(\Lambda-QSQ)^{-1}QSP\|
\le\frac{\eta_d^2}{\delta-2\eta_d}=:\kappa_d.
\]
The min–max principle first gives \(\Lambda_j\ge\mu_j\), for \(j=1,2\). For the upper bounds, the Schur-complement inertia identity (or counting the eigenvalues above any threshold exceeding \(\lambda_1+\eta_d\)) shows that \(\Lambda_j\le\mu_j+\kappa_d\). Indeed, if \(\Lambda_j>\mu_j+\kappa_d\), then \(M(\Lambda_j)\le PSP+\kappa_dI\) has fewer than \(j\) eigenvalues at least \(\Lambda_j\), contrary to its Schur-inertia count. This proves both inequalities.

Finally,
\[
\frac{e^{-(d-2\sqrt{s})^2}}{e^{-d^2/2}}
=\exp\!\left(-\frac{d^2}{2}+4d\sqrt{s}-4s\right)\longrightarrow0.
\]
Consequently the Schur error is of strictly smaller exponential order than the coherent overlap, yielding the sharp limits and spectral-gap equivalence. \(\square\)

## Verification

A standalone numerical reproducer, `CHECKER.py`, constructs finite Fock-monomial Galerkin matrices using independent angular and radial disk quadratures, compares increasing truncations, and checks the predicted signed splitting for several separations at \(s=1\). In its recorded execution it passed 16 assertions. These finite-dimensional checks corroborate the exact proof; they do not establish the infinite-dimensional limit by themselves. The kernel bound and min–max/Schur argument above provide that justification.

## Relationship to prior work

Nicola and Tilli prove the sharp disk concentration inequality for the Gaussian short-time Fourier transform and identify its extremizers [1]. Their theorem motivates the single-disk reference concentration \(\lambda_0\), but it does not state the leading splitting of the two largest eigenvalues for two disks separated by a diverging distance.

Marceca and Romero study spectral deviations for short-time Fourier concentration operators on general domains [2]; their eigenvalue-counting estimates do not determine this exponentially small, fixed-index splitting coefficient. Ramos studies structural properties and separated-profile phenomena for time-frequency localization [3], without the coefficient claimed here. Classical radial localization spectral formulas go back to Daubechies [4]. Those earlier facts are used only as input or context; the new claim is the quantitative two-disk separation law.

## Limitations

The two disks must have the same fixed positive area. The result concerns the two largest eigenvalues, not the entire spectrum, a varying-radius regime, or the case of nearby/overlapping disks. The explicit bound becomes informative when \(d\) is sufficiently large; it is not presented as optimal at finite separation. Historical priority remains subject to specialized literature not identified by the searches; the mathematical proof does not assert that no prior equivalent result exists.

## References

[1] F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423, first version 2021-06-07.

[2] F. Marceca and J. L. Romero, *Spectral deviation of concentration operators for the short time Fourier transform*, arXiv:2104.06150, first version 2021-04-13.

[3] J. P. G. Ramos, *Eigenfunctions, Free Boundaries, and Time-Frequency Localization*, arXiv:2607.21590, first version 2026-07-23.

[4] I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Transactions on Information Theory **34** (1988), 605–612.
