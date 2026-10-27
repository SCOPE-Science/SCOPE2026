# Pointwise non-Zeno behavior without a uniform dwell-time bound for a sampled-data heat equation

## Finding

Consider the Neumann heat equation on \(X=L^2(0,1)\), with \(A=\partial_{\xi\xi}\), identity input operator \(B=I\), and rank-one feedback \(Fx=-\langle x,\phi_0\rangle\phi_0\), where \(\phi_0(\xi)=1\). The held input is \(u(t)=Fx(t_k)\) for \(t_k\le t<t_{k+1}\), and events are defined by

\[
t_{k+1}=\inf\{t>t_k:\|x(t)-x(t_k)\|>\varepsilon\|x(t)\|\},\qquad \varepsilon>0.
\]

For every fixed initial state \(x^0\in X\), the event times have no finite accumulation point. This is a pointwise non-Zeno statement; it does **not** provide a positive dwell-time bound uniform over all initial states. In fact, for every \(n\ge1\), if \(x^0=\phi_n(\xi)=\sqrt2\cos(n\pi\xi)\), then every inter-event interval equals \(\log(1+\varepsilon)/(n^2\pi^2)\), so the infimum over initial states is zero.

## Assumptions and scope

The state space is real \(L^2(0,1)\). The Neumann Laplacian has orthonormal eigenfunctions \(\phi_0(\xi)=1\) and \(\phi_n(\xi)=\sqrt2\cos(n\pi\xi)\) for \(n\ge1\), with \(A\phi_n=-n^2\pi^2\phi_n\). The input operator is the identity and the feedback acts only on the constant mode: \(Fx=-\langle x,\phi_0\rangle\phi_0\). The event condition compares the full state difference with the current full-state norm, not the feedback-output error. The threshold \(\varepsilon\) is any fixed positive real number.

## Proof

Write \(x(t)=a(t)\phi_0+h(t)\), with \(a(t)=\langle x(t),\phi_0\rangle\) and \(h(t)\perp\phi_0\). The feedback is constant on each hold interval, so if \(a_k=a(t_k)\), then

\[
a(t_k+\tau)=(1-\tau)a_k,
\qquad h(t)=e^{tA_h}h_0,
\]

where \(h_0=h(0)\) and \(A_h\) is the Neumann Laplacian restricted to the orthogonal complement of \(\phi_0\). In particular, the higher modes evolve independently of the event sequence.

If \(h_0=0\) and \(a_0\ne0\), the trigger ratio before the first event is \(\tau/(1-\tau)\) for \(0\le\tau<1\). Its threshold crossing is exactly \(\tau=\varepsilon/(1+\varepsilon)\); the same interval repeats after each update. If \(x^0=0\), the state remains zero and there are no events.

Now suppose \(h_0\ne0\) and, for a contradiction, that infinitely many event times accumulate at a finite \(T\). Strong continuity gives \(t_1>0\), hence \(T>0\), and the intervals \(\Delta_k=t_{k+1}-t_k\) tend to zero. For all sufficiently large \(k\), one has \(t_k\ge T/2\) and \(0<\Delta_k<1\). On this tail, \(a_{k+1}=(1-\Delta_k)a_k\), so \( |a_k|\le |a_{k_0}|\) for some fixed tail index \(k_0\).

The heat semigroup is injective, so \(h(T)\ne0\). Since \(\|h(t)\|\) is nonincreasing, put \(m=\|h(T)\|>0\); then \(\|x(t)\|\ge\|h(t)\|\ge m\) on \([T/2,T]\). Spectral expansion gives, for \(t\ge T/2\),

\[
\|A_hh(t)\|\le \sup_{r\ge0} r e^{-rt}\,\|h_0\|=\frac{\|h_0\|}{et}\le\frac{2\|h_0\|}{eT}.
\]

Thus on every sufficiently late hold interval, with \(C=|a_{k_0}|+2\|h_0\|/(eT)\),

\[
\|x(t_k+\tau)-x(t_k)\|\le C\tau,\qquad
\|x(t_k+\tau)\|\ge m,\quad 0\le\tau\le\Delta_k.
\]

At a finite event time the continuous trigger ratio reaches its threshold, so \(C\Delta_k\ge\varepsilon m\). This positive lower bound contradicts \(\Delta_k\to0\). Hence no finite accumulation is possible.

Finally, for \(x^0=\phi_n\), the feedback vanishes and \(x(t_k+\tau)=e^{-n^2\pi^2\tau}x(t_k)\). The trigger equation is \(1-e^{-n^2\pi^2\tau}=\varepsilon e^{-n^2\pi^2\tau}\), giving \(\tau=\log(1+\varepsilon)/(n^2\pi^2)\). This tends to zero as \(n\to\infty\), proving the absence of a uniform first-event lower bound while remaining consistent with pointwise non-Zeno behavior.

## Verification

The mode decomposition, hold-interval formula, high-mode derivative estimate, and eigenmode event-time formula are derived analytically. The no-accumulation argument treats separately the pure constant mode and every initial state with a nonzero higher-mode component. No finite-mode computation is used as a proof for the infinite-dimensional state space. The conclusion is restricted to this Neumann heat model, this rank-one feedback, and this full-state relative trigger.

## Relationship to prior work

Wakaiki and Sano study this same heat-equation example in their discussion of minimum inter-event times. Their Example 3.2 proves that the first inter-event time has infimum zero over initial states by taking \(x^0=\phi_n\), and it gives the same exact eigenmode formula. That statement alone does not imply that a fixed trajectory has Zeno accumulation, nor does it prove the converse. The result here supplies a pointwise no-finite-accumulation proof for every fixed initial state in that example while retaining the sharp failure of a uniform lower bound. A separate PDE–ODE event-triggered adaptive-control result uses a different dynamic trigger and an explicit maximum dwell time, so it does not imply this claim.

## Limitations

The theorem does not assert a dwell-time lower bound uniform in the initial state, and it does not claim a uniform lower bound over all time for each fixed state. It does not extend automatically to other semigroups, feedback operators, boundary actuators, or event conditions based on feedback-output errors. The literature search was not exhaustive; an unindexed proof of the same pointwise statement may exist.

## References

1. M. Wakaiki and H. Sano, “Event-triggered Control of Infinite-dimensional Systems,” arXiv:1801.05521, first publicly posted 2018-01-17; later published in *SIAM Journal on Control and Optimization* 58(2) (2020), 605–635. The source's model and Example 3.2 are available at https://arxiv.org/abs/1801.05521; DOI: https://doi.org/10.1137/18M1179717.
2. J. Wang and M. Krstic, “Event-Triggered Adaptive Control of a Parabolic PDE-ODE Cascade with Piecewise-Constant Inputs and Identification,” arXiv:2110.05680 (2021), especially the distinct dynamic trigger and dwell-time result in Sections IV–V. Available at https://arxiv.org/abs/2110.05680.
