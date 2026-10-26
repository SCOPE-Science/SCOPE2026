# A sharp critical-gain phase diagram for quadratic adaptive SIS recovery

## Finding
Consider a single well-mixed susceptible–infected–susceptible population whose recovery-rate multiplier increases with the square of the infected fraction:
\[
\dot x=x\bigl[\beta(1-x)-\delta g\bigr],\qquad
\dot g=\alpha x^2.
\]
Suppose \(\beta>\delta>0\), \(\alpha>0\), \(x(0)=x_0\in(0,1]\), and \(g(0)=g_0\in[1,\beta/\delta)\). The limiting multiplier \(g_\infty\) always exists and the infection always vanishes, but eradication may be either critically slow or exponential. Define
\[
y_0=\beta/\delta-g_0>0,\quad z_0=x_0/y_0,\quad
\Delta=\beta^2-4\alpha\delta.
\]
The **exact phase diagram** is:

* If \(\Delta<0\), then \(g_\infty>\beta/\delta\) for **every** admissible \(x_0,g_0\).
* If \(\Delta\ge0\), put \(z_+=(\beta+\sqrt\Delta)/(2\alpha)\). Then
  \[
  g_\infty=\beta/\delta\quad\Longleftrightarrow\quad z_0\le z_+;
  \qquad g_\infty>\beta/\delta\quad\Longleftrightarrow\quad z_0>z_+.
  \]
  Equality \(z_0=z_+\) belongs to the critical (not exponentially decaying) regime.

For every critical trajectory, set
\[
z_\infty=\begin{cases}
(\beta-\sqrt\Delta)/(2\alpha),&\Delta>0,\ z_0<z_+,\\
 z_+,&\Delta>0,\ z_0=z_+,\\
\beta/(2\alpha),&\Delta=0,\ z_0\le z_+.
\end{cases}
\]
Then the sharp physical-time laws are
\[
\lim_{t\to\infty}t\,x(t)=\frac1{\alpha z_\infty},\qquad
\lim_{t\to\infty}t\,\bigl(\beta/\delta-g(t)\bigr)=\frac1{\alpha z_\infty^2}.
\]
For every strictly overcontrolled trajectory, \(g_\infty>\beta/\delta\) and
\[
\lim_{t\to\infty}\frac{\log x(t)}t=\beta-\delta g_\infty<0.
\]
Thus the sharp adaptation-rate boundary separating **possible** critical control from **universal** exponential decay is \(\alpha=\beta^2/(4\delta)\), with an additional exact initial-burden separatrix below and at this boundary. The frozen-control limiting reproduction number equals \(\beta/(\delta g_\infty)\), so it is exactly one in the critical region and strictly below one otherwise.

## Assumptions and scope
The model is an autonomous deterministic single-population SIS equation with mass-action incidence, positive baseline infection and recovery parameters, monotonically increasing multiplicative recovery gain, and quadratic prevalence-based adaptation (the exponent-two member of the recovery-gain family). The control gain is initialized below the disease-free static threshold, with \(g_0\ge1\); \(x_0=0\) is excluded because no control would activate. All asymptotic statements are for physical continuous time \(t\to\infty\). The statement does not concern finite-population stochastic extinction, arbitrary graph structures, or infection-rate (as opposed to recovery-rate) adaptation.

## Proof
**1. Global feasibility and extinction.** The infected interval \([0,1]\) is positively invariant since \(\dot x=0\) at \(x=0\) and \(\dot x=-\delta g<0\) at \(x=1\). Positivity of \(x_0\) gives \(x(t)>0\) at all finite times; \(g\) increases. There is no finite-time blow-up because \(\dot g\le\alpha\). If \(g\) tended to infinity, after \(g\ge2\beta/\delta\) one would have \(\dot x\le-\beta x\), making \(\int x^2dt\) finite thereafter, contrary to \(\dot g=\alpha x^2\). Hence \(g\) has a finite limit \(g_\infty\). In consequence \(\int_0^\infty x^2dt<\infty\); the uniformly bounded derivative of \(x\) then implies \(x(t)\to0\). The logarithmic equation \(\dot x/x=\beta-\delta g-\beta x\) rules out \(g_\infty<\beta/\delta\).

