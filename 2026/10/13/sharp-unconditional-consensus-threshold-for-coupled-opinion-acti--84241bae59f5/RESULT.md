# Sharp unconditional consensus threshold for coupled opinion–action averaging

## Finding

**Theorem (a sharp worst-case confidence threshold).** Fix an integer \(n\ge2\), a decision weight \(0<\phi<1\), and a confidence radius \(\varepsilon\in[0,1]\). For arbitrary initial opinions and actions \(x_i(0),y_i(0)\in[0,1]\), let
\[
D_0=\max_i\{x_i(0),y_i(0)\}-\min_i\{x_i(0),y_i(0)\}.
\]
In the opinion–action coevolution system (1)–(2) below, if
\[
\boxed{\;2\varepsilon\ge(1+\phi)D_0\;},
\]
then every opinion and action converges to **one common limit**. Moreover, unless \(D_0=0\), all confidence neighborhoods become complete after a finite time, and convergence is then exponential. No prior assumption that the interaction graph eventually stabilizes is needed.

The bound is sharp **uniformly over all finite population sizes**: for every \(0<\phi<1\), every \(0<d\le1\), and every \(\varepsilon<(1+\phi)d/2\) (with \(\varepsilon\ge0\)), a two-person stationary nonconsensus state has initial joint diameter exactly \(d\). In particular, for initial data in \([0,1]\), the exact worst-case population-independent threshold is \(\varepsilon=(1+\phi)/2\), with equality included.

## Assumptions and scope

The population has \(n\ge2\) agents with *private opinion* \(x_i(t)\in[0,1]\) and *public action* \(y_i(t)\in[0,1]\) at integer times \(t\ge0\). The agents are potential neighbors of every other agent, but an observation qualifies only when opinion and public action lie within the homogeneous confidence radius. More precisely, define
\[
N_i(t)=\{j\ne i:|x_i(t)-y_j(t)|\le\varepsilon\},\qquad k_i(t)=|N_i(t)|.
\]
Updates are sequential within each time step:
\[
\begin{aligned}
x_i(t+1)&=\frac{x_i(t)+\sum_{j\in N_i(t)}y_j(t)}{1+k_i(t)},\\
y_i(t+1)&=\phi x_i(t+1)+(1-\phi)\overline y(t),\\
\overline y(t)&=\frac1n\sum_{j=1}^ny_j(t).
\end{aligned}\tag{1–2}
\]
The self-opinion in the first equation is always included; self-action is excluded from \(N_i(t)\). Equality is accepted in the confidence test. No randomness, heterogeneous weights, restricted social graph, or extra time delays are assumed. The strict inequalities \(0<\phi<1\) are essential to the proof.

## Proof

**1. A stochastic map and nested envelopes.** Write \(z(t)=(x_1(t),\ldots,x_n(t),y_1(t),\ldots,y_n(t))\). Equations (1–2) give \(z(t+1)=P(t)z(t)\), where \(P(t)\) is a nonnegative row-stochastic \(2n\times2n\) matrix. If \(k_i=k_i(t)\), its opinion row has coefficient \(1/(k_i+1)\) at \(x_i\) and coefficient \(1/(k_i+1)\) at each eligible \(y_j\). Its action row is \(\phi\) times that opinion row plus coefficient \((1-\phi)/n\) at **every** action coordinate. Every nonzero coefficient of \(P(t)\) is at least
\[
\eta=\frac{\min\{\phi,1-\phi\}}n>0.
\]
In particular, \(m_t=\min_j z_j(t)\) is nondecreasing, \(M_t=\max_j z_j(t)\) is nonincreasing, and \(D_t=M_t-m_t\downarrow D_\infty\ge0\). Write \(m=\lim m_t\), \(M=\lim M_t\), so \(D_\infty=M-m\le D_0\).

