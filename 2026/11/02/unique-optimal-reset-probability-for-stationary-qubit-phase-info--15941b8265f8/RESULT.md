# Unique optimal reset probability for stationary qubit phase information

## Finding

Consider a single qubit subjected, once per clock tick, either to a phase gate or to complete state resetting. At a fixed nonresonant gate phase, its stationary mixed state has a **unique** reset probability maximizing the quantum Fisher information (QFI) for estimating that phase. This optimum is global, interior, and simple. The optimizer has an exact polynomial characterization for every phase; at a half-turn it equals \(2/3\), whereas near an identity-gate resonance it follows a sharp linear detuning law with a divergent optimal QFI.

Precisely, for \(0<p<1\), let the completely positive trace-preserving update be

\[
\mathcal E_{p,\theta}(\rho)=p|+\rangle\langle+|+(1-p)U_\theta\rho U_\theta^\dagger,
\qquad U_\theta=e^{i\theta\sigma_z/2},
\qquad |+\rangle=(|0\rangle+|1\rangle)/\sqrt2.
\]

For each \(\theta\in(0,2\pi)\), let \(F(p,\theta)\) be the symmetric-logarithmic-derivative QFI of the unique stationary state, with \(p\) held fixed when differentiating in \(\theta\). Put \(t=\sin^2(\theta/2)\), \(x=p/(1-p)\), and \(A=x^2+4t(1+x)\). Then

\[
F(p,\theta)=\frac{x^2[A+x^2(1+x)(1-t)]}{A^3}.
\]

The sole maximizer is \(p_*(\theta)=x_*(t)/(1+x_*(t))\), where \(x_*(t)>0\) is the unique positive root of

\[
\begin{aligned}
P_t(x)={}&-(1-t)x^5-2(4t^2-5t+2)x^4+8t(2-3t)x^3\\
&+16t(1-t)x^2+32t^2x+32t^2.
\end{aligned}
\]

At \(\theta=\pi\), \(p_*(\pi)=2/3\) and \(\max_p F(p,\pi)=1/64\). Writing \(\delta=\min\{\theta,2\pi-\theta\}\) for the distance from a nearby identity-gate resonance, as \(\delta\downarrow0\) along nonresonant phases,

\[
\boxed{\frac{p_*(\theta)}{\delta}\longrightarrow\sqrt{\frac{1+\sqrt3}{2}},\qquad
\delta^2\max_{0<p<1}F(p,\theta)\longrightarrow\frac{2\sqrt3}{9}.}
\]

## Assumptions and scope

The qubit is ideal; every reset replaces its density matrix by \(|+\rangle\langle+|\), independently of its prior state. Reset events are independent Bernoulli trials with constant probability \(p\) at every tick, and the alternative unitary operation is \(U_\theta\). The unknown real gate phase is estimated from a copy of the stationary **unconditioned** qubit state, without observing the random reset history. Reset probability is an experimentally selected, known control parameter, constant during differentiation in phase. All assertions of interior uniqueness concern \(0<p<1\) and nonresonant \(\theta\notin2\pi\mathbb Z\). The near-resonance limit is punctured: it is not an assertion about the QFI evaluated exactly at the rank-changing resonant phase.

No claim is made about quantum Fisher information per consumed gate, finite-time preparation, collective measurements on temporally correlated outputs, or access to a classical record of reset times.

## Proof

**1. Unique stationary state and Bloch coefficient.** The affine update contracts traceless matrix differences by factor \(1-p\) in trace norm, hence has one stationary state and attracts all initial states. The upper-right entry of a density matrix is multiplied by \(e^{i\theta}\) under \(U_\theta\). Therefore its stationary state is

\[
\rho_{p,\theta}=\frac12\begin{pmatrix}1&z\\\bar z&1\end{pmatrix},
\qquad z=\frac{p}{1-(1-p)e^{i\theta}}.
\]

Let \(q=1-p\), \(t=\sin^2(\theta/2)\), and \(\Delta=p^2+4qt=|1-qe^{i\theta}|^2\). Then \(|z|^2=p^2/\Delta\), and

\[
1-|z|^2=\frac{4qt}{\Delta}>0
\]

in the stated domain, so the SLD QFI full-rank formula applies.

**2. Exact QFI.** For an equatorial qubit with Bloch coefficient \(z\), the SLD QFI is

\[
F=|\partial_\theta z|^2+
\frac{\{\operatorname{Re}(\bar z\partial_\theta z)\}^2}{1-|z|^2}.
\]

Here \(|\partial_\theta z|^2=p^2q^2/\Delta^2\), while \(\operatorname{Re}(\bar z\partial_\theta z)=-p^2q\sin\theta/\Delta^2\). Substitution gives the exact, nonnegative expression

\[
F=\frac{p^2q^2}{\Delta^2}
+\frac{p^4q\cos^2(\theta/2)}{\Delta^3}.
\]

The odds substitution \(x=p/q\) gives the expression in the Finding section.

**3. Unique interior maximum.** Direct algebra, or exact symbolic differentiation, yields

