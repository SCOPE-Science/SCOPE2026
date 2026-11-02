# A Gumbel–Gamma law for reset-event harmonic energy extremes and their selected cycle ages

## Finding

A particle trapped by a harmonic force and instantaneously reset to the origin has an exactly computable hierarchy of **pre-reset potential-energy** rare events. The maximum energy at the first \(n\) complete resetting events is asymptotically Gumbel. The reset interval that produces this maximum has a Gamma-distributed exponential-age mark and grows only as \(\log\log n\), despite the longest reset interval growing as \(\log n\). A separate sharp transition determines whether the stationary reset-event energy has a finite exponential moment at the natural inverse-thermal-energy scale.

With the assumptions below, put \(\beta=r/(2\mu)>0\), \(C_\beta=\Gamma(\beta+1)/\sqrt\pi\), and
\[
a_n=\log n-(\beta+\tfrac12)\log\log n+\log C_\beta.
\]
For all sufficiently large integers \(n\), write \(M_n=\max_{1\le i\le n}E_i\) and let \(J_n\) be its unique maximizing cycle. There are independent random variables \(G\) (standard Gumbel, \(\Pr(G\le x)=e^{-e^{-x}}\)) and \(V\sim\operatorname{Gamma}(\beta,1)\) such that
\[
\boxed{\bigl(M_n-a_n,\ a_ne^{-2\mu T_{J_n}}\bigr)\ \Longrightarrow\ (G,V).}
\]
Consequently,
\[
\boxed{2\mu T_{J_n}-\log\log n\ \Longrightarrow\ -\log V.}
\]
In contrast, the longest of the \(n\) reset intervals satisfies
\[
\frac{r\max_{i\le n}T_i}{\log n}\longrightarrow1\qquad\text{in probability},
\]
and its pre-reset energy is negligible compared with \(M_n\). In particular, the probability that the longest interval also produces the largest energy tends to zero.

The underlying one-cycle energy satisfies the sharp tail
\[
\boxed{\Pr(E_1>w)\sim\frac{\Gamma(\beta+1)}{\sqrt\pi}\,e^{-w}w^{-\beta-1/2}}
\qquad(w\to\infty),
\]
and the exact exponential-moment boundary
\[
\boxed{\mathbb E e^{sE_1}<\infty\ \Longleftrightarrow\
\bigl(s<1\bigr)\ \text{or}\ \bigl(s=1\text{ and }r>\mu\bigr),\qquad s\in\mathbb R.}
\]
These statements describe a **potential-energy decrement under an ideal instantaneous position reset**, not the stochastic thermodynamic work or entropy production of a finite-time physical reset mechanism.

## Assumptions and scope

Let \(\mu,D,r>0\). Between resets a real-valued position follows the overdamped Ornstein–Uhlenbeck stochastic differential equation
\[
dX_t=-\mu X_t\,dt+\sqrt{2D}\,dB_t.
\]
The reset times form an independent homogeneous Poisson process of rate \(r\); at each reset, \(X\) is set exactly to zero and a fresh Brownian increment process drives the next interval. Define \(T_i\) as the duration of complete cycle \(i\), \(X_i^-\) as its position immediately before resetting, and
\[
E_i=\frac{\mu}{2D}(X_i^-)^2.
\]
This is dimensionless harmonic potential energy \(\mu X^2/2\), measured in units of \(D\); the deterministic reset moves the coordinate to the potential minimum. It is not claimed that this is a universal implementation-dependent work or heat increment. All probability laws here concern independent complete cycles \(i=1,2,\ldots\), not the maximum sampled continuously within a cycle or the incomplete final cycle in a fixed time window. Gamma uses shape \(\beta\) and unit rate. Limits hold for every fixed \(\mu,D,r>0\) as \(n\to\infty\).

## Proof

**1. Independent cycle representation.** The explicit OU propagator, starting at zero, gives
\[
X_i^-\ \stackrel d=\sqrt{\frac D\mu\bigl(1-e^{-2\mu T_i}\bigr)}\,Z_i,
\]
where \(T_i\) are iid exponential of rate \(r\), the \(Z_i\) are iid standard normal, and the two collections are independent. This follows by normalizing the Gaussian stochastic integral using its conditional variance. Define \(U_i=e^{-2\mu T_i}\). Then, for \(0<u<1\),
\[
\Pr(U_i\le u)=\Pr\bigl(T_i\ge-\tfrac{1}{2\mu}\log u\bigr)=u^\beta,
\]
so \(U_i\) are iid \(\operatorname{Beta}(\beta,1)\) and
\[
E_i\ \stackrel d=\frac{1-U_i}{2}Z_i^2.
\]
The pairs \((U_i,Z_i)\) are independent across complete cycles, including when conditioned on their lengths.

