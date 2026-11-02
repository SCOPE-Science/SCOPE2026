# Exact global regret identity for renewal resetting in reversible diffusion

## Finding

A complete squared-ratio identity upgrades the conjugate-launch stationarity principle for stochastic resetting to a **global optimality theorem**, with an explicit nonnegative loss and uniqueness at the level of hitting profiles. It holds for every continuously differentiable confining potential on a finite interval and for every pair of independent, identically distributed positive reset waiting-time laws with finite means. In particular, this proves a global optimality assertion for the entire infinite-dimensional class of renewal clocks, rather than only for competing Poisson clocks or a selected parametric family.

Let \(f_p\) be the no-reset probability of hitting an absorbing endpoint before an independent reset time drawn from a reference law \(p\). The conjugate spatial launch density is

\[
 w_p(x)=\frac{m(x)f_p(x)^2}{Z_p},\qquad m(x)=e^{-V(x)/D},\qquad Z_p=\int_0^L m(x)f_p(x)^2\,dx.
\]

For any other reset-clock law \(q\), put \(h(x)=f_q(x)/f_p(x)\). With the positive, symmetric killed Green kernel

\[
 K_V(x,y)=\frac1D\int_0^{\min(x,y)}e^{V(z)/D}\,dz,
\]

the exact difference between the spatially averaged mean first-passage times is

\[
 \boxed{\mathcal R_p(q)-\mathcal R_p(p)=\frac1{2Z_p}\int_0^L\!\int_0^L K_V(x,y)m(x)m(y)f_p(x)f_p(y)\frac{(h(x)-h(y))^2}{h(x)h(y)}\,dx\,dy\ge0.}
\]

Equality holds precisely when \(f_q=f_p\) everywhere. No assertion is made that the two clock laws must then coincide. The same expression is bounded below by replacing the squared ratio by \((\log h(x)-\log h(y))^2\), giving a quantitative stability inequality.

## Assumptions and scope

