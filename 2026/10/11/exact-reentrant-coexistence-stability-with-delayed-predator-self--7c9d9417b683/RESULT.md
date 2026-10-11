# Exact reentrant coexistence stability with delayed predator self-regulation

## Finding

In a positive-parameter two-species predator–prey system whose only delay acts on predator self-limitation, increasing the delay can **destabilize, restabilize, and then destabilize again** a fixed positive coexistence equilibrium. One exact parameter witness yields all three transitions in a specified delay range, and the phenomenon holds throughout an open neighborhood of that witness.

For integers \(j\ge0\), put
\[
\begin{aligned}
\omega_+&=\sqrt{8/5}, & \theta_+&=\arccos(-9/11), & \tau_+^{(j)}&=\frac{\theta_++2\pi j}{\omega_+},\\
\omega_-&=\sqrt{27/20}, & \theta_-&=\arccos(-7/8), & \tau_-^{(j)}&=\frac{\theta_-+2\pi j}{\omega_-}.
\end{aligned}
\]
The exact threshold ordering begins
\[
0<\tau_+^{(0)}<\tau_-^{(0)}<\tau_+^{(1)}<\tau_-^{(1)}.
\]
The positive equilibrium is locally asymptotically stable on
\[
[0,\tau_+^{(0)})\quad\text{and}\quad(\tau_-^{(0)},\tau_+^{(1)}),
\]
and unstable on \((\tau_+^{(0)},\tau_-^{(0)})\), where it has exactly two right-half-plane characteristic roots. Thus stability is recovered without any additional control, maturation mechanism, or delay-dependent equilibrium displacement.

## Assumptions and scope

Consider the retarded functional differential equation
\[
\begin{aligned}
\dot x(t)&=x(t)(h_1-a_1x(t))-\frac{d_1x(t)y(t)}{1+bx(t)},\\
\dot y(t)&=y(t)\bigl(h_2-a_2y(t-\tau)\bigr)+\frac{dd_1x(t)y(t)}{1+bx(t)},
\end{aligned}
\]
where \(h_1,a_1,h_2,a_2,d_1,b,d>0\), \(\tau\ge0\), and initial histories lie in a sufficiently small neighborhood of a strictly positive constant history in \(C([-\tau,0],\mathbb R^2)\). At \(\tau=0\) this is the corresponding ordinary differential equation. Fix the exact demographic vector
\[
(h_1,a_1,h_2,a_2,d_1,b,d)=\left(\frac{21}{2},\frac92,\frac3{10},1,12,1,\frac7{60}\right).
\]
The constant state \((x_*,y_*)=(1,1)\) solves both equilibrium equations for every \(\tau\). All stability assertions are local to this equilibrium. A positive-demographic-parameter neighborhood in the theorem means an open subset of \((0,\infty)^7\).

## Proof

**1. Exact Jacobian and characteristic function.** At the stated equilibrium the instantaneous matrix and delayed matrix are, by differentiation of the displayed right-hand side,
\[
A=\begin{pmatrix}-3/2&-6\\7/20&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
\]
For perturbations \((u,v)\), the linearized equations are
\[
\dot u(t)=-\frac32u(t)-6v(t),\qquad
\dot v(t)=\frac7{20}u(t)-v(t-\tau).
\]
Consequently the characteristic function is
\[
\Delta(\lambda,\tau)=\lambda^2+\frac32\lambda+\frac{21}{10}+
\left(\lambda+\frac32\right)e^{-\lambda\tau}.
\]
Write \(P(\lambda)=\lambda^2+\frac32\lambda+\frac{21}{10}\) and \(Q(\lambda)=\lambda+\frac32\). At zero delay, \(P+Q=\lambda^2+\frac52\lambda+\frac{18}{5}\) is Hurwitz, so the equilibrium is initially locally asymptotically stable.