**2. Exact density.** Conditionally on \(U_i=u\), the energy has gamma density
\[
f(w\mid u)=\frac{e^{-w/(1-u)}}{\sqrt{\pi w(1-u)}},\qquad w>0.
\]
Integration against \(\beta u^{\beta-1}du\) gives
\[
f_\beta(w)=\frac\beta{\sqrt{\pi w}}\int_0^1u^{\beta-1}(1-u)^{-1/2}e^{-w/(1-u)}du.
\]
The change of variables \(t=u/(1-u)\) and the standard integral representation of Tricomi's function yield
\[
f_\beta(w)=\frac{\Gamma(\beta+1)}{\sqrt{\pi w}}e^{-w}\,U\!\left(\beta,\tfrac12,w\right).
\]
The exact marginal law and its corresponding stationary spatial distribution are not claimed as new; their role here is to support the marked extreme-value analysis.

**3. Sharp tail and limiting age mark.** The normal tail is
\[
S_\beta(w)=\Pr(E_i>w)=\beta\int_0^1u^{\beta-1}\operatorname{erfc}\!\left(\sqrt{\frac{w}{1-u}}\right)du.
\]
Set \(v=wu\) and use \(\operatorname{erfc}(\sqrt y)\sim e^{-y}/\sqrt{\pi y}\) as \(y\to\infty\). After division by \(e^{-w}w^{-\beta-1/2}/\sqrt\pi\), the transformed integrand converges pointwise to \(\beta v^{\beta-1}e^{-v}\). The elementary upper bound
\[
\operatorname{erfc}(\sqrt y)\le\frac{e^{-y}}{\sqrt{\pi y}},\qquad y>0,
\]
gives the bound \(\beta v^{\beta-1}e^{-v}\), because \(w/(1-v/w)-w=v/(1-v/w)\ge v\) and \(\sqrt{1-v/w}\le1\). Dominated convergence gives
\[
S_\beta(w)\sim\frac{\beta\Gamma(\beta)}{\sqrt\pi}e^{-w}w^{-\beta-1/2}.
\]
The same calculation with an indicator \(\{wu\in A\}\) gives, for every Gamma-continuity set \(A\subset(0,\infty)\),
\[
\Pr(wU_i\in A\mid E_i>w)\longrightarrow\frac1{\Gamma(\beta)}\int_Av^{\beta-1}e^{-v}dv.
\]
No assumption about the age distribution *conditioned on a large energy* has been made in advance; it is derived from this integral.

**4. Exponential moments.** Conditional normal integration yields for \(s\in\mathbb R\)
\[
\mathbb E(e^{sE_i}\mid U_i=u)=\bigl(1-s(1-u)\bigr)^{-1/2}
\]
if \(s(1-u)<1\), and infinity otherwise. If \(s<1\), the mixture is finite. If \(s>1\), a positive-measure set of small \(u\)'s has infinite conditional moment. For \(s=1\), the remaining beta integral is
\[
\mathbb E e^{E_i}=\beta\int_0^1u^{\beta-3/2}du
=\begin{cases}\beta/(\beta-1/2),&\beta>1/2,\\+\infty,&\beta\le1/2.\end{cases}
\]
This proves the stated critical criterion \(r>\mu\) for finiteness at the boundary.

**5. Extreme values and Gamma-mark independence.** The tail asymptotic and the definition of \(a_n\) imply for fixed \(x\in\mathbb R\),
\[
n\Pr(E_1>a_n+x)\longrightarrow e^{-x}.
\]
Thus \(\Pr(M_n\le a_n+x)=[1-\Pr(E_1>a_n+x)]^n\to e^{-e^{-x}}\). Furthermore, the conditional Gamma-mark result with \(w=a_n+x\), and \(a_n/(a_n+x)\to1\), gives
\[
n\Pr(E_1>a_n+x,\ a_nU_1\in A)\longrightarrow e^{-x}\Pr(V\in A).
\]
For finitely many disjoint rectangles in \(\mathbb R\times(0,\infty)\) bounded below in the first coordinate, independence of complete cycles and the binomial-to-Poisson limit give a marked Poisson point process with intensity
\[
e^{-x}dx\,\frac{v^{\beta-1}e^{-v}}{\Gamma(\beta)}dv.
\]
Its largest first coordinate exists and has the standard Gumbel law; the attached second coordinate is independent with the Gamma distribution. The continuous-mapping argument for the unique largest point gives the boxed joint limit (a standard truncation below a large negative first coordinate removes noncompactness). Since \(V\in(0,\infty)\) almost surely, logarithmic continuity yields
\[
2\mu T_{J_n}-\log a_n=-\log(a_nU_{J_n})\Longrightarrow-\log V.
\]
Because \(a_n/\log n\to1\), the replacement \(\log a_n=\log\log n+o(1)\) is valid.