**2. Exact homogeneous reduction.** While \(g<\beta/\delta\), introduce \(y=\beta/\delta-g>0\). The equations become the **homogeneous quadratic system**
\[
\dot x=x(\delta y-\beta x),\qquad\dot y=-\alpha x^2.
\]
Write \(z=x/y>0\) and reparametrize by \(\tau(t)=\int_0^t y(s)\,ds\), as long as \(y>0\). Direct differentiation gives
\[
\frac{dz}{d\tau}=zQ(z),\qquad
\frac{dy}{d\tau}=-\alpha z^2y,\qquad
\frac{d\log x}{d\tau}=\delta-\beta z,
\quad Q(z)=\delta-\beta z+\alpha z^2.
\]
The one-dimensional projective equation contains the entire phase decision; its positive roots exist exactly when \(\Delta\ge0\). If \(\Delta>0\) the roots are \(z_-<z_+\), and the sign of \(zQ(z)\) is positive below \(z_-\), negative between them, and positive above \(z_+\). If \(\Delta=0\) the double root is \(z_+=z_-=\beta/(2\alpha)\), with positive projective drift except at that root. If \(\Delta<0\), the drift is positive everywhere.

**3. Bounded projective trajectories are exactly critical.** For \(\Delta>0\), every \(0<z_0<z_+\) converges to \(z_-\) in projective time, whereas \(z_0=z_+\) stays fixed. For \(\Delta=0\), every \(0<z_0\le z_+\) converges to the double root. In all these cases \(z\) stays between positive constants. Because \(\dot y=-\alpha z^2y^2\),
\[
\frac1{y(t)}=\frac1{y_0}+\alpha\int_0^t z(s)^2\,ds.
\]
Consequently \(y(t)\to0\), so \(g_\infty=\beta/\delta\). Moreover \(y(t)\) is comparable to \(1/t\), implying \(\tau(t)\to\infty\), consistently with the projective limit. Cesàro averaging yields \(t y(t)\to1/(\alpha z_\infty^2)\), and \(x=zy\) yields \(t x(t)\to1/(\alpha z_\infty)\).

**4. Unbounded projective trajectories cross the threshold at a finite time.** The remaining cases are \(\Delta<0\) (every \(z_0>0\)), or \(\Delta\ge0\) with \(z_0>z_+\). There \(Q(z)>0\) for every \(z\ge z_0\) and \(Q(z)\sim\alpha z^2\). The projective explosion time satisfies
\[
\tau_* = \int_{z_0}^{\infty}\frac{du}{uQ(u)}<\infty.
\]
But the physical infection does not disappear as \(z\to\infty\): using the third equation in Step 2,
\[
\log\frac{x_*}{x_0}
=\int_{z_0}^{\infty}\frac{\delta-\beta u}{uQ(u)}\,du
\]
converges to a finite real number. Hence \(x_*>0\), \(y=x/z\to0\), and even physical threshold-crossing time is finite because
\[
t_* =\int_{z_0}^{\infty}\frac{du}{x(u)Q(u)}<\infty,
\]
with integrand asymptotic to \(1/(\alpha x_*u^2)\). At \(t_*\), \(x(t_*)=x_*>0\) and \(g(t_*)=\beta/\delta\), so \(\dot g(t_*)>0\). The gain therefore passes strictly above the threshold and stays there. Thus \(g_\infty>\beta/\delta\); Step 1 gives \(x\to0\), and the Cesàro limit of \(\dot{\log x}\) proves the stated negative exponential rate.

