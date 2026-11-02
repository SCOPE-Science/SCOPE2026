# Sharp reachable covariance intervals and single-switch optimal noise-color control

## Finding
For a harmonically confined particle driven by an active Ornstein–Uhlenbeck bath of constant instantaneous force variance, bounded control of the bath's correlation rate gives an **exact interval** of achievable terminal position variances at each observation horizon, conditional on reaching a prescribed position–bath cross-covariance. Its endpoints are attained by two opposite single-switch protocols. Consequently, steering between any two distinct stationary Gaussian states corresponding to *interior* admissible bath rates has a finite minimum duration; the unique minimum-time protocol, up to equality almost everywhere, uses the slower bath rate followed by the faster rate when the target cross-covariance increases, and the reverse order when it decreases. The result is global over all measurable bounded protocols, not an optimization within a chosen polynomial or smooth family.

## Assumptions and scope
Fix a trap relaxation rate \(a>0\), coupling \(v>0\), thermal diffusivity \(D\ge0\), and two bounded active-bath decay rates \(0<u_-<u_+\). For independent Brownian motions \(W\) and \(B\), consider the centered Gaussian process
\[
 dX_t=(-aX_t+vY_t)\,dt+\sqrt{2D}\,dW_t,\qquad
 dY_t=-u(t)Y_t\,dt+\sqrt{2u(t)}\,dB_t.
\]
The measurable deterministic control satisfies \(u_-\le u(t)\le u_+\) almost everywhere. Two distinct initial and final *interior* rates \(u_i,u_f\in(u_-,u_+)\) prescribe the stationary initial Gaussian law and the desired stationary final Gaussian law. There are no restrictions on derivatives or total variation of the control, and instantaneous changes are permitted. The active bath's one-time variance is identically one, while its temporal correlation decay rate changes. Only one particle in one spatial dimension and a fixed harmonic trap are considered.

Let \(z(t)=\mathbb E[X_tY_t]\) and \(s(t)=\mathbb E[X_t^2]\). Put
\[
 k_\pm=a+u_\pm,\quad m_\pm=\frac v{k_\pm},\quad
 z_i=\frac v{a+u_i},\quad z_f=\frac v{a+u_f},\quad
 s_i=\frac Da+\frac va z_i,\quad s_f=\frac Da+\frac va z_f.
\]
Thus \(0<m_+<z_i,z_f<m_-\). For a horizon \(T>0\) define
\[
 f_\pm(t)=m_\pm+(z_i-m_\pm)e^{-k_\pm t},\qquad
 b_\pm(t)=m_\pm+(z_f-m_\pm)e^{k_\pm(T-t)}.
\]
The smallest time when the cross-covariance alone can reach \(z_f\) is
\[
 T_z=-\frac1{a+u_*}\log\left(\frac{z_f-v/(a+u_*)}{z_i-v/(a+u_*)}\right),\qquad
 u_*=\begin{cases}u_-,&z_f>z_i,\\u_+,&z_f<z_i.\end{cases}
\]
The logarithm is of a number in \((0,1)\), so \(T_z>0\).

For every \(T\ge T_z\), define two explicit envelopes
\[
 z_{\rm lo}(t)=\max\{f_+(t),b_-(t)\},\qquad
 z_{\rm hi}(t)=\min\{f_-(t),b_+(t)\},\qquad 0\le t\le T.
\]
Each maximum/minimum has exactly one crossing, interpreted as an endpoint switch at \(T=T_z\) when appropriate. In \(z_{\rm hi}\), run \(u_-\) until the crossing \(f_-=b_+\), then \(u_+\); in \(z_{\rm lo}\), run \(u_+\) until \(f_+=b_-\), then \(u_-\). Set
\[
 S_{\rm lo/hi}(T)=\frac Da+e^{-2aT}\left(s_i-\frac Da\right)
   +2v\int_0^T e^{-2a(T-t)}z_{\rm lo/hi}(t)\,dt.
\]

**Theorem (complete finite-horizon terminal-variance interval).** For every \(T\ge T_z\), the set of \(s(T)\) achievable by all measurable rate controls with \(z(T)=z_f\) is exactly the closed interval
\[
 \boxed{[S_{\rm lo}(T),\ S_{\rm hi}(T)].}
\]
For \(0\le T<T_z\) the target cross-covariance is unreachable. In particular, the entire prescribed terminal Gaussian law is achievable exactly when
\[
 S_{\rm lo}(T)\le s_f\le S_{\rm hi}(T).
\]
For \(z_f>z_i\), one always has \(S_{\rm lo}(T)<s_f\), and the minimum time \(T_*\) is the first \(T\ge T_z\) for which \(S_{\rm hi}(T)=s_f\). For \(z_f<z_i\), one always has \(S_{\rm hi}(T)>s_f\), and \(T_*\) is the first \(T\ge T_z\) for which \(S_{\rm lo}(T)=s_f\). In either case \(T_z<T_*<\infty\), the switching time lies strictly inside \((0,T_*)\), and the optimal control is unique up to modifications on null sets. The first equality is a rigorous sharp global speed-limit characterization; no claim is made that later exact return times form a single interval.

