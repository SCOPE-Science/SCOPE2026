# Exact phase windows and bistability resonances for a sinusoidal interval map

## Finding

Consider the real map
\[
F_{A,\omega,\phi}(x)=A\sin\bigl(\omega(x-\phi)\bigr),
\qquad A>0,\quad\omega>0,\quad\phi\in\mathbb R.
\]
Put \(\rho=A\omega>1\), \(\theta=\omega\phi\pmod{2\pi}\), and define
\[
h=\arcsin(1/\rho),\qquad
c=\sqrt{\rho^2-1}-\pi/2,
\qquad
\operatorname{dist}_{2\pi}(u,v)=\min_{k\in\mathbb Z}|u-v-2\pi k|.
\]
The number of **hyperbolically attracting fixed points** of \(F_{A,\omega,\phi}\) is exactly
\[
N(\rho,\theta)=
\mathbf 1\{\operatorname{dist}_{2\pi}(\theta,c)<h\}
+\mathbf 1\{\operatorname{dist}_{2\pi}(\theta,-c)<h\}.
\]
The first indicator counts a unique positive fixed point and the second a unique negative fixed point. Thus \(N\le2\), independently of the frequency and of the total number of fixed points. At the endpoints of either phase window the corresponding fixed point has multiplier \(+1\) or \(-1\), and is not counted as a hyperbolic attractor.

In particular, writing
\[
d=\min_{k\in\mathbb Z}|2c-2\pi k|\in[0,\pi],
\]
there are two simultaneous hyperbolic sinks for some phase precisely when \(d<2h\). Their phase-set length in a period of length \(2\pi\) is exactly \(\max\{0,2h-d\}\), and the fraction of uniformly distributed phases exhibiting bistability is
\[
\boxed{\frac{\max\{0,2h-d\}}{2\pi}.}
\]
There are infinitely many exact full-overlap resonances:
\[
\rho_j=\sqrt{1+\bigl((j+\tfrac12)\pi\bigr)^2},\qquad j=0,1,2,\ldots.
\]
At each \(\rho=\rho_j\), the two phase windows coincide, centered at \(\theta=j\pi\pmod{2\pi}\), with width \(2\arcsin(1/\rho_j)\). Every phase strictly inside that interval yields two hyperbolic sinks with disjoint open local attraction basins. Their phase fraction equals \(\arcsin(1/\rho_j)/\pi\sim1/(\pi\rho_j)\).

## Assumptions and scope

