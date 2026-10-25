# Two-target bang–bang resetting: exact bias thresholds and universal discounted optimality

## Finding

Fix \(D>0\), \(r>0\), and \(0<a<L\). An independent, hidden, fixed target \(B\) is \(+L\) with probability \(p\in[0,1]\) and \(-L\) otherwise. A one-dimensional Brownian searcher of diffusivity \(D\) launches at a random point sampled from a freely chosen Borel probability measure \(\mu\) on \([-a,a]\). At the times of an independent rate-\(r\) Poisson process it is instantaneously returned to a new, independent sample from the same \(\mu\); it is absorbed on first reaching the *chosen* target \(B\). The alternate candidate target is not absorbing. Write \(T\) for this time, averaging over the fixed random target and the walk.

**Theorem (complete mean-time optimum).** Set \(c=\sqrt{r/D}\), \(v=e^{ca}\), \(w=e^{-ca}\), \(S=v+w\), and \(h=\sqrt p/(\sqrt p+\sqrt{1-p})\). Among *all* Borel probability laws on \([-a,a]\), the unique minimizer of \(\mathbb ET\) is
\[
\mu_*=(1-\theta_*)\delta_{-a}+\theta_*\delta_{+a},\qquad
\theta_*=\left[\frac{Sh-w}{v-w}\right]_{0}^{1},
\]
where \([z]_0^1=\min\{1,\max\{0,z\}\}\). Let \(p_-=1/(1+e^{4ca})\) and \(p_+=1-p_-\). Then \(\theta_*=0\) exactly when \(p\le p_-\), \(0<\theta_*<1\) exactly when \(p_-<p<p_+\), and \(\theta_*=1\) exactly when \(p\ge p_+\). At both transition values the optimizer is the indicated single endpoint (not a continuum of optima). In the strictly mixed regime,
\[
\min_\mu\mathbb ET=
\frac1r\left(\frac{e^{cL}(\sqrt p+\sqrt{1-p})^2}{S}-1\right).
\]
Outside this regime the same minimum is given by substituting \(\theta_*\) into the exact expression in the proof.

**Theorem (all-discount optimum).** For every \(s>0\), let \(\Phi_\mu(s)=\mathbb E_\mu(e^{-sT})\), \(\lambda=\sqrt{(r+s)/D}\), \(q=e^{-\lambda L}\), \(v_s=e^{\lambda a}\), \(w_s=e^{-\lambda a}\), and \(C_s=2s+rq(v_s+w_s)\). The *unique* maximizer of \(\Phi_\mu(s)\) over the same class is the endpoint law with plus-endpoint mass
\[
\theta_s=\left[\frac{(C_s h-s)/(rq)-w_s}{v_s-w_s}\right]_0^1.
\]
For the symmetric hidden target \(p=1/2\), this simplifies to \(\theta_s=1/2\) for **every** \(s>0\), independent of \(D,r,L,a\). Thus equal endpoint resetting uniquely maximizes all Laplace transforms of the completion time, not merely its mean; this is a Laplace-transform order claim, *not* a claim of ordinary stochastic dominance. The same symmetric endpoint law uniquely minimizes the worst-target mean \(\max\{\mathbb E(T\mid B=+L),\mathbb E(T\mid B=-L)\}\). Relative to resetting to the midpoint, its exact improvement in symmetric-prior mean is \(e^{cL}(1-1/\cosh(ca))/r>0\).

## Assumptions and scope

The Brownian convention is \(dX_t=\sqrt{2D}\,dW_t\) between resets. The hidden target is drawn **once** before the motion and stays fixed throughout all resets; the initial location and every reset location are independent draws from the same design law \(\mu\), independent of the target and Brownian noise. There is no relocation time or relocation cost, and the reset rate \(r\) is fixed during distributional optimization. Endpoints of the relocation interval are admissible, and all probability laws, including point masses and singular laws, are admissible. The strict spatial separation \(a<L\) makes the Brownian single-attempt hitting transforms exponentiate with uniform signs.