**6. Strict separation from the longest cycle.** The maximum \(T_{(n)}\) of \(n\) independent \(\operatorname{Exp}(r)\) variables satisfies \(rT_{(n)}/\log n\to1\) in probability by elementary exponential-tail estimates. The maximizing-energy cycle has \(T_{J_n}/\log\log n\to1/(2\mu)\) in probability, hence \(\Pr(J_n=\operatorname{argmax}_iT_i)\to0\). Additionally, because the Gaussian marks are independent of the entire duration vector, the \(Z_i\) attached to the longest interval is a fresh standard normal. Therefore \(E_{I_n}\le Z_{I_n}^2/2\) is tight, while \(M_n/a_n\to1\) in probability with \(a_n\to\infty\). Thus \(E_{I_n}/M_n\to0\) in probability.

## Verification

The standalone script `verify.py` uses SciPy special functions and quadrature to compare the exact beta-mixture density with the Kummer–Tricomi representation, check integral identities and boundary moments, and test numerical convergence of the scaled tail and conditional-age integrals for multiple parameter choices. Run `python -m pip install -r requirements.txt` followed by `python verify.py` to obtain its deterministic check count. These are finite cross-checks. All limiting distribution statements, including marked independence and the longest-cycle comparison, are justified by the preceding proof, not simulations or numerical extrapolations.

## Relationship to prior work

Farago's 2026 analysis of a resetting harmonic-oscillator heat engine develops the OU Gaussian transition law and thermodynamic costs of the resetting protocol; here that transition law is the starting point, and physical protocol-dependent cost is deliberately excluded. Trajanovski and collaborators (2023) already give exact stationary positional distributions for OU processes with resetting; the stationary marginal, the one-cycle density and the Gaussian-mixture setup are not priority claims. Gupta, Olsen and Krishnamurthy (2025), and Olsen and collaborators (2024), analyze fluctuating erasure work and associated moment generating functions under physical trap protocols that differ from instantaneous coordinate resetting. Singh and Pal (2021) consider the largest **continuous-path spatial excursion** and its attainment time, a different extremal observable from energy measured immediately **at resets**. A prior companion result on the maximum absolute area within a scaled-Brownian reset interval concerns an accumulated path functional with logarithmic winning durations, rather than the pre-reset harmonic energy and doubly logarithmic selected age here. The new focus is the joint Gumbel–Gamma marked extreme law and its consequent distinct age scale, together with the exact critical exponential-moment threshold.

## Limitations

The result assumes one-dimensional linear OU drift, thermal Gaussian forcing, constant independent Poisson reset rate, full instantaneous resetting to the origin and fully renewed increments. It does not model a finite-duration erasure protocol, assign thermodynamic entropy production to an instantaneous reset, analyze continuous-time excursion maxima, prove rates of Gumbel convergence, or cover non-Poisson renewal schedules. The marked Poisson-process step uses a classical limit theorem whose general form is prior methodology. The exact source-level novelty assessment is best-knowledge rather than an independent universal priority certification; general unlocated marked-extremes theorems may encompass related constructions.

## References

1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression* (2026), arXiv:2605.28445v1, first submitted 2026-05-27, https://arxiv.org/abs/2605.28445 .
2. S. Trajanovski and collaborators, *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting* (2023), arXiv:2301.12304v1, https://arxiv.org/abs/2301.12304 .
3. D. Gupta, K. S. Olsen, and S. Krishnamurthy, *Thermodynamic cost of recurrent erasure*, *Communications Physics* (2025), https://www.nature.com/articles/s42005-025-02249-2 .
4. K. S. Olsen, D. Gupta, F. Mori, and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, *Physical Review Research* **6**, 033343 (2024), https://doi.org/10.1103/PhysRevResearch.6.033343 .
5. R. K. Singh and A. Pal, *Extremal statistics for stochastic resetting systems* (2021), arXiv:2102.07111, https://arxiv.org/abs/2102.07111 .