**2. All possible imaginary frequencies.** If \(\Delta(i\omega,\tau)=0\) for real \(\omega>0\), necessarily \(|P(i\omega)|=|Q(i\omega)|\). With \(X=\omega^2\), this gives the exact factorization
\[
\begin{aligned}
F(X)&=(21/10-X)^2+(9/4)X-(X+9/4)\\
&=\left(X-\frac{27}{20}\right)\left(X-\frac85\right).
\end{aligned}
\]
Thus the only positive imaginary frequencies are \(\omega_-\) and \(\omega_+\) in the Finding. There is no zero characteristic root because \(\Delta(0,\tau)=18/5\) for every delay.

**3. All crossing delays and their initial order.** At a candidate frequency, \(e^{-i\omega\tau}=-P(i\omega)/Q(i\omega)\), so writing \(\theta=\omega\tau\) modulo \(2\pi\) gives
\[
\cos\theta=-\frac{(3/2)(21/10)}{\omega^2+9/4},\qquad
\sin\theta=\frac{\omega(\omega^2+9/4-21/10)}{\omega^2+9/4}>0.
\]
Substitution gives \((\cos\theta_-,\sin\theta_-)=(-7/8,\sqrt{15}/8)\) and \((\cos\theta_+,\sin\theta_+)=(-9/11,2\sqrt{10}/11)\). Therefore every crossing delay is exactly one of \(\tau_\pm^{(j)}\). Since \(\theta_+<\theta_-<\pi\) and \(\omega_+>\omega_->0\), it follows that \(\tau_+^{(0)}<\tau_-^{(0)}\). Moreover, \(\omega_+<2\omega_-\) gives
\[
\tau_-^{(0)}<\frac\pi{\omega_-}<\frac{2\pi}{\omega_+}<\tau_+^{(1)}<\tau_-^{(1)}.
\]
For reference, the first four crossings are approximately \(1.9993800253\), \(2.2689073751\), \(6.9666741582\), and \(7.6766122764\), respectively; the exact formulas, not these decimals, determine their ordering.

