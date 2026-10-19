# Exact reachability and an immutable edge exponent for fixed-speed run-and-tumble control

## Finding

For a zero-temperature, one-dimensional, harmonically confined run-and-tumble particle of **fixed propulsion speed** \(v>0\), with arbitrary bounded continuous *strictly positive* time-dependent trap stiffness and tumbling-rate controls, the joint stationary law at parameters \((\kappa_i,\alpha_i)\) can be mapped **exactly** to the joint stationary law at \((\kappa_f,\alpha_f)\) in a prescribed time \(T>0\), with controls matching the specified endpoints, **if and only if**

\[
\boxed{\ \frac{\alpha_i}{2\kappa_i}=\frac{\alpha_f}{2\kappa_f}\quad\text{and}\quad \frac{v}{\kappa_f}-\frac{v}{\kappa_i}<vT.\ }
\]

The equality fixes the boundary power \(\beta=\alpha/(2\kappa)-1>-1\). No positive finite-time protocol can exactly transform a stationary boundary exponent \(\beta_i\) into a different \(\beta_f\); in particular no exact active-like-to-passive-like conversion is possible in this control class. Compression is possible in arbitrarily short positive time with unboundedly strong but finite controls; expansion has the sharp **unattained** lower time \(T_*=(R_f-R_i)/v\), where \(R_j=v/\kappa_j\).

More generally, without assuming a final stationary distribution, the exact right-edge asymptotic at time \(T\) for every such protocol is

\[
\mathbb P\{X_T>R_T-\varepsilon\}=\frac{2^{\beta_i}e^{-\Lambda}}{(\beta_i+1)Z_{\beta_i}}\left(\frac{\varepsilon}{sR_i}\right)^{\beta_i+1}\bigl(1+O(\varepsilon)\bigr),\qquad \varepsilon\downarrow0,
\]

where \(s=\exp[-\int_0^T\kappa(t)dt]>0\), \(\Lambda=\frac12\int_0^T\alpha(t)dt\), \(Z_b=\int_{-1}^{1}(1-y^2)^bdy\), and \(R_T=sR_i+v\int_0^T\exp[-\int_t^T\kappa(u)du]dt\). In particular \(\beta_i+1\) is a conserved **finite-time support-tail exponent**, despite generally time-varying coefficients and arbitrary numbers of tumbles.

## Assumptions and scope

Let \(\sigma_t\in\{-1,+1\}\) change sign at a position-independent, time-inhomogeneous Poisson rate \(\alpha(t)/2\), independently of the initial state. Between switches,

\[
\dot X_t=-\kappa(t)X_t+v\sigma_t,
\]

with a fixed \(v>0\) and no thermal diffusion. Assume \(\kappa,\alpha:[0,T]\to(0,\infty)\) are continuous, hence bounded and bounded away from zero, with endpoint values \(\kappa(0)=\kappa_i\), \(\kappa(T)=\kappa_f\), \(\alpha(0)=\alpha_i\), \(\alpha(T)=\alpha_f\). The constructive controls below can be chosen smooth. Exact transfer concerns the full joint distribution of position and orientation, not merely its low moments. There are no restrictions on how large a *finite* positive control may become; if physical upper/lower control bounds are additionally imposed, the sufficiency statement need not hold.

For fixed coefficients, write \(R=v/\kappa\) and \(b=\alpha/(2\kappa)-1>-1\). The normalized stationary joint densities are

\[
p_\pm(x;R,b)=\frac{(1\pm x/R)(1-(x/R)^2)^b}{2RZ_b}\,\mathbf 1_{\{|x|<R\}},\qquad Z_b=\frac{\sqrt\pi\,\Gamma(b+1)}{\Gamma(b+3/2)}.
\]

Thus the position density is \(\rho(x)=(1-(x/R)^2)^b/(RZ_b)\), and the orientation polarization is \(p_+(x)-p_-(x)=(x/R)\rho(x)\). These formulas can also be directly checked in the coupled transport-switching equations.

## Proof

**1. Reachable support and right-edge representation.** Set \(w(t)=\exp[-\int_t^T\kappa(u)du]\), \(s=w(0)\). Variation of constants gives, for every realization,

\[
X_T=sX_0+v\int_0^T w(t)\sigma_tdt.
\]

Since \(X_0\le R_i\) and \(\sigma_t\le1\), the rightmost support endpoint is

\[
R_T=sR_i+v\int_0^T w(t)dt.
\]