**2. Every action stays strictly within any persistent envelope.** For any two successive matrices \(P(t+1)P(t)\), **every action row has all \(2n\) entries at least \(\eta^2\)**. Indeed, each old opinion \(x_j(t)\) enters action \(y_j(t+1)\) with weight \(\phi/(1+k_j(t))\ge\eta\), and every old action enters every action at the next step with weight at least \((1-\phi)/n\ge\eta\). An old action enters every intermediate action with the same lower bound. Hence, for each \(i\) and every \(t\),
\[
m_t+\eta^2 D_t\le y_i(t+2)\le M_t-\eta^2D_t.\tag{3}
\]
If \(D_\infty>0\), (3) gives a constant \(\delta>0\) and a time \(T\) such that all \(t\ge T\) and all \(i\) satisfy
\[
m+\delta\le y_i(t)\le M-\delta.\tag{4}
\]
This conclusion does **not** require any graph stabilization.

**3. Persistent extreme opinions become permanent isolated leaders.** Assume \(D_\infty>0\). Make \(T\) larger, if necessary, so \(M_t\le M+\delta/4\) and \(m_t\ge m-\delta/4\) for \(t\ge T\). If opinion \(i\) has any neighbor at some \(t\ge T\), its updated value, using (4) and \(k_i(t)\ge1\), is at most
\[
\frac{M+\delta/4+k_i(t)(M-\delta)}{1+k_i(t)}\le M-\delta/4.
\]
All later opinion values remain \(\le M-\delta/4\), because subsequent updates use only that opinion and actions bounded by \(M-\delta\). The symmetrical argument says an opinion that is updated at a late time subsequently remains \(\ge m+\delta/4\). Consequently, any opinion with \(\limsup_{t\to\infty}x_i(t)=M\), or \(\liminf_{t\to\infty}x_i(t)=m\), must be isolated at every sufficiently late step and therefore must equal its respective endpoint forever. Since (4) keeps all actions away from both endpoints, the extreme coordinates defining \(m_t,M_t\), for arbitrarily large \(t\), must be opinion coordinates. Finiteness of \(n\) supplies *distinct* agents \(a,b\) with
\[
x_a(t)=m,\quad x_b(t)=M,\quad N_a(t)=N_b(t)=\varnothing
\qquad(t\ge T_1).
\]

**4. Two isolated extremes are incompatible with the threshold.** Put \(B_t=\overline y(t)\). Since \(m_t\le B_t\le M_t\), any accumulation value of \(B_t\) lies in \([m,M]\). For all sufficiently large \(t\), the action identities give
\[
y_b(t)=\phi M+(1-\phi)B_{t-1}>m,\qquad
y_a(t)=\phi m+(1-\phi)B_{t-1}<M.
\]
Because \(a\) and \(b\) remain isolated and are distinct, each of these cross-actions is excluded from the corresponding neighborhood:
\[
y_b(t)-m>\varepsilon,\qquad M-y_a(t)>\varepsilon.
\]
Adding yields the **exact identity and strict obstruction**
\[
2\varepsilon <[y_b(t)-m]+[M-y_a(t)]=(1+\phi)(M-m)\le(1+\phi)D_0.
\]
This contradicts \(2\varepsilon\ge(1+\phi)D_0\). Therefore \(D_\infty=0\), and the monotone envelopes force every coordinate to converge to the common value \(m=M\).

**5. Finite complete-neighborhood onset and exponential convergence.** If \(D_0>0\) under the displayed threshold, then \(\varepsilon>0\). Since \(D_t\to0\), some finite \(T_2\) has \(D_{T_2}<\varepsilon\). Every pair \(x_i(t),y_j(t)\) then satisfies the confidence test for all \(t\ge T_2\). The matrix becomes the fixed complete-neighborhood matrix \(P_*\). Every entry of \(P_*^2\) is at least \(\eta^2\): to reach any action, go through an intermediate action; to reach an opinion, go through that opinion's own self-loop or, for a different action, through any eligible intermediate action. Because \(n\ge2\), the latter route always exists. Thus the stochastic-matrix diameter bound yields
\[
D_{t+2}\le (1-2n\eta^2)D_t\qquad(t\ge T_2),\tag{5}
\]
with \(0<1-2n\eta^2<1\). This proves eventual geometric convergence.