All states and parameters are real; \(A>0\), \(\omega>0\), \(\rho>1\), and \(\phi\) is arbitrary. Stability means the strict one-dimensional multiplier criterion \(|F'(x_*)|<1\). No claim is made about nonlinear stability at the two boundary multipliers or about period-two or higher attractors. Every fixed point lies in \([-A,A]\), since the map has that range.

## Proof

Scale \(x=Au\). The fixed-point equation and multiplier become
\[
u=\sin(\rho u-\theta),\qquad
\lambda=\rho\cos(\rho u-\theta).
\]
At any fixed point, \(\lambda^2=\rho^2(1-u^2)\). Therefore the strict sink criterion is equivalent to \(|u|>s\), where \(s=\sqrt{1-\rho^{-2}}\). In particular no zero fixed point is a hyperbolic sink when \(\rho>1\).

For \(s<u\le1\), the sine equation is equivalent, modulo \(2\pi\), to either of the phase parameterizations
\[
\theta_+(u)=\rho u-\arcsin u,
\qquad
\theta_-(u)=\rho u-\pi+\arcsin u.
\]
The first is strictly decreasing on \((s,1)\), since its derivative is \(\rho-1/\sqrt{1-u^2}<0\); the second is strictly increasing, since its derivative is \(\rho+1/\sqrt{1-u^2}>0\). At the lower endpoint, using \(\arcsin s=\pi/2-h\),
\[
\theta_+(s)=c+h,\qquad \theta_-(s)=c-h.
\]
At \(u=1\), both parameterizations equal \(\rho-\pi/2\). This common value lies strictly between \(c-h\) and \(c+h\): indeed
\[
\rho-\sqrt{\rho^2-1}=\tan(h/2)<h
\quad(0<h<\pi/2).
\]
Consequently the two monotone branches fill the single open phase interval \((c-h,c+h)\) without overlap other than their common endpoint at \(u=1\). Since \(2h<\pi<2\pi\), reduction modulo \(2\pi\) introduces no second positive sink. This proves the positive indicator and its uniqueness, with strict endpoints corresponding respectively to multipliers \(-1\) and \(+1\).

The substitution \(u\mapsto-u\), \(\theta\mapsto-\theta\) preserves the fixed-point equation. Thus negative sinks occupy the reflection \((-c-h,-c+h)\) modulo \(2\pi\), with exactly one negative sink at every interior phase. The total count is therefore the sum of the two indicator functions.

Two arcs of equal half-width \(h<\pi/2\), with circular center distance \(d\in[0,\pi]\), intersect in an arc of length \((2h-d)_+\). Here the centers are \(c\) and \(-c\), giving the asserted coexistence condition and probability. If \(\rho=\rho_j\), then \(\sqrt{\rho^2-1}=(j+1/2)\pi\), so \(c=j\pi\), and the center distance is zero. The window width and asymptotics follow directly from \(h=\arcsin(1/\rho)\). Every hyperbolic sink admits an open attracting neighborhood by the mean-value theorem; distinct fixed points have disjoint basins. This completes the proof.

## Verification

The included standalone `verify.py` performs deterministic numerical root counting against the phase-window prediction away from bifurcation boundaries, checks the exact resonance formulas, and constructs both attracting fixed points at multiple resonances, confirming their residuals and strict multipliers. Running `python3 verify.py` prints the number of passed checks. These finite tests supplement, but do not replace, the analytic proof above.

## Relationship to prior work

Ali Ali, Sriram, Natiq, Ahmadi, Rajagopal and Jafari (2023) introduced and numerically studied this single-sine map alongside a two-sine extension. In the accessible mathematical discussion of their Sections 2.1 and 3.1, the stability test is formulated as the derivative bound and the phase effects are exhibited in bifurcation diagrams. The theorem above instead classifies the complete strict phase set at every \(\rho>1\), derives its exact measure, proves a universal two-sink cap, and isolates infinitely many complete-overlap resonances. Standard saddle-node and flip theory identifies the local mechanisms of the endpoint multipliers but does not itself give these global parameter windows. The accessible primary material does not document the exact classification; remaining source-access uncertainty is stated below.

## Limitations

The classification covers hyperbolically attracting **fixed points**, not all attractors or all fixed points. On the boundary of each arc, multipliers equal \(\pm1\) and nonlinear one-sided attraction is not resolved. The quoted probability refers to uniformly distributed phase parameters, not to random initial conditions or invariant measures. For \(0<\rho<1\), the map is a global contraction and has one attracting fixed point for every phase; this elementary regime is distinct from the claimed \(\rho>1\) phase classification. The complete twelve-page originating article was not accessible for inspection; relevant indexed mathematical sections and the conclusion were examined, but an unnoticed formulation elsewhere in that text or in historical sine-map literature remains a priority risk.

## References

1. A. M. Ali Ali, S. Sriram, H. Natiq, A. Ahmadi, K. Rajagopal, and S. Jafari, "A novel multi-stable sinusoidal chaotic map with spectacular behaviors," *Communications in Theoretical Physics* **75** (2023), 115001. First verified public release: 2023-09-29. DOI: https://doi.org/10.1088/1572-9494/acf307.
2. "Saddle-node bifurcation for maps," *Scholarpedia* (2008), https://www.scholarpedia.org/article/Saddle-node_bifurcation_for_maps (general bifurcation background, not a source for the new phase formula).