It is the actual support endpoint: initial states with \(\sigma_0=+1\) have positive probability arbitrarily close to \(R_i\), and there is positive probability of no tumbling over the finite interval. The exact nonnegative distance to the frontier is

\[
D_T:=R_T-X_T=s(R_i-X_0)+2v\int_0^T w(t)\mathbf1_{\{\sigma_t=-1\}}dt. \tag{1}
\]

**2. Sharp edge-tail invariant.** Since \(\kappa(t)>0\), \(s\le w(t)\le1\). If \(D_T<\varepsilon\), then \(R_i-X_0<\varepsilon/s\) and the total negative-orientation occupation time \(S_T=\int_0^T\mathbf1_{\{\sigma_t=-1\}}dt\) is less than \(\varepsilon/(2vs)\). Stationary initial edge probabilities, using the explicit densities, are

\[
\begin{aligned}
\mathbb P(X_0>R_i-h,\sigma_0=+1)&=\frac{2^{b}}{(b+1)Z_b}\left(\frac{h}{R_i}\right)^{b+1}[1+O(h)],\\
\mathbb P(X_0>R_i-h,\sigma_0=-1)&=O(h^{b+2}).
\end{aligned}\tag{2}
\]

Here \(b=\beta_i\), and the estimates hold for all \(b>-1\), including integrably divergent stationary densities. For initial \(\sigma_0=+1\), the no-tumble event has probability \(e^{-\Lambda}\), \(\Lambda=\frac12\int_0^T\alpha(t)dt\), and on this event \(D_T=s(R_i-X_0)\). Consequently its contribution to \(\mathbb P(D_T<\varepsilon)\) is precisely \(e^{-\Lambda}\) times the first expression in (2), with \(h=\varepsilon/s\).

It remains to bound paths with tumbles. Put \(\lambda_*:=\max_{t\in[0,T]}\alpha(t)/2<\infty\) and \(\delta=\varepsilon/(2vs)\). Conditional on \(\sigma_0=+1\), an event with at least one tumble but total negative occupation time \(S_T<\delta\) must have either (i) its first switch in the last \(\delta\) units of time or (ii) two consecutive switches less than \(\delta\) apart. For an inhomogeneous Poisson process dominated by rate \(\lambda_*\), these events have total probability at most \(\lambda_*\delta+\lambda_*^2T\delta\): the second estimate follows by bounding the expected number of ordered close pairs. This event is independent of \(X_0\) given \(\sigma_0=+1\). Multiplying by the first estimate in (2) gives \(O(\varepsilon^{b+2})\). The contribution from \(\sigma_0=-1\) is at most the second estimate in (2), also \(O(\varepsilon^{b+2})\), regardless of later switches. Hence

\[
\mathbb P(D_T<\varepsilon)=e^{-\Lambda}\frac{2^{b}}{(b+1)Z_b}\left(\frac{\varepsilon}{sR_i}\right)^{b+1}+O(\varepsilon^{b+2}).\tag{3}
\]

The coefficient is finite and strictly positive. Thus every finite-time protocol retains the initial exponent \(b+1\), irrespective of transient changes in \(\alpha\) or \(\kappa\). If the final law were stationary at \((\kappa_f,\alpha_f)\), the actual support endpoint would equal \(R_f\), and its right-edge power would be \(\beta_f+1\). Equation (3) therefore forces \(\beta_f=\beta_i\).

**3. Sharp expansion speed limit.** For the moving support endpoint \(R(t)\), computed as in step 1 at arbitrary intermediate times, differentiating its explicit integral representation gives \(\dot R(t)=v-\kappa(t)R(t)<v\), since \(R(t)>0\) and \(\kappa(t)>0\). Integrating yields \(R_f-R_i<vT\) whenever the final law is stationary. Equality cannot occur for any strictly positive continuous stiffness. For compression \(R_f\le R_i\), this inequality is automatic.

**4. Explicit exact-transfer construction.** Conversely assume \(\beta_i=\beta_f=b>-1\) and \(R_f-R_i<vT\). Select any smooth positive \(R:[0,T]\to(0,\infty)\) with \(R(0)=R_i\), \(R(T)=R_f\), \(\dot R(0)=\dot R(T)=0\) and \(\sup_t\dot R(t)<v\). For expansion, such a path exists because its average slope \((R_f-R_i)/T\) is strictly less than \(v\): take a positive smooth bump derivative whose normalized integral is one and whose maximum approaches the uniform derivative from above; a monotone compressed path poses no restriction. Set