## Proof
**1. Exact moment closure and positivity.** Itô's formula and independence of the two noises yield
\[
 (\mathbb E[Y_t^2])'=2u(t)(1-\mathbb E[Y_t^2]),\quad
 z'=v-(a+u(t))z,\quad
 s'=-2as+2vz+2D.
\]
The stationary initial law has \(\mathbb E[Y_0^2]=1\); hence this moment remains exactly one even during a varying control. The variation-of-constants formula for \(z\) shows \(z(t)>0\) for every finite \(t\). The stationary expressions in the assumptions follow by setting derivatives equal to zero. The joint law remains centered Gaussian, so specifying \((s,z,1)\) specifies the complete joint Gaussian law, not merely a positional marginal.

**2. Forward and backward scalar order bounds.** As \(u_-\le u\le u_+\) and \(z>0\), comparison for the scalar equation gives
\[
 f_+(t)\le z(t)\le f_-(t).
\]
Applying the same comparison backwards from \(z(T)=z_f\) (or its variation-of-constants formula in reverse time) gives
\[
 b_-(t)\le z(t)\le b_+(t).
\]
Therefore \(z_{\rm lo}\le z\le z_{\rm hi}\) pointwise. Forward bounds at time \(T\) show that \(z(T)=z_f\) is possible if and only if \(T\ge T_z\): the earliest feasible path uses the extremal rate \(u_*\) throughout. When \(T\ge T_z\), the function \(f_-\) is strictly increasing and \(b_+\) strictly decreasing, while \(f_+\) is strictly decreasing and \(b_-\) strictly increasing. Each pair crosses exactly once. Their piecewise assembly is a valid solution with the claimed two rate segments, initial condition \(z_i\), and terminal condition \(z_f\). Thus both pointwise bounds are **attained** by admissible controls.

