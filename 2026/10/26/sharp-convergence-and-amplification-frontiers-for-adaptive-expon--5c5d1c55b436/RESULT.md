# Sharp convergence and amplification frontiers for adaptive exponential Gaussian inference

## Finding

For the exact one-dimensional Gaussian-target exponential integrator specified below, let \(H>0\) denote the maximum time step and \(\beta>0\) the adaptive step cap. The complete global convergence frontier for the **coupled mean and covariance** is
\[
\boxed{0<H<2,\qquad \beta>0.}
\]
In this entire region, every initial normalized covariance \(s_0>0\) and mean error \(v_0\in\mathbb R\) converge to \((s,v)=(1,0)\), eventually at a geometric rate. The cap need not satisfy \(\beta\le1\). At \(H=2\) every positive covariance still converges to one, but the coupled method is not globally convergent: \(s_0=1\) and \(v_0\ne0\) give \(v_n=(-1)^n v_0\). For \(H>2\), even the exact covariance state \(s_0=1\) yields unbounded mean errors when \(v_0\ne0\).

Independently, the **sharp one-step mean nonexpansivity condition**, uniform over all \(s>0\), is
\[
\boxed{H+\beta\le2.}
\]
The exact worst-state mean-error multiplier is
\[
\sup_{s>0}\left|1-s\min\!\left(H,\frac{\beta}{|s-1|}\right)\right|
=\max\{1,H+\beta-1\},
\]
with the time-step at \(s=1\) defined to be \(H\). The upper endpoint \(H+\beta\) of the dimensionless gain \(hs\) is attained at \(s=1+\beta/H\). Thus \(H+\beta>2\) permits genuine transient amplification even when \(H<2\) guarantees eventual convergence.

At the critical cap \(H=2\), every covariance trajectory not reaching \(s=1\) at finite time has the universal rate
\[
\boxed{\lim_{n\to\infty}\sqrt n\,|\log s_n|=\frac{\sqrt3}{2}.}
\]
If additionally \(v_0\ne0\) and no finite mean multiplier vanishes, its mean satisfies \(|v_n|\sim C n^{-3/2}\) with a finite \(C>0\). If a covariance trajectory reaches \(s=1\), the mean subsequently alternates at constant magnitude (or remains zero). Such finite capture occurs, for example, from \(s_0=e^\beta\) when \(H=2\).

## Assumptions and scope

Consider a normalized univariate Gaussian target with mean zero and variance one, exact evaluation of Gaussian expectations, and deterministic arithmetic. For every integer \(n\ge0\), start from arbitrary \(s_0>0\) and \(v_0\in\mathbb R\), set
\[
 h_n=\begin{cases}
 H,&s_n=1,\\
 \min\{H,\beta/|s_n-1|\},&s_n\ne1,
 \end{cases}
 \qquad s_{n+1}=s_n e^{h_n(1-s_n)},\qquad
 v_{n+1}=(1-h_n s_n)v_n.
\]
These are the scalar specialization of the covariance and normalized-mean recursions in Che et al., equations (12)–(14), with a constant scheduler. \(H\) and \(\beta\) are fixed positive real parameters. Every statement is about these deterministic scalar recursions; no Gaussian mixture interaction, Monte Carlo error, floating-point underflow, or matrix-valued covariance is assumed.

## Proof

**Step 1: bounded log dynamics.** Put \(u=\log s\). The covariance update is the continuous map
\[
 g(u)=u-q(u),\qquad
 q(u)=\begin{cases}
 \min\{H(e^u-1),\beta\},&u\ge0,\\
 -\min\{H(1-e^u),\beta\},&u<0.
 \end{cases}
\]
The sole fixed point is \(u=0\). For \(u>0\), \(-\beta\le g(u)<u\); for \(u<0\), \(u<g(u)\le u+H\). Consequently, for every starting \(u_0\) the closed interval
\[
 [\min\{u_0,-\beta\},\max\{u_0,H\}]
\]
is forward invariant, so the orbit is bounded.

