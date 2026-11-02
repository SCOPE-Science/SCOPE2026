# Universal weak-confinement entropy-production crossover for reversible Markov propulsion

## Finding
Let \(Y_t\) be any finite-state irreducible reversible continuous-time Markov chain with stationary distribution \(\pi\), started in \(\pi\). A particle with state-dependent real propulsion \(v_{Y_t}\), positive diffusivity \(D\), and harmonic confinement strength \(\kappa>0\) starts from \(X_0=0\):
\[
dX_t=(v_{Y_t}-\kappa X_t)\,dt+\sqrt{2D}\,dB_t.
\]
The Brownian motion and the chain are independent. Put \(u=\sum_i\pi_i v_i\), \(\sigma^2=\sum_i\pi_i(v_i-u)^2\), and \(W=\int_0^\infty\operatorname{Cov}(v_{Y_t},v_{Y_0})\,dt\). Reversibility and irreducibility imply \(0\le W<\infty\).

Define the instantaneous **full joint-state even-orientation entropy-production rate** \(\Pi_\kappa(t)\) as in the next section. For every fixed \(0<a<b<\infty\),
\[
\boxed{\lim_{\kappa\downarrow0}\ \kappa\int_{a/\kappa}^{b/\kappa}\Pi_\kappa(t)\,dt
=\frac{\sigma^2}{D}(b-a)+\frac{u^2}{2D}(e^{-2a}-e^{-2b}).}
\]
Moreover, for every \(\kappa>0\), the absolute difference from this limit is at most
\[
\boxed{\kappa\left\{\frac{(b-a)(2W+D)}{D}
+\frac12\log\!\left[\frac{D+W}{D(1-e^{-2a})}\right]\right\}.}
\]
Thus the finite-time macroscopic crossover across weak confinement has a universal \(e^{-2s}\) drift-memory profile, even for non-symmetric two-state propulsion, and depends on the chain's rates only through the explicit error bound. The claim concerns **scaled observation-window averages**, not a pointwise limit of \(\Pi_\kappa(s/\kappa)\).

## Assumptions and scope
Let \(I\) be a finite set and \(Q=(q_{ij})\) an irreducible generator with \(\pi_iq_{ij}=\pi_jq_{ji}\), \(\pi_i>0\), and \(q_{ii}=-\sum_{j\ne i}q_{ij}\). Fix any finite real values \(v_i\), \(D>0\), and \(\kappa>0\); Brownian noise and the stationary chain are independent. Write \(p_i(x,t)\) for the joint density of \(X_t=x\) and \(Y_t=i\) and
\[
J_i(x,t)=(v_i-\kappa x)p_i(x,t)-D\partial_xp_i(x,t).
\]
At every positive time these densities are smooth and positive. Set
\[
\begin{aligned}
\Pi_\kappa(t)&=\sum_i\int_{\mathbb R}\frac{J_i(x,t)^2}{D p_i(x,t)}\,dx\\
&\quad+\sum_{\substack{i<j\\q_{ij}>0}}\int_{\mathbb R}
(q_{ij}p_i-q_{ji}p_j)\log\frac{q_{ij}p_i}{q_{ji}p_j}\,dx.
\end{aligned}
\]
The second sum is over unordered edges, and each term is nonnegative. Reversible internal switches are treated as even under time reversal, following the joint-density entropy-production convention of Paoluzzi--Puglisi--Angelani (2024). This definition does **not** assert a unique physical entropy production under alternative parity conventions for internal velocities. The initial spatial position is fixed at zero; translation of this fixed position does not alter the leading theorem, but is not needed here.

For the physical two-heading run-and-tumble particle with \(v_R>0\), \(v_L>0\), actual velocities \(v_R,-v_L\), and heading-flip rates \(\alpha_R/2,\alpha_L/2\), one has
\[
\begin{aligned}
u&=\frac{\alpha_Lv_R-\alpha_Rv_L}{\alpha_R+\alpha_L},\\
\sigma^2&=\frac{\alpha_R\alpha_L(v_R+v_L)^2}{(\alpha_R+\alpha_L)^2},\\
W&=\frac{2\sigma^2}{\alpha_R+\alpha_L},\qquad \kappa=\mu k.
\end{aligned}
\]
Consequently the result directly quantifies the transient singularity of the free versus harmonically confined anisotropic model in arXiv:2404.16955v1.