**3. Exact interval rather than only bounds.** Variation of constants in the \(s\)-equation gives exactly
\[
 s(T)=\frac Da+e^{-2aT}\left(s_i-\frac Da\right)
 +2v\int_0^T e^{-2a(T-t)}z(t)\,dt.
\]
Its kernel is strictly positive, so \(S_{\rm lo}\le s(T)\le S_{\rm hi}\). Conversely fix \(\theta\in[0,1]\) and interpolate the two extremal trajectories as \(z_\theta=(1-\theta)z_{\rm lo}+\theta z_{\rm hi}>0\). If \(u_{\rm lo}\) and \(u_{\rm hi}\) are their piecewise constant controls, set
\[
 u_\theta(t)=\frac{(1-\theta)u_{\rm lo}(t)z_{\rm lo}(t)
    +\theta u_{\rm hi}(t)z_{\rm hi}(t)}{z_\theta(t)}.
\]
This is a positive-weighted average, hence remains in \([u_-,u_+]\); direct substitution gives \(z_\theta'=v-(a+u_\theta)z_\theta\). It has the required endpoints and produces terminal position variance \((1-\theta)S_{\rm lo}+\theta S_{\rm hi}\). This proves exact reachability of every point in the interval.

**4. Strict gap at the cross-covariance-only minimum.** If \(z_i<z_f\), the upper extremal path at \(T_z\) is the constant \(u_-\) trajectory, which stays strictly below \(z_f\) until its endpoint. Since \(s_i<s_f\), solving \((s-s_f)'=-2a(s-s_f)+2v(z-z_f)\) shows \(S_{\rm hi}(T_z)<s_f\). If \(z_i>z_f\), the analogous \(u_+\) trajectory remains strictly above \(z_f\), so \(S_{\rm lo}(T_z)>s_f\).

**5. Guaranteed finite crossing and global optimality.** Suppose \(z_i<z_f\). The lower envelope first decreases under \(u_+\) and finally increases under \(u_-\) toward \(z_f\); it remains strictly below \(z_f\) throughout \([0,T)\). With \(s_i<s_f\) this yields \(S_{\rm lo}(T)<s_f\) for all feasible horizons. For the upper envelope, as \(T\to\infty\), the initial \(u_-\) phase grows indefinitely while the final \(u_+\) phase converges to a finite positive duration
\[
 \delta_+=\frac1{k_+}\log\left(\frac{m_--m_+}{z_f-m_+}\right)>0.
\]
Throughout that last phase the limiting \(z\)-trajectory lies strictly **above** \(z_f\) before returning to \(z_f\), and the initial \(s\)-value of that phase approaches \(D/a+vm_-/a>s_f\). Hence \(\lim_{T\to\infty}S_{\rm hi}(T)>s_f\). By continuity, at least one finite crossing exists, and the *first* such crossing is exactly the earliest achievable complete Gaussian steady-state transfer because of the exact reachable interval. The opposite case \(z_i>z_f\) is symmetric: the upper envelope always stays strictly above \(z_f\), and the lower envelope's final \(u_-\) segment begins asymptotically from \(z=m_+<z_f\), giving a large-time lower variance strictly below \(s_f\). This proves existence and the claimed correct switching order.

**6. Uniqueness almost everywhere at optimum.** At the earliest crossing in either direction, the target value is an endpoint of the exact variance interval. Since the position-variance integral has a strictly positive kernel and all feasible \(z\) are pointwise bounded by the extremal path, equality of terminal variance forces equality of the entire continuous cross-covariance trajectories. Their controls are then determined almost everywhere by the identity \(u(t)=[v-z'(t)]/z(t)-a\), valid since \(z(t)>0\). Hence each fastest control is unique up to null sets.

## Verification
A standalone standard-library Python checker (`verify.py`) accompanies this statement. It computes both envelope switches and terminal variances from the explicit constant-rate propagator, brackets the first full-transfer time in either direction, verifies closed-form and independent Runge–Kutta propagation agree for sample parameters, checks cross-covariance reachability, and runs deterministic randomized parameter trials. The generated results for \((a,v,D,u_-,u_+)=(1,1,0.2,0.1,5)\) are:

- Increasing target covariance (\(u_i=3\) to \(u_f=0.4\)): \(T_z\approx1.108055833\), \(T_*\approx1.734596902\), optimal switch \(\approx1.708160286\), rate order \(0.1\to5\).
- Decreasing target covariance (\(u_i=0.4\) to \(u_f=3\)): \(T_z\approx0.313788541\), \(T_*\approx1.196165821\), optimal switch \(\approx1.088905551\), rate order \(5\to0.1\).

These numerical tests do not replace the scalar comparison and interpolation proof. The exact optimal switching times are specified by unique intersection equations and the first terminal-variance equality, not by floating-point numbers.

## Relationship to prior work
Boriskovsky et al. (2026) introduce the noise-color-controlled active Ornstein–Uhlenbeck bath and inverse-engineer finite-time transfers by prescribing moment trajectories. Their abstract specifically reports physical speed constraints and optimization of admissible times within a family of chosen trajectories, establishing important prior art for the model and the control objective. The claim here is confined to **the exact full reachable terminal-variance interval for all bounded measurable rate controls**, its pointwise extremizers, and the corresponding global minimum-time one-switch characterization. It does not claim invention of finite-time active-bath engineering, the Gaussian moment equations, or bang–bang control principles in general. Meibohm et al. study optimal protocols for a different stochastic-control cost; Li, Cheng and Tu use an auxiliary potential rather than bounded noise-color control. A general bilinear-system reachability theorem may subsume the proof technique, but the model-specific two-moment interval and transfer-time formulas were not located by the stated searches.

## Limitations
The motivating article's complete text and supplemental material could not be inspected, despite attempts through its preprint and lawful open-access mirrors; the accessible abstract does discuss minimizing an admissible transition time, making possible hidden overlap the principal publication-priority risk. The comparison is a qualified best-knowledge assessment, not proof of novelty, and the reader should examine the full article before public priority assertions. No result is claimed for derivative-bounded or smooth controls, fluctuating-temperature protocols, additional harmonic dimensions, nonlinear confinement, or independent optimization of thermodynamic work. The source model may use an alternative noise normalization; the present result applies **exactly** to the stated constant-unit-active-variance SDE. External mathematical review and publication-priority auditing have not been performed.

## References
1. D. Boriskovsky, S. Dago, C. Genet, R. Goerlich, V. Hardel, P.-A. Hervieux, H. L. F. Ip, G. Manfredi and L. Mertz, *Controlling transitions between nonequilibrium states through active bath engineering*, arXiv:2610.11831v1 (first publicly submitted 8 October 2026), https://arxiv.org/abs/2610.11831 .
2. G. Li, G. Cheng and Z. C. Tu, *Shortcuts to state transitions for active matter*, arXiv:2604.05585 (2026), https://arxiv.org/abs/2604.05585 .
3. J. Meibohm, S. Monter, C. Bechinger and S. A. M. Loos, *Equivalence classes of finite-time transitions in optimal control and non-equilibrium relaxation*, arXiv:2609.03862 (2026), https://arxiv.org/abs/2609.03862 .
4. P. R. Zulkowski, D. A. Sivak and M. R. DeWeese, *Optimal control of transitions between nonequilibrium steady states*, arXiv:1303.6596 (2013), https://arxiv.org/abs/1303.6596 .