\[
\boxed{\quad\kappa(t)=\frac{v-\dot R(t)}{R(t)},\qquad\alpha(t)=2(b+1)\frac{v}{R(t)}.\quad}\tag{4}
\]

They are smooth, strictly positive, and match both endpoint control pairs. Let \((Y_u,\eta_u)\) be the stationary dimensionless RTP with \(dY_u/du=-Y_u+\eta_u\) and orientation flips at rate \(b+1\). Define

\[
q(t)=\int_0^t\frac{v}{R(s)}ds,\qquad X_t=R(t)Y_{q(t)},\quad \sigma_t=\eta_{q(t)}.
\]

Differentiating gives \(\dot X_t=-(v-\dot R(t))X_t/R(t)+v\sigma_t\) between tumbles. The time-change transforms the flip rate into \((b+1)v/R(t)=\alpha(t)/2\). Stationarity of \((Y,\eta)\) therefore shows that at **every** intermediate time the full joint law of \((X_t,\sigma_t)\) equals the law \(p_\pm(x;R(t),b)\). At the endpoint it is exactly the desired stationary law. This proves sufficiency and the full equivalence.

## Verification

The standalone `verify.py` numerically integrates the exact first four mixed moment equations for five nontrivial expansion/compression parameter sets and compares them with the explicit time-dependent stationary-shape moments. The maximal absolute difference was approximately \(2.6\times10^{-10}\). It also integrates four stationary orientation-resolved edge tails and checks the coefficient in (2); their coefficient ratios at layer thickness \(10^{-4}\) were between \(0.99985\) and \(1\). All tested stiffnesses were strictly positive. These **finite checks are independent sanity tests**; the infinite-dimensional transfer and impossibility results are proved by the pathwise argument and time change above, not inferred from numerics.

Run with Python, NumPy and SciPy: `python verify.py`.

## Relationship to prior work

Baldovin and Manacorda [1] study **the same fixed-speed, athermal harmonic RTP** with stiffness and flip-rate controls. They supply the exact stationary beta-shaped density and construct a moment hierarchy; their explicit protocols use a long-duration closure with documented boundary-matching errors, rather than an exact finite-time if-and-only-if classification. The present result proves an exact reachable-state obstruction and constructs exact transfers on its allowed leaf without closing a moment hierarchy. Their proposed fully recursive approach does not itself establish convergence or positivity of controls when the initial and target edge exponents differ; the pathwise obstruction here identifies a specific barrier under the stated controls.

Frim and DeWeese [2] independently construct exact RTP shortcuts for **different actuators**, prominently changing propulsion speed while manipulating harmonic stiffness, with different endpoint constraints and optional thermal noise. Their scale-engineering mechanism is related to the constructive half of (4), but their statements do not imply that **fixed propulsion speed with stiffness and tumbling controls alone** admits exactly the same-beta leaf and no other finite-time transfers. A 2026 active-matter shortcut treatment [3] addresses a different active Ornstein–Uhlenbeck setting. The possibility that a more general transport-support theorem elsewhere implies part of the edge argument remains a residual literature risk.

## Limitations

The theorem concerns zero thermal noise, fixed positive propulsion speed, symmetric orientation flips independent of position, and **bounded positive continuous** coefficients on a finite time interval. It does not claim impossibility if propulsion speed can be controlled, if thermal diffusion is added, if rates can have singular impulsive components or if negative stiffness is allowed. Nor does it optimize energetic cost or bounded-amplitude constrained control. The open strict lower bound \(T_*\) for expansion is an infimum, not an attainable minimum. Exact equality of the joint laws is essential; arbitrarily close approximate transfer for different edge exponents is not ruled out. Independent external validation has not been performed.

## References

1. M. Baldovin and A. Manacorda, *Control protocols for harmonically confined run-and-tumble particles*, arXiv:2602.04560, first posted 2026-02-04; *Physical Review E* **114**, 014112 (2026). https://arxiv.org/html/2602.04560v2
2. A. G. Frim and M. R. DeWeese, *Shortcut engineering of active matter: run-and-tumble particles*, arXiv:2304.06023, first posted 2023-04-12. https://arxiv.org/html/2304.06023v1
3. *Shortcuts to state transitions for active matter*, arXiv:2604.05585 (2026). https://arxiv.org/abs/2604.05585