**5. Boundary and exact examples.** When \(\Delta\ge0\) and \(z_0=z_+\), the invariant ray \(x=z_+ y\) has the exact solution
\[
y(t)=\frac{y_0}{1+\alpha z_+^2 y_0t},\quad
x(t)=z_+ y(t),\quad g(t)=\beta/\delta-y(t),
\]
showing directly that the equality case remains critical. For \(\beta=2,\delta=\alpha=1,\ x_0=g_0=1\), this reduces to \(x(t)=1/(1+t)\), \(g(t)=2-1/(1+t)\).

A single **same-parameter, different-initial-burden** witness takes \(\beta=11/10\), \(\delta=1\), \(\alpha=1/5\), \(g_0=1\). Here \(\Delta=41/100\), \(z_+=(11+\sqrt{41})/4\) and \(y_0=1/10\). Initial infection \(x_0=1/5\) gives \(z_0=2<z_+\), hence exactly critical \(g_\infty=11/10\). Initial infection \(x_0=3/5\) gives \(z_0=6>z_+\), hence strictly overcontrolled \(g_\infty>11/10\). At the same baseline rates, increasing \(\alpha\) to \(2/5\) makes \(\Delta=-39/100<0\), guaranteeing strict overcontrol at every positive initial infection. All inequalities are exact.

## Verification
The complete standalone `verify.py` uses only the Python standard library. It independently checks the projective derivative identities on an exact-rational grid, the exact invariant-ray solution, the exact side inequalities for the stated witness parameters, and integrates the original two-variable system (fourth-order Runge–Kutta) for the critical and overcontrolled witnesses. It reports 300,228 passing checks with critical trajectory \(x(10000)\approx0.00043165954\), \(g(10000)\approx1.09962439\), and distinct strictly supercritical final recovery multipliers near \(1.11595853\) and \(1.10525871\) in the two overcontrolled examples. Numerics confirm illustrative behavior only; Steps 1–5 constitute the infinite-time proof. Reproduce using `python verify.py` in the directory containing this result and the script.

## Relationship to prior work
Walsh, Ye, Anderson, and Sun introduced both adaptive infection-rate and adaptive recovery-rate SIS network controllers. Their 26 May 2023 publicly accessible preprint, equations (17)–(20), Theorem 3, and surrounding discussion establish disease elimination and finite limiting recovery gains; they do not give this exact quadratic recovery-control critical/subcritical phase diagram or the sharp initial-condition separatrix. Their Proposition 3 addresses the corresponding strict spectral margin for **linear** (power-one) infection-rate feedback. The later open-access journal presentation (2025) discusses the parameter exponent and explicitly identifies finer rate analysis for exponents above one as a research direction. The known global-eradication result is not claimed as new here: the new object is the exact division of limiting spectral margins and physical-time decay regimes within the recovery-controller specialization. The projective substitution is elementary phase-plane theory; the scientific contribution is its exact application to a natural controller and complete parameter/initial-state classification.

## Limitations
The finding does not classify arbitrary networks, mixed feedback exponents, exponents other than two, stochastic epidemics, delayed/discrete updates, or nonautonomous intervention. An equilibrium multiplier exactly at the static threshold still eradicates infection asymptotically but not exponentially; the critical cases do **not** provide a strictly subcritical frozen reproduction ratio. No absolute publication-priority certification is claimed; related closed-form classifications might exist under different adaptive-control terminology. The 2025 journal open-access PDF was not machine-readable in this investigation, but its relevant indexed text and the accessible 2023 full-length source were examined.

## References
1. L. Walsh, M. Ye, B. D. O. Anderson and Z. Sun, *Decentralised adaptive-gain control for eliminating epidemic spreading on networks*, arXiv:2305.16658v1 (first submitted 26 May 2023), particularly Sections 2.2, 3.2, and 3.3: https://arxiv.org/html/2305.16658v1 .
2. L. Walsh, M. Ye, B. D. O. Anderson and Z. Sun, *Decentralised adaptive-gain control for eliminating epidemic spreading on networks*, Automatica **174** (2025), 112143, doi:10.1016/j.automatica.2025.112143. Publication information and relevant indexed text: https://research.tue.nl/en/publications/decentralised-adaptive-gain-control-for-eliminating-epidemic-spre/ .
