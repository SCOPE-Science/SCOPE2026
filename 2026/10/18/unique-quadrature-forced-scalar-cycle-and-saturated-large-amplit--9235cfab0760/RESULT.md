# Unique quadrature-forced scalar cycle and saturated large-amplitude Floquet contraction

## Finding
Consider the first-harmonic scalar piecewise differential equation
\[
 x'(t)=a\cos(t)|x(t)|+\sin(t),\qquad t\in\mathbb R,\quad a\in\mathbb R.
\]
For **every** nonzero \(a\), there is exactly **one** real \(2\pi\)-periodic solution \(u_a\). It has the antiperiodicity symmetry \(u_a(t+\pi)=-u_a(t)\). Its only two zeros in each forcing period are \(\theta(a)\in(0,\pi)\) and \(\theta(a)+\pi\), and it is positive strictly between those crossings. The phase is the unique root of
\[
 H_a(\theta):=\int_\theta^\pi \sin(s)e^{-a\sin(s)}\,ds-\int_0^\theta\sin(s)e^{a\sin(s)}\,ds=0.
\]
Its exact period-return Floquet multiplier is
\[
 \mu(a)=\exp[-4a\sin\theta(a)].
\]
For \(a>0\) this unique periodic state attracts the time-\(2\pi\) iterates of **every** real initial condition; for \(a<0\), every other initial condition escapes to negative or positive infinity under those iterates. At \(a=0\), every solution is \(2\pi\)-periodic, so the unique hyperbolic cycle emerges from a global center.

The weak- and strong-coefficient limits are sharp:
\[
\theta(a)=\frac\pi2-\frac{\pi a}{4}+O(a^3),\qquad
\log\mu(a)=-4a+\frac{\pi^2a^3}{8}+O(a^5)\quad(a\to0),
\]
and, writing \(c>1\) for the unique solution of \(c\tanh c=1\),
\[
\theta(a)=\frac ca+O(a^{-3}),\qquad
\mu(a)=e^{-4c}\bigl(1+O(a^{-2})\bigr)\quad(a\to+\infty).
\]
The saturation constant is \(c=1.1996786402577338\ldots\), hence \(e^{-4c}=0.008240332688721675\ldots\). The limiting multiplier is **strictly positive**, despite arbitrarily large coefficient amplitude.

## Assumptions and scope
The state variable is real and time is original unscaled time. Periodicity means \(u(t+2\pi)=u(t)\) for all real \(t\); the nonconstant solutions here also have minimal period \(2\pi\), since their two zeros are separated by exactly \(\pi\) and their signs alternate. The coefficient \(a\) is any real number, including both signs and the center case \(a=0\). The right-hand side is continuous and globally Lipschitz in \(x\) with finite-time Lipschitz bound \(|a|\), so every initial value has a unique global classical \(C^1\) solution. Stability and escape refer to iterations of the forward period map on the real line. All asymptotic statements are for the explicitly stated one-sided limits; no assertion is made about arbitrary trigonometric coefficients or higher harmonics.

## Proof
**1. Root geometry.** Fix \(a\ne0\). At a zero of a solution, its velocity equals \(\sin t\). Thus every sign-changing periodic solution has one upward crossing at \(t_1\in(0,\pi)\) and one downward crossing at \(t_2\in(\pi,2\pi)\), and no others. A possible tangency at \(0\) (respectively \(\pi\)) is a strict local minimum (respectively maximum), since the one-sided second derivative there equals \(+1\) (respectively \(-1\)); such a tangency is incompatible with a sign-changing periodic orbit by the permitted crossing directions. More generally, the forced sign-change classification follows directly by the same elementary crossing argument.

There is no all-nonnegative or all-nonpositive periodic solution for \(a\ne0\): on a positive orbit the linear integrating factor is \(e^{-a\sin t}\), and the full-period weighted forcing is
\[
 B_-(a)=\int_0^{2\pi}\sin t\,e^{-a\sin t}dt
 =\int_0^\pi\sin t\bigl(e^{-a\sin t}-e^{a\sin t}\bigr)dt\ne0.
\]
On a negative orbit the integrating factor is \(e^{a\sin t}\), giving \(B_+(a)=-B_-(a)\ne0\). Any isolated tangency at a zero leaves the corresponding signed linear solution unchanged by uniqueness and cannot repair this return mismatch. Accordingly any periodic state must have the two transverse crossings above.

