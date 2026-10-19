# Sharp stationary-variance envelope for renewal-reset Brownian forcing in a harmonic trap

## Finding

Let a harmonic particle be driven by a Brownian force that is reset to zero at independent renewal epochs, while the particle position itself is never reset. Fix the force diffusivity \(D>0\), the trapping rate \(\mu>0\), and both the mean \(m>0\) and second moment \(s\ge m^2\) of the positive resetting intervals. Then the variance \(V\) of the **time-stationary** particle position is determined by the Laplace transform of the resetting interval \(T\):

\[
V=\frac{D}{m\mu}\left[\frac{s}{\mu}-\frac{2m}{\mu^2}+\frac{2}{\mu^3}\bigl(1-\mathbb E e^{-\mu T}\bigr)\right]. \tag{1}
\]

For \(s>m^2\), the **complete attainable set** of \(V\) over all laws with \(T>0\) almost surely and the two prescribed moments is exactly the open interval \((V_-,V_+)\), where

\[
V_- = \frac{D}{m\mu}\left[\frac{s}{\mu}-\frac{2m}{\mu^2}+\frac{2m^2}{s\mu^3}\bigl(1-e^{-\mu s/m}\bigr)\right],\tag{2}
\]
\[
V_+ = \frac{D}{m\mu}\left[\frac{s}{\mu}-\frac{2m}{\mu^2}+\frac{2}{\mu^3}\bigl(1-e^{-\mu m}\bigr)\right].\tag{3}
\]

Neither endpoint is attained, but each can be approximated by two-point waiting-time laws with strictly positive support, and every intermediate variance is realized by some such two-point law. If \(s=m^2\), the only admissible law is \(T=m\) almost surely, giving the single value \(V=D F_\mu(m)/(m\mu)\), with \(F_\mu\) defined below.

The stationary force variance is always \(C_Y(0)=Ds/m\), and is therefore **identical for every protocol in this fixed-two-moment class**. The open interval classifies different positional fluctuations despite this exact equality of force intensity and average renewal cadence.

There is also a structural comparison: among two admissible interval laws with the same mean and finite second moments, convex-order increase of resetting-interval variability increases **every lag** of the stationary force covariance and therefore cannot decrease the position variance. At fixed mean alone, deterministic waiting intervals uniquely minimize the variance.

## Assumptions and scope

Construct an equilibrium two-sided renewal point process from independent positive interarrival durations distributed as \(T\), with \(\mathbb E T=m\in(0,\infty)\) and \(\mathbb E T^2=s<\infty\). If \(T\) is deterministic, randomize the periodic phase uniformly over a period; thus the object is strictly stationary in physical time rather than sampled exclusively at renewal epochs. In each interarrival interval, assign an independent standard Brownian path \(B^{(j)}\), independent of the renewal process, and set the force at age \(a\) in that interval to \(Y=\sqrt{2D}\,B^{(j)}_a\). In particular, force values on different renewal intervals are independent and have mean zero. Define the continuously evolving particle position by the stationary \(L^2\) solution

\[
X_t=\int_0^\infty e^{-\mu u}Y_{t-u}\,du,
\qquad\text{equivalently }\dot X_t=-\mu X_t+Y_t.
\]

Only \(Y\) resets at the renewal epochs. No particle-position reset, additive thermal noise, correlated intervals, finite-time initialization, or pathwise tail theorem is part of the assertion. The renewal law may have atoms and need not be exponentially distributed.

## Proof

**1. Existence and renewal covariance.** The equilibrium renewal age \(A\) and forward residual \(R\) have the occupation identity

\[
\mathbb E\,\varphi(A,R)=\frac1m\mathbb E\left[\int_0^T\varphi(u,T-u)\,du\right]
\]