**4. Opposite and nonzero crossing directions.** For an imaginary root of \(P(\lambda)+Q(\lambda)e^{-\lambda\tau}=0\), implicit differentiation and elimination of the exponential term yield
\[
\left(\frac{d\lambda}{d\tau}\right)^{-1}
=-\frac1\lambda\left(\frac{P'(\lambda)}{P(\lambda)}-\frac{Q'(\lambda)}{Q(\lambda)}\right)-\frac\tau\lambda.
\]
Since \(\lambda=i\omega\), differentiation of \(F(X)=|P(i\sqrt X)|^2-|Q(i\sqrt X)|^2\) at \(X=\omega^2\), where the squared moduli are equal, gives
\[
\operatorname{Re}\left[\left(\frac{d\lambda}{d\tau}\right)^{-1}\right]
=\frac{F'(\omega^2)}{|P(i\omega)|^2}.
\]
Here \(F'(27/20)=-1/4\) and \(F'(8/5)=1/4\). Each crossing is simple and transversal; the \(\omega_+\) pair crosses from the stable into the unstable half-plane as delay increases, while the \(\omega_-\) pair crosses back. The sign of the real part of a nonzero complex number is the sign of the real part of its reciprocal, so this establishes the direction for \(d\lambda/d\tau\) itself.

**5. Counting roots and stability.** On each bounded delay interval the characteristic equation admits a uniform bound on its right-half-plane roots: for \(\operatorname{Re}\lambda\ge0\), \(|e^{-\lambda\tau}|\le1\) and hence \(|\lambda|^2\le(5/2)|\lambda|+18/5\). No unstable characteristic root can therefore arrive from infinity without crossing the imaginary axis. Initially there are none, and there are no zero roots. The first \(\omega_+\) crossing creates exactly one unstable conjugate pair, the subsequent \(\omega_-\) crossing removes that pair, and the next \(\omega_+\) crossing terminates the second stable interval. The standard linearization principle for retarded equations transfers exponential linear stability or linear instability to the nonlinear equilibrium on the strict intervals asserted. No nonlinear stability conclusion is made at a crossing.

**6. Open-set robustness.** The positive equilibrium is a regular root of the delay-independent equilibrium equations because the zero-delay Jacobian has determinant \(18/5>0\). It thus varies smoothly with all seven positive demographic parameters. The coefficients of the linearized single-delay characteristic quasipolynomial vary smoothly as well; the imaginary-frequency equation remains a quadratic in \(X=\omega^2\) and retains two simple positive roots near \(27/20\) and \(8/5\). Its characteristic phases, strict crossing directions, zero-delay Hurwitz property, and strict first-crossing ordering persist by continuity. This proves the same stable–unstable–stable sequence on a nonempty open neighborhood of the displayed vector, with perturbed crossing delays.

## Verification

A standalone Python checker (`check.py`) evaluates the equilibrium and Jacobian with exact rational arithmetic, reproduces the two factors of the frequency polynomial, verifies the rational cosine and squared-sine phase identities, and computes the first crossing ordering. Run with `python3 check.py`; it uses only Python's standard library and prints `CHECK_OK`. These finite algebraic checks are corroboration, not an exhaustive computation of all characteristic roots: the infinite-dimensional root count is proved above by the factorization, transversality, and no-entry-from-infinity argument.

## Relationship to prior work

Ou et al.'s model (1.2) [1] is exactly the system in this note. Their Section 3 and Theorem 3.1 analyze a sufficient one-frequency condition and the first Hopf threshold; in particular, their assumption (A2) makes the constant term of their squared-frequency polynomial negative. Our two-frequency case has positive constant term \(54/25\), falls outside that sufficient regime, and exhibits recovery after the first loss of stability. We do not claim to discover stability switches in predator–prey systems generally.

Sui and Du [2] already rigorously demonstrate stability restoration for a *different*, spatially diffusive predator–prey model with delayed fear response in prey reproduction; their model has other characteristic coefficients and does not imply the parameter witness here. Earlier fear-delay work [3] and the stage-structured maturation-delay study [4] establish related stability-switch phenomena, not the stated two-population predator self-regulation case. General geometric stability-switch theory [5] provides background root methods but does not by itself supply this biological feasible parameter vector and open parameter region. The source comparisons are model-specific rather than claims of global novelty of delay-induced restabilization.

## Limitations

Only local equilibrium stability away from the threshold values is asserted. The result does not classify attractors, prove nonlinear periodic branches, establish global extinction or permanence, or settle nonlinear stability at the three crossing instants. The open parameter neighborhood is established by continuity but is not furnished with explicit maximal bounds. Related stage-structured literature was compared on accessible indexed material where full text was not retrievable; coverage beyond that material remains a residual literature risk.

## References

[1] W. Ou, C. Xu, Q. Cui et al., “Hopf bifurcation exploration and control technique in a predator-prey system incorporating delay,” *AIMS Mathematics* 9(1), 1622–1651 (first public 2023-12-13), DOI 10.3934/math.2024080. https://www.aimspress.com/aimspress-data/math/2024/1/PDF/math-09-01-080.pdf

[2] M. Sui and Y. Du, “Bifurcations, stability switches and chaos in a diffusive predator-prey model with fear response delay,” *Electronic Research Archive* 31(9), 5124–5150 (2023), DOI 10.3934/era.2023262. https://www.aimspress.com/aimspress-data/era/2023/9/PDF/era-31-09-262.pdf

[3] P. Panday, S. Samanta, N. Pal and J. Chattopadhyay, “Delay induced multiple stability switch and chaos in a predator–prey model with fear effect,” *Mathematics and Computers in Simulation* 172, 134–158 (2020), DOI 10.1016/j.matcom.2019.12.015.

[4] Z.-W. Liang and X.-Y. Meng, “Stability and Hopf Bifurcation of a Delayed Predator–Prey Model with a Stage Structure for Generalist Predators and a Holling Type-II Functional Response,” *Symmetry* 16, 597 (2024), DOI 10.3390/sym16050597.

[5] E. Beretta and Y. Kuang, “Geometric stability switch criteria in delay differential systems with delay dependent parameters,” *SIAM Journal on Mathematical Analysis* 33, 1144–1165 (2002), DOI 10.1137/S0036141000376086.