## Proof
**1. Entropy balance.** The Fokker--Planck equations are
\[
\partial_t p_i=-\partial_xJ_i+\sum_{j\ne i}(q_{ji}p_j-q_{ij}p_i).
\]
Let \(S_\kappa(t)=-\sum_i\int p_i\log p_i\,dx\). Integration by parts yields the usual diffusion entropy production and flux. The jump entropy derivative is
\[
\sum_{i<j}\int(q_{ij}p_i-q_{ji}p_j)\log\frac{p_i}{p_j}\,dx.
\]
Its difference from the jump term in \(\Pi_\kappa\) is a sum of \(\log(q_{ij}/q_{ji})\) multiplied by integrated edge currents. Each integrated edge current vanishes individually: \(\int p_i\,dx=\pi_i\) for all times and \(\pi_iq_{ij}=\pi_jq_{ji}\). Hence, with
\[
\Phi_\kappa(t)=\frac1D\sum_i\int(v_i-\kappa x)J_i(x,t)\,dx,
\]
one has the **exact** identity \(S_\kappa'(t)=\Pi_\kappa(t)-\Phi_\kappa(t)\) for every \(t>0\). The positive-time Gaussian convolution supplies the requisite integrability and integration-by-parts boundary conditions.

**2. Exact flux and covariance.** Integration by parts, using the linear drift derivative \(-\kappa\), gives
\[
D\Phi_\kappa(t)=\mathbb E[(v_{Y_t}-\kappa X_t)^2]-\kappa D.
\]
Let \(C(s)=\operatorname{Cov}(v_{Y_s},v_{Y_0})\). The finite reversible generator is self-adjoint in \(L^2(\pi)\) and has positive nonzero relaxation rates \(\lambda_\ell\), so
\[
C(s)=\sum_\ell c_\ell e^{-\lambda_\ell s},\qquad
c_\ell\ge0,\quad \sum_\ell c_\ell=\sigma^2,\quad
W=\sum_\ell c_\ell/\lambda_\ell.
\]
The stochastic convolution is
\[
X_t=\int_0^t e^{-\kappa(t-s)}v_{Y_s}\,ds
+\sqrt{2D}\int_0^t e^{-\kappa(t-s)}\,dB_s.
\]
Thus
\[
\begin{aligned}
\mathbb E[X_t]&=\frac{u}{\kappa}(1-e^{-\kappa t}),\\
R_\kappa(t)&:=\operatorname{Cov}(v_{Y_t},X_t)
=\int_0^t e^{-\kappa s}C(s)\,ds\in[0,W],\\
V_\kappa'(t)&=-2\kappa V_\kappa(t)+2R_\kappa(t)+2D,
\end{aligned}
\]
where \(V_\kappa(t)=\operatorname{Var}(X_t)\), \(V_\kappa(0)=0\). In particular
\(0\le V_\kappa(t)\le(D+W)/\kappa\). Substitution and expansion of the squared drift yield
\[
D\Phi_\kappa(t)=\sigma^2+u^2e^{-2\kappa t}
+\kappa^2V_\kappa(t)-2\kappa R_\kappa(t)-\kappa D.
\]
Since the three residual terms have a nonnegative first term and two nonpositive terms,
\[
\left|\Phi_\kappa(t)-\frac{\sigma^2+u^2e^{-2\kappa t}}{D}\right|
\le\frac{\kappa(2W+D)}{D}.
\]
This bound is uniform in \(t\ge0\).

**3. Uniform entropy endpoint bound.** The internal chain has entropy \(H(\pi)\) at every time. Write \(X_t=A_t+G_t\), where the Brownian convolution \(G_t\), independent of \((A_t,Y_t)\), is centered Gaussian with variance \(D(1-e^{-2\kappa t})/\kappa\). Conditional mutual-information nonnegativity implies
\[
S_\kappa(t)=H(\pi)+h(X_t\mid Y_t)
\ge H(\pi)+\frac12\log\frac{2\pi eD(1-e^{-2\kappa t})}{\kappa}.
\]
On the other hand, conditioning reduces entropy and the centered Gaussian maximizes entropy at fixed variance:
\[
S_\kappa(t)\le H(\pi)+h(X_t)
\le H(\pi)+\frac12\log\frac{2\pi e(D+W)}{\kappa}.
\]
For every \(t\in[a/\kappa,b/\kappa]\), these inequalities confine \(S_\kappa(t)\) to an interval of width
\[
B_a=\frac12\log\frac{D+W}{D(1-e^{-2a})}.
\]
In particular \(\left|S_\kappa(b/\kappa)-S_\kappa(a/\kappa)\right|\le B_a\).

**4. Integration and limit.** Integrate \(\Pi_\kappa=S_\kappa'+\Phi_\kappa\) between the two observation times and multiply by \(\kappa\). The entropy endpoints contribute at most \(\kappa B_a\). The uniform flux estimate contributes at most \(\kappa(b-a)(2W+D)/D\). Finally
\[
\kappa\int_{a/\kappa}^{b/\kappa}\frac{\sigma^2+u^2e^{-2\kappa t}}D\,dt
=\frac{\sigma^2}{D}(b-a)+\frac{u^2}{2D}(e^{-2a}-e^{-2b}).
\]
These three identities prove the quantitative inequality and its limit, without exchanging unjustified limits under the entropy-production integral.

## Verification
The included standalone Python file `verify.py` runs with the standard library. It verifies exact moment and flux formulas for an asymmetric two-state chain, a symmetric three-state chain with two relaxation modes, a constant drift, and a zero-mean propulsion case; checks the finite-\(\kappa\) uniform flux estimate and integrated moment limits; and compares an independently simulated switching-and-Brownian path ensemble with the exact flux. These are finite diagnostics, not a numerical proof of the entropy-production limit. The proof of the latter is the analytic entropy balance and the uniform entropy-endpoint bound above.

The exact stationary fixed-\(\kappa\) consequence is
\[
\Pi_{\kappa,\mathrm{st}}=\Phi_{\kappa,\mathrm{st}}
=\frac1D\sum_\ell\frac{c_\ell\lambda_\ell}{\kappa+\lambda_\ell},
\]
while the direct free-particle limiting flux is \((\sigma^2+u^2)/D\). Therefore the difference in stationary free and weakly trapped rates is \(u^2/D\), in agreement with the cited anisotropic two-state model. This is a consistency check, not an additional independent novelty claim.

## Relationship to prior work
Paoluzzi, Puglisi and Angelani (arXiv:2404.16955v1, equations (72) and (75)) compute exact **stationary** entropy-production rates and point out that the free and weakly trapped limits differ in asymmetric run-and-tumble dynamics. Their work does not establish the scaled finite-time window limit, its universal exponential memory term, the explicit uniform finite-\(\kappa\) error, or the reversible multistate extension proved here. García-Millán and Pruessner (arXiv:2012.02900v1) develop RTP field theory, time-dependent correlators and stationary entropy-production calculations, but not the claimed window-averaged weak-confinement asymptotic. Bao and Hou (arXiv:2211.15973v1) study thermodynamic uncertainty bounds for run-and-tumble entropy production, not this harmonic-confinement crossover.

The argument uses standard Gaussian entropy bounds, reversible-chain spectral calculus and the entropy balance. Those are established tools; novelty is asserted only for their exact combination in the specified transient singular-limit question. Broader general theorems on entropy-production boundary layers or homogenized active systems could subsume this application and remain a priority risk.

## Limitations
The theorem assumes fixed finite reversible internal dynamics, stationary initial heading, positive thermal diffusivity, a linear harmonic force, and observation windows bounded away from the initial time in scaled units. It proves the integrated macroscopic crossover, not a pointwise instantaneous entropy-production limit, a uniform statement at scaled time zero, a result for nonreversible internal cycles, position-dependent switches, or physical odd-parity reversal conventions. It does not independently validate the mathematical result or demonstrate experimentally realizable heat dissipation beyond the defined entropy-production convention.

## References
1. M. Paoluzzi, A. Puglisi and L. Angelani, *Entropy production of run-and-tumble particles*, arXiv:2404.16955v1 (first public version April 25, 2024), https://arxiv.org/html/2404.16955v1 .
2. R. García-Millán and G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900v1 (2020), https://arxiv.org/abs/2012.02900 .
3. X. Bao and C. Hou, *Improving estimation of entropy production rate for run-and-tumble particle systems by high-order thermodynamic uncertainty relation*, arXiv:2211.15973v1 (2022), https://arxiv.org/abs/2211.15973 .
4. G. Pruessner and R. García-Millán, *Field theories of active particle systems and their entropy production*, arXiv:2211.11906v2 (2025 revision of a November 21, 2022 preprint), https://arxiv.org/html/2211.11906v2 . Its general entropy-production formalism does not itself specify this weak-confinement time-window limit.