for any nonnegative measurable test function \(\varphi\). Thus \(\mathbb E Y_0^2=2D\mathbb E A=Ds/m<\infty\), establishing the stationary \(L^2\) convolution defining \(X_t\). For \(h\ge0\), \(Y_0\) and \(Y_h\) have nonzero covariance only if their renewal interval is the same. On this event, conditional Brownian covariance equals \(2DA\). Hence, with \(u\) the age of the current interval,

\[
\begin{aligned}
C_Y(h)&=\mathbb E[Y_0Y_h]=\frac{2D}{m}\mathbb E\int_0^{(T-h)_+}u\,du\\
&=\frac Dm\mathbb E\bigl[(T-h)_+^2\bigr].
\end{aligned}\tag{4}
\]

By stationarity, \(C_Y(-h)=C_Y(h)\). This formula is for the Brownian **driving noise**, not for the filtered particle position.

**2. Harmonic filtering.** The integrability of the exponential kernel and nonnegative covariance permit Fubini in the filtered second moment. Splitting the double integral along \(u-v=h\) gives

\[
V=\int_0^\infty\int_0^\infty e^{-\mu(u+v)}C_Y(u-v)\,du\,dv
=\frac1\mu\int_0^\infty e^{-\mu h}C_Y(h)\,dh.
\]

Combining this with (4), define

\[
F_\mu(t):=\int_0^t e^{-\mu h}(t-h)^2\,dh
=\frac{t^2}{\mu}-\frac{2t}{\mu^2}+\frac{2(1-e^{-\mu t})}{\mu^3}.
\]

Then \(V=D\mathbb E F_\mu(T)/(m\mu)\), yielding (1).

**3. Strict two-moment bounds.** Suppose \(s>m^2\). Since \(t\mapsto e^{-\mu t}\) is strictly convex, Jensen gives

\[
\mathbb E e^{-\mu T}>e^{-\mu m},
\]

which by (1) yields the strict upper bound \(V<V_+\). For the other direction, introduce the size-biased waiting-time law \(\mathbb P_*(T\in dt)=t\,\mathbb P(T\in dt)/m\). Its mean is \(s/m\). The function

\[
g(t)=\frac{1-e^{-\mu t}}{t}=\int_0^\mu e^{-ut}\,du,\qquad g(0)=\mu,
\]

is strictly convex on \([0,\infty)\), because \(g''(t)=\int_0^\mu u^2e^{-ut}\,du>0\). Applying Jensen to \(\mathbb P_*\) gives

\[
\mathbb E(1-e^{-\mu T})
=m\,\mathbb E_*g(T)
\ge\frac{m^2}{s}\left(1-e^{-\mu s/m}\right).
\]

Equality requires a point-mass size-biased law; with \(T>0\) almost surely this implies that \(T\) itself is constant, contrary to \(s>m^2\). Thus the lower bound in (2) is also strict.

**4. Sharpness, attainability, and degenerate boundary.** Put \(v=s-m^2>0\). For each \(a\in(0,m)\), define

\[
b(a)=m+\frac{v}{m-a},\qquad
q(a)=\frac{m-a}{b(a)-a},\qquad
\mathbb P\{T=a\}=1-q(a),\quad \mathbb P\{T=b(a)\}=q(a).
\]

Both waiting times are positive and direct substitution gives \(\mathbb E T=m\) and \(\mathbb E T^2=s\). As \(a\downarrow0\), the laws converge to mass \(1-m^2/s\) at zero and mass \(m^2/s\) at \(s/m\); the corresponding variances tend to \(V_-\). The limiting zero atom is **not an admissible positive waiting time**, so it does not attain the bound. As \(a\uparrow m\), \(b(a)\uparrow\infty\) and \(q(a)\downarrow0\); despite preserving the fixed second moment, the Laplace transform tends to \(e^{-\mu m}\), and (1) yields \(V_+\). This limit also does not have an admissible law attaining the bound. The map \(a\mapsto V(a)\) is continuous and has endpoint limits \(V_-\) and \(V_+\); the intermediate value theorem shows that **every** variance in the open interval is realized. If \(s=m^2\), nonnegativity of \(\operatorname{Var}T\) forces \(T=m\) almost surely and the stated single-value formula follows.

