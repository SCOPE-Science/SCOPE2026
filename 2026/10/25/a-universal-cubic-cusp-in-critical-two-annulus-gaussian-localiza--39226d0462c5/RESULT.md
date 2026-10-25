# A universal cubic cusp in critical two-annulus Gaussian localization

## Finding
For every fixed \(\kappa\in\mathbb R\setminus\{1/2\}\), the two-annulus Gaussian localization operator defined below has a universal order-\(R^{1/3}\) Hermite-mode transition, governed by
\[
P_\kappa(y)=\kappa y^2-\frac{y^4}{12}-\frac{2y}{3},\qquad P'_\kappa(y)=2\kappa y-\frac{y^3}{3}-\frac23.
\]
For \(\kappa<1/2\) there is one local-maximum plateau; for \(\kappa>1/2\) there are two, separated by one local-minimum plateau, once \(R\) is sufficiently large. Their rescaled degree positions converge to the distinct real roots of \(y^3-6\kappa y+2=0\). The globally largest eigenvalue is always the leftmost local maximum. With \(y_-(\kappa)\) its limiting degree,
\[
\|T_{R,\kappa}\|=\frac{2e^{-\delta_R^2/2}}{\sqrt{2\pi R}}\left[1+R^{-2/3}P_\kappa(y_-(\kappa))+o_\kappa(R^{-2/3})\right].
\]
At \(\kappa=0\), the optimal mode is \(R-2^{1/3}R^{1/3}+o(R^{1/3})\), and \(P_0(-2^{1/3})=2^{-2/3}\).

## Assumptions and scope
Use the Bargmann--Fock Hilbert space of entire functions with norm \(\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). Given a fixed \(\kappa\), choose sufficiently large real \(R>0\) and set \(\delta_R=1+\kappa R^{-1/3}\). Let \(E_{R,\kappa}\) be the union of the two disjoint unit intervals centered at \(R-\delta_R\sqrt R\) and \(R+\delta_R\sqrt R\), contained in \((0,\infty)\). Define the radial Toeplitz/localization operator \(T_{R,\kappa}=P_{\mathcal F}M_{\mathbf1_{\{|z|^2\in E_{R,\kappa}\}}}\) on Fock space. Under the Gaussian Bargmann transform, its eigenvectors are Hermite modes. The normalized monomials \(z^n/\sqrt{n!}\) have eigenvalues
\[
\lambda_n(R,\kappa)=\sum_{v\in\{-\delta_R,\delta_R\}}\int_{R+v\sqrt R-1/2}^{R+v\sqrt R+1/2}\frac{e^{-t}t^n}{n!}\,dt,\quad n=0,1,\ldots.
\]
A plateau is a maximal consecutive set of one or two equal neighboring eigenvalues at a local extremum. A limiting index statement \(n_R=R+yR^{1/3}+o(R^{1/3})\) applies to every index in the corresponding plateau. All asymptotics fix \(\kappa\) and are not uniform at \(\kappa=1/2\).

## Proof
**1. Diagonalization and exact first differences.** Polar integration gives the displayed gamma integrals, their nonnegativity, and \(\|T_{R,\kappa}\|=\max_{n\ge0}\lambda_n\). Write \(A_\pm=R\pm\delta_R\sqrt R-1/2\) and \(B_\pm=A_\pm+1\). Integration by parts yields the exact identity
\[
\lambda_{n+1}-\lambda_n=\frac{F_R(n+1)}{(n+1)!},\qquad F_R(s)=\sum_{\sigma\in\{-,+\}}\bigl(e^{-A_\sigma}A_\sigma^s-e^{-B_\sigma}B_\sigma^s\bigr).
\]
The four bases are strictly ordered \(0<A_-<B_-<A_+<B_+\). The coefficients in increasing-base order have three sign changes \(+,-,+,-\); the generalized Descartes theorem for real exponential sums (proved below) gives at most three real zeros, counted with multiplicity, for \(F_R\). Indeed, for any ordered real exponents \(\xi_1<\dots<\xi_m\), an exponential sum \(\sum_i c_i e^{\xi_i s}\) has at most the number of coefficient sign changes as real zeros, counted with multiplicity. Divide by the smallest exponential and differentiate; the derivative has coefficients \(c_i(\xi_i-\xi_1)\), \(i\ge2\). Rolle's theorem (with endpoint signs at \(-\infty\)) gives induction; equivalently the variation-diminishing property of the kernel \(e^{s\xi}\). For the present four-term pattern the standard generalized Descartes bound is three. Also \(F_R(n+1)>0\) if \(n+1\le A_-\), and \(F_R(n+1)<0\) if \(n+1\ge B_+\), because each individual band difference has that sign. Hence all switches are in a bounded central window of order \(\sqrt R\).

