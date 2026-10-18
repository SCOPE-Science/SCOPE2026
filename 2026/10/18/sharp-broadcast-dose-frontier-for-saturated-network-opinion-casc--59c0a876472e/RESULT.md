# Sharp broadcast-dose frontier for saturated network opinion cascades

## Finding
A nonnegative uniform broadcast stimulus to a homogeneous saturated nonlinear-opinion network has a sharp, **network-independent** minimum total dose for triggering persistent collective activation. Among all finite-duration, nonnegative, measurable broadcast profiles, the successful-dose set is the strict half-line \((D_*,\infty)\), where
\[
D_*=(1+k-a)q+\frac{kq^2}{2}+(k-a)\log(1-q),\qquad
 a=1-\mu-\gamma,\quad q=\frac ak.
\]
The infimum is not a successful dose: the limiting optimal stimulus reaches the unstable activation threshold exactly and stops there. For a rectangular pulse of height \(b\) and duration \(T\), the exact critical duration is
\[
T_b=\int_0^q\max\!\left\{\frac1{1-s},\frac1{b-as+ks^2}\right\}\,ds
\]
when \(b>a^2/(4k)\). Such a pulse succeeds precisely when \(T>T_b\). The rectangular-pulse critical cost \(E(b)=bT_b\) has a **unique** minimizing amplitude \(b_{\mathrm{opt}}\in(\max\{a^2/(4k),1-q\},1)\), and its minimum is strictly greater than \(D_*\). These conclusions hold for every size and every nonnegative row-stochastic interaction matrix, because broadcast stimulation from the zero state remains on the exactly invariant synchronous manifold.

For example, \(\mu=\gamma=1/4\) and \(k=1\) give \(q=1/2\),
\[
D_*=\frac78-\frac{\log 2}{2}=0.528426409720027\ldots,
\]
whereas the unique best rectangular pulse has \(b_{\mathrm{opt}}=0.559923943977420\ldots\), \(T_{b_{\mathrm{opt}}}=0.970283867532391\ldots\), and \(\inf_b E(b)=0.543285169886401\ldots\).

## Assumptions and scope
Fix an integer \(n\ge2\), a nonnegative matrix \(W\in\mathbb R^{n\times n}\) with \(W\mathbf1=\mathbf1\), and constants \(\mu>0\), \(\gamma>0\), \(k\ge1\), satisfying \(\mu+\gamma<1\). The state belongs to \([0,1]^n\). The continuous-time system is
\[
\dot x_i=-x_i+\operatorname{sat}\!\left(\mu x_i+kx_i^2+\gamma\sum_{j=1}^nW_{ij}x_j+u(t)\right),\qquad x_i(0)=0,
\]
where \(\operatorname{sat}(v)=\min\{1,\max\{0,v\}\}\). A broadcast campaign is any bounded, piecewise-continuous input \(u:[0,T]\to[0,\infty)\) for some finite \(T>0\); it vanishes afterward. Its cost is \(D=\int_0^T u(t)\,dt\), counting amplitude per agent rather than multiplying by \(n\). Success means \(x_i(t)\to1\) for **every** node after the campaign. The theorem covers no spatially heterogeneous intervention or heterogeneity in \(\mu\), \(\gamma\), or \(k\).

Let \(a=1-\mu-\gamma\in(0,1)\), \(q=a/k\in(0,1)\), and \(g(s)=as-ks^2\). The minimum sustained-broadcast fold height is \(b_*=a^2/(4k)\). Set \(c(s)=1-s+g(s)\) for \(0\le s\le q\).

## Proof
**1. Exact reduction and post-intervention boundary.** The vector field is Lipschitz on the invariant cube, even though saturation has corners. Because every row of \(W\) sums to one and every initial state and broadcast input is identical, uniqueness of solutions gives \(x_i(t)=s(t)\) for all nodes. Thus
\[
\dot s=-s+\operatorname{sat}((1-a)s+ks^2+u(t)).
\]
For \(s\in[0,q]\), the argument of saturation is nonnegative; hence
\[
\dot s=\min\{1-s,u(t)-g(s)\}.
\]
After switching off the input, for \(0<s<q\) the derivative is \(-g(s)<0\); for \(q<s<1\), the unsaturated derivative is \(-g(s)>0\), while if saturation is active the derivative is \(1-s>0\). Consequently the autonomous outcomes are \(s\to0\) when \(s(T)<q\), \(s\equiv q\) when \(s(T)=q\), and \(s\to1\) when \(s(T)>q\). In particular equality with the unstable threshold is not success.

