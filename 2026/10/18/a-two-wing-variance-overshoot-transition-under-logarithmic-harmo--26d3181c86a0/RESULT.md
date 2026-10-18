# A two-wing variance-overshoot transition under logarithmic-harmonic resetting

## Finding
Consider a Brownian coordinate in the logarithmic-harmonic potential, independently reset to a fixed positive position at a Poisson rate. The stationary variance of its *squared position* (equivalently, of the harmonic contribution to potential energy) may first **increase** when resetting is introduced, before inevitably decreasing to zero at strong resetting. The complete classification has two distinct reset-location wings when the logarithmic repulsion is sufficiently strong.

Precisely, put
\[
m=\frac{\alpha+D}{\beta},\qquad
q=\frac{r}{2\beta},\qquad
w=\frac{x_0^2}{m},\qquad
\eta=\frac{2D}{\alpha+D}\in(0,2).
\]
The stationary squared-position variance \(V(r)=\operatorname{Var}(X^2)\) satisfies
\[
\boxed{\frac{V(r)}{m^2}=F_{\eta,w}(q)
=\frac{2\eta(1+wq)}{(q+1)(q+2)}
+\frac{(w-1)^2q}{(q+1)^2(q+2)}.}
\]
Define
\[
A=(w-1)^2+\eta(2w-3),\quad
w_{\pm}=1-\eta\pm\sqrt{\eta(1+\eta)}.
\]
For every \(D,\alpha,\beta,x_0>0\):

1. If \(A\le0\), the variance is strictly decreasing for all \(r>0\), starting at its no-reset equilibrium value. There is no variance overshoot.
2. If \(A>0\), the variance initially increases and has exactly one stationary point on \(r>0\), a strict global maximum. Its rate is \(r_*=2\beta q_*\), where \(q_*>0\) is the **unique** positive solution of the cubic equation displayed below.
3. The overshoot region is exactly \(w>w_+\), together with the additional wing \(0<w<w_-\) **if and only if** \(\alpha>5D\). For \(0<\alpha\le5D\), the small-reset-position wing does not exist.

At any positive critical position \(w_c\in\{w_-,w_+\}\), fixing \(\eta\) and approaching from its overshoot side gives the sharp continuous onset
\[
q_*=\frac{A}{B_c}+O(A^2),\qquad
F_{\eta,w}(q_*)-F_{\eta,w}(0)=\frac{A^2}{4B_c}+O(A^3),
\]
where \(B_c=(w_c-1)^2+\eta(5-2w_c)>0\). The physical energy \(\beta X^2/2\) has exactly the same rate-maximizer and overshoot classification.

## Assumptions and scope
Let \(D,\alpha,\beta,x_0>0\). Between resets the positive radial diffusion solves, away from the origin,
\[
dX_t=\left(\frac{\alpha}{X_t}-\beta X_t\right)\,dt+\sqrt{2D}\,dW_t.
\]
At independent exponential times of rate \(r>0\), set \(X_t=x_0\), regardless of the pre-reset state. For the boundary-attainable range \(0<\alpha<D\), use the canonical nonnegative radial/Bessel realization, with instantaneous nonabsorbing behavior at the origin. Equivalently—and without ambiguity at the origin—define \(Z_t=X_t^2\) as the nonnegative mean-reverting square-root diffusion
\[
dZ_t=2(\alpha+D-\beta Z_t)\,dt+2\sqrt{2D Z_t}\,dW_t,
\]
reset to \(z_0=x_0^2\). All variance statements concern the unique stationary law of \(Z\). At \(r=0\) they concern its ordinary equilibrium law. No behavior is asserted for absorbing zero boundaries, arbitrary reset-site distributions, or non-Poisson clocks.

## Proof
**Stationarity and exact moments.** The unreset square-root diffusion is positive recurrent, with its equilibrium gamma law having mean \(m=(\alpha+D)/\beta\) and variance \(2Dm/\beta\). Resetting to \(z_0>0\) at an independent positive rate produces a unique stationary regenerative law: sample an age \(T\sim\operatorname{Exp}(r)\), run the unreset diffusion from \(z_0\) for time \(T\), and observe its value. This law has all polynomial moments. The reset generator is
\[
\mathcal G f(z)=2(\alpha+D-\beta z)f'(z)+4Dz f''(z)+r[f(z_0)-f(z)].
\]
Applying stationary generator balance to \(f(z)=z\) and \(f(z)=z^2\) gives
\[
(2\beta+r)\mathbb EZ=2(\alpha+D)+rz_0,
\qquad(4\beta+r)\mathbb EZ^2=4(\alpha+3D)\mathbb EZ+rz_0^2.
\]
Solving and subtracting the squared mean produces the stated formula for \(F_{\eta,w}(q)\). This derivation uses only the genuine stationary law, not a truncated series or finite experiment. In particular \(F(0)=\eta\), and \(F(q)\to0\) as \(q\to\infty\).