Write \(t_2=\pi+r\), with \(r\in(0,\pi)\), and set
\[
 C(v)=\int_0^v\sin(s)e^{-a\sin s}ds,\qquad
 D(v)=\int_0^v\sin(s)e^{a\sin s}ds.
\]
Integrating on the positive arc \((t_1,t_2)\) gives \(C(t_2)=C(t_1)\). Integrating on the negative arc \((t_2,t_1+2\pi)\), then shifting time by \(\pi\), gives \(C(t_1+\pi)=C(r)\). With \(B=C(\pi)\), the half-period identities \(C(v+\pi)=B-D(v)\) reduce these equations to
\[
 B-D(r)=C(t_1),\qquad B-D(t_1)=C(r).
\]
Subtracting yields \(D(t_1)-C(t_1)=D(r)-C(r)\). But
\[
 [D(v)-C(v)]'=2\sin v\,\sinh(a\sin v)
\]
has a constant strict sign for \(v\in(0,\pi)\), hence \(r=t_1\). Therefore **every** periodic solution must have its downward zero at \(t_1+\pi\), and its upward zero must solve \(H_a(t_1)=0\).

Direct differentiation gives
\[
 H'_a(t)=-2\sin t\,\cosh(a\sin t)<0\qquad(0<t<\pi).
\]
Also \(H_a(0)>0\) and \(H_a(\pi)<0\). Hence there is exactly one phase \(\theta(a)\in(0,\pi)\).

**2. Existence and antiperiodicity.** Starting at \(u_a(\theta)=0\), define on \([\theta,\theta+\pi]\)
\[
 u_a(t)=e^{a\sin t}\int_\theta^t\sin s\,e^{-a\sin s}ds.
\]
The condition \(H_a(\theta)=0\) makes the endpoint value zero (use \(C(\theta+\pi)=C(\theta)\)). The integral is initially strictly increasing until \(\pi\), then strictly decreasing to zero, so the state is strictly positive in the open half-period. Extend by \(u_a(t+\pi)=-u_a(t)\) and periodic continuation. The vector-field identity \(f(t+\pi,-x)=-f(t,x)\) shows both halves solve the original equation. At joining zeros the derivatives from both sides equal \(\sin t\), so the extension is classical. This establishes existence, and Step 1 establishes global uniqueness.

**3. Exact multiplier and complete basin.** Along this solution, the variational coefficient exists outside its two transverse zeros and equals \(a\cos t\,\operatorname{sgn}(u_a(t))\). Integrating across the two arcs gives
\[
\log\mu(a)=a\int_0^{2\pi}\cos t\,\operatorname{sgn}(u_a(t))dt
=2a\int_\theta^{\theta+\pi}\cos t\,dt
=-4a\sin\theta.
\]
Let \(P_a(x)\) be the time-\(2\pi\) map. Scalar order preservation makes \(P_a\) continuous and strictly increasing; Step 1 proves it has precisely one fixed point \(x_*\). For sufficiently large positive initial values trajectories stay positive throughout a period, and the return displacement is \(P_a(x)-x=B_-(a)\); for sufficiently large negative initial values trajectories stay negative and the displacement equals \(B_+(a)=-B_-(a)\). The sign of \(B_-(a)\) is opposite the sign of \(a\). The continuous displacement has no other zero, so these are its signs on the whole intervals \((x_*,\infty)\) and \(( -\infty,x_*)\), respectively. If \(a>0\), monotone iterates on either side approach the unique fixed point; if \(a<0\), monotone iterates move away and must be unbounded, or their finite limit would be another fixed point. At \(a=0\), solutions satisfy \(x(t)=x(0)+1-\cos t\), and all are periodic.

**4. Weak-coefficient asymptotics and sign symmetry.** The equality \(H_{-a}(\pi-t)=-H_a(t)\) yields \(\theta(-a)=\pi-\theta(a)\). Since \(H_0(\pi/2)=0\) and \(\partial_t H_0(\pi/2)=-2\), the analytic implicit-function theorem applies. Evaluating at \(\pi/2\) gives
\[
H_a(\pi/2)=-2a\int_0^{\pi/2}\sin^2 s\,ds+O(a^3)=-\frac{\pi a}{2}+O(a^3).
\]
Thus \(\theta(a)=\pi/2-\pi a/4+O(a^3)\); symmetry eliminates even powers. Expanding \(-4a\sin\theta(a)\) gives the displayed cubic multiplier exponent and \(O(a^5)\) remainder.

**5. Strong-coefficient boundary layer.** Put \(z=a\theta\) and consider \(a\to+\infty\). For fixed bounded \(z>0\), Taylor's formula \(\sin(u/a)=u/a+O(u^3/a^3)\), with exponential-tail domination near both endpoints, gives uniformly on compact positive \(z\)-ranges
\[
\begin{aligned}
 a^2\int_{z/a}^\pi\sin s\,e^{-a\sin s}ds
 &= (z+1)e^{-z}+1+O(a^{-2}),\\
 a^2\int_0^{z/a}\sin s\,e^{a\sin s}ds
 &= (z-1)e^z+1+O(a^{-2}).
\end{aligned}
\]
For the first integral, the contributions are the \(s=z/a\) boundary with scaled integral \(\int_z^\infty u e^{-u}du\), and the \(s=\pi\) boundary with \(\int_0^\infty u e^{-u}du=1\). Outside any fixed endpoint neighborhoods, \(\sin s\) is bounded away from zero and the integrals decay exponentially, justifying the uniform remainder by dominated Taylor bounds (choose endpoint neighborhoods and absorb exponentially small interiors).