**2. A pointwise sharp integral bound for arbitrary broadcast profiles.** Define \(\Phi(0)=0\) by
\[
\Phi'(s)=1+\frac{g(s)}{1-s}=\frac{c(s)}{1-s},\qquad 0\le s\le q.
\]
Because \(g(s)\ge0\) on this interval, the inequality
\[
u(t)\ge\Phi'(s(t))\dot s(t)
\]
holds whenever \(s(t)\in[0,q]\). To verify it, first suppose \(u\le c(s)\). Then \(\dot s=u-g(s)\) and the gap on the left equals \(g(s)(c(s)-u)/(1-s)\ge0\). When \(u\ge c(s)\), the derivative is \(1-s\) and the gap equals \(u-c(s)\ge0\). The inequality also permits temporary backward motion and hence needs no monotonicity assumption.

Every successful continuous path crosses \(q\) at a first finite time \(\tau\). Integrating the pointwise bound on \([0,\tau]\) and using the chain rule yields \(\int_0^\tau u(t)\,dt\ge\Phi(q)=D_*\). Since an input-free trajectory starting precisely from \(q\) cannot leave \(q\), every successful path additionally uses a strictly positive input integral after \(\tau\). Thus \(D>D_*\). Polynomial division or differentiation evaluates
\[
\Phi(q)=(1+k-a)q+\frac{kq^2}{2}+(k-a)\log(1-q).
\]
The result is sharp: for \(0\le t\le t_0=-\log(1-q)\), put \(s_*(t)=1-e^{-t}\) and \(u_*(t)=c(s_*(t))\). Then the scalar flow is exactly \(s_*(t)\), the broadcast dose is \(D_*\), and the state at time \(t_0\) is \(q\). Given any \(\varepsilon>0\), extend the pulse by using the constant value \(u=1\) for a duration \(\varepsilon\). This spends exactly \(D_*+\varepsilon\) and puts the state strictly above \(q\). Therefore all and only doses strictly above \(D_*\) can succeed. The shortest time to reach the threshold under any broadcast is \(t_0\), because \(\dot s\le1-s\).

**3. Exact threshold for a rectangular campaign.** With \(u=b\) constant and \(b\le b_*\), the concave function \(g\) reaches \(b_*\) at \(s=q/2\); consequently the scalar trajectory cannot traverse the first point where \(b-g(s)\le0\) and cannot reach \(q\). When \(b>b_*\), the velocity is strictly positive on \([0,q]\), and separation of variables gives the finite, exact crossing time \(T_b\) displayed above. At exactly \(T_b\) the post-campaign state is \(q\); crossing in a longer pulse triggers full activation, and a shorter pulse fails.

**4. Strict convexity and uniqueness of the best rectangle.** For \(b>b_*\) the critical cost can be expressed as
\[
E(b)=\int_0^q\max\left\{\frac{b}{b-g(s)},\frac{b}{1-s}\right\}ds.
\]
The second integrand is affine in \(b\). The first is strictly convex where \(g(s)>0\), since its second derivative is \(2g(s)/(b-g(s))^3>0\). Their maximum is convex, and on any compact interval of amplitudes contained in \((b_*,1)\) the first integrand is active on a positive-length interval of small \(s\), giving *strict* convexity on \((b_*,1)\). As \(b\downarrow b_*\), \(E(b)\to\infty\) because the velocity has a quadratic minimum near \(q/2\). For \(b\ge1\), saturation is active throughout the threshold crossing and \(E(b)=b\log(1/(1-q))\), strictly increasing.

