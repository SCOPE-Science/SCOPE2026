# Raw and centered dispersion at periodic asymmetric permeable membranes

## Finding

Consider an infinite array of equal cells of length \(L\) with interior diffusivity \(D\) and identical interfaces of rightward and leftward permeabilities \(a,b>0\). Set \(S=a+b\), \(\Delta=a-b\), \(H=2D+LS\), and \(v=2D\Delta/H\). Let \(X_t\) be physical position measured from the center of the starting cell, and \(u_0\in(0,L)\) the initial coordinate from that cell's left end, so \(x_0=u_0-L/2\). Then
\[
\begin{aligned}
\mathbb E X_t&=vt+c(u_0)+o(1),\\
\operatorname{Var}(X_t)&=2D_{\rm var}t+o(t),\\
\mathbb E X_t^2&=v^2t^2+2[D_{\rm var}+vc(u_0)]t+o(t),\\
D_{\rm var}&=\frac{DLS}{H}-\frac{DL^2(4D+LS)\Delta^2}{3H^3}.
\end{aligned}
\]
Here, with \(\alpha=2D/H\), \(\eta=L\Delta/H\), and \(y=u/L\),
\[
\chi(Ly)=-L[\alpha y+\eta y(1-y)],\qquad
c(u_0)=x_0+\chi(u_0)-L[-\alpha/2+\alpha\eta/6-\eta/6].
\]
In particular for a start at the cell center, the linear coefficient of the raw second moment, divided by two, is
\[
D_{\rm raw}^{\rm mid}=\frac{DLS}{H}-\frac{DL^2(14D+3LS)\Delta^2}{6H^3}.
\]
For this same center-start convention, the true raw coefficient differs from the value printed in Eq. (26) of Kay and Giuggioli [1] by
\[
D_{\rm raw}^{\rm mid}-D_{[1]}=-\frac{DL^2\Delta^2}{3H^2}.
\]
For asymmetric permeabilities the printed expression never agrees with the true raw coefficient at a center start. Its difference from the centered diffusivity is \(D_{\rm var}-D_{[1]}=DL^2(2D-LS)\Delta^2/(6H^3)\), so agreement with the centered value at \(LS=2D\) does not cancel the raw-moment error. For example, when \(D=L=1\), \(a=3/2\), and \(b=1/2\), the centered and printed values are both \(15/32\) but the center-start raw coefficient is \(43/96\).

## Assumptions and scope

\(D,L,a,b\) are strictly positive and time-independent. All cells have the same diffusivity and there is no interior force. At a right interface of cell \(n\), both sides have the common physical net flux \(a p_n(L)-b p_{n+1}(0)\), where \(u\in[0,L]\) is the local coordinate. Endpoint states are distinguished on the two sides of a membrane. The variance uses the mean at the actual observation time. The raw coefficient depends on the specified physical origin and initial phase. The single-cell corrector below uses the equivalent reflecting-diffusion representation with direction-specific exponential switching thresholds on boundary local time.

## Proof