The limiting difference is
\[
 F(z)=(z+1)e^{-z}-(z-1)e^z.
\]
It satisfies \(F(0)=2\), \(F(z)\to-\infty\), and \(F'(z)=-2z\cosh z<0\) for \(z>0\). Its unique root \(c>1\) is equivalently characterized by \(c\tanh c=1\). Bracket \(c\) between any two fixed positive arguments with opposite signs of \(F\). The strict monotonicity of \(H_a\) then traps \(a\theta(a)\) in a compact interval around \(c\). The displayed uniform \(O(a^{-2})\) expansion, together with \(F'(c)\ne0\), implies \(a\theta(a)=c+O(a^{-2})\), hence \(\theta(a)=c/a+O(a^{-3})\). Finally \(a\sin\theta(a)=c+O(a^{-2})\), which proves \(\mu(a)=e^{-4c}(1+O(a^{-2}))\).

## Verification
The numerical companion `verify.py` runs Simpson quadrature and monotone bisection using only the Python standard library. It checks the phase-defining integral, positivity and zero of the constructed positive arc, predicted Floquet factors for several positive coefficient values, both asymptotic regimes, and the value of the saturation root. It prints `CHECK_OK`. These are independently reproducible finite evaluations; the complete uniqueness, stability and asymptotic assertions are established analytically by Steps 1–5 and do not depend on sampling. Numerical values are illustrative, not interval-certified constants.

## Relationship to prior work
Bravo, Fernández and Ojeda (2023 preprint, 2024 journal article) treat precisely the general first-harmonic family containing this equation: they characterize centers, prove finiteness, and derive a general upper bound. Their Section 2 gives useful half-map conditions but does not give the uniqueness classification, exact Floquet multiplier, and strong-quadrature boundary-layer constant here. Bravo, Fernández and Tineo (2007) treat distributions of periodic solutions for general piecewise scalar equations; this does not by itself entail the explicit result. Gasull and Zhao (2023) prove an at-most-two theorem when **one** coefficient keeps a fixed sign; both coefficients here change sign, so that theorem does not cover this case. Bravo and Trinidad-Forte (2026) extend composition criteria for global centers, not the noncenter cycle and large-coefficient spectrum. Published work on four first-harmonic piecewise cycles concerns a different family with constant-bias perturbations of an aligned global center, not the quadrature-forcing family analyzed here. A distinct half-wave fold result concerns constant positive magnitude multiplying \(|x|\) and a varying additive bias, whereas the multiplier here is a sign-changing cosine. Neither statement implies the present complete parameter classification or the limiting value \(e^{-4c}\).

## Limitations
The exact result applies to the specified quadrature-aligned single-harmonic slice; it is not a theorem for arbitrary phase differences, coefficients with nonzero means, or higher harmonics. Global attraction and escape refer to discrete period iterates; the proof does not claim a uniform convergence rate over all initial values. The numerical computations are not infinite proofs. Although the most relevant available primary work and nearby published mathematical records were compared, the literature search cannot logically establish absolute novelty; an equivalent treatment in older switched-oscillator terminology remains a residual priority risk.

## References
1. J. L. Bravo, M. Fernández, I. Ojeda, *Hilbert number for a family of piecewise nonautonomous equations*, arXiv:2307.15578v1 (first posted 2023-07-28), https://arxiv.org/html/2307.15578v1; *Qualitative Theory of Dynamical Systems* **23** (2024), article 119, DOI:10.1007/s12346-023-00922-9.
2. J. L. Bravo, M. Fernández, A. Tineo, *Periodic solutions of a periodic scalar piecewise ODE*, *Communications on Pure and Applied Analysis* **6** (2007), 213–228, DOI:10.3934/cpaa.2007.6.213.
3. A. Gasull, Y. Zhao, *Existence of at most two limit cycles for some non-autonomous differential equations*, *Communications on Pure and Applied Analysis* **22** (2023), 970–982, DOI:10.3934/cpaa.2023016.
4. J. L. Bravo, R. Trinidad-Forte, *Global Centers in Piecewise Linear Equations in the Cylinder*, *Qualitative Theory of Dynamical Systems* **25** (2026), article 26, DOI:10.1007/s12346-025-01425-5.