\[
\frac{\partial F}{\partial x}=\frac{xP_t(x)}{[x^2+4t(1+x)]^4}.
\]

For \(0<t<1\), the coefficients of \(P_t\), read in descending powers, are: a negative quintic coefficient; a strictly negative quartic coefficient (since \(4t^2-5t+2>0\), whose discriminant is \(-7\)); a cubic coefficient with either sign; a strictly positive quadratic coefficient; and positive linear and constant coefficients. Thus the nonzero coefficient sequence has **exactly one sign change**. For \(t=1\), the leading nonzero coefficients are negative in degrees four and three and positive in degrees one and zero, again giving exactly one sign change. Descartes' rule of signs therefore permits at most one positive root, counted with multiplicity. Since \(P_t(0)=32t^2>0\) and its leading nonzero coefficient is negative, continuity guarantees a positive root. It is unique and simple. The derivative is positive before that root and negative afterward. Finally \(F\to0\) both as \(x\downarrow0\) and \(x\to\infty\), proving global optimality and uniqueness.

**4. Half-turn benchmark.** For \(t=1\), \(A=(x+2)^2\) and \(F=x^2/(x+2)^4\). Its unique positive stationary point is \(x=2\), giving \(p=2/3\) and \(F=1/64\).

**5. Singular resonance scaling.** Put \(\delta=\min\{\theta,2\pi-\theta\}\). As \(\delta\downarrow0\), \(t=\delta^2/4+O(\delta^4)\). For every fixed \(y>0\),

\[
\delta^{-4}P_t(\delta y)\longrightarrow -4y^4+4y^2+2.
\]

The limiting polynomial has exactly one positive zero at \(y_0=\sqrt{(1+\sqrt3)/2}\), is positive below it and negative above it. Fix any positive lower and upper bounds straddling \(y_0\). For sufficiently small detuning the same signs hold at those two scaled test points. Since \(P_t\) has exactly one positive zero, those bounds trap \(x_*(t)/\delta\); shrinking the bounds proves convergence to \(y_0\). Because \(p=x/(1+x)\) and \(x_*(t)\to0\), the asserted optimizer scaling follows. Evaluating the exact QFI at \(x=\delta y_0+o(\delta)\) gives

\[
\lim_{\delta\downarrow0}\delta^2F(p_*(\theta),\theta)
=\frac{y_0^2(2y_0^2+1)}{(1+y_0^2)^3}
=\frac{2\sqrt3}{9}.
\]

These are limits of exact stationary states; no interchange of finite-time and stationary limits is used.

## Verification

The accompanying `verify.py` reproduces the rational QFI identity, exactly factors its reset-odds derivative, and checks the half-turn value and resonance constant symbolically using SymPy. Independently of this symbolic route, it constructs the two-by-two fixed-point density matrix, checks the quantum channel fixed-point equation, and computes its QFI from the spectral SLD formula using numerical phase differentiation. It compares those values with the derived closed form at 24 parameter pairs; all comparisons pass at the stated tolerances. It also brackets each positive optimum and reports near-resonance convergence. Execute `python verify.py` after installing NumPy and SymPy. The finite tests support but do not replace the analytic root-count and asymptotic proof above.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo derive the geometric-mixture stationary state for discrete-time quantum gates with random resetting and investigate resonant coherences and two-qubit correlations. Their stationary-state formula is a **premise** here, not a novelty claim; a direct fixed-point derivation is provided for this qubit. Their full accessible preprint, including correlation appendices, does not state a stationary phase-QFI optimization or the present unique positive-root and punctured-resonance scaling classification. Li, Tong and Bao's later reset-metrology study derives a general QFI reset-rate response identity in continuous-time dissipative quantum dynamics, a different channel family; it does not imply the stated discrete-time polynomial root classification. O'Connor and collaborators study Fisher information rates for sequentially measured quantum systems, not the unconditioned stationary snapshot QFI used here. The exact originality claim is the sharp global optimizer and its singular phase-detuning law, not the generic SLD formula or geometric reset resolvent.

## Limitations

The conclusion is for the minimal equatorial single-qubit gate/reset protocol only. At exactly an identity-gate resonance the stationary state becomes pure, so the full-rank QFI expression has a singular limit and must not be substituted there as an exact-resonance formula. Unconditioned stationary snapshot QFI is distinct from trajectory-resolved information and from a cost-normalized precision rate: the preparation time typically grows when resetting becomes rare. No independent publication-priority determination or external experimental validation is claimed.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1 (first public version October 15, 2024), https://arxiv.org/html/2410.11497v1 .
2. S. Li, Q. Tong, and R. Bao, *Reset-Enhanced Dissipative Quantum Metrology*, arXiv:2610.31249 (October 22, 2026), https://arxiv.org/abs/2610.31249 .
3. E. O'Connor, S. Campbell, and G. T. Landi, *Fisher information rates in sequentially measured quantum systems*, New Journal of Physics **26**, 033048 (2024), https://doi.org/10.1088/1367-2630/ad345c .
