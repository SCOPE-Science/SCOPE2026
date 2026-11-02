# Zero-mean telegraph affinity: an exact storage–dissipation frontier for a two-state battery

## Finding

A two-state battery driven by a *symmetric, zero-mean* telegraph affinity can hold strictly positive excess free energy while dissipating at a nonzero stationary rate. For the finite-state model specified below, the excess charged-state probability and the full four-state Markov entropy-production rate obey an exact affine complementarity for **every** positive parameter choice and every positive switching rate. Their dependence on switching rate is strictly opposite, and the stored free energy traces a strictly convex decreasing curve against dissipation.

Write \(\epsilon=\beta E>0\), \(\alpha=\beta a>0\), and define
\[
C=\cosh(\epsilon/2),\quad B=\sinh(\epsilon/2),\quad c=\cosh(\alpha/2),\quad s=\sinh(\alpha/2),\quad H=k(C^2+s^2),\quad G=Cc.
\]
For positive intrinsic jump scale \(k\) and telegraph flip rate \(\nu\), the thermal population is \(p_{\rm eq}=(1+e^{\epsilon})^{-1}\), and the stationary charged-state population, oriented cycle current and dimensionless entropy-production rate are exactly
\[
\begin{aligned}
p_\nu-p_{\rm eq}&=\frac{k B s^2}{2C(H+\nu G)},\\
J_\nu&=\frac{k\nu s c}{2(H+\nu G)},\\
\sigma_\nu&=2\alpha J_\nu=\frac{\alpha k\nu s c}{H+\nu G}.
\end{aligned}
\]
In particular \(p_{\rm eq}<p_\nu<1/2\), so the zero-mean source stores a positive resource but never creates population inversion. Define positive limiting constants
\[
\delta_0=\lim_{\nu\downarrow0}(p_\nu-p_{\rm eq})=\frac{B s^2}{2C(C^2+s^2)},\qquad
\sigma_\infty=\lim_{\nu\to\infty}\sigma_\nu=\frac{\alpha k s}{C}.
\]
The **exact storage–dissipation complementarity** is
\[
\boxed{\frac{p_\nu-p_{\rm eq}}{\delta_0}+\frac{\sigma_\nu}{\sigma_\infty}=1\qquad(\nu>0).}
\]
As \(\nu\) increases, stationary charge decreases strictly from \(p_{\rm eq}+\delta_0\) to \(p_{\rm eq}\), while dissipation increases strictly from zero to \(\sigma_\infty\). Thus fast driving can dissipate at a positive limiting rate even as the observed battery marginal approaches thermal equilibrium.

Using the usual excess nonequilibrium free energy of the storage marginal,
\[
\mathcal A_\nu=\beta^{-1}D_{\rm KL}\!\left(\operatorname{Bern}(p_\nu)\,\middle\|\,\operatorname{Bern}(p_{\rm eq})\right),
\]
the complete frontier, parameterized by \(0<z<\sigma_\infty\), is
\[
\boxed{\mathcal A(z)=\beta^{-1}D_{\rm KL}\!\left(\operatorname{Bern}\!\left(p_{\rm eq}+\delta_0\left(1-\frac{z}{\sigma_\infty}\right)\right)\,\middle\|\,\operatorname{Bern}(p_{\rm eq})\right).}
\]
It is strictly decreasing and strictly convex. The result is an exact stationary statement, not a bound or a finite-time optimal-control assertion.

## Assumptions and scope

Fix inverse temperature \(\beta>0\), upper-level energy \(E>0\), affinity amplitude \(a>0\), intrinsic jump prefactor \(k>0\) and switching rate \(\nu>0\). The continuous-time Markov process has four states \((X,S)\in\{0,1\}\times\{+1,-1\}\), with \(X\) the occupied upper level and \(S\) the autonomous source sign. Sign flips \(S\mapsto-S\) occur at rate \(\nu\) independently of \(X\). For fixed \(S=\pm1\), transitions of \(X\) have rates
\[
u_\pm=k\exp((\pm\alpha-\epsilon)/2),\qquad v_\pm=k\exp(-(\pm\alpha-\epsilon)/2),
\]
where \(\epsilon=\beta E\), \(\alpha=\beta a\). (Here the symbol \(u_\pm\) denotes the \(0\to1\) rate, and \(v_\pm\) the \(1\to0\) rate.) These are the symmetric-splitting local-detailed-balance rates used for the constant-affinity battery in the cited source, now coupled to a symmetric telegraph source. The telegraph marginal is stationary uniform, \(\Pr(S=\pm1)=1/2\); hence its **mean affinity is zero**.