**Step 2: exclude all nontrivial two-cycles for \(0<H\le2\).** A two-cycle cannot lie entirely in \((0,\infty)\) or entirely in \(( -\infty,0)\), because the map moves strictly toward the origin on each respective side. A nontrivial two-cycle must therefore consist of \(u>0>v\), with \(\delta=u-v>0\) and \(q(u)=\delta=-q(v)\). Since
\[
 \delta\le H(e^u-1),\qquad
 \delta\le H(1-e^v)<H,
\]
we have
\[
 u\ge\log(1+\delta/H),\qquad
 v\le\log(1-\delta/H).
\]
It follows that
\[
 \delta=u-v\ge\log\frac{1+\delta/H}{1-\delta/H}
 >\frac{2\delta}{H}\ge\delta,
\]
a contradiction. The strict inequality uses \(\operatorname{artanh}(t)>t\) for \(0<t<1\). By the standard interval-iteration theorem of Coppel (a continuous interval self-map with no nonfixed two-cycle has every orbit convergent), the bounded orbit converges to a fixed point. As the only fixed point is zero, \(u_n\to0\), equivalently \(s_n\to1\), for **every** \(\beta>0\) and every \(0<H\le2\).

**Step 3: global mean convergence exactly below two.** Since \(s_n\to1\) and \(\beta>0\), eventually the cap is inactive, so \(h_n=H\). For \(0<H<2\), \(1-h_ns_n\to1-H\in(-1,1)\). Thus \(|v_n|\) decays geometrically from some finite iteration onward, regardless of any earlier amplification. The same local argument gives geometric convergence of \(u_n\) because \(g'(0)=1-H\), whose modulus is below one. For \(H=2\), taking \(s_0=1\) gives \(s_n=1\) and \(v_n=(-1)^n v_0\), which does not converge to zero when \(v_0\ne0\). For \(H>2\), the same initialization gives \(v_n=(1-H)^n v_0\), which diverges in magnitude. This proves the global **if and only if** claim for the coupled system and establishes sharpness without treating bounded numerical experiments as proof.

**Step 4: the independent one-step mean frontier.** Write \(r(s)=s\min\{H,\beta/|s-1|\}\), using \(r(1)=H\). For \(0<s\le1\), \(0<r(s)\le H\). For \(s>1\), the function \(Hs\) increases, whereas \(\beta s/(s-1)\) decreases. Their minimum attains its maximum where they cross, at \(s_*=1+\beta/H\). Hence
\[
 \inf_{s>0}r(s)=0\quad\text{(not attained)},\qquad
 \max_{s>0}r(s)=H+\beta.
\]
Taking the supremum of \(|1-r|\) over that interval yields \(\max\{1,|1-H-\beta|\}=\max\{1,H+\beta-1\}\). Therefore \(|1-r(s)|\le1\) for all positive \(s\) exactly when \(H+\beta\le2\). If \(H+\beta>2\), the explicit state \(s_*\) strictly amplifies every nonzero mean error in one step.

**Step 5: sharp critical rates and finite capture.** At \(H=2\), the cap becomes inactive in a neighborhood of \(u=0\), and the log map has the Taylor expansion
\[
 g(u)=u-2(e^u-1)=-u-u^2-\tfrac13u^3+O(u^4),
\]
so
\[
 g(g(u))=u-\tfrac43u^3+O(u^4).
\]
For an orbit that never hits zero, Step 2 gives \(u_n\to0\). Its even subsequence eventually has a constant nonzero sign, and its reciprocal squared magnitudes satisfy
\[
 u_{2k+2}^{-2}-u_{2k}^{-2}=\tfrac83+O(|u_{2k}|).
\]
This first implies \(|u_{2k}|=\Theta(k^{-1/2})\), then summation sharpens the expansion to
\[
 u_{2k}^2=\frac{3}{8k}+O(k^{-3/2}).
\]
Since \(g(u)=-u+O(u^2)\), the identical leading magnitude holds at odd indices, proving the displayed \(\sqrt n\) limit. Moreover the two-step mean multiplier, as a function of the initial log covariance of the pair, satisfies
\[
 (1-2e^u)(1-2e^{g(u)})=1-4u^2+O(u^3).
\]
Its magnitude therefore equals \(1-\frac{3}{2k}+O(k^{-3/2})\) on late pairs. The logarithm of the product differs from \(-\frac32\log k\) by a convergent correction, proving the claimed positive finite \(n^{-3/2}\) prefactor whenever no finite multiplier vanishes. Finally, for \(s_0=e^\beta\), the adaptive branch satisfies \(h_0=\beta/(e^\beta-1)<2\), whence \(s_1=e^\beta e^{-\beta}=1\). Its first mean multiplier \(1-\beta e^\beta/(e^\beta-1)\) is strictly negative and nonzero. Therefore a nonzero mean enters a persistent two-cycle even though its covariance reaches the target exactly. If any mean multiplier is zero instead, the mean remains identically zero thereafter.

## Verification

Execute `python verify.py` with the standard Python 3 library. The deterministic program checks the sharp gain identity at its maximizing state, one-step inequalities across sample parameters, scalar covariance convergence for a broad parameter grid, joint convergence examples above the prior restrictions, exact critical oscillations and finite covariance capture, the critical \(\sqrt n\) rate, the \(n^{-3/2}\) mean envelope, and local mean divergence beyond the boundary. In the recorded execution the verifier reported `VERIFICATION_OK checks= 1152`. Taylor coefficients of the critical two-step map and mean multiplier were independently expanded symbolically. These finite calculations do not replace the analytic proofs of Steps 1–5.

## Relationship to prior work

Che, Chen, Huang, Mao and Wang [1], equations (12)–(14) and Theorem 1, prove deterministic Gaussian covariance and mean convergence under \(H\le1\) and \(\beta\le1\); the argument uses monotonic decrease of scalar covariance error. The present theorem removes the restriction on \(\beta\), extends the sharp global coupled convergence cap to \(H<2\), classifies the separate one-step damping region \(H+\beta\le2\), and resolves the covariance/mean distinction at the critical boundary. The monotonic-error premise in [1] does not cover the oscillatory regime admitted here.

The constant-parameter one-dimensional Ricker map is known to converge globally up to its classical flip parameter two; Baigent et al. [2], pp. 2–3, discuss that established result as a restriction of their planar model. The present adaptive map agrees locally with that map but contains a state-dependent truncation, so a constant-parameter Ricker theorem does not supply the global statement for arbitrary \(\beta\). The no-two-cycle argument above treats that truncation explicitly. Coppel's interval-iteration theorem [3] is a standard tool, not a claimed innovation. The critical scalar flip expansion is used only in conjunction with the numerical scheme's separate mean recursion, which has the exceptional persistent oscillations described above.

## Limitations

All assertions concern a deterministic, normalized scalar Gaussian target and exact exponential covariance updates. Results do not cover arbitrary matrix covariances, stochastic quadrature, interacting mixture components, finite-precision underflow, or adaptive decay schedules. Uniform transient mean nonexpansivity is stricter than eventual convergence; it cannot be inferred from the latter. The theorem does not assert a novel global-stability law for the classical constant-parameter Ricker map. Historical priority for the complete capped-map and coupled-mean phase diagram is not independently certified.

## References

[1] B. Che, Y. Chen, D. Z. Huang, X. Mao and W. Wang, *Adaptive Exponential Integration for Stable Gaussian Mixture Black-Box Variational Inference*, arXiv:2601.14855 (initial public posting January 21, 2026). https://arxiv.org/abs/2601.14855

[2] S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira and R. Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications 29 (2023), 575–591. doi:10.1080/10236198.2023.2222855. An open-access manuscript is at https://repository.londonmet.ac.uk/8616/.

[3] W. A. Coppel, *The solution of equations by iteration*, Proceedings of the Cambridge Philosophical Society 51 (1955), 41–43. doi:10.1017/S030500410002990X.