**6. Exact sharpness.** Fix \(d\in(0,1]\) and \(a\in[0,1-d]\). For \(n=2\), define
\[
(x_1,x_2)=(a,a+d),\qquad
(y_1,y_2)=\left(a+\frac{1-\phi}{2}d,\ a+\frac{1+\phi}{2}d\right).
\]
Both cross confidence distances equal \((1+\phi)d/2\). If \(\varepsilon<(1+\phi)d/2\), both neighborhoods are empty, both opinions remain fixed, and the action rule reproduces the displayed two actions because their mean equals \(a+d/2\). This is a stationary polarized configuration with initial joint diameter \(d\), excluding any smaller universal threshold. At equality the cross-links are included; the obstruction no longer applies. This finishes the proof.

## Verification

The included `verify.py` constructs the **undelayed** exact one-step stochastic matrix with rational arithmetic. It checks all neighbor masks for two and three agents (including all ordered pairs of masks in the two-step action-row test), verifies the positive two-step action-row lower bound, and checks exact stationary two-agent sharpness below the threshold versus activation at equality. One hundred bounded floating-point trajectories supply independent numerical diagnostics. Run `python verify.py`; expected output begins `VERIFY_OK`. The infinite-time theorem relies on the proof, not the finite computations.

## Relationship to prior work

Song, Fontan, Su, Hendrickx, Cvetkovic and Johansson [1] analyze exactly equations (1–2), including their finite-graph-state matrix and the cases with isolated agents. Their Theorem 3 assumes that strongly connected components stabilize in finite time. Their Remark 4 states that such stabilization is unproved, and their conclusion explicitly asks for a threshold in the confidence and decision parameters. The present result supplies a **sharp universal worst-case threshold** and, above it, proves both convergence and subsequent complete-neighborhood stabilization directly. It does **not** claim the exact consensus-versus-clustering phase boundary for every fixed distribution, network variant, or finite population size.

The earlier model paper [2] introduces opinion–action interaction and explores parameter dependence, but its reported sensitivity analysis is not a proof of the present worst-case bound. Classical Hegselmann–Krause stabilization and consensus results [3] concern updates against **other opinions** rather than this model's dynamically mixed public actions, so they do not yield equation (3) or the sharp threshold directly. General stochastic-matrix arguments provide familiar ingredients; the cross-action obstruction and its sharp realization are model-specific.

## Limitations

The threshold is necessary and sufficient for a **uniform guarantee across all finite population sizes and all initial configurations with prescribed joint diameter**. It need not be necessary for any particular trajectory or fixed size \(n>2\). The proof assumes all potential interpersonal contacts are available before applying the confidence filter, homogeneous \(\varepsilon\) and \(\phi\), deterministic synchronous updates, the precise sequential opinion-then-action rule, and \(0<\phi<1\). The limiting consensus value and pre-asymptotic time to complete connectivity are not explicit. No population-independent exponential rate from time zero is claimed. The result does not address \(\phi=0\), \(\phi=1\), heterogeneous parameters, graph-restricted contacts, or stochastic observations.

## References

1. C. Song, A. Fontan, R. Su, J. M. Hendrickx, V. Cvetkovic, K. H. Johansson, *On the Convergence of an Opinion–Action Coevolution Model with Bounded Confidence*, arXiv:2604.06140v1, publicly submitted 7 April 2026; https://arxiv.org/html/2604.06140v1. Relevant material: equations (3)–(5), Theorem 3, Remarks 4–5, and conclusion.
2. C. Song, V. Cvetkovic, R. Su, *Why Do Opinions and Actions Diverge? A Dynamic Framework to Explore the Impact of Subjective Norms*, IEEE Transactions on Computational Social Systems, doi:10.1109/TCSS.2025.3598697; model introduction and numerical sensitivity investigation.
3. V. D. Blondel, J. M. Hendrickx, J. N. Tsitsiklis, *On Krause's Multi-Agent Consensus Model with State-Dependent Connectivity*, IEEE Transactions on Automatic Control 54 (2009), 2586–2597; classical opinion-only bounded-confidence model.