**Stationary phase.** Let \(U_t\) be the split-cell phase and \(N_t\) the signed number of crossings from the initial cell, so \(X_t=LN_t+U_t-L/2\). The unique stationary phase density is
\[
\rho(u)=\frac{1}{L}\left[1+\eta(1-2u/L)\right].
\]
Indeed it is positive and normalized, and \(-D\rho'=v/L=a\rho(L)-b\rho(0)\). The phase converges to this density from every starting point: at any fixed positive time the transition kernel dominates the heat kernel for motion with no membrane transfer, which is the Robin-killed interval kernel with finite killing rates. That kernel is continuous and strictly positive on the compact closed interval at positive time (including endpoint starting and final positions); its positive lower bound gives a Doeblin minorization. In particular the expectations and expected time averages of bounded phase observables converge to their stationary values.

**Poisson corrector and mean.** Normalize the reflection regulators \(K^0,K^L\) so that the continuously varying part of \(U\) has differentials \(\sqrt{2D}\,dW+dK^0-dK^L\). Left and right transfer counting intensities are respectively \((b/D)dK^0\) and \((a/D)dK^L\), as required by the stated flux (or by integration by parts in the backward generator). Let \(Q=2DL/H\) and choose \(\psi(0)=0\), \(\psi'(u)=Q(b+\Delta u/L)/D\). Direct integration gives \(Q=L+\psi(0)-\psi(L)\) and \(D\psi''=v\). A transfer changes \(LN+\psi(U)\) by \(+Q\) or \(-Q\). Its reflection terms are canceled by the compensators for the jumps, because \(D\psi'(0)=bQ\) and \(D\psi'(L)=aQ\). Itô's formula gives the zero-mean martingale
\[
M_t=LN_t+\psi(U_t)-\psi(u_0)-vt .
\]
Consequently \(X_t=x_0+vt+M_t+\chi(u_0)-\chi(U_t)\), where \(\chi(u)=\psi(u)-u\) is the stated quadratic. Integrating against \(\rho\) uses \(\mathbb E_\rho[U/L]=1/2-\eta/6\) and \(\mathbb E_\rho[(U/L)(1-U/L)]=1/6\), giving \(c(u_0)\). At \(u_0=L/2\), \(c=-L\eta(1+2\alpha)/12=-L^2\Delta(6D+LS)/(12H^2)\).

**Martingale variance.** For any smooth \(g\) with equal endpoint values, there are no jumps in \(g(U)\). Itô's formula implies
\[
\mathbb E[g(U_t)-g(u_0)]
=D\mathbb E\int_0^t g''(U_s)\,ds+g'(0)\mathbb E K_t^0-g'(L)\mathbb E K_t^L.
\]
The endpoint derivatives can be prescribed independently by cubic interpolation; these identities, also usable with localization, give finite expected regulators at every finite time. Dividing by \(t\), using phase convergence and integrating \(\int g''\rho\) by parts with \(\rho''=0\) and equal endpoint values of \(g\), gives \(\mathbb E K_t^0/t\to D\rho(0)\), \(\mathbb E K_t^L/t\to D\rho(L)\). The continuous and compensated jump parts of \(M\) are orthogonal and square-integrable on finite horizons by these bounds and bounded \(\psi'\). Their bracket contributions give
\[
\lim_{t\to\infty}\frac{\mathbb E M_t^2}{2t}=D\int_0^L (\psi')^2\rho\,du+\frac{Q^2}{2}[a\rho(L)+b\rho(0)].
\]
The bounded phase term changes the variance by at most \(O(\sqrt t)+O(1)\), by Cauchy–Schwarz, so the displayed limit is \(D_{\rm var}\). In the integral put \(r=u/L-1/2\); the density in \(r\) is \(1-2\eta r\) on \([-1/2,1/2]\), and \(D\psi'/Q=S/2+\Delta r\). Thus the integral contribution is \(Q^2(S^2/4+\Delta^2/12-\eta S\Delta/6)/D\), and the jump contribution is \(Q^2(S/L-\Delta^2/H)/2\). Their sum simplifies to the stated formula.

**Raw moments and the printed formula.** Squaring \(vt+c(u_0)+o(1)\) adds \(2vc(u_0)t\) to the linear coefficient of the centered moment. Equation (26) of [1], with \(a=\kappa_-\) and \(b=\kappa_+\), simplifies to
\[
D_{[1]}=\frac{DLS}{H}-\frac{DL^2(10D+LS)\Delta^2}{6H^3}.
\]
The raw comparison here uses the same cell-centered origin and midpoint initial condition as the calculation in [1, Appendix D, Eqs. (D2)–(D6), (D20)–(D31)]. In particular it compares the coefficient of \(2t\) after subtracting \(v^2t^2\), not the leading relative equivalence of two quadratically growing functions. Substitution yields both differences in the finding.

## Verification

The accompanying `verify.py` checks the phase density, endpoint and drift identities, elementary integrals, and both comparisons with the primary printed expression in exact symbolic arithmetic. It is supplementary to the martingale and ergodic proof. In the continuous one-way limit \(D=L=a=1,b\downarrow0\), \(D_{\rm var}\to22/81\), \(D_{\rm raw}^{\rm mid}\to37/162\), and \(D_{[1]}\to43/162\). The centered limit is independently consistent with renewal theory: in the one-way model the reflecting-to-transmitting crossing time from the left endpoint has transform \(1/(\cosh\sqrt{s}+\sqrt{s}\sinh\sqrt{s})\), obtained by the reflecting/Robin backward boundary-value problem. Its mean is \(3/2\) and its variance is \(11/6\), giving the centered limit \((11/6)/(2(3/2)^3)=22/81\) for the renewal count, and hence physical position by bounded displacement. This boundary-limit check is not an assumption of the theorem.

## Relationship to prior work and limitations

Kay and Giuggioli [1, §III.A and Appendix D] establish the interface model, exact periodic propagator and leading drift. Their Fourier–Laplace denominator in Eq. (D6) contains the counting-tilted characteristic equation after reweighting the cell index; that equation, their propagator and the drift are not claimed as contributions here. Their second-moment calculation starts from a raw moment, while the physical effective diffusion usually means the centered quantity. The corrector obtains the missing initial-phase-dependent mean offset, separates both coefficients, and permits a like-for-like comparison to their printed raw coefficient. The comparison is specifically to the cited version's printed formula, not to any unidentified later correction. Formulae for neither transient higher cumulants nor nonperiodic, non-Poisson or higher-dimensional barriers are established here.

## Reference

[1] T. Kay and L. Giuggioli, *Local time statistics and permeable barrier crossing: from Poisson to Birth-Death Diffusion Equations*, arXiv:2406.07142v2, §III.A and Appendix D, https://arxiv.org/abs/2406.07142v2.