**The cubic and its signs.** Direct differentiation yields
\[
\frac{dF}{dq}=\frac{2P(q)}{(q+1)^3(q+2)^2},\qquad
P(q)=A-Bq-Cq^2-\eta wq^3,
\]
where
\[
A=(w-1)^2+\eta(2w-3),\quad
B=(w-1)^2+\eta(5-2w),\quad
C=(w-1)^2+\eta(w+2).
\]
Here \(C>0\) and \(\eta w>0\). Also \(B>0\): for \(w\le5/2\), both terms in its expression are nonnegative and cannot vanish together; for \(w>5/2\), since \(\eta<2\),
\[
B>(w-1)^2+2(5-2w)=(w-3)^2+2>0.
\]
Consequently \(P\) is strictly decreasing on \([0,\infty)\) and tends to \(-\infty\). If \(A\le0\), then \(P(q)<0\) for every \(q>0\), proving strict decay. If \(A>0\), a unique positive root \(q_*\) exists, and the derivative changes once from positive to negative; hence it is the unique global maximum.

**Two reset-position wings.** The quadratic \(A\), viewed as a function of \(w\), factors as \((w-w_-)(w-w_+)\). The upper root is always strictly positive. The lower root is positive precisely if \(\eta<1/3\), equivalent to \(\alpha>5D\). As \(w>0\), the overshoot condition \(A>0\) is therefore exactly the two stated possibilities. At equality \(A=0\), the derivative at zero vanishes but the derivative is strictly negative at every positive rate.

**Sharp onset.** Fix \(\eta\) and a positive critical root \(w_c\). On its overshoot side, \(A\downarrow0\) while \(B\to B_c>0\) and \(C\) stays finite. The implicit equation \(A-Bq_*-Cq_*^2-\eta wq_*^3=0\) therefore gives \(q_*=A/B_c+O(A^2)\). Expanding the proved derivative uniformly for \(0\le q\le q_*\) and integrating yields the increase \(A^2/(4B_c)+O(A^3)\). This holds only when the critical root lies at a positive reset position; it does not claim the same expansion at the excluded \(x_0=0\) boundary.

## Verification
The supplied `check.py` uses an independent generator-moment evaluation, independent regenerative-age quadrature of the noncentral square-root transition law, exact rational identities for selected parameters, finite-difference derivatives, root-location checks, and exact-transition Monte Carlo sampling. Execution completed successfully with **1,826 assertions**. The all-positive-parameter classification and critical expansion are mathematical consequences of the proof above, not numerical extrapolations. Run `python check.py` with the dependencies listed in `requirements.txt`.

## Relationship to prior work
Gültekin (2023, arXiv:2306.08770) studies this logarithmic-harmonic resetting diffusion and derives a special-function stationary density, identifying qualitative density-shape regimes. The present analysis uses the *same physical model* but asks a different question: global variance response of its squared position to the reset rate. Its exact two-wing overshoot criterion, the new \(\alpha>5D\) distinction for small reset positions, and uniqueness/critical onset of the maximizing rate are not stated in that inspected paper.

Ray and Reuveni (2020, arXiv:2004.01898) analyze diffusion with resetting in the logarithmic potential **without** the added harmonic confinement; their transition concerns absorption and does not imply the present stationary squared-position variance diagram. Pal (2014/2015, arXiv:1408.1230) provides a general framework for diffusion in a potential under resetting; renewal and generator methods are established tools. The square-root/Cox–Ingersoll–Ross moment recursion itself is also classical. The contribution assessed here is the fully evaluated physical variance-overshoot phase diagram rather than the underlying renewal identity or standard CIR moments. Pal's full text was not available for examination; an unrecognized specialization or other equivalent earlier analysis remains a literature-priority risk.

## Limitations
The theorem concerns stationary variance of \(X^2\), not stationary variance of \(X\), fourth cumulants, first-passage times, or a thermodynamic efficiency optimum. In particular, the global **minimum** variance over resetting rates is the unattained strong-reset limit zero; the nontrivial optimum in this theorem is a global **maximum**. For \(0<\alpha<D\), using an absorbing boundary at zero in place of the canonical reflecting radial diffusion changes the model. The criteria rely on a fixed positive reset position and positive parameters, and do not cover non-Poisson or state-dependent resetting. No independent scholarly audit or uniqueness-in-literature certificate has been obtained.

## References
1. Özgür Gültekin, *The steady state distribution for diffusion in a logarithmic-harmonic potential with stochastic resetting*, arXiv:2306.08770, first posted 14 June 2023, https://arxiv.org/abs/2306.08770.
2. Arnab Pal, *Diffusion in a potential landscape with stochastic resetting*, arXiv:1408.1230 (2014); *Physical Review E* **91**, 012113 (2015), https://doi.org/10.1103/PhysRevE.91.012113.
3. Somrita Ray and Shlomi Reuveni, *Diffusion with resetting in a logarithmic potential*, arXiv:2004.01898 (2020), https://arxiv.org/abs/2004.01898. This log-only, non-harmonic model is distinct from the confining model treated here.
4. Cox, Ingersoll and Ross, *A Theory of the Term Structure of Interest Rates*, *Econometrica* **53** (1985), 385–407. Referenced for the classical square-root diffusion family, not for the resetting-variance classification.