**2. Local expansion at the degenerate two-peak threshold.** Put \(\varepsilon=R^{-1/2}\), \(u=(x-R)/\sqrt R\), \(a=\delta_R=1+\kappa\varepsilon^{2/3}\), and for a real nonnegative degree \(x\), replace \(n!\) by \(\Gamma(x+1)\) to interpolate smoothly. Uniform Stirling expansion for bounded \(u,v,w\), where \(t=R+v\sqrt R+w\), gives
\[
\frac{e^{-t}t^x}{\Gamma(x+1)}=\frac{e^{-(u-v)^2/2}}{\sqrt{2\pi R}}\left[1+\varepsilon\left((u-v)w+\frac{u(u-v)^2}{2}-\frac{(u-v)^3}{3}-\frac u2\right)+O(\varepsilon^2)\right].
\]
The expansion remains valid under two derivatives in bounded \(u\), since Stirling and Taylor remainders are differentiable there. Integrating symmetrically over \(-1/2\le w\le1/2\) removes the linear \(w\) term. Define
\[
h_a(u)=e^{-(u-a)^2/2}+e^{-(u+a)^2/2},\quad
j_a(u)=\sum_{v=\pm a}e^{-(u-v)^2/2}\left[\frac{u(u-v)^2}{2}-\frac{(u-v)^3}{3}-\frac u2\right].
\]
Thus \(\lambda_x=(2\pi R)^{-1/2}[h_a(u)+\varepsilon j_a(u)+O(\varepsilon^2)]\), with the same statement for the first two \(u\)-derivatives. Direct differentiation gives \(j_1(0)=0\) and \(j'_1(0)/h_1(0)=-2/3\). Also
\[
\frac{h_a(u)}{h_a(0)}=1+\frac{a^2-1}{2}u^2-\frac{u^4}{12}+O(u^6+|a-1|u^4),\quad h_a(0)=2e^{-a^2/2}.
\]
With \(u=\varepsilon^{1/3}y=yR^{-1/6}\) (equivalently \(x=R+yR^{1/3}\)), these combine to the \(C^2_{\mathrm{loc}}\) convergence
\[
R^{2/3}\left(\frac{\lambda_{R+yR^{1/3}}}{2e^{-a^2/2}/\sqrt{2\pi R}}-1\right)\longrightarrow P_\kappa(y),\qquad P_\kappa(y)=\kappa y^2-\frac{y^4}{12}-\frac{2y}{3}.
\]
In particular the same local expansion holds for the discrete first difference, with normalization
\[
\frac{\sqrt{2\pi}\,R^{3/2}}{2e^{-a^2/2}}\bigl(\lambda_{n+1}-\lambda_n\bigr)\longrightarrow P'_\kappa(y),\quad n=R+yR^{1/3}+O(1),
\]
uniformly with one derivative in \(y\) if the difference is smoothly interpolated via the displayed exact endpoint formula. The \(O(R^{-1})\) remainder in the gamma expansion is safely smaller than the \(R^{-2/3}\) cusp correction in the normalized eigenvalues.

**3. Excluding all other critical points.** A zero of the interpolated first difference must lie between the extreme squared-radius endpoints. For \(u\) in any compact subinterval of \(\mathbb R\setminus\{0\}\), the normalized first difference converges with positive scaling to
\(h'_1(u)=h_1(u)(\tanh u-u)\), which is strictly positive at negative \(u\) and strictly negative at positive \(u\). Uniform tail estimates of the same explicit Gaussian and gamma ratios give that sign through the remaining bounded endpoints \(|u|\le1+o(1)\). For the overlap region \(u\to0\) but \(|u|\gg\varepsilon^{1/3}\), Taylor expansion of the difference gives, relative to its positive prefactor,
\[
-\frac{u^3}{3}+O(|u|^5+\varepsilon^{2/3}|u|+\varepsilon),
\]
with the remainder \(o(|u|^3)\) in this range, hence again a definite sign. Therefore all real zeros must lie in \(u=O(\varepsilon^{1/3})\), i.e. \(n=R+O(R^{1/3})\). In that window, the scaled difference converges in \(C^1\) to \(P'_\kappa\). Its roots are simple whenever \(\kappa\ne1/2\): the cubic \(y^3-6\kappa y+2=0\) has one real root for \(\kappa<1/2\) and three for \(\kappa>1/2\). Around each simple root, \(C^1\) convergence gives one nearby zero and its crossing sign, while away from these root neighborhoods there are none. The generalized Descartes bound additionally excludes any extraneous zeros. Every sign change determines exactly one discrete extremum plateau, of one or (at an exact tie) two indices. The sign pattern is \(+,-\) for one root and \(+,-,+,-\) for three roots, giving exactly the asserted plateau counts.

**4. Global selection and norm.** The stationary cubic has a unique negative root \(y_-\), corresponding to a strict local maximum, and for \(\kappa>1/2\) the remaining local maximum occurs at a positive root. For \(y>0\), \(P_\kappa(-y)-P_\kappa(y)=4y/3>0\). Thus the global maximum of the coercive quartic \(P_\kappa\) is achieved uniquely at its negative critical point: even a positive candidate is beaten by its reflection, and the negative half-line has exactly one critical point. The finite difference sign classification bounds all finite-spectrum maxima to these plateaux. Evaluating the uniform local expansion at the maximizing indices gives the stated operator-norm formula and strict inward dominance. At \(\kappa=0\), the negative root is \(-2^{1/3}\) and direct substitution yields \(P_0(-2^{1/3})=2^{-2/3}\). This establishes every claimed asymptotic and classification.

## Verification
The included standalone `critical_shells_check.py` independently evaluates the gamma-integral eigenvalues using Gauss--Legendre quadrature and stable `gammaln` arithmetic. It checks five fixed parameter values \(\kappa=-1,0,0.2,0.7,1\) and two large radii \(R=10^5,10^6\), comparing global mode positions and scaled norm corrections with the cubic and quartic formulas; all 20 finite assertions passed. Symbolic expansion separately gives \(j_1(0)=0\), \(j'_1(0)/h_1(0)=-2/3\), and the coefficient \(-1/12\) of the quartic term. These finite checks corroborate but do not prove the limiting claims. The proof above establishes the infinite-range statements.

## Relationship to prior work
Galbis (2021, arXiv:2102.02031) develops norms of selfadjoint Toeplitz operators on Fock space; Abreu--Dörfler (2012, arXiv:1202.5841) discusses localization operators and radial eigenfunctions; Huang--Zhang (2024, arXiv:2405.11147) addresses nonradial extensions. The radial gamma eigenvalues and general mode-count bound are background, not new. Known fixed-separation \(\delta\in(0,1)\cup(1,\infty)\) two-band asymptotics do not apply uniformly when \(\delta_R\to1\); in fact their nonzero-order \(\sqrt R\) peaks collapse. The result proved here concerns the previously unresolved double-scaling window \(\delta_R=1+\kappa R^{-1/3}\), its asymmetric cubic discriminant threshold \(\kappa=1/2\), the universal quartic profile, and sharp inward-mode selection. A generic finite-m interval bound implies no more than two maxima but not the threshold, localization scale, or norm coefficient.

## Limitations
The exactly degenerate discriminant case \(\kappa=1/2\) is excluded from the plateau count, as are sequences \(\kappa=\kappa_R\) without fixed limiting noncritical value. Constants and errors need not be uniform as \(\kappa\to1/2\). This is a radial Gaussian/Fock/Hermite result, not a claim about arbitrary windows, nonradial masks, or nonlinear phase retrieval. Historical originality remains conditional on unindexed literature under alternative terminology. Independent scientific verification is not included.

## References
1. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space* (first public 2021-02-03), arXiv:2102.02031; https://arxiv.org/abs/2102.02031.
2. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators* (2012), arXiv:1202.5841; https://arxiv.org/abs/1202.5841.
3. Huang and Zhang, *Norm bounds for self-adjoint Toeplitz operators with non-radial symbols* (2024), arXiv:2405.11147; https://arxiv.org/abs/2405.11147.