For \(b\in(\max\{b_*,1-q\},1)\), there is a unique switching value \(z_b\in(0,q)\) determined by
\[
(1-a)z_b+kz_b^2=1-b.
\]
The flow is unsaturated on \([0,z_b]\) and saturated on \([z_b,q]\), and differentiation under the integral (boundary terms cancel because both speeds agree at \(z_b\)) gives
\[
E'(b)=-\int_0^{z_b}\frac{g(s)}{(b-g(s))^2}\,ds+\log\frac{1-z_b}{1-q}.
\]
Before this switching range, if it exists, every crossing state is unsaturated and \(E'(b)<0\). In the displayed range \(E'(1^-)=\log(1/(1-q))>0\). Strict convexity and the endpoint behavior therefore prove the existence of exactly one minimizing amplitude \(b_{\mathrm{opt}}\) in that open interval, characterized by \(E'(b_{\mathrm{opt}})=0\).

Finally, equality in the sharp pointwise bound of Step 2 at a progressing interior state \(s\in(0,q)\) requires \(u=c(s)\). But \(c'(s)=-1+a-2ks<0\); no fixed rectangular input can equal the state-dependent optimal value for almost every crossing state. Hence \(E(b)>D_*\) for every finite successful rectangular threshold crossing, including the unique optimal rectangle.

## Verification
The accompanying standalone `verify.py` uses exact symbolic differentiation to check the cost primitive and pointwise calibration identity; high-accuracy quadrature and scalar minimization to check the quoted constants; and numerical integration of an irreducible three-node directed-cycle network to check 10 pulse threshold crossings. Running `python verify.py` with `scipy` and `sympy` produces PASS messages. These numerical tests are corroboration only; universal quantifiers follow from the proof above. Input profiles are bounded piecewise-continuous, so the ODE solution and its crossing time are well-defined.

## Relationship to prior work
Belaustegui et al. (arXiv:2603.29214, 2026; v1 March 31, revised September 14) introduced the clipped, quadratic nonlinear-opinion cascade equation and analyzed thresholds, seed sets, and qualitative responses to time-separated square-wave inputs. Section VI and its conclusion explicitly leave systematic time-varying-input analysis for future work. The present finding studies the *homogeneous zero-initial-state, row-stochastic, uniform-broadcast specialization* and supplies a sharp arbitrary-waveform dose frontier plus a unique constant-pulse optimum, none of which is a statement in the inspected source.

Earlier nonlinear-opinion control papers by Bizyaeva et al. (arXiv:2103.14764) and Franci et al. (arXiv:2103.12223) address centrality, bifurcations, agreement and disagreement, and distributed input to a **different smooth sigmoid with attention feedback**; they do not establish this clipped-quadratic dose identity. Gastaldi, Muscinelli and Gerstner (arXiv:1805.10116) discuss optimal stimulation in a different, two-timescale synaptic consolidation model; the existence of nontrivial optimal stimuli is not claimed new in general. The novelty asserted here is only the exact, globally sharp, model-specific NOD law and rectangle classification.

## Limitations
This is a deterministic, synchronous, uniform-broadcast theorem; it does not establish optimality for heterogeneous graph weights with nonuniform input, local node actuation, arbitrary initial states, stochastic adoption, or competing social groups. The dose counts one broadcast amplitude, not summed per-node expenditure; multiplying by \(n\) converts to a per-node summed cost. The exact value and the strict infimum use an idealized saturated response and no maximum-amplitude cap. The best rectangular pulse gives only an infimum of *successful* rectangular doses because the critical duration itself lands at the unstable threshold. The numerical decimals are approximations, not independent certificates of their final digits.

## References
1. I. X. Belaustegui, H. Sinhmar, L.-W. Kong, A. M. Hein, N. E. Leonard, *A Continuous-Time and State-Space Relaxation of the Linear Threshold Model with Nonlinear Opinion Dynamics*, arXiv:2603.29214v1 (2026-03-31), v2 (2026-09-14), https://arxiv.org/html/2603.29214v2.
2. A. Bizyaeva, T. Sorochkin, A. Franci, N. E. Leonard, *Control of Agreement and Disagreement Cascades with Distributed Inputs*, arXiv:2103.14764 (2021), https://arxiv.org/abs/2103.14764.
3. A. Franci, A. Bizyaeva, S. Park, N. E. Leonard, *Analysis and Control of Agreement and Disagreement Opinion Cascades*, arXiv:2103.12223 (2021), https://arxiv.org/abs/2103.12223.
4. C. Gastaldi, S. P. Muscinelli, W. Gerstner, *Optimal Stimulation Protocol in a Bistable Synaptic Consolidation Model*, arXiv:1805.10116 (2018), https://arxiv.org/abs/1805.10116.