The finite positive-rate chain is irreducible and has a unique stationary law. \(\sigma_\nu\) is its *full four-state stationary path entropy-production rate*, in nats per physical-time unit, computed from the directed Markov edges. It is **not** an all-inclusive account of upstream fuel consumption or the energetic cost of physically realizing source switching. The useful storage figure is the excess free energy of the battery **marginal** after the source is disconnected; it does not assert a protocol-independent efficiency.

## Proof

**1. Stationarity.** Set \(\lambda_\pm=u_\pm+v_\pm\), \(z_\pm=\Pr_{\rm st}(X=1,S=\pm1)\). Since the sign marginal is uniform, \(\Pr(X=0,S=\pm1)=1/2-z_\pm\). The two exact balance equations are
\[
(\lambda_++\nu)z_+-\nu z_-=u_+/2,\qquad
-\nu z_++(\lambda_-+\nu)z_-=u_-/2.
\]
Let \(\Delta=\lambda_+\lambda_-+\nu(\lambda_++\lambda_-)\). Positivity gives \(\Delta>0\). Direct inversion yields
\[
z_+=\frac{u_+(\lambda_-+\nu)+\nu u_-}{2\Delta},\qquad
z_-=\frac{u_-(\lambda_++\nu)+\nu u_+}{2\Delta}.
\]
Hyperbolic identities imply
\[
\lambda_+\lambda_-=4k^2(C^2+s^2)=4kH,\quad
\lambda_++\lambda_-=4kCc=4kG,\quad \Delta=4k(H+\nu G).
\]
Substituting into \(p_\nu=z_++z_-\), and subtracting \(p_{\rm eq}=\tfrac12-B/(2C)\), gives exactly \(p_\nu-p_{\rm eq}=kBs^2/[2C(H+\nu G)]\). This is positive because \(\epsilon,\alpha,k,\nu>0\), and
\[
0<p_\nu-p_{\rm eq}<\frac{B}{2C}=\frac12-p_{\rm eq},
\]
because \(k s^2<H+\nu G\). Therefore \(p_{\rm eq}<p_\nu<1/2\).

**2. Cycle current and entropy production.** Orient the rectangle as \((0,+)\to(1,+)\to(1,-)\to(0,-)\to(0,+)\). All four stationary edge currents agree by nodewise conservation, and
\[
J_\nu=\nu(z_+-z_-)=\frac{k\nu s c}{2(H+\nu G)}>0.
\]
The product of forward/reverse transition-rate ratios around this cycle is
\[
\frac{u_+\,\nu\,v_-\,\nu}{v_+\,\nu\,u_-\,\nu}
=\exp(2\alpha).
\]
The stationary path relative-entropy-rate formula for a finite reversible-edge Markov chain is the sum of oriented edge currents times their edge affinities. In a single-cycle stationary network, vertex-probability terms telescope. Therefore \(\sigma_\nu=J_\nu\log(e^{2\alpha})=2\alpha J_\nu\), yielding the announced formula. This computation includes both sign-flip edges and both battery edges; ignoring the source sign would hide the nonequilibrium circulation.

**3. Exact complementarity and limits.** Define \(\delta_0\) and \(\sigma_\infty\) as above. Algebra gives
\[
\frac{p_\nu-p_{\rm eq}}{\delta_0}=\frac{H}{H+\nu G},\qquad
\frac{\sigma_\nu}{\sigma_\infty}=\frac{\nu G}{H+\nu G}.
\]
Their sum is exactly one. Since \(H,G>0\), differentiation establishes
\[
\frac{d(p_\nu-p_{\rm eq})}{d\nu}=-\frac{\delta_0 HG}{(H+\nu G)^2}<0,\qquad
\frac{d\sigma_\nu}{d\nu}=\frac{\sigma_\infty HG}{(H+\nu G)^2}>0.
\]
The endpoint limits follow directly. The finite value \(\delta_0\) is a \(\nu\downarrow0\) limit; at \(\nu=0\) the chain is reducible and its stationary law need not be unique, so no uniqueness claim is made there.