## Proof

**1. Renewal identities.** For ordinary Brownian motion started at \(x\), the first-passage time \(\tau_b\) of \(b\) satisfies \(\mathbb E_x(e^{-u\tau_b})=e^{-|b-x|\sqrt{u/D}}\) for \(u>0\). For any \(u>0\), define \(M_+(u)=\int e^{x\sqrt{u/D}}\mu(dx)\) and \(M_-(u)=\int e^{-x\sqrt{u/D}}\mu(dx)\). Conditional on target \(b=\pm L\), the probability an attempt hits before an independent exponential reset is \(F_\pm=e^{-cL}M_\pm(r)>0\). The renewal mean is
\[
\mathbb E(T\mid B=\pm L)=\frac{1-F_\pm}{rF_\pm}
=\frac1r\left(\frac{e^{cL}}{M_\pm(r)}-1\right).
\]
Consequently
\[
\mathbb ET=\frac1r\left[e^{cL}\left(\frac p{M_+(r)}+\frac{1-p}{M_-(r)}\right)-1\right].
\]
For \(s>0\), set \(f_\pm=e^{-\lambda L}\int e^{\pm\lambda x}\mu(dx)\). The first-attempt success contribution to \(\mathbb E(e^{-sT})\) is \(f_\pm\); the first-reset contribution is \(r(1-f_\pm)/(r+s)\). Summing the renewal series gives
\[
\Phi_\mu(s)=p\,g_s(f_+)+(1-p)g_s(f_-),\quad
 g_s(z)=\frac{(r+s)z}{s+rz}.
\]
Here \(g_s'(z)>0\) and \(g_s''(z)=-2(r+s)sr/(s+rz)^3<0\) on positive \(z\).

**2. Endpoint support is globally forced.** For each \(x\in[-a,a]\), put \(\alpha_x=(x+a)/(2a)\). Strict convexity of the exponential gives, simultaneously for either sign and any \(\lambda>0\),
\[
e^{\pm\lambda x}\le (1-\alpha_x)e^{\mp\lambda a}+\alpha_x e^{\pm\lambda a},
\]
with strict inequality at every \(x\in(-a,a)\). Replace \(\mu\) by the endpoint law placing plus-endpoint mass \(\theta=\int\alpha_x\mu(dx)\). Both positive exponential moments weakly increase, and increase strictly if \(\mu((-a,a))>0\). The formulas in step 1 show that any interior mass strictly increases the mean, and strictly lowers every discounted success transform. Hence every optimum for every criterion must be supported on \(\{-a,a\}\). This is global over arbitrary measures; no differentiability or density assumption was made.

**3. Exact optimal endpoint mass.** For the endpoint law, the two moments are \(M_+=w+(v-w)\theta\), \(M_-=v-(v-w)\theta\). Apart from a positive affine factor, the mean objective is
\[
H(\theta)=\frac p{w+(v-w)\theta}+
\frac{1-p}{v-(v-w)\theta}.
\]
It is strictly convex on \([0,1]\): its second derivative is positive for all \(p\in[0,1]\). Its sole unconstrained stationary point, for \(0<p<1\), satisfies \(M_+/M_-=\sqrt{p/(1-p)}\) and is \((Sh-w)/(v-w)\); clipping is therefore the unique constrained optimizer, including \(p=0,1\). The unclipped point enters \([0,1]\) precisely between \(p_-\) and \(p_+\). In this interior range \(M_+=Sh\), \(M_-=S(1-h)\), yielding the displayed exact minimum.

For \(s>0\), define \(f_+(\theta)=q(w_s+(v_s-w_s)\theta)\), \(f_-(\theta)=q(v_s-(v_s-w_s)\theta)\). The discounted objective is strictly concave in \(\theta\) by the strictly negative curvature of \(g_s\). Its first-order equation is \((s+rf_+)/(s+rf_-)=\sqrt{p/(1-p)}\). Solving this linear equation in \(\theta\) and clipping gives \(\theta_s\), uniquely also in degenerate prior limits by monotonicity. When \(p=1/2\), the equation is \(f_+=f_-\), hence \(\theta_s=1/2\) for all \(s>0\). Alternatively, Jensen's inequality and \(f_++f_-\le 2q\cosh(\lambda a)\) prove the same simultaneous optimum directly, with strict equality conditions.

**4. Worst-target and baseline.** With \(p=1/2\), the worst-target mean is \((e^{cL}/\min\{M_+,M_-\}-1)/r\). For arbitrary \(\mu\), \(M_++M_-=2\int\cosh(cx)\mu(dx)\le2\cosh(ca)\), with equality only for laws supported at the endpoints. Hence \(\min\{M_+,M_-\}\le\cosh(ca)\), with equality only when the two endpoint weights are each \(1/2\). This proves unique minimax optimality. At this law both moments equal \(\cosh(ca)\); resetting solely at zero has both moments equal to one, proving the quoted strict improvement.

## Verification

The accompanying standalone `verify.py` can be executed with `python verify.py` using NumPy and SciPy. It cross-checks the closed-form endpoint optimizer against independent scalar optimization for 160 parameter settings, compares endpoint replacements of arbitrary interior laws, checks the transition priors and seven distinct discounts, and performs 40,000 simulations of *exact Brownian first-passage attempts* using the Lévy first-passage law (not a time-discretized Brownian path). An example simulation gave mean \(12.036206\) against predicted \(12.016518\), and discounted success \(0.505020\) against predicted \(0.505490\) for its stated test parameters. These finite checks supplement but are not substitutes for the convexity and renewal proof.

## Relationship to prior work

The general single-target Brownian resetting renewal and resolvent formulas are established by Evans and Majumdar (2011). Their equation-level arbitrary-reset-location formulas imply the renewal starting point here but do not provide the global endpoint-support theorem for an unobserved binary target, its exact prior transitions, unique minimax criterion, or the simultaneous all-discount result. Méndez, Flaquer-Galmés, and Campos (2024, initially public January 2) analyze random reset positions and target-outside-support regimes, optimizing resetting rate or a prescribed interval family for a *fixed target*; the current result instead optimizes over all reset-location probability measures with one hidden binary target. Julián-Salgado, Dagdug, and Boyer (2023) likewise use two resetting points with one fixed target and focus on resetting-rate optimization. García-Valladares, Plata, Prados, and Manacorda (2023) optimize spatial *reset rates* for heterogeneous searches, not the probability law for reset locations. Classical strict convexity and Jensen inequalities are used, not claimed novel. An independently uniform-target graph-resetting result is restricted to finite vertex-transitive graphs and does not imply these continuum binary-target or discounted claims.

## Limitations

The result assumes exact Brownian motion, independent Poisson resets at fixed rate, independent identically distributed launch/reset positions, a target chosen once from two symmetric options, and admissible endpoint point masses. It does not optimize the resetting rate itself, impose relocation costs or entropy constraints, prove ordinary stochastic dominance, or treat a target known to the searcher. The Laplace-transform result is exact only for \(s>0\); the mean is derived separately (and agrees with the limit as \(s\downarrow0\)). Independent scientific validation has not been conducted. Broader equivalence to an as-yet-unidentified theorem in continuous stochastic search cannot be excluded solely by search.

## References

1. V. Méndez, R. Flaquer-Galmés, D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1 (2024-01-02), https://arxiv.org/abs/2401.01125 .
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), https://arxiv.org/abs/1107.4225 .
3. D. Julián-Salgado, L. Dagdug, D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023), https://arxiv.org/abs/2311.11897 .
4. I. García-Valladares, C. A. Plata, A. Prados, A. Manacorda, *Optimal resetting strategies for search processes in heterogeneous environments*, arXiv:2305.14245 (2023), https://arxiv.org/abs/2305.14245 .