Fix \(D,L>0\) and \(V\in C^2([0,L])\), not necessarily convex. Consider the killed, reflected diffusion with generator \(\mathcal L=D\partial_x^2-V'(x)\partial_x\), absorbing at \(x=0\) and reflecting at \(x=L\). The reference potential is arbitrary, including nonlinear traps and biasing forces. Let \(H_x\) denote its first hitting time of zero from \(x\in(0,L]\), with \(H_0=0\). For each reset-clock distribution \(q\), assume \(\tau_q\in(0,\infty)\) almost surely, \(0<\mathbb E\tau_q<\infty\), and the waiting times are independent of the diffusion and resampled independently after each unsuccessful attempt. Each restart returns the particle to its original, fixed, sampled position \(x\); a new launch site is **not** drawn after every reset. The expectation defining \(\mathcal R_p(q)\) is over the launch location sampled once according to \(w_p\).

Define

\[
 f_q(x)=\mathbb P(H_x<\tau_q),\qquad a_q(x)=\mathbb E[\min(H_x,\tau_q)],\qquad T_q(x)=\frac{a_q(x)}{f_q(x)},\qquad \mathcal R_p(q)=\int_0^L w_p(x)T_q(x)\,dx.
\]

The equality event \(H_x=\tau_q\) has probability zero for \(x>0\), including deterministic waiting times; hence the strict inequality convention does not affect the result. The function \(f_q\) is continuous and strictly positive throughout the closed interval, including \(f_q(0)=1\). Therefore the risk integrals are finite for all allowed clocks on this finite interval.

## Proof

**1. Restart renewal identity.** At fixed \(x\), one attempt lasts \(\min(H_x,\tau_q)\). Its success probability is \(f_q(x)>0\). Summing the successive independent failures gives the exact restarted mean \(T_q(x)=a_q(x)/f_q(x)\). This holds for arbitrary probability laws on positive reset times, with or without densities.

**2. Green representation.** Let \(P_t\) be the diffusion semigroup killed on hitting zero and reflected at \(L\). Write \(P_t1(x)=\mathbb P(H_x>t)\). Fubini and the finite mean give

\[
 a_q=\mathbb E\int_0^{\tau_q}P_t1\,dt,\qquad f_q=\mathbb E(1-P_{\tau_q}1).
\]

The generator identity \(\mathcal L\int_0^t P_s1\,ds=P_t1-1\), first for each \(t>0\) and then by bounded-domain regularity/approximation for general \(q\), yields \(-\mathcal La_q=f_q\) in the interior, with \(a_q(0)=0\) and \(a_q'(L)=0\). Solving the one-dimensional divergence-form equation

\[
 -\mathcal La=-D e^{V(x)/D}\frac{d}{dx}\left(e^{-V(x)/D}a'(x)\right)=f_q
\]

and applying the mixed boundary conditions gives

\[
 a_q(x)=\int_0^L K_V(x,y)m(y)f_q(y)\,dy.
\]

The kernel \(K_V\) is symmetric and strictly positive whenever both arguments are positive, regardless of whether \(V\) is monotone.

**3. Exact symmetrization.** By the preceding identity,

\[
 \mathcal R_p(q)=\frac1{Z_p}\int_0^L\!\int_0^L K_V(x,y)m(x)m(y)f_p(x)f_p(y)\frac{h(y)}{h(x)}\,dy\,dx.
\]

For \(q=p\), the final ratio is one. Symmetry of \(K_V(x,y)m(x)m(y)f_p(x)f_p(y)\) allows the difference to be averaged with its \(x\leftrightarrow y\) transpose. Because

\[
 \frac12\left(\frac{h(y)}{h(x)}+\frac{h(x)}{h(y)}-2\right)=\frac{(h(x)-h(y))^2}{2h(x)h(y)},
\]

the stated identity follows. Its integrand is nonnegative, proving global minimality without any second-variation or parametric assumption.

**4. Equality and quantitative separation.** Strict positivity of the kernel on \((0,L]^2\) forces \(h(x)=h(y)\) for almost every pair when the gap vanishes. Continuity makes \(h\) constant on \([0,L]\), and the common hitting boundary value \(f_q(0)=f_p(0)=1\) sets the constant to one. Conversely \(f_q=f_p\) makes the gap zero. Finally, for \(u,v>0\),

\[
 \frac{(u-v)^2}{uv}=2\bigl(\cosh(\log u-\log v)-1\bigr)\ge(\log u-\log v)^2,
\]

which proves the weighted squared-log-ratio lower bound.

**5. Explicit biased-diffusion benchmark.** Suppose \(V(x)=vx\) with \(v\ge0\), and choose a Poisson reference clock of rate \(r>0\). Let \(\delta=v/(2D)\) and \(\gamma=\sqrt{\delta^2+r/D}\). Direct solution of \(Df''-vf'=rf\), with \(f(0)=1\) and \(f'(L)=0\), gives

\[
 f_r(x)=\frac{e^{\delta x}\left[\cosh(\gamma(L-x))+(\delta/\gamma)\sinh(\gamma(L-x))\right]}{\cosh(\gamma L)+(\delta/\gamma)\sinh(\gamma L)}.
\]

Thus \(w_r\) is proportional to the square of the bracketed expression, with no residual exponential prefactor; the optimization theorem applies to every competitor clock at this explicit launch distribution. The same method applies to arbitrary \(C^2\) potentials without needing a closed expression for \(f_r\).

As an additional half-line corollary, for inward constant drift \(-v\) with \(v>0\), absorption at zero and natural behavior at infinity, a Poisson reference clock produces

\[
 f_r(x)=e^{-a_r x},\quad a_r=\frac{\sqrt{v^2+4Dr}-v}{2D},\quad w_r(x)=\lambda e^{-\lambda x},\quad \lambda=\frac{\sqrt{v^2+4Dr}}D.
\]

For an exponential launch density with rate \(\lambda>v/D\), the unique matching Poisson rate \(r_*=\frac{D^2\lambda^2-v^2}{4D}\) minimizes the spatially averaged mean over **all** positive finite-mean renewal clocks, and the minimum equals \(4D/(D\lambda+v)^2\). The proof uses the half-line Green kernel \(K_v(x,y)=[e^{v\min(x,y)/D}-1]/v\), its symmetric speed-measure representation, and Tonelli; for a competitor with infinite averaged mean the inequality is immediate. For a competitor with finite mean, the preceding symmetrization applies by truncation/monotone convergence to the nonnegative squared-ratio integrand.

## Verification

The complete `CHECK.py` file is included. It tests the identity using 66 exact-rational reversible birth-death chains with absorbing and reflecting endpoints, including nonuniform masses, conductances and two competing exponential clocks. It separately evaluates the continuous constant-force case by 801-node numerical quadrature and Poisson hitting transforms (four parameter configurations), and verifies an exact symbolic factorization of the half-line Poisson regret. It passed 479 deterministic assertions. These finite tests corroborate but do not replace the analytic proof.

For the reflecting example \(D=0.8\), \(v=0.5\), \(L=2\), and Poisson rates \(r=1.3\) and \(s=0.6\), the integrated means are approximately \(\mathcal R_r(r)=0.43398180014\) and \(\mathcal R_r(s)=0.44575937977\), with strictly positive difference \(0.01177757964\).

## Relationship to prior work

Evans and Ray (arXiv:2410.01941v1, October 2, 2024) introduced the conjugate-target formula for free diffusion \(P_T^*\propto f_p^2\), established functional stationarity, and supplied numerical minimization evidence for selected protocol families. Their original article explicitly distinguishes stationarity from global minimization (main text around its equation (16) and Figure 2), and names diffusion in a potential as a future direction. The finding here credits that formula and develops a separate global squared-ratio identity, a strict profile-equality criterion, and a weighted potential-generalization. The May 2025 revision and 2025 journal publication were checked for stronger coverage of those specific points.

Earlier resetting work, including Evans and Majumdar (arXiv:1107.4225) and Ray, Mondal and Reuveni (arXiv:1811.08239), studies resetting rates, search sites or drift-diffusion first passage. Those works are not treated as claiming the global all-clock positive regret identity. Related self-adjoint Green-kernel principles may provide an equivalent general mathematical formulation; absence of a matching indexed statement does not establish historical priority.

## Limitations

The result is mathematical, not a claim of experimentally implemented optimization. It is one-dimensional, reversible, time-homogeneous, and assumes complete renewal to the same launch position on each failed attempt. The potential is \(C^2\), thermal diffusion is strictly positive, and the target is an absorbing endpoint with reflection at the other boundary (or inward drift and a natural half-line boundary in the explicit corollary). It does not cover changing launch locations after every reset, state-dependent reset clocks, active nonreversible propulsion, or arbitrary higher-dimensional domains. Optimality is unique in the probability-of-success **profile**, not necessarily in the clock distribution itself. The half-line extension has a finite-risk qualification for the gap identity; infinite-risk competitors are handled by the inequality alone. Novelty is a qualified literature comparison, not independent certification.

## References

1. M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941v1 (public October 2, 2024), https://arxiv.org/html/2410.01941v1. Subsequent arXiv:2410.01941v2 (2025), https://arxiv.org/html/2410.01941v2; *Physical Review Letters* **134**, 247102 (2025), https://doi.org/10.1103/2wpq-gl2j.
2. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, arXiv:1107.4225 (2011), https://arxiv.org/abs/1107.4225.
3. S. Ray, D. Mondal and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239 (2018), https://arxiv.org/abs/1811.08239.
