# A universal fourth-order time arrow in Poisson-kicked harmonic confinement

## Finding
Consider a stationary one-dimensional harmonically confined particle driven by thermal Brownian noise and independent Poisson kicks. A fourth-order, **time-ordered** correlation distinguishes forward from backward observations, even for symmetric kicks. Its exact lag profile is independent of thermal diffusion, and its unique optimal observation lag is independent of the kick distribution.

Let \(Y_t=X_t-\mathbb E X_t\), and for \(t\geq0\) define
\[
\Delta(t)=\mathbb E[Y_0Y_t^3]-\mathbb E[Y_0^3Y_t].
\]
For every \(t\geq0\),
\[
\boxed{\Delta(t)=-\frac{\lambda\mathbb E[J^4]}{4\gamma}
 e^{-\gamma t}(1-e^{-2\gamma t}).}
\]
In particular, when the kick amplitude \(J\) is nonzero with positive probability, \(\Delta(t)<0\) for every finite \(t>0\). The magnitude has a **unique** maximum at
\[
\boxed{t_*=\frac{\log3}{2\gamma},\qquad
M_*:=\max_{t\geq0}|\Delta(t)|
=\frac{\lambda\mathbb E[J^4]}{6\sqrt3\,\gamma}.}
\]
Thus the entire fourth-moment kick intensity and the trap relaxation parameter can be recovered from the ideal correlation curve without knowing the thermal diffusivity:
\[
\boxed{\gamma=\frac{\log3}{2t_*},\qquad
\lambda\mathbb E[J^4]=\frac{3\sqrt3\log3}{t_*}M_*.}
\]
These statements hold for symmetric or asymmetric kick laws and also for nonzero kick means, provided the *particle* observations are centered. They recover neither the kick arrival rate nor its fourth moment **separately** without further information.

**Independent reversible-noise invariance.** If observations are \(Z_t=Y_t+V_t\), where \(V\) is any independent, centered, stationary **time-reversible** process with finite fourth moments, the same \(\Delta(t)\) is obtained from \(Z\). In particular, arbitrarily strong independent stationary reversible measurement contamination does not alter this population-level witness. This is an exact identity for ensemble expectations, not a claim about finite-sample estimation variance.

More generally, for positive integers \(p,q\) with \(n=p+q\geq3\) and \(\mathbb E|J|^n<\infty\), define \(K_{p,q}(t)\) as the joint cumulant with \(p\) copies of \(Y_0\) and \(q\) copies of \(Y_t\). Then
\[
\boxed{K_{p,q}(t)-K_{q,p}(t)=
\frac{\lambda\mathbb E[J^n]}{n\gamma}
\big(e^{-q\gamma t}-e^{-p\gamma t}\big).}
\]
The fourth-order case \((p,q)=(1,3)\) is a sign-definite universal witness because \(\mathbb E[J^4]>0\) for every nontrivial kick law.

## Assumptions and scope
The particle is the unique strictly stationary solution, on the full real time axis, of
\[
dX_t=-\gamma X_t\,dt+\sqrt{2D}\,dB_t+d\!\left(\sum_{T_j\leq t}J_j\right),
\]
where \(\gamma>0\), \(D\geq0\), the \(T_j\) form a homogeneous rate-\(\lambda>0\) Poisson process, and the i.i.d. real marks \(J_j\) are independent of the Poisson process and of the Brownian motion. The interpretation of the displayed jump sum is through increments over bounded intervals. Assume \(\mathbb E|J|^4<\infty\), and \(\mathbb P(J\ne0)>0\) for strict conclusions. The stationary mean is \(\mathbb EX_t=\lambda\mathbb EJ/\gamma\). Higher-order cumulant identities require the corresponding finite absolute moments.

The time reversal refers only to the order of two stationary observations; the sign-definite witness proves violation of two-time exchangeability of \((Y_0,Y_t)\), hence violation of reversibility. It is not a numerical value of entropy production or a fluctuation theorem.

## Proof
**1. Stationary representation and cumulants.** With \(m=\lambda\mathbb EJ/\gamma\), the centered stationary solution can be represented as an exponentially filtered sum of Brownian increments and compensated Poisson jumps. Fourth-moment finiteness guarantees the integrals and all expectations below. The cumulants of \(Y_0\) obey
\[
\kappa_2=\frac D\gamma+\frac{\lambda\mathbb EJ^2}{2\gamma},\qquad
\kappa_n=\frac{\lambda\mathbb EJ^n}{n\gamma}\quad(n\geq3),
\]
where the second formula is asserted only when \(\mathbb E|J|^n<\infty\). This follows by differentiating the characteristic exponent of the compensated Poisson integral; its \(n\)-th cumulant is \(\lambda\mathbb EJ^n\int_0^\infty e^{-n\gamma s}\,ds\). Brownian motion contributes only to the second cumulant. In particular, for \(v=\mathbb EY_0^2\),
\[
\mathbb EY_0^4-3v^2=\frac{\lambda\mathbb EJ^4}{4\gamma}.
\]

**2. Time-separated moments.** For \(t\geq0\), the independent-increment property gives
\[
Y_t=q_tY_0+\eta_t,\quad q_t=e^{-\gamma t},\quad
\eta_t\perp Y_0,\quad
\mathbb E\eta_t=0,\quad
\mathbb E\eta_t^2=v(1-q_t^2).
\]
Expansion yields
\[
\mathbb E[Y_0Y_t^3]=q_t^3\mathbb EY_0^4+3q_tv^2(1-q_t^2),
\qquad
\mathbb E[Y_0^3Y_t]=q_t\mathbb EY_0^4.
\]
Their difference is \(-q_t(1-q_t^2)(\mathbb EY_0^4-3v^2)\), giving the displayed exact formula. No Gaussian assumption on the marks is used.