**4. Free-energy geometry.** Let \(q=p_{\rm eq}\). For \(q<p<1/2\),
\[
\frac{d}{dp}D_{\rm KL}(\operatorname{Bern}(p)\|\operatorname{Bern}(q))
=\log\frac{p(1-q)}{q(1-p)}>0,\qquad
\frac{d^2}{dp^2}D_{\rm KL}(\operatorname{Bern}(p)\|\operatorname{Bern}(q))
=\frac{1}{p(1-p)}>0.
\]
The affine relation \(p=q+\delta_0(1-z/\sigma_\infty)\) has negative nonzero slope. Its composition with the divergence is strictly decreasing and strictly convex on the stated interval, with
\[
\mathcal A''(z)=\frac{\delta_0^2}{\beta\sigma_\infty^2 p(1-p)}>0.
\]
This proves all claimed quantifiers and strictness assertions.

## Verification

The accompanying standalone `verify.py` independently constructs the four-state generator, solves stationary equations in exact rational arithmetic for many choices of exponential parameters, compares stationary probabilities and all four edge currents against the claimed formulas, and symbolically checks stationary balance, both derivatives and the exact frontier. Execution command: `python verify.py`. It reports 339 deterministic symbolic and exact-rational checks. These finite checks are supporting reproducibility evidence; the all-parameter result follows from the algebraic proof above. No simulations, numeric tail extrapolations, or independence claims are used as proofs.

## Relationship to prior work

Lin, Liu and Ma (2026), *Active-Matter Battery*, arXiv:2610.00428v1, establishes the constant-affinity local-detailed-balance battery, excess-free-energy storage definition, and charge/store/discharge motivation. The independently switching positive/negative affinity, the joint four-state stationary law, and the exact marginal-storage versus full-chain dissipation frontier are the specific additions here; the constant-affinity equations and stored free-energy functional are not claimed as new.

Bena (2006), *Dichotomous Markov Noise: Exact results for out-of-equilibrium systems*, arXiv:cond-mat/0606116v3, Section VII, equations (116)–(118), already treats a two-well particle with a switching two-state drive as a four-state master equation and evaluates its mean switching rate. Thus neither the telegraph construction, nor master-equation inversion, nor noise-induced nonequilibrium response is new in general. The source's symmetric-well switching-rate observable does not state or imply **as written** the asymmetric battery-marginal storage and normalized entropy-production complementarity, though the latter may be obtainable by adapting the same general four-state method; that is an originality limitation.

Esposito and Parrondo (2013/2015), *Stochastic thermodynamics of hidden pumps*, arXiv:1310.2987v3, develops network entropy-production and hidden-pump analysis. The standard cycle-current times affinity identity used here is pre-existing thermodynamic theory, not a newly introduced formula. Their externally driven hidden-pump schemes are not the autonomous symmetric telegraph-affinity model, and they do not give the particular affine storage–dissipation frontier above.

## Limitations

The theorem is restricted to a single two-level storage element, equal-magnitude independent telegraph flips, identical state-independent switching rates, symmetric splitting of both battery transition rates, and positive parameters. The exact linear frontier can change if any of these assumptions is relaxed; no universal tradeoff across different models is claimed. The stationary storage measurement uses the source-disconnected battery marginal. The complete energetic cost of maintaining and implementing an active telegraph source is not modeled, so \(\sigma_\nu\) must not be read as a device-wide fuel-efficiency denominator. The zero-switching endpoint is a one-sided limit, not a claim of a unique steady state at \(\nu=0\). Potential subsumption by a broader telegraph-driven two-state stochastic-thermodynamics formula is a residual originality risk; no independent research-priority assessment has been performed.

## References

1. Y.-Q. Lin, R.-H. Liu and Y.-H. Ma, *Active-Matter Battery*, arXiv:2610.00428v1 (first publicly submitted 2026-09-30). https://arxiv.org/html/2610.00428v1
2. I. Bena, *Dichotomous Markov Noise: Exact results for out-of-equilibrium systems. A review*, arXiv:cond-mat/0606116v3 (first publicly submitted 2006-06-05), especially Section VII and equation (117). https://arxiv.org/html/cond-mat/0606116v3
3. M. Esposito and J. M. R. Parrondo, *Stochastic thermodynamics of hidden pumps*, arXiv:1310.2987v3 (first publicly submitted 2013-10-10). https://arxiv.org/html/1310.2987v3