**5. Convex-order structure.** The function \(t\mapsto(t-h)_+^2\) is convex for every \(h\ge0\). If two waiting laws of the same mean satisfy \(T_1\le_{\mathrm{cx}}T_2\), then (4) yields \(C_{Y_1}(h)\le C_{Y_2}(h)\) for every lag and integrating against the positive kernel gives \(V_1\le V_2\). In particular \(F_\mu''(t)=2(1-e^{-\mu t})/\mu>0\) for \(t>0\), so direct strict Jensen in \(V=D\mathbb EF_\mu(T)/(m\mu)\) establishes the unique fixed-mean minimum at deterministic \(T=m\).

## Verification

The bundled standard-library program `verify.py` evaluates the two-atom formulas by three independent numerical routes: direct integration of \(F_\mu\), its moment–Laplace representation, and numerical convolution of the renewal-force covariance. It checks the two strict bounds, constructs positive two-point approximations to both endpoints, and tests fixed-mean convexity. It separately compares the exponential-waiting specialization with the Markovian covariance formula and checks the uniform-phase periodic stationary variance against direct within-cycle integration of the published reset-epoch variance formula. The numerical assertions are consistency checks only; the all-distribution and all-parameter conclusions rely on the analytic proof.

For the concrete normalized case \(D=\mu=m=1\), \(s=2\), the strict interval is

\[
1-e^{-2}\;<\;V\;<\;2(1-e^{-1}),
\]

numerically \(0.8646647168<V<1.2642411177\). Exponentially distributed reset intervals of mean one and second moment two give \(V=1\), strictly within these bounds.

## Relationship to prior work

Guéneau, Majumdar, and Schehr [1] introduce and analyze the **same resetting-Brownian-force harmonic-trap mechanism**, developing Kesten-variable and renewal tools. Their Section 3.1 derives an exact variance under deterministic periodic resets **at reset epochs** (their Eq. 11); Section 4 treats Poissonian resetting, and the general setup admits independent waiting durations. The new assertion is specifically the time-stationary arbitrary-renewal force covariance (4) and the **complete sharp interval at simultaneously fixed first and second waiting-time moments**, including strict nonattainment and two-atom realization. Neither the known periodic-epoch result nor the Poissonian specialization by itself supplies this two-moment classification. The phase-averaged periodic variance in this work is not the same observable as the reset-epoch variance in [1]; the accompanying check reconciles them.

Eule and Metzger [2] develop non-Poissonian renewal resetting of **the evolving position**, rather than the force. Den Hollander, Majumdar, Meylahn, and Touchette [3] study additive functionals of processes with Poissonian resetting. Those models supply background methods, but their main claims do not state the present waiting-moment optimization for a continuously evolving harmonic response to renewed Brownian forcing. Classical Jensen and size-bias inequalities are used transparently and are not claimed to be new mathematics on their own.

## Limitations

The result classifies the **stationary variance**, not the full non-Gaussian stationary position distribution or finite-time convergence rates. It requires positive independent renewal intervals with finite second moment, independently restarted Brownian-force excursions, and a positive harmonic relaxation rate. The limiting extremizers at nonzero waiting-time variance are not admissible distributions: one approaches zero-length intervals, the other sends a rare interval to arbitrarily large length. Unrestricted renewal laws with infinite second moment are outside the \(L^2\) statement. More general published results for constrained Laplace transforms or renewal-filtered processes may imply parts of the derivation; this is a remaining priority risk and the theorem has not received independent validation.

## References

[1] M. Guéneau, S. N. Majumdar, G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (first public version 15 June 2023), https://arxiv.org/abs/2306.09453, especially Sections 2–5, Eq. (11), and Appendix C.

[2] S. Eule, J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876, https://arxiv.org/abs/1510.07876.

[3] F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909, https://arxiv.org/abs/1801.09909.