**3. Sharp observation lag and parameter inversion.** Put \(q=e^{-\gamma t}\in(0,1]\). The positive amplitude factor is \(q-q^3\). Its derivative is \(1-3q^2\); its only interior critical point, \(q=1/\sqrt3\), is a strict global maximum because both endpoints give zero and the second derivative there is negative. Substitution proves \(t_*\), \(M_*\), and both inversion identities. Positivity of \(\mathbb EJ^4\) yields the strict time arrow.

**4. Additive reversible contamination.** For *any* centered stationary process \(U\) with finite fourth moments, the Wick-type moment-cumulant decomposition gives
\[
\mathbb E[U_0U_t^3]-\mathbb E[U_0^3U_t]
=\operatorname{cum}(U_0,U_t,U_t,U_t)
-\operatorname{cum}(U_0,U_0,U_0,U_t).
\]
The three pair-partition terms on each side equal \(3\operatorname{Cov}(U_0,U_t)\operatorname{Var}(U_0)\), and cancel by stationarity. For independent processes, joint cumulants of their sum add. A stationary time-reversible process has the same joint law forward and backward, so its displayed cumulant difference vanishes. Taking \(U=Y+V\) proves the robustness statement, including colored, non-Gaussian reversible noise.

**5. Entire mixed-cumulant hierarchy.** By independent increments, every joint cumulant with at least one \(Y_0\) argument and \(q\) future-time arguments receives contributions only from the shared variable in \(Y_t=q_tY_0+\eta_t\). Multilinearity gives \(K_{p,q}(t)=q_t^q\kappa_{p+q}\). Exchanging the numbers of early and late arguments and inserting the cumulant formula proves the hierarchy. The third-order asymmetry may vanish under a symmetric kick distribution, whereas the fourth-order \((1,3)\) asymmetry cannot vanish for nontrivial kicks at any positive finite lag.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The file independently evaluates stationary fourth moments by polynomial generator equations, compares them to Poisson-integral fourth cumulants, reconstructs both chronological fourth moments from independent innovations, checks the thermal-noise invariance over several jump laws and parameters, verifies the exact peak location and inversion, and checks the mixed-cumulant coefficient algebra. The deterministic checks passed for both symmetric and asymmetric kicks, including a nonzero-mean deterministic kick law, with and without thermal noise. Analytic differentiation and cumulant identities, not finite computation, establish the conclusions for all admissible parameters and times.

## Relationship to prior work
Di Bello, Majumdar, Marathe, Metzler, and Roldán (arXiv:2309.13424, first posted 2023-09-23) give the harmonic Poisson-kick model, a stationary characteristic function and moments, and display the \(X,X^3\) chronological asymmetry numerically in their Fig. 5 and Eq. (68). Those model identities and qualitative asymmetry are **prior results**. The contribution here is the *evaluated full lag profile*, its exact universal optimizer and parameter inversion, and the independent reversible-noise invariance, with the connected-cumulant hierarchy as a unifying derivation. The present calculation uses standard stationary Lévy–Ornstein–Uhlenbeck and cumulant properties, not a new construction of those tools.

Spiliopoulos (arXiv:0807.2832) treats stationary Lévy–Ornstein–Uhlenbeck moments and estimation, emphasizing first two input moments and ordinary autocorrelation. Yuvan and Bier (Phys. Rev. E 104, 014119, 2021) study a different arrow-of-time statistic for symmetric alpha-stable Lévy forcing, generally outside finite-fourth-moment conditions. Ohga, Ito, and Kolchinsky (arXiv:2303.13116) bound cross-correlation asymmetry in finite-state Markov systems; their inequality does not evaluate this Poisson-kick lag dependence or its sharp maximizer. The relation to general shot-noise stationary cumulant literature is acknowledged: the stationary fourth cumulant alone is not claimed to be new.

## Limitations
The exact profile requires stationary initialization, linear restoring force, independent homogeneous Poisson jumps and finite fourth jump moment. The sharp time-lag inference presumes ideal knowledge of the full ensemble-expectation curve; finite observations can give noisy or biased estimates, especially in heavy-tailed regimes. An additional **irreversible** sensor process can change the witness. Neither finite-sample optimality nor total entropy production is derived. More general nonlinear traps, state-dependent kick rates, nonstationary starting states, and infinite-fourth-moment Lévy laws are not covered. A more general published joint-cumulant identity could subsume the evaluated formulas; originality beyond the inspected literature is not independently certified.

## References
1. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler, and É. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424 (2023), https://arxiv.org/html/2309.13424v2 .
2. K. Spiliopoulos, *Method of Moments Estimation of Ornstein-Uhlenbeck Processes Driven by General Lévy Process*, arXiv:0807.2832 (2008), https://arxiv.org/abs/0807.2832 .
3. S. Yuvan and M. Bier, *Breaking of time-reversal symmetry for a particle in a parabolic potential that is subjected to Lévy noise*, Phys. Rev. E 104, 014119 (2021), https://doi.org/10.1103/PhysRevE.104.014119 .
4. N. Ohga, S. Ito, and A. Kolchinsky, *Thermodynamic Bound on the Asymmetry of Cross-Correlations*, Phys. Rev. Lett. 131, 077101 (2023), https://arxiv.org/abs/2303.13116 .
5. I. Eliazar and J. Klafter, *Non-linear shot noise: Lévy, Noah, & Joseph*, Physica A 360, 227–260 (2006), https://doi.org/10.1016/j.physa.2005.06.056 .
